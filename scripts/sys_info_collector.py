#!/usr/bin/env python3
# Python 3.9+

import json
import platform
from typing import List, Iterable, Tuple, Optional, Set
import subprocess
import re
import socket

MAC_RE_STD = re.compile(r"^[0-9a-f]{2}(:[0-9a-f]{2}){5}$")

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

def uniq_preserve_by_mac(items: Iterable[Tuple[str, Optional[str]]]) -> List[Tuple[str, Optional[str]]]:
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

def macs_and_ifaces_from_networksetup_macos() -> List[Tuple[str, Optional[str]]]:
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
            if line.startswith("Hardware Port:"):
                device_name = line.split(":", 1)[1].strip()
            elif line.startswith("Device:"):
                device = line.split(":", 1)[1].strip()
            elif line.startswith("Ethernet Address:"):
                mac_raw = line.split(":", 1)[1].strip()
                mac = normalize_mac(mac_raw)
                if mac:
                    result.append((device_name, device, mac))
                device = None  # reset for safety
    except Exception:
        pass
    return result


def get_all_mac_addresses_with_interfaces() -> List[Tuple[str, Optional[str]]]:
    """
    Return a list of (mac, interface_name) tuples.
    interface_name may be None if it couldn't be determined for that MAC.
    The list is deduplicated by MAC while preserving the first-seen order.
    """
    system = platform.system().lower()

    if system == "windows":
        pass
    elif system == "linux":
        # Prefer sysfs as it's reliable, then cross-check with command outputs
        pass
    elif system == "darwin":
        return macs_and_ifaces_from_networksetup_macos()
    else:
        # Generic fallbacks
        pass

def main() -> None:
    system_name = platform.node() or socket.gethostname()
    mac_addresses = get_all_mac_addresses_with_interfaces()

    result = {
        "system_name": system_name,
        "mac_addresses": mac_addresses,
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()