# Netcat
swiss army knife for tcp communication. Can both listen and send

https://github.com/tlmader/netcat

# Installation
## MacOS
    brew install netcat
## Debian
    apt install netcat

# Examples

## Open a listener on port 443
    sudo nc -lvp 443
## Open a listener on port 80 and log the connections
    sudo nc -lvp 80 -o web_log.txt -k
NOTE: the **-k** option only works in linux, not the macOS version installed by Homebrew. It keeps the netcat listener open instead of closing after the first connection.

# Help output
```
help output
```