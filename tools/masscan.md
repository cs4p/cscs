# masscan
MASSCAN is a fast port scanner. The primary input parameters are the IP addresses/ranges you want to scan, and the port numbers.

https://github.com/robertdavidgraham/masscan

# Installation
## Debian
    apt install masscan

# Examples

## Basic scan
Usage is similar to nmap. To scan a network segment for some ports:

    sudo masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112

This will:

* scan the 10.x.x.x subnet, and 2603:3001:2d00:da00::x subnets
* scans port 80 and the range 8000 to 8100, or 102 ports total, on both subnets
* print output to <stdout> that can be redirected to a file

## Port scan a host
    sudo masscan -p 0-65535 $target

## Create a config file
To see the complete list of options, use the --echo feature. This dumps the current configuration and exits. This output can be used as input back into the program:

    sudo masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112 --echo > xxx.conf
    masscan -c xxx.conf --rate 1000

## Using masscan, you can scan all TCP and UDP ports in roughly 2-3 minutes.
    masscan -p1-65535,U:1-65535 $target --rate=1000 -e tun0

# Help output
```
usage:
masscan -p80,8000-8100 10.0.0.0/8 --rate=10000
 scan some web ports on 10.x.x.x at 10kpps
masscan --nmap
 list those options that are compatible with nmap
masscan -p80 10.0.0.0/8 --banners -oB <filename>
 save results of scan in binary format to <filename>
masscan --open --banners --readscan <filename> -oX <savefile>
 read binary scan results in <filename> and save them as xml in <savefile>
dan in ~/hackthebox/lame λ masscan --help
MASSCAN is a fast port scanner. The primary input parameters are the
IP addresses/ranges you want to scan, and the port numbers. An example
is the following, which scans the 10.x.x.x network for web servers:
 masscan 10.0.0.0/8 -p80
The program auto-detects network interface/adapter settings. If this
fails, you'll have to set these manually. The following is an
example of all the parameters that are needed:
 --adapter-ip 192.168.10.123
 --adapter-mac 00-11-22-33-44-55
 --router-mac 66-55-44-33-22-11
Parameters can be set either via the command-line or config-file. The
names are the same for both. Thus, the above adapter settings would
appear as follows in a configuration file:
 adapter-ip = 192.168.10.123
 adapter-mac = 00-11-22-33-44-55
 router-mac = 66-55-44-33-22-11
All single-dash parameters have a spelled out double-dash equivalent,
so '-p80' is the same as '--ports 80' (or 'ports = 80' in config file).
To use the config file, type:
 masscan -c <filename>
To generate a config-file from the current settings, use the --echo
option. This stops the program from actually running, and just echoes
the current configuration instead. This is a useful way to generate
your first config file, or see a list of parameters you didn't know
about. I suggest you try it now:
 masscan -p1234 --echo
```
