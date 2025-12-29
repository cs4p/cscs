# Netstat

Netstat (network statistics) is a command-line network utility that displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

* https://man7.org/linux/man-pages/man8/netstat.8.html

# Installation

## MacOS
```bash
# Pre-installed on most versions
```

## Debian
```bash
sudo apt install net-tools
```

# Examples

## Show all listening ports
```bash
netstat -tuln
```

## Show all connections with PIDs
```bash
sudo netstat -tulnp
```

**-t** Show TCP connections

**-u** Show UDP connections

**-l** Show only listening sockets

**-n** Show numerical addresses (don't resolve hostnames)

**-p** Show process ID and program name

## Show all active connections
```bash
netstat -ant
```

## Display routing table
```bash
netstat -r
```

## Show network interface statistics
```bash
netstat -i
```

## Find which program is using a specific port
```bash
sudo netstat -tulnp | grep :443
```

# Note
On modern Linux systems, `ss` (socket statistics) is the recommended replacement for netstat.

# Help output
```
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -I[<Iface>] | [-veenNac] -i | [-cnNe] -M | -s [-6tuw] } [delay]

        -r, --route              display routing table
        -I, --interfaces=<Iface> display interface table for <Iface>
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets

  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25)
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP)
    x25 (CCITT X.25)
```
