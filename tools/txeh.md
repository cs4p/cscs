# txeh
Etc Hosts Management Utility & Go Library

https://github.com/txn2/txeh

# Installation
## MacOS
brew install txn2/tap/txeh
## Debian
https://github.com/txn2/txeh/releases


# Examples

## Add an entry to /etc/hosts
sudo txeh add $target sneakycorp.htb

## Example 2
something else

# Help output
```
dan in ~/Downloads λ txeh -h
_            _
| |___  _____| |__
| __\ \/ / _ \ '_ \
| |_ >  <  __/ | | |
\__/_/\_\___|_| |_| v1.4.0

Add, remove and re-associate hostname entries in your /etc/hosts file.
Read more including useage as a Go library at https://github.com/txn2/txeh

Usage:
txeh [flags]
txeh [command]

Available Commands:
add         Add hostnames to /etc/hosts
help        Help about any command
remove      Remove a hostname or ip address
show        Show hostnames in /etc/hosts
version     Print the version number of txeh

Flags:
-d, --dryrun         dry run, output to stdout (ignores quiet)
-h, --help           help for txeh
-q, --quiet          no output
-r, --read string    (override) Path to read /etc/hosts file.
-w, --write string   (override) Path to write /etc/hosts file.

Use "txeh [command] --help" for more information about a command.

```

