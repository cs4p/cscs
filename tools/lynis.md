# Lynis
Lynis is an open source security tool. It helps with auditing systems running UNIX-alike systems (Linux, macOS, BSD), and providing guidance for system hardening and compliance testing. This document contains the basics to use the software.

https://cisofy.com/documentation/lynis/

# Installation
## Script
Clone the github repo:
```
git clone https://github.com/CISOfy/lynis
cd lynis && ./lynis audit system
```
## Debian
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 013baa07180c50a7101097ef9de922f1c2fde6c4
    sudo apt install apt-transport-https
    echo "deb https://packages.cisofy.com/community/lynis/deb/ stable main" | sudo tee /etc/apt/sources.list.d/cisofy-lynis.list
    apt update
    apt install lynis

# Examples

## Example 1
    something

## Example 2
    something else

# Help output
```
[ Lynis 3.0.2 ]

################################################################################
Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
welcome to redistribute it under the terms of the GNU General Public License.
See the LICENSE file for details about using this software.

2007-2020, CISOfy - https://cisofy.com/lynis/
Enterprise support available (compliance, plugins, interface and tools)
################################################################################


[+] Initializing program
------------------------------------


Usage: lynis command [options]


Command:

audit
audit system                  : Perform local security scan
audit system remote <host>    : Remote security scan
    audit dockerfile <file>       : Analyze Dockerfile

        show
        show                          : Show all commands
        show version                  : Show Lynis version
        show help                     : Show help

        update
        update info                   : Show update details


        Options:

        Alternative system audit modes
        --forensics                       : Perform forensics on a running or mounted system
        --pentest                         : Non-privileged, show points of interest for pentesting

        Layout options
        --no-colors                       : Don't use colors in output
        --quiet (-q)                      : No output
        --reverse-colors                  : Optimize color display for light backgrounds
        --reverse-colours                 : Optimize colour display for light backgrounds

        Misc options
        --debug                           : Debug logging to screen
        --no-log                          : Don't create a log file
        --profile <profile>               : Scan the system with the given profile file
            --view-manpage (--man)            : View man page
            --verbose                         : Show more details on screen
            --version (-V)                    : Display version number and quit
            --wait                            : Wait between a set of tests
            --slow-warning <seconds>  : Threshold for slow test warning in seconds (default 10)

                Enterprise options
                --plugindir <path>                : Define path of available plugins
                    --upload                          : Upload data to central node

                    More options available. Run '/usr/sbin/lynis show options', or use the man page.

```