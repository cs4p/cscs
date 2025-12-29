# LinPEAS

LinPEAS (Linux Privilege Escalation Awesome Script) is a script that searches for possible paths to escalate privileges on Linux/Unix*/MacOS hosts. It's part of the PEASS-ng (Privilege Escalation Awesome Scripts suite).

* https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
* https://github.com/carlospolop/PEASS-ng

# Installation

## Script
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh -o linpeas.sh
chmod +x linpeas.sh
```

## Alternative: wget
```bash
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
```

# Examples

## Basic execution
```bash
./linpeas.sh
```

## Run with output to file
```bash
./linpeas.sh | tee linpeas_output.txt
```

## Run with all checks (no skips)
```bash
./linpeas.sh -a
```

## Download and execute in memory
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```

# Key Features
- **System Information**: Kernel version, OS details, environment variables
- **Available Software**: Installed compilers, languages, and useful binaries
- **Processes & Cron**: Running processes, scheduled tasks, timers
- **Network Information**: Network interfaces, open ports, established connections
- **User Information**: Current user privileges, sudo rights, other users
- **File System**: SUID/SGID files, writable files, interesting files
- **Software Versions**: Detect vulnerable versions of installed software
- **Container Detection**: Identify if running inside a container
- **Cloud Detection**: Detect AWS, GCP, Azure instances and metadata

# Important Notes
- **Always get permission** before running on systems you don't own
- Review the output carefully - not all findings are exploitable
- Red/Yellow highlighted items are typically the most interesting
- Use `-a` flag for thorough checks (may take longer)
- Output can be very long - consider redirecting to a file
- Some checks require sudo/root privileges for complete results

# Help output
```
USAGE: ./linpeas.sh [options]

OPTIONS:
  -a      Execute all checks (default: false)
  -h      Display this help message
  -o <file>   Output to file (accepts file path or stdout)
  -p      Request password for sudo checks
  -q      Quiet mode, less output
  -s      Search for specific keywords in all files
  -n      Do not use colors
  -P      Indicate that linpeas is being run in a pentest

EXAMPLES:
  ./linpeas.sh -a              # Run all checks
  ./linpeas.sh -o output.txt   # Save output to file
  ./linpeas.sh -q -a           # Run all checks quietly
  ./linpeas.sh -p              # Request password for sudo checks
  ./linpeas.sh -n              # No colors
```
