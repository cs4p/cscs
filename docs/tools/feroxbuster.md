# Feroxbuster

Feroxbuster is a fast, simple, recursive content discovery tool written in Rust. It's designed for forced browsing and finding hidden files/directories on web servers. Known for its speed, recursion capabilities, and extensive filtering options.

* https://github.com/epi052/feroxbuster
* https://epi052.github.io/feroxbuster-docs/overview/

# Installation

## MacOS
```bash
brew install feroxbuster
```

## Debian
```bash
# Using apt (Kali Linux)
sudo apt install feroxbuster

# From GitHub releases
wget https://github.com/epi052/feroxbuster/releases/latest/download/feroxbuster_amd64.deb
sudo dpkg -i feroxbuster_amd64.deb
```

## Rust (Cargo)
```bash
cargo install feroxbuster
```

# Examples

## Basic scan
```bash
feroxbuster -u https://example.com
```

## With wordlist and extensions
```bash
feroxbuster -u https://example.com -w wordlist.txt -x php,html,txt
```

## Recursive scan
```bash
feroxbuster -u https://example.com -w wordlist.txt -r
```

## Limit recursion depth
```bash
feroxbuster -u https://example.com -w wordlist.txt -r -d 3
```

# Common Options

| Option | Description |
|--------|-------------|
| `-u URL` | Target URL |
| `-w WORDLIST` | Wordlist path |
| `-t THREADS` | Number of threads (default: 50) |
| `-r` | Enable recursion |
| `-d DEPTH` | Max recursion depth (default: 4) |
| `-x EXTENSIONS` | File extensions to search for |
| `-k` | Skip SSL certificate verification |
| `-n` | Don't scan recursively |
| `-o FILE` | Output file |
| `--json` | JSON output |
| `-s CODES` | Status codes to include (default: 200,204,301,302,307,308,401,403,405) |
| `-C CODES` | Status codes to filter out |
| `-S SIZE` | Response size to filter |
| `--filter-words N` | Filter responses with N words |
| `--filter-lines N` | Filter responses with N lines |
| `--filter-regex REGEX` | Filter by regex pattern |
| `-H HEADER` | Add custom header |
| `-a USER_AGENT` | Set User-Agent |
| `--random-agent` | Use random User-Agent |
| `-p PROXY` | Proxy URL |
| `--burp` | Use Burp proxy (127.0.0.1:8080) |
| `--burp-replay` | Replay responses in Burp |

## Examples

### Basic Enumeration
```bash
# Simple scan
feroxbuster -u https://example.com -w /usr/share/wordlists/dirb/common.txt

# With file extensions
feroxbuster -u https://example.com -w wordlist.txt -x php,html,txt
```

### Recursive Scanning
```bash
# Enable recursion
feroxbuster -u https://example.com -w wordlist.txt -r

# Limit recursion depth
feroxbuster -u https://example.com -w wordlist.txt -r -d 3

# Disable recursion explicitly
feroxbuster -u https://example.com -w wordlist.txt -n
```

### Performance Tuning
```bash
# Increase threads
feroxbuster -u https://example.com -w wordlist.txt -t 100

# Adjust timeout
feroxbuster -u https://example.com -w wordlist.txt --timeout 10

# Rate limiting
feroxbuster -u https://example.com -w wordlist.txt --rate-limit 100
```

### Status Code Filtering
```bash
# Only show 200 responses
feroxbuster -u https://example.com -w wordlist.txt -s 200

# Include multiple status codes
feroxbuster -u https://example.com -w wordlist.txt -s 200,301,302

# Exclude status codes
feroxbuster -u https://example.com -w wordlist.txt -C 404,403
```

### Size Filtering
```bash
# Filter by response size
feroxbuster -u https://example.com -w wordlist.txt -S 1234

# Filter multiple sizes
feroxbuster -u https://example.com -w wordlist.txt -S 1234,5678

# Filter by word count
feroxbuster -u https://example.com -w wordlist.txt --filter-words 42

# Filter by line count
feroxbuster -u https://example.com -w wordlist.txt --filter-lines 10
```

### Regex Filtering
```bash
# Filter responses matching regex
feroxbuster -u https://example.com -w wordlist.txt --filter-regex "not found"

# Filter 404 pages with custom messages
feroxbuster -u https://example.com -w wordlist.txt --filter-regex "Page not found|404"
```

### SSL/TLS Options
```bash
# Skip SSL verification
feroxbuster -u https://example.com -w wordlist.txt -k

# Force HTTP/2
feroxbuster -u https://example.com -w wordlist.txt --force-http2
```

### Authentication
```bash
# Basic auth
feroxbuster -u https://example.com -w wordlist.txt -a username:password

# Custom headers
feroxbuster -u https://example.com -w wordlist.txt -H "Authorization: Bearer token123"

# Cookies
feroxbuster -u https://example.com -w wordlist.txt -H "Cookie: session=abc123"

# Multiple headers
feroxbuster -u https://example.com -w wordlist.txt -H "Header1: value1" -H "Header2: value2"
```

