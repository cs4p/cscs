import os
from pathlib import Path
import requests

OWNER = "ohmyzsh"
REPO = "ohmyzsh"
BRANCH = "master"  # or "main" if a repo uses main
BASE_RAW = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/plugins"

CANDIDATES = ("README.md", "README.plugin.md")


def fetch_text(url: str, timeout: float = 15.0) -> str | None:
    r = requests.get(url, timeout=timeout)
    if r.status_code == 200:
        return r.text
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return None


def download_plugin_readme(plugin: str, out_dir: Path) -> Path | None:
    out_dir.mkdir(parents=True, exist_ok=True)

    for name in CANDIDATES:
        url = f"{BASE_RAW}/{plugin}/{name}"
        text = fetch_text(url)
        if text is not None:
            out_path = out_dir / f"{plugin}-{name}"
            out_path.write_text(text, encoding="utf-8")
            return out_path

    return None


def main() -> None:
    plugins = ["1password", "asdf", "aliases", "alias-finder", "common-aliases", "command-not-found", "docker", "git", "kubectl", "nmap", "pip", "python", "sudo", "themes", "tailscale"]
    out_dir = Path("ohmyzsh-plugin-readmes")

    saved = 0
    missing = []

    for p in plugins:
        result = download_plugin_readme(p, out_dir)
        if result:
            print(f"saved: {result}")
            saved += 1
        else:
            print(f"missing README: {p}")
            missing.append(p)

    print(f"\nDone. Saved {saved}/{len(plugins)} readmes.")
    if missing:
        print("No README found for:", ", ".join(missing))


if __name__ == "__main__":
    main()
