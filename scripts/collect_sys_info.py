#!/usr/bin/env python3
# Python 3.9+
import glob
import json
import os
import platform
import re
import socket
import subprocess
from pathlib import Path
from typing import Iterable, List, Optional, Set, Tuple


def run_cmd(cmd: List[str], timeout: int = 5) -> str:
    try:
        out = subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL,
            timeout=timeout
        )
        return out.decode("utf-8", errors="replace")
    except Exception:
        return ""


MAC_RE_STD = re.compile(r"^[0-9a-f]{2}(:[0-9a-f]{2}){5}$")


def normalize_mac(raw: str) -> Optional[str]:
    """
    Normalize a MAC to lowercase colon-separated form: xx:xx:xx:xx:xx:xx
    Accepts formats with '-', ':', or Cisco-style 'aaaa.bbbb.cccc'.
    """
    if not raw:
        return None
    mac = raw.strip().lower()

    # Handle Cisco dotted format aaaa.bbbb.cccc
    if "." in mac and mac.count(".") == 2:
        mac = mac.replace(".", "")

    # Replace dashes with colons
    mac = mac.replace("-", ":")

    # If all hex without separators and length 12, insert colons
    hex_only = re.sub(r"[^0-9a-f]", "", mac)
    if len(hex_only) == 12:
        mac = ":".join(hex_only[i:i + 2] for i in range(0, 12, 2))

    # Collapse multiple separators just in case
    mac = re.sub(r":{2,}", ":", mac)

    if not MAC_RE_STD.match(mac):
        return None

    # Exclude all-zero and broadcast addresses
    if mac in ("00:00:00:00:00:00", "ff:ff:ff:ff:ff:ff"):
        return None

    return mac


