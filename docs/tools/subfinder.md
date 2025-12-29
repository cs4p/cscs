# Subfinder

Subfinder is a subdomain discovery tool that discovers valid subdomains for websites by using passive online sources. It's designed to be fast, simple, and modular, making it ideal for automated workflows and reconnaissance.

* https://github.com/projectdiscovery/subfinder
* https://docs.projectdiscovery.io/tools/subfinder

# Installation

## MacOS
```bash
brew install subfinder
```

## Debian
```bash
sudo apt install subfinder
```

## Go
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

# Examples

## Basic subdomain enumeration
```bash
subfinder -d example.com
```

## Multiple domains
```bash
subfinder -d example.com,test.com
```

## Silent mode (output only)
```bash
subfinder -d example.com -silent
```

## Use all sources (thorough)
```bash
subfinder -d example.com -all
```

# Common Options

| Option | Description |
|--------|-------------|
| `-d DOMAIN` | Domain to find subdomains for |
| `-dL FILE` | File containing list of domains |
| `-silent` | Show only subdomains in output |
| `-o FILE` | Output file |
| `-oJ` | JSON output |
| `-oD DIR` | Output directory for results |
| `-nW` | Remove wildcard subdomains |
| `-r RESOLVERS` | Comma-separated list of resolvers |
| `-rL FILE` | File containing resolver list |
| `-t THREADS` | Number of concurrent threads (default: 10) |
| `-timeout INT` | Timeout in seconds (default: 30) |
| `-max-time INT` | Max time for enumeration in minutes |
| `-v` | Verbose output |
| `-all` | Use all sources (slow but thorough) |
| `-recursive` | Recursive subdomain enumeration |
| `-active` | Active DNS resolution |

## Data Sources

Subfinder uses multiple passive sources:
- **AlienVault**
- **AnubisDB**
- **BeVigil**
- **BinaryEdge**
- **Censys**
- **CertSpotter**
- **Chaos**
- **Chinaz**
- **DNSDB**
- **DNSDumpster**
- **Fofa**
- **FullHunt**
- **GitHub**
- **HackerTarget**
- **Intelx**
- **PassiveTotal**
- **RapidDNS**
- **SecurityTrails**
- **Shodan**
- **ThreatBook**
- **VirusTotal**
- **WhoisXML API**
- **ZoomEye**

## Examples

### Basic Enumeration
```bash
# Single domain
subfinder -d example.com

# Multiple domains
subfinder -d example.com,target.com,test.com

# From domain list
subfinder -dL domains.txt

# Save to file
subfinder -d example.com -o subdomains.txt
```

### Silent Mode
```bash
# Only output subdomains (no banner)
subfinder -d example.com -silent

# Silent with output file
subfinder -d example.com -silent -o output.txt

# Perfect for piping
subfinder -d example.com -silent | httpx
```

### Remove Wildcards
```bash
# Filter out wildcard DNS entries
subfinder -d example.com -nW

# Combine with silent mode
subfinder -d example.com -silent -nW
```

### Using All Sources
```bash
# Use all configured sources (slower but more complete)
subfinder -d example.com -all

# With verbose output to see sources used
subfinder -d example.com -all -v
```

### Recursive Enumeration
```bash
# Find subdomains of subdomains
subfinder -d example.com -recursive

# Recursive with depth limit
subfinder -d example.com -recursive -max-time 10
```

### JSON Output
```bash
# Output in JSON format
subfinder -d example.com -oJ -o results.json

# Multiple domains to JSON
subfinder -dL domains.txt -oJ -o all_results.json
```

### Custom Resolvers
```bash
# Use specific DNS resolvers
subfinder -d example.com -r 8.8.8.8,1.1.1.1

# From resolver file
subfinder -d example.com -rL resolvers.txt
```

### Performance Tuning
```bash
# Increase threads
subfinder -d example.com -t 50

# Set timeout
subfinder -d example.com -timeout 60

# Limit max time
subfinder -d example.com -max-time 5
```

### Active Resolution
```bash
# Actively verify subdomains
subfinder -d example.com -active

# Active with custom resolvers
subfinder -d example.com -active -r 8.8.8.8,1.1.1.1
```

