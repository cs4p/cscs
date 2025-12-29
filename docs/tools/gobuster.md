# Gobuster

Gobuster is a tool used to brute-force:
* URIs (directories and files) in web sites.
* DNS subdomains (with wildcard support).
* Virtual Host names on target web servers.
* Open Amazon S3 buckets.
* Open Google Cloud buckets.
* TFTP servers.

* https://github.com/OJ/gobuster

# Installation

## MacOS
```bash
brew install gobuster
```

## Debian
```bash
apt install gobuster
```

# Examples

## Directory and file brute-forcing
```bash
gobuster dir -u http://192.168.211.35/ -w /usr/share/wordlists/dirb/common.txt
```

## Scan with specific extensions and custom User-Agent
```bash
gobuster dir -u http://$target -w wordlist.txt -x php,html,txt -a "Mozilla/5.0"
```

## DNS subdomain brute-forcing
```bash
gobuster dns -d example.com -w subdomains.txt
```

## VHost brute-forcing
```bash
gobuster vhost -u http://example.com -w vhosts.txt
```

# Help output
```
Usage:
  gobuster [command]

Available Commands:
  dir         Uses directory/file enumeration mode
  dns         Uses DNS subdomain enumeration mode
  fuzz        Uses fuzzing mode
  gcs         Uses Google Cloud Storage bucket enumeration mode
  help        Help about any command
  s3          Uses AWS S3 bucket enumeration mode
  tftp        Uses TFTP enumeration mode
  vhost       Uses VHost enumeration mode
```