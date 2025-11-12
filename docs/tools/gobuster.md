# goBuster
scans a webserver to brute force valid paths

https://github.com/OJ/gobuster

# Installation

# MacOS
    brew install gobuster

# Debian
    apt install gobuster

# Examples

# Basic scan
    gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 10 --url http://192.168.211.35/

## Another scan
    sudo gobuster dir --expanded --url http://$target --useragent "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" --output scan_results.gobuster --wordlist /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-big.txt --extensions php,htm,html,txt

The extension filter can be helpful, but be carefull about making it to restrictive and missing files

**--expand** \
**--includelength** \
**--url** \
**-a** Set the User-Agent string \
**--output** \
**--wordlist** \
**--extensions** \

# Help output
```
help output
```