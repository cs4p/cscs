# dirsearch

## Overview
dirsearch is a powerful command-line tool for web content discovery and directory/file brute-forcing. Written in Python, it's designed to find hidden paths, directories, and files on web servers through dictionary-based enumeration.

## Installation

```bash
# Clone from GitHub
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch

# Install via pip
pip3 install dirsearch
```

## Basic Usage

```bash
# Basic scan
python3 dirsearch.py -u https://target.com

# Using pip installation
dirsearch -u https://target.com
```

## Common Options

| Option | Description |
|--------|-------------|
| `-u URL` | Target URL |
| `-l FILE` | URL list file |
| `-e EXTENSIONS` | Extensions list (e.g., php,html,js) |
| `-w WORDLIST` | Custom wordlist path |
| `-t THREADS` | Number of threads (default: 30) |
| `-r` | Recursive scan |
| `-R DEPTH` | Max recursion depth |
| `--exclude-status` | Exclude status codes (e.g., 404,403) |
| `--include-status` | Only include status codes |
| `-x EXTENSIONS` | Exclude extensions |
| `-i CODES` | Include status codes |
| `--random-agent` | Use random User-Agent |
| `-H HEADER` | Add custom header |
| `--cookie COOKIE` | Add cookie |
| `-o FILE` | Output file |
| `--format FORMAT` | Output format (simple, json, xml, md, csv, html) |

## Examples

### Basic Enumeration
```bash
# Scan with common extensions
dirsearch -u https://target.com -e php,html,js,txt

# Scan multiple targets
dirsearch -l urls.txt -e php,asp,aspx
```

### Custom Wordlists
```bash
# Use custom wordlist
dirsearch -u https://target.com -w /usr/share/wordlists/dirb/common.txt

# Combine with extensions
dirsearch -u https://target.com -w custom.txt -e php,bak,old
```

### Recursive Scanning
```bash
# Recursive scan with depth limit
dirsearch -u https://target.com -r -R 3

# Recursive with specific extensions
dirsearch -u https://target.com -r -e php,html
```

### Filtering Results
```bash
# Exclude specific status codes
dirsearch -u https://target.com --exclude-status 404,403,500

# Include only specific status codes
dirsearch -u https://target.com -i 200,301,302

# Exclude response sizes
dirsearch -u https://target.com --exclude-sizes 1234,5678
```

### Authentication & Headers
```bash
# Add custom headers
dirsearch -u https://target.com -H "Authorization: Bearer token123"

# Use cookies
dirsearch -u https://target.com --cookie "session=abc123"

# Random User-Agent
dirsearch -u https://target.com --random-agent

# HTTP authentication
dirsearch -u https://target.com --auth username:password
```

### Performance Tuning
```bash
# Increase threads
dirsearch -u https://target.com -t 50

# Add delay between requests (milliseconds)
dirsearch -u https://target.com --delay 100

# Set timeout
dirsearch -u https://target.com --timeout 10
```

### Output Options
```bash
# Save results to file
dirsearch -u https://target.com -o results.txt

# Save in JSON format
dirsearch -u https://target.com -o results.json --format json

# Save in multiple formats
dirsearch -u https://target.com -o results --format simple,json,html
```

### Advanced Techniques
```bash
# Follow redirects
dirsearch -u https://target.com --follow-redirects

# Scan with proxy
dirsearch -u https://target.com --proxy 127.0.0.1:8080

# Force extensions on all paths
dirsearch -u https://target.com -e php --force-extensions

# Scan subdirectories only
dirsearch -u https://target.com/admin/ -e php
```

## Useful Wordlists

- **Built-in**: dirsearch comes with default wordlists
- **SecLists**: `/usr/share/seclists/Discovery/Web-Content/`
  - `directory-list-2.3-medium.txt`
  - `common.txt`
  - `raft-large-files.txt`
- **Dirb**: `/usr/share/wordlists/dirb/`
- **Custom**: Create targeted wordlists based on target technology

## Tips & Tricks

1. **Start with small wordlists** to quickly identify low-hanging fruit
2. **Use extensions wisely** - identify the web server technology first
3. **Monitor status codes** - 403 may indicate existing but forbidden resources
4. **Check response sizes** - identical sizes may indicate false positives
5. **Use recursive scanning carefully** - can generate many requests
6. **Adjust threads based on target** - too many threads may trigger WAF/rate limiting
7. **Combine with other tools** - use alongside nikto, gobuster, or ffuf
8. **Save your results** - always output to file for later analysis

## Common Status Codes

- **200**: Found - resource exists and is accessible
- **301/302**: Redirect - may lead to interesting locations
- **401**: Unauthorized - authentication required
- **403**: Forbidden - exists but access denied
- **404**: Not Found - resource doesn't exist
- **500**: Internal Server Error - may indicate vulnerable endpoint

## Comparison with Similar Tools

| Feature | dirsearch | gobuster | ffuf |
|---------|-----------|----------|------|
| Speed | Fast | Fastest | Fastest |
| Language | Python | Go | Go |
| Recursion | Yes | Limited | Yes |
| Ease of Use | Easy | Easy | Moderate |
| Features | Rich | Minimal | Very Rich |

## References

- **GitHub**: https://github.com/maurosoria/dirsearch
- **Documentation**: https://github.com/maurosoria/dirsearch/wiki
