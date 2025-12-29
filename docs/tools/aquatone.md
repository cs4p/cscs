# Aquatone

## Overview
Aquatone is a tool for visual reconnaissance of websites across large numbers of hosts. It takes screenshots of web pages, generates reports, and helps identify interesting targets during reconnaissance. It's particularly useful for quickly assessing large numbers of domains or IP addresses.

## Installation

```bash
# Download latest release
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip

# Extract
unzip aquatone_linux_amd64_1.7.0.zip

# Make executable
chmod +x aquatone

# Move to PATH (optional)
sudo mv aquatone /usr/local/bin/

# Install dependencies
sudo apt install chromium-browser
```

## Basic Usage

```bash
# From subdomain list
cat domains.txt | aquatone

# From nmap XML
cat nmap.xml | aquatone -nmap

# Specify output directory
cat domains.txt | aquatone -out ./results
```

## Common Options

| Option | Description |
|--------|-------------|
| `-chrome-path PATH` | Path to Chrome/Chromium executable |
| `-out DIR` | Output directory (default: ./aquatone) |
| `-ports` | Ports to scan (default: 80,443,8000,8080,8443) |
| `-scan-timeout` | Timeout for port scans (default: 100ms) |
| `-screenshot-timeout` | Timeout for screenshots (default: 30s) |
| `-threads` | Number of threads (default: number of CPUs) |
| `-http-timeout` | HTTP request timeout (default: 3s) |
| `-resolution` | Screenshot resolution (default: 1440,900) |
| `-save-body` | Save response bodies |
| `-proxy` | Proxy URL (e.g., http://127.0.0.1:8080) |
| `-session` | Load previous session |
| `-nmap` | Parse Nmap/Masscan XML |
| `-silent` | Suppress all output except errors |

## Examples

### Basic Subdomain Enumeration
```bash
# From subdomain enumeration tool
subfinder -d example.com | aquatone

# From multiple tools
cat subdomains.txt | aquatone -out example_recon

# With custom ports
cat domains.txt | aquatone -ports 80,443,8000,8080,8443,3000
```

### From Nmap/Masscan Results
```bash
# From Nmap XML
nmap -iL targets.txt -oX scan.xml
cat scan.xml | aquatone -nmap

# From Masscan
masscan -p80,443,8080 10.0.0.0/8 -oX scan.xml
cat scan.xml | aquatone -nmap
```

### Performance Tuning
```bash
# Increase threads
cat domains.txt | aquatone -threads 10

# Adjust timeouts
cat domains.txt | aquatone -scan-timeout 500 -screenshot-timeout 60000

# Custom resolution
cat domains.txt | aquatone -resolution 1920,1080
```

### With Proxy
```bash
# Through Burp Suite
cat domains.txt | aquatone -proxy http://127.0.0.1:8080

# Through custom proxy
cat domains.txt | aquatone -proxy http://proxy.example.com:3128
```

### Save Response Bodies
```bash
# Save HTML responses
cat domains.txt | aquatone -save-body

# Useful for later analysis or grep
grep -r "admin" aquatone/html/
```

### Session Management
```bash
# Resume previous session
aquatone -session aquatone/session.json

# Useful if scan was interrupted
```

## Output Files

Aquatone creates several files in the output directory:

| File | Description |
|------|-------------|
| `aquatone_report.html` | Main HTML report with screenshots |
| `aquatone_urls.txt` | List of discovered URLs |
| `aquatone_session.json` | Session data for resuming |
| `screenshots/` | Directory containing screenshots |
| `html/` | Response bodies (if -save-body used) |
| `headers/` | Response headers |

## Integration with Other Tools

### With Subfinder
```bash
# Find subdomains and screenshot
subfinder -d example.com -silent | aquatone -out example_screenshots
```

### With Amass
```bash
# Comprehensive subdomain enumeration
amass enum -d example.com | aquatone -out amass_recon
```

### With Assetfinder
```bash
# Quick subdomain discovery
assetfinder --subs-only example.com | aquatone
```

### With Httprobe
```bash
# Verify alive hosts first
cat subdomains.txt | httprobe | aquatone
```

### With Masscan
```bash
# Large-scale IP scanning
masscan -p80,443,8080,8443 10.0.0.0/8 --rate 10000 -oX scan.xml
cat scan.xml | aquatone -nmap -out masscan_results
```

### With Nuclei
```bash
# First screenshot, then vulnerability scan
cat domains.txt | aquatone
cat aquatone/aquatone_urls.txt | nuclei -t cves/
```

## Workflow Examples

### Complete Subdomain Reconnaissance
```bash
#!/bin/bash
DOMAIN="example.com"
OUTPUT="recon_${DOMAIN}"

# Step 1: Subdomain enumeration
subfinder -d $DOMAIN -silent > subs.txt
amass enum -passive -d $DOMAIN >> subs.txt
assetfinder --subs-only $DOMAIN >> subs.txt

# Step 2: Remove duplicates
sort -u subs.txt -o subs.txt

# Step 3: Probe for alive hosts
cat subs.txt | httprobe > alive.txt

# Step 4: Screenshot with Aquatone
cat alive.txt | aquatone -out $OUTPUT -threads 5

# Step 5: Review report
firefox $OUTPUT/aquatone_report.html
```

### Port-based Web Discovery
```bash
#!/bin/bash
# Scan common web ports and screenshot

TARGET="10.0.0.0/24"
PORTS="80,443,8000,8080,8443,3000,5000,8888,9000"

# Masscan for speed
masscan -p$PORTS $TARGET --rate 1000 -oX scan.xml

# Aquatone for screenshots
cat scan.xml | aquatone -nmap -out port_scan_results
```

### Cloud Asset Discovery
```bash
# Find cloud assets for organization
echo "example.com" | subfinder -silent | \
  grep -E '(amazonaws\.com|cloudfront\.net|azurewebsites\.net|storage\.googleapis\.com)' | \
  aquatone -out cloud_assets
```

## Report Analysis

The HTML report includes:
- **Screenshot gallery** - Visual overview of all sites
- **HTTP headers** - Response headers for each host
- **Technologies** - Detected technologies (via Wappalyzer)
- **Response codes** - HTTP status codes
- **Page titles** - HTML title tags
- **Interesting headers** - Security headers, server info

### Identifying Interesting Targets
Look for:
- Login pages
- Admin panels
- Dashboard interfaces
- Development/staging servers
- Default installations
- Error messages revealing info
- Unusual ports or services

## Tips & Tricks

1. **Start with small lists** - Test on subset before full run
2. **Use httprobe first** - Filter to only alive hosts
3. **Adjust timeouts for slow networks** - Increase if many failures
4. **Save response bodies** - Useful for post-analysis with grep
5. **Review screenshots manually** - Automated tools miss context
6. **Look for patterns** - Similar screenshots may indicate default configs
7. **Check unusual ports** - Often less hardened
8. **Use with proxy** - Capture all traffic in Burp for later analysis
9. **Resume sessions** - Don't waste time on interrupted scans
10. **Filter subdomains** - Focus on interesting TLDs or patterns

## Common Issues

### Chrome/Chromium Not Found
```bash
# Specify Chrome path
aquatone -chrome-path /usr/bin/chromium-browser

# Or install Chromium
sudo apt install chromium-browser
```

### Timeout Issues
```bash
# Increase timeouts for slow targets
cat domains.txt | aquatone -screenshot-timeout 60000 -http-timeout 10000
```

### Too Many Threads
```bash
# Reduce threads if system is overwhelmed
cat domains.txt | aquatone -threads 2
```

### Large Result Sets
```bash
# Process in chunks
split -l 100 domains.txt chunk_
for file in chunk_*; do
  cat $file | aquatone -out results_$file
done
```

## Security Considerations

- **Respect scope** - Only scan authorized targets
- **Rate limiting** - Adjust threads to avoid DoS
- **Legal compliance** - Ensure permission before scanning
- **Network impact** - Large scans can be noisy
- **Data handling** - Screenshots may contain sensitive data

## Alternatives

| Tool | Description | Use Case |
|------|-------------|----------|
| **EyeWitness** | Similar to Aquatone, Python-based | More reporting options |
| **Gowitness** | Go-based, faster | Large-scale screenshots |
| **WebScreenshot** | Python, simple | Basic screenshot needs |
| **HttpScreenshot** | Nmap script | Quick Nmap integration |

## Comparison

| Feature | Aquatone | EyeWitness | Gowitness |
|---------|----------|------------|-----------|
| Language | Go | Python | Go |
| Speed | Fast | Medium | Fastest |
| Report Quality | Excellent | Good | Good |
| Ease of Use | Easy | Easy | Easy |
| Maintenance | Limited | Active | Active |
| Dependencies | Minimal | Many | Minimal |

## Post-Processing

### Extract Specific Technologies
```bash
# Find WordPress sites
grep -i wordpress aquatone/aquatone_session.json

# Find specific headers
grep -r "X-Powered-By: PHP" aquatone/headers/
```

### Find Login Pages
```bash
# Search HTML for login indicators
grep -ri "login\|sign in\|password" aquatone/html/
```

### Organize by Status Code
```bash
# Extract URLs by response code
jq -r '.pages[] | select(.status==200) | .url' aquatone/aquatone_session.json
```

## References

- **GitHub**: https://github.com/michenriksen/aquatone
- **Blog Post**: https://michenriksen.com/blog/aquatone-visual-inspection-of-websites/
