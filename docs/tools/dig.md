# Dig

Dig (Domain Information Groper) is a powerful command-line tool for querying DNS nameservers. It's used for network troubleshooting, DNS diagnostics, and information gathering during reconnaissance.

* https://linux.die.net/man/1/dig
* https://www.isc.org/bind/

# Installation

## MacOS
```bash
brew install bind
```

## Debian
```bash
sudo apt install dnsutils
```

# Examples

## Basic query
```bash
dig example.com
```

## Query specific record type
```bash
dig example.com A
dig example.com MX
dig example.com NS
```

## Short answer only
```bash
dig example.com +short
```

## Reverse DNS lookup
```bash
dig -x 8.8.8.8
```

## Trace delegation path
```bash
dig example.com +trace
```

## Query specific DNS server
```bash
dig @8.8.8.8 example.com
```

# Common Record Types

| Type | Description |
|------|-------------|
| `A` | IPv4 address |
| `AAAA` | IPv6 address |
| `MX` | Mail exchange servers |
| `NS` | Nameservers |
| `CNAME` | Canonical name (alias) |
| `TXT` | Text records |
| `SOA` | Start of authority |
| `PTR` | Pointer (reverse DNS) |
| `SRV` | Service records |
| `CAA` | Certification authority authorization |

## Common Options

| Option | Description |
|--------|-------------|
| `+short` | Short output (answer only) |
| `+noall +answer` | Only show answer section |
| `@server` | Query specific DNS server |
| `-x IP` | Reverse DNS lookup |
| `+trace` | Trace delegation path |
| `+dnssec` | Request DNSSEC records |
| `-4` | Force IPv4 |
| `-6` | Force IPv6 |
| `-p PORT` | Use specific port |

## Examples

### Basic Queries
```bash
# Get A record
dig example.com A

# Get all records
dig example.com ANY

# Short answer only
dig example.com +short

# Clean output (answer only)
dig example.com +noall +answer
```

### Specific DNS Servers
```bash
# Query Google DNS
dig @8.8.8.8 example.com

# Query Cloudflare DNS
dig @1.1.1.1 example.com

# Query specific nameserver
dig @ns1.example.com example.com
```

### Mail Records
```bash
# Get MX records
dig example.com MX

# Short format
dig example.com MX +short

# Get MX with priority
dig example.com MX +noall +answer
```

### Nameserver Queries
```bash
# Get nameservers
dig example.com NS

# Get SOA record
dig example.com SOA

# Get nameservers from root
dig example.com NS @a.root-servers.net
```

### Reverse DNS Lookup
```bash
# Reverse lookup
dig -x 8.8.8.8

# Short format
dig -x 8.8.8.8 +short

# Query specific server
dig -x 8.8.8.8 @1.1.1.1
```

### DNS Tracing
```bash
# Trace delegation path
dig example.com +trace

# Trace with short output
dig example.com +trace +short

# Trace specific record type
dig example.com MX +trace
```

### TXT Records
```bash
# Get TXT records (SPF, DKIM, etc.)
dig example.com TXT

# Get specific subdomain TXT
dig _dmarc.example.com TXT

# SPF records
dig example.com TXT | grep spf
```

### DNSSEC Queries
```bash
# Request DNSSEC validation
dig example.com +dnssec

# Check DNSKEY records
dig example.com DNSKEY

# Check DS records
dig example.com DS
```

### Advanced Queries
```bash
# Query with TCP instead of UDP
dig example.com +tcp

# Set custom timeout
dig example.com +time=5

# Set number of retries
dig example.com +tries=3

# Show query time statistics
dig example.com +stats

# Verbose output
dig example.com +qr
```

### Zone Transfer (AXFR)
```bash
# Attempt zone transfer
dig @ns1.example.com example.com AXFR

# Zone transfer with specific nameserver
dig @dns.example.com example.com AXFR

# Note: Most nameservers block unauthorized zone transfers

# Zone transfer with text-fu to grab the domains as a list
dig @dns.example.com example.com axfr | grep -oE '(\w+\.)?\w+\.com' | sort -u
```

### Batch Queries
```bash
# Query multiple domains
dig example.com google.com github.com

# Query from file
dig -f domains.txt

# Query multiple record types
dig example.com A MX NS
```

## Output Format

```
; <<>> DiG 9.18.1 <<>> example.com
;; QUESTION SECTION:
;example.com.			IN	A

;; ANSWER SECTION:
example.com.		3600	IN	A	93.184.216.34

;; Query time: 20 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Mon Dec 23 10:30:00 UTC 2024
;; MSG SIZE  rcvd: 56
```

### Understanding Output Sections
- **QUESTION**: The query sent
- **ANSWER**: The response from DNS
- **AUTHORITY**: Authoritative nameservers
- **ADDITIONAL**: Additional information (glue records, etc.)

## Useful Combinations

### DNS Reconnaissance
```bash
# Get all important records
dig example.com ANY +noall +answer
dig example.com NS +short
dig example.com MX +short
dig example.com TXT +short

# Check nameservers
for ns in $(dig example.com NS +short); do
  echo "=== $ns ==="
  dig @$ns example.com
done
```

### Compare DNS Servers
```bash
# Compare responses from different servers
dig @8.8.8.8 example.com +short
dig @1.1.1.1 example.com +short
dig @208.67.222.222 example.com +short
```

### DNS Propagation Check
```bash
# Check multiple authoritative nameservers
for ns in $(dig example.com NS +short); do
  echo "Server: $ns"
  dig @$ns example.com A +short
done
```

## Common DNS Servers

| Provider | IPv4 | IPv6 |
|----------|------|------|
| Google | 8.8.8.8, 8.8.4.4 | 2001:4860:4860::8888 |
| Cloudflare | 1.1.1.1, 1.0.0.1 | 2606:4700:4700::1111 |
| Quad9 | 9.9.9.9 | 2620:fe::fe |
| OpenDNS | 208.67.222.222 | 2620:119:35::35 |

## Tips & Tricks

1. **Use +short for scripting** - Clean output for parsing
2. **Check multiple DNS servers** - Verify propagation
3. **Use +trace for delegation issues** - Debug DNS hierarchy
4. **Try AXFR on new targets** - Misconfigured servers may allow zone transfers
5. **Check TXT records** - Often contain useful information (SPF, DKIM, verification tokens)
6. **Use @server to bypass local DNS** - Get fresh results
7. **Check both IPv4 and IPv6** - Some records may differ
8. **Look for CNAMEs** - Can reveal infrastructure (CDN, cloud providers)

# Help output
```
Usage:  dig [@global-server] [domain] [q-type] [q-class] {q-opt}
```