## Configuration

### API Keys Setup

```bash
# Create config directory
mkdir -p ~/.config/subfinder

# Edit provider config
nano ~/.config/subfinder/provider-config.yaml
```

Example `provider-config.yaml`:
```yaml
binaryedge:
  - YOUR_API_KEY
censys:
  - YOUR_API_ID:YOUR_API_SECRET
certspotter:
  - YOUR_API_KEY
chaos:
  - YOUR_API_KEY
dnsdb:
  - YOUR_API_KEY
fofa:
  - YOUR_EMAIL:YOUR_API_KEY
fullhunt:
  - YOUR_API_KEY
github:
  - YOUR_API_KEY
intelx:
  - YOUR_API_KEY
passivetotal:
  - YOUR_EMAIL:YOUR_API_KEY
securitytrails:
  - YOUR_API_KEY
shodan:
  - YOUR_API_KEY
threatbook:
  - YOUR_API_KEY
virustotal:
  - YOUR_API_KEY
whoisxmlapi:
  - YOUR_API_KEY
zoomeye:
  - YOUR_EMAIL:YOUR_API_KEY
```

### Getting API Keys

Most sources offer free API keys:
- **GitHub**: https://github.com/settings/tokens
- **Shodan**: https://account.shodan.io/
- **VirusTotal**: https://www.virustotal.com/gui/my-apikey
- **Censys**: https://censys.io/account/api
- **SecurityTrails**: https://securitytrails.com/app/account/credentials
- **Chaos**: https://chaos.projectdiscovery.io/

## Integration with Other Tools

### With Httpx (Probe Alive Hosts)
```bash
# Find subdomains and check which are alive
subfinder -d example.com -silent | httpx -silent

# With status codes
subfinder -d example.com -silent | httpx -status-code
```

### With Nuclei (Vulnerability Scanning)
```bash
# Find subdomains and scan for vulnerabilities
subfinder -d example.com -silent | httpx -silent | nuclei -t cves/
```

### With Aquatone (Screenshots)
```bash
# Find subdomains and take screenshots
subfinder -d example.com -silent | aquatone -out recon_output
```

### With Nmap (Port Scanning)
```bash
# Find subdomains and port scan
subfinder -d example.com -silent > subs.txt
nmap -iL subs.txt -oA scan_results
```

### With Ffuf (Directory Brute Force)
```bash
# Find subdomains and brute force directories
for sub in $(subfinder -d example.com -silent); do
  ffuf -u https://$sub/FUZZ -w wordlist.txt
done
```

### With Amass (Correlation)
```bash
# Combine with Amass for better coverage
subfinder -d example.com -silent > subfinder.txt
amass enum -d example.com -o amass.txt
cat subfinder.txt amass.txt | sort -u > all_subs.txt
```

### With Dnsx (DNS Resolution)
```bash
# Resolve and filter valid subdomains
subfinder -d example.com -silent | dnsx -silent

# With A records
subfinder -d example.com -silent | dnsx -a -resp
```

## Workflow Examples

### Complete Subdomain Reconnaissance
```bash
#!/bin/bash
DOMAIN="example.com"
OUTPUT_DIR="recon_${DOMAIN}"
mkdir -p $OUTPUT_DIR

# Subdomain enumeration
echo "[*] Running subfinder..."
subfinder -d $DOMAIN -all -silent -o $OUTPUT_DIR/subdomains.txt

# Resolve subdomains
echo "[*] Resolving subdomains..."
cat $OUTPUT_DIR/subdomains.txt | dnsx -silent -a -resp -o $OUTPUT_DIR/resolved.txt

# Probe alive hosts
echo "[*] Probing alive hosts..."
cat $OUTPUT_DIR/resolved.txt | httpx -silent -o $OUTPUT_DIR/alive.txt

# Screenshot
echo "[*] Taking screenshots..."
cat $OUTPUT_DIR/alive.txt | aquatone -out $OUTPUT_DIR/screenshots

echo "[*] Done! Results in $OUTPUT_DIR/"
```