def uniq_preserve(items: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    out: List[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def _uniq_preserve_by_mac(
    items: Iterable[Tuple[str, Optional[str]]]
) -> List[Tuple[str, Optional[str]]]:
    """
    Deduplicate (mac, iface) pairs by MAC address while preserving the order
    of first appearance. If the same MAC appears with multiple interface names,
    the first encountered is kept.
    """
    seen: Set[str] = set()
    out: List[Tuple[str, Optional[str]]] = []
    for mac, iface in items:
        if mac not in seen:
            seen.add(mac)
            out.append((mac, iface))
    return out

def _macs_and_ifaces_from_sysfs_linux() -> List[Tuple[str, Optional[str]]]:
    """
    Read MAC addresses from /sys/class/net/<iface>/address on Linux.
    """
    result: List[Tuple[str, Optional[str]]] = []
    try:
        for addr_path in glob.glob("/sys/class/net/*/address"):
            iface = os.path.basename(os.path.dirname(addr_path))
            try:
                with open(addr_path, "r", encoding="utf-8", errors="ignore") as f:
                    raw = f.read().strip()
                mac = normalize_mac(raw)
                if mac:
                    result.append((mac, iface))
            except Exception:
                # Ignore a single interface read issue and continue
                pass
    except Exception:
        pass
    return result

def _macs_and_ifaces_from_ifconfig() -> List[Tuple[str, Optional[str]]]:
    """
    Parse `ifconfig -a` (or `ifconfig`) output for (iface, mac) pairs (macOS/BSD/Linux variants).
    """
    result: List[Tuple[str, Optional[str]]] = []
    out = run_cmd(["ifconfig", "-a"]) or run_cmd(["ifconfig"])
    if not out:
        return result

    current_iface: Optional[str] = None
    for line in out.splitlines():
        # Interface header line (e.g., "en0: flags=..." or "eth0: flags=...")
        m_iface = re.match(r"^\s*([^\s:]+):", line)
        if m_iface:
            current_iface = m_iface.group(1).strip()

        # MAC line: "ether xx:.." (macOS/BSD/Linux) or "lladdr xx:.." (some BSDs)
        m_mac = re.search(
            r"\b(?:ether|lladdr)\s+([0-9A-Fa-f:]{2}(?::[0-9A-Fa-f]{2}){5})", line
        )
        if m_mac:
            mac_raw = m_mac.group(1)
            mac = normalize_mac(mac_raw)
            if mac:
                result.append((mac, current_iface))
    return result

def _macs_and_ifaces_from_networksetup_macos() -> List[Tuple[str, Optional[str]]]:
    """
    Parse `networksetup -listallhardwareports` on macOS for (device, mac) pairs.
    """
    result: List[Tuple[str, Optional[str]]] = []
    try:
        out = run_cmd(["networksetup", "-listallhardwareports"])
        if not out:
            return result

        device: Optional[str] = None
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("Device:"):
                device = line.split(":", 1)[1].strip()
            elif line.startswith("Ethernet Address:"):
                mac_raw = line.split(":", 1)[1].strip()
                mac = normalize_mac(mac_raw)
                if mac:
                    result.append((mac, device))
                device = None  # reset for safety
    except Exception:
        pass
    return result


def _macs_and_ifaces_from_ipconfig_windows() -> List[Tuple[str, Optional[str]]]:
    """
    Parse `ipconfig /all` output on Windows for (iface, mac) pairs.
    """
    result: List[Tuple[str, Optional[str]]] = []
    try:
        out = run_cmd(["ipconfig", "/all"])
        if not out:
            return result

        current_iface: Optional[str] = None
        for raw_line in out.splitlines():
            line = raw_line.strip()

            # Section header typically like: "Ethernet adapter Ethernet:" or "Wireless LAN adapter Wi-Fi:"
            if line.lower().endswith(":") and "adapter" in line.lower():
                # Keep the whole header text (without trailing colon) as interface name for clarity
                current_iface = line[:-1]

            # MAC line: "Physical Address. . . . . . . . . : xx-xx-xx-xx-xx-xx"
            m_mac = re.search(
                r"Physical Address[.\s]*:\s*([0-9A-Fa-f\-]{12,17})", line, re.IGNORECASE
            )
            if m_mac:
                mac_raw = m_mac.group(1)
                mac = normalize_mac(mac_raw)
                if mac:
                    result.append((mac, current_iface))
    except Exception:
        pass
    return result

def macs_from_sysfs_linux() -> List[str]:
    macs: List[str] = []
    base = Path("/sys/class/net")
    if not base.exists():
        return macs
    for iface in base.iterdir():
        try:
            if iface.name == "lo":
                continue
            addr_file = iface / "address"
            if addr_file.exists():
                raw = addr_file.read_text(encoding="utf-8", errors="ignore").strip()
                mac = normalize_mac(raw)
                if mac:
                    macs.append(mac)
        except Exception:
            continue
    return macs


def macs_from_ifconfig() -> List[str]:
    macs: List[str] = []
    # Try with -a first to include inactive interfaces
    out = run_cmd(["ifconfig", "-a"])
    if not out:
        out = run_cmd(["ifconfig"])
    if not out:
        return macs
    # Match both 'ether xx:..' (macOS/BSD) and 'lladdr xx:..' (some BSDs)
    for m in re.finditer(r"\b(?:ether|lladdr)\s+([0-9A-Fa-f:.-]{11,23})", out):
        mac = normalize_mac(m.group(1))
        if mac:
            macs.append(mac)
    return macs


def macs_from_ip_link() -> List[str]:
    macs: List[str] = []
    out = run_cmd(["ip", "-o", "link"])
    if not out:
        out = run_cmd(["ip", "link"])
    if not out:
        return macs
    # Example: link/ether 12:34:56:78:9a:bc ...
    for m in re.finditer(r"\blink/ether\s+([0-9A-Fa-f:]{17})\b", out):
        mac = normalize_mac(m.group(1))
        if mac:
            macs.append(mac)
    return macs


def macs_from_networksetup_macos() -> List[str]:
    macs: List[str] = []
    out = run_cmd(["networksetup", "-listallhardwareports"])
    if not out:
        return macs
    for m in re.finditer(r"Ethernet Address:\s*([0-9A-Fa-f:.-]{11,23})", out):
        mac = normalize_mac(m.group(1))
        if mac:
            macs.append(mac)
    return macs


def macs_from_getmac_windows() -> List[str]:
    macs: List[str] = []
    out = run_cmd(["getmac", "/v", "/fo", "csv"])
    if not out:
        out = run_cmd(["getmac"])
    if not out:
        return macs
    for m in re.finditer(r"([0-9A-Fa-f]{2}(?:[-:][0-9A-Fa-f]{2}){5})", out):
        mac = normalize_mac(m.group(1))
        if mac:
            macs.append(mac)
    return macs


def macs_from_ipconfig_windows() -> List[str]:
    macs: List[str] = []
    out = run_cmd(["ipconfig", "/all"])
    if not out:
        return macs
    # Physical Address. . . . . . . . . : xx-xx-xx-xx-xx-xx
    for m in re.finditer(r"Physical Address[^:]*:\s*([0-9A-Fa-f-]{17})", out):
        mac = normalize_mac(m.group(1))
        if mac:
            macs.append(mac)
    return macs


# def get_all_mac_addresses() -> List[str]:
#     system = platform.system().lower()
#     candidates: List[str] = []
#
#     if system == "windows":
#         candidates.extend(macs_from_getmac_windows())
#         candidates.extend(macs_from_ipconfig_windows())
#     elif system == "linux":
#         candidates.extend(macs_from_sysfs_linux())
#         candidates.extend(macs_from_ip_link())
#         candidates.extend(macs_from_ifconfig())
#     elif system == "darwin":
#         candidates.extend(macs_from_networksetup_macos())
#         candidates.extend(macs_from_ifconfig())
#     else:
#         # Try generic commands
#         candidates.extend(macs_from_ifconfig())
#         candidates.extend(macs_from_ip_link())
#
#     # Fallback: include uuid.getnode() if nothing else found
#     try:
#         import uuid
#         node = uuid.getnode()
#         # uuid.getnode() may return a random 48-bit number if no MAC found
#         # We add it only if it appears to be a real MAC (multicast bit not set)
#         if node is not None and isinstance(node, int) and node != 0:
#             mac_hex = f"{node:012x}"
#             # multicast bit is the least significant bit of the first octet
#             first_octet = int(mac_hex[0:2], 16)
#             is_multicast = (first_octet & 1) == 1
#             mac = normalize_mac(mac_hex)
#             if mac and not is_multicast:
#                 candidates.append(mac)
#     except Exception:
#         pass
#
#     # Deduplicate while preserving order
#     macs = uniq_preserve([m for m in candidates if m])
#     return macs

def get_all_mac_addresses_with_interfaces() -> List[Tuple[str, Optional[str]]]:
    """
    Return a list of (mac, interface_name) tuples.
    interface_name may be None if it couldn't be determined for that MAC.
    The list is deduplicated by MAC while preserving the first-seen order.
    """
    system = platform.system().lower()
    candidates: List[Tuple[str, Optional[str]]] = []

    if system == "windows":
        candidates.extend(_macs_and_ifaces_from_ipconfig_windows())
    elif system == "linux":
        # Prefer sysfs as it's reliable, then cross-check with command outputs
        candidates.extend(_macs_and_ifaces_from_sysfs_linux())
        candidates.extend(_macs_and_ifaces_from_ip_link())
        candidates.extend(_macs_and_ifaces_from_ifconfig())
    elif system == "darwin":
        candidates.extend(_macs_and_ifaces_from_networksetup_macos())
        candidates.extend(_macs_and_ifaces_from_ifconfig())
    else:
        # Generic fallbacks
        candidates.extend(_macs_and_ifaces_from_ifconfig())
        candidates.extend(_macs_and_ifaces_from_ip_link())

    # Fallback: include uuid.getnode() if nothing else found and it looks like a real MAC
    try:
        import uuid

        node = uuid.getnode()
        if node is not None and isinstance(node, int) and node != 0:
            mac_hex = f"{node:012x}"
            first_octet = int(mac_hex[0:2], 16)
            is_multicast = (first_octet & 1) == 1
            mac = normalize_mac(mac_hex)
            if mac and not is_multicast:
                candidates.append((mac, None))
    except Exception:
        pass

    # Normalize, filter empties (parsers already normalize, but be defensive)
    normalized: List[Tuple[str, Optional[str]]] = []
    for mac, iface in candidates:
        nmac = normalize_mac(mac)
        if nmac:
            normalized.append((nmac, iface))

    # Deduplicate by MAC, preserving order; keep the first interface name we saw
    pairs = _uniq_preserve_by_mac(normalized)
    return pairs

def get_all_mac_addresses() -> List[str]:
    pairs = get_all_mac_addresses_with_interfaces()
    return [mac for mac, _ in pairs]


def main() -> None:
    system_name = platform.node() or socket.gethostname()
    mac_addresses = get_all_mac_addresses()

    result = {
        "system_name": system_name,
        "mac_addresses": mac_addresses,
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()