### Proxy Usage
```bash
# Use proxy
feroxbuster -u https://example.com -w wordlist.txt -p http://127.0.0.1:8080

# Burp Suite shortcut
feroxbuster -u https://example.com -w wordlist.txt --burp

# Burp with replay
feroxbuster -u https://example.com -w wordlist.txt --burp --burp-replay
```

### User-Agent Manipulation
```bash
# Custom User-Agent
feroxbuster -u https://example.com -w wordlist.txt -a "Mozilla/5.0 Custom"

# Random User-Agent
feroxbuster -u https://example.com -w wordlist.txt --random-agent
```

### Output Options
```bash
# Save to file
feroxbuster -u https://example.com -w wordlist.txt -o results.txt

# JSON output
feroxbuster -u https://example.com -w wordlist.txt --json -o results.json

# Quiet mode (less output)
feroxbuster -u https://example.com -w wordlist.txt -q

# Silent mode (minimal output)
feroxbuster -u https://example.com -w wordlist.txt --silent
```

### Advanced Techniques
```bash
# Scan with specific methods
feroxbuster -u https://example.com -w wordlist.txt -m GET,POST

# Follow redirects
feroxbuster -u https://example.com -w wordlist.txt --redirects

# Collect words from responses
feroxbuster -u https://example.com -w wordlist.txt --collect-words

# Extract links
feroxbuster -u https://example.com -w wordlist.txt --extract-links

# Scan with delay
feroxbuster -u https://example.com -w wordlist.txt --scan-delay 100
```

## Wordlists

### Recommended Wordlists
```bash
# Small/Fast
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/raft-small-words.txt

# Medium (balanced)
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt

# Large (comprehensive)
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt
/usr/share/seclists/Discovery/Web-Content/raft-large-files.txt

# Technology-specific
/usr/share/seclists/Discovery/Web-Content/CMS/
/usr/share/seclists/Discovery/Web-Content/api/
```

## Configuration File

Create `~/.config/feroxbuster/ferox-config.toml`:

```toml
# Basic settings
threads = 50
wordlist = "/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt"
redirects = true
insecure = true

# Recursion
recursion_depth = 4
auto_tune = true

# Output
output = "ferox_output.txt"
```

### Use config file:
After built-in default values are set, any values defined in a ferox-config.toml config file will override the built-in defaults.

feroxbuster searches for ferox-config.toml in the following locations (in the order shown):

/etc/feroxbuster/ (global) \
CONFIG_DIR/feroxbuster/ (per-user) \
The same directory as the feroxbuster executable (per-user) \
The user’s current working directory (per-target) 

CONFIG_DIR is defined as the following:

Linux: $XDG_CONFIG_HOME or $HOME/.config i.e. /home/bob/.config \
MacOS: $HOME/Library/Application Support i.e. /Users/bob/Library/Application Support \
Windows: {FOLDERID_RoamingAppData} i.e. C:\Users\Bob\AppData\Roaming 

If more than one valid configuration file is found, each one overwrites the values found previously.

If no configuration file is found, nothing happens at this stage.

As an example, let’s say that we prefer to use a different wordlist as our default when scanning; we can set the wordlist value in the config file to override the baked-in default.

Notes of interest:

    it’s ok to only specify values you want to change without specifying anything else
    variable names in ferox-config.toml must match their command-line counterpart


## Integration with Other Tools

### With Subfinder/Amass
```bash
# Discover subdomains then scan each
subfinder -d example.com -silent | while read sub; do
  feroxbuster -u https://$sub -w wordlist.txt -q
done
```

### With Httpx
```bash
# Verify alive hosts first
subfinder -d example.com -silent | httpx -silent | while read url; do
  feroxbuster -u $url -w wordlist.txt
done
```

### With Nuclei
```bash
# Discover paths then scan for vulnerabilities
feroxbuster -u https://example.com -w wordlist.txt -q --json -o paths.json
jq -r '.url' paths.json | nuclei -t cves/
```

### With Burp Suite
```bash
# Send all requests through Burp
feroxbuster -u https://example.com -w wordlist.txt --burp --burp-replay
```

### With FFuf
```bash
# Use feroxbuster for directories, ffuf for parameters
feroxbuster -u https://example.com -w dirs.txt -q -o found_dirs.txt
cat found_dirs.txt | ffuf -u FUZZ -w params.txt
```

## Workflow Examples

### Complete Web Enumeration
```bash
#!/bin/bash
TARGET="https://example.com"
WORDLIST="/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt"
OUTPUT_DIR="ferox_results"

mkdir -p $OUTPUT_DIR

# Initial scan
echo "[*] Running initial scan..."
feroxbuster -u $TARGET -w $WORDLIST -r -d 3 -x php,html,txt \
  -o $OUTPUT_DIR/initial_scan.txt

# Deep scan on interesting paths
echo "[*] Deep scanning interesting paths..."
grep "200\|301" $OUTPUT_DIR/initial_scan.txt | awk '{print $1}' | while read path; do
  feroxbuster -u $path -w $WORDLIST -d 2 -o $OUTPUT_DIR/deep_$(echo $path | md5sum | cut -d' ' -f1).txt
done

echo "[*] Scan complete! Results in $OUTPUT_DIR/"
```

### Multi-Target Scan
```bash
#!/bin/bash
# Scan multiple targets from file

cat targets.txt | while read url; do
  echo "[*] Scanning $url"
  domain=$(echo $url | awk -F[/:] '{print $4}')
  feroxbuster -u $url -w wordlist.txt -r -d 2 -o "results_${domain}.txt"
done
```

### Bug Bounty Reconnaissance
```bash
#!/bin/bash
DOMAIN="target.com"
WORDLIST="/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt"

# Subdomain enumeration
subfinder -d $DOMAIN -silent > subs.txt

# Probe alive
cat subs.txt | httpx -silent > alive.txt

# Feroxbuster scan
cat alive.txt | while read url; do
  echo "[*] Scanning $url"
  feroxbuster -u $url -w $WORDLIST -r -d 2 \
    -x php,asp,aspx,jsp,html \
    --random-agent \
    -s 200,204,301,302,307,401,403 \
    -o "ferox_$(echo $url | md5sum | cut -d' ' -f1).txt"
done
```

### API Discovery
```bash
# API endpoint discovery
feroxbuster -u https://api.example.com \
  -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt \
  -x json,xml \
  -H "Authorization: Bearer token" \
  -s 200,201,400,401,403,500 \
  --json -o api_discovery.json
```

## Auto-Tuning and Auto-Bail

Feroxbuster includes smart features:

### Auto-Tune
Automatically adjusts scan speed based on errors:
```bash
feroxbuster -u https://example.com -w wordlist.txt --auto-tune
```

### Auto-Bail
Stops scanning directories with too many 404s:
```bash
feroxbuster -u https://example.com -w wordlist.txt --auto-bail
```

## Comparison with Similar Tools

| Feature | Feroxbuster | Gobuster | Dirb | Dirsearch |
|---------|-------------|----------|------|-----------|
| Language | Rust | Go | C | Python |
| Speed | Very Fast | Very Fast | Slow | Fast |
| Recursion | Excellent | Limited | Yes | Yes |
| Filtering | Extensive | Good | Basic | Good |
| Auto-tune | Yes | No | No | No |
| Config File | Yes | No | Yes | No |
| Active Dev | Yes | Yes | No | Yes |

## Tips & Tricks

1. **Start small** - Use small wordlist first to test
2. **Use recursion wisely** - Limit depth to avoid rabbit holes
3. **Filter aggressively** - Remove false positives early
4. **Monitor progress** - Watch for patterns in responses
5. **Use config files** - Save common settings
6. **Combine wordlists** - Merge multiple lists for coverage
7. **Check status codes** - 403 often means something exists
8. **Use extensions** - Target specific technologies
9. **Enable auto-tune** - Let feroxbuster optimize itself
10. **Save JSON output** - Easier to parse and analyze

## Common Issues

### Too Many False Positives
```bash
# Filter by size
feroxbuster -u https://example.com -w wordlist.txt -S 4242

# Filter by regex
feroxbuster -u https://example.com -w wordlist.txt --filter-regex "not found"

# Enable auto-bail
feroxbuster -u https://example.com -w wordlist.txt --auto-bail
```

### Connection Errors
```bash
# Reduce threads
feroxbuster -u https://example.com -w wordlist.txt -t 10

# Increase timeout
feroxbuster -u https://example.com -w wordlist.txt --timeout 15

# Add delay
feroxbuster -u https://example.com -w wordlist.txt --scan-delay 200
```

### SSL Errors
```bash
# Skip certificate verification
feroxbuster -u https://example.com -w wordlist.txt -k
```

### Rate Limiting
```bash
# Add rate limit
feroxbuster -u https://example.com -w wordlist.txt --rate-limit 50

# Add delay between requests
feroxbuster -u https://example.com -w wordlist.txt --scan-delay 100
```

## Interactive Commands

During scan, press:
- **ENTER**: Display current scan statistics
- **CTRL+C**: Cancel current scan, continue with others

## Output Format

```
200      GET       15l       30w      300c https://example.com/admin
301      GET        9l       28w      312c https://example.com/images => https://example.com/images/
403      GET        7l       10w      175c https://example.com/private
```

Format: `STATUS METHOD LINES WORDS SIZE URL [=> REDIRECT]`

## Best Practices

### For Penetration Testing
```bash
feroxbuster -u https://target.com \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
  -x php,html,txt,bak,old \
  -r -d 3 \
  -s 200,204,301,302,307,401,403,405 \
  --auto-tune --auto-bail \
  -o pentest_results.txt
```

### For Bug Bounty
```bash
feroxbuster -u https://target.com \
  -w wordlist.txt \
  -r -d 4 \
  -x php,asp,aspx,jsp,html,js \
  --random-agent \
  --collect-words \
  --extract-links \
  --json -o bounty_results.json
```

### For CTF/HackTheBox
```bash
feroxbuster -u http://target.htb \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -r -d 3 \
  -x php,txt,html,zip,bak \
  -k \
  -o ctf_results.txt
```

# Help output
```
feroxbuster - A fast, simple, recursive content discovery tool written in Rust.
```