### Multi-Domain Enumeration
```bash
#!/bin/bash
# Process multiple domains

cat domains.txt | while read domain; do
  echo "[*] Processing $domain"
  subfinder -d $domain -silent -o "results_${domain}.txt"
done

# Combine all results
cat results_*.txt | sort -u > all_subdomains.txt
```

### Continuous Monitoring
```bash
#!/bin/bash
# Monitor for new subdomains

DOMAIN="example.com"
OLD_FILE="old_subs.txt"
NEW_FILE="new_subs.txt"

# Run subfinder
subfinder -d $DOMAIN -silent -o $NEW_FILE

# Compare with previous results
if [ -f $OLD_FILE ]; then
  comm -13 <(sort $OLD_FILE) <(sort $NEW_FILE) > diff.txt

  if [ -s diff.txt ]; then
    echo "[!] New subdomains found:"
    cat diff.txt
    # Send notification, webhook, etc.
  fi
fi

# Update old file
cp $NEW_FILE $OLD_FILE
```

### Cloud Asset Discovery
```bash
# Find cloud-hosted subdomains
subfinder -d example.com -silent | \
  grep -E '(amazonaws\.com|azurewebsites\.net|cloudapp\.net|googleapis\.com)' | \
  tee cloud_assets.txt
```

## Output Formats

### Text Output (Default)
```bash
subfinder -d example.com -o output.txt
```

### JSON Output
```bash
# Structured JSON output
subfinder -d example.com -oJ -o output.json

# Parse with jq
subfinder -d example.com -oJ | jq -r '.host'
```

### Directory Output
```bash
# Save each domain to separate file
subfinder -dL domains.txt -oD results/
```

## Tips & Tricks

1. **Use API keys** - Significantly increases results
2. **Combine tools** - Use with amass, assetfinder for better coverage
3. **Monitor regularly** - Run periodically to find new subdomains
4. **Filter wildcards** - Use `-nW` to reduce noise
5. **Use silent mode** - Perfect for piping to other tools
6. **Verify results** - Use httpx or dnsx to validate
7. **Check recursively** - Find subdomains of subdomains
8. **Save raw results** - Keep JSON output for later analysis
9. **Use all sources** - `-all` flag for comprehensive results
10. **Rate limiting** - Respect API limits with timeouts

## Common Issues

### No Results
```bash
# Try with all sources
subfinder -d example.com -all -v

# Check if API keys are configured
cat ~/.config/subfinder/provider-config.yaml

# Try with specific sources
subfinder -d example.com -sources certspotter,crtsh
```

### Timeout Issues
```bash
# Increase timeout
subfinder -d example.com -timeout 60

# Set max time
subfinder -d example.com -max-time 10
```

### Rate Limiting
```bash
# Reduce threads
subfinder -d example.com -t 5

# Add delay between requests (not directly supported, use wrapper script)
```

## Comparison with Alternatives

| Tool | Speed | Sources | Active DNS | Recursive |
|------|-------|---------|------------|-----------|
| **Subfinder** | Fast | 30+ | Optional | Yes |
| **Amass** | Slow | 50+ | Yes | Yes |
| **Assetfinder** | Very Fast | 10+ | No | No |
| **Findomain** | Fast | 20+ | Optional | No |
| **Sublist3r** | Medium | 10+ | No | No |

## Best Practices

### For Bug Bounty
```bash
# Maximum coverage
subfinder -d target.com -all -recursive -silent | \
  dnsx -silent | \
  httpx -silent -tech-detect -status-code | \
  tee results.txt
```

### For Penetration Testing
```bash
# Quick and verified results
subfinder -d target.com -silent -nW | \
  dnsx -silent -a | \
  httpx -silent -title -status-code
```

### For Asset Discovery
```bash
# Comprehensive enumeration
subfinder -d company.com -all -recursive -oJ -o assets.json
```

## Performance Benchmarks

Typical performance (varies by domain):
- Small domain (< 100 subs): 30-60 seconds
- Medium domain (100-1000 subs): 1-3 minutes
- Large domain (1000+ subs): 5-10 minutes

With API keys: 2-5x more results

# Help output
```
subfinder -h
```
