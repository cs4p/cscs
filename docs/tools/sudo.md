# Sudo

Sudo (superuser do) allows a permitted user to execute a command as the superuser or another user, as specified by the security policy. It's a fundamental tool for privilege management on Unix-like systems.

* https://www.sudo.ws/
* https://man7.org/linux/man-pages/man8/sudo.8.html

# Installation

## MacOS
```bash
# Pre-installed on all versions
```

## Debian
```bash
apt install sudo
```

# Examples

## Run command as root
```bash
sudo command
```

## Run command as specific user
```bash
sudo -u username command
```

## Switch to root shell
```bash
sudo -i
```

## List user's sudo privileges
```bash
sudo -l
```

# Configuration

# Sudoers File Configuration

## Basic syntax
	user HOST=(USER:GROUP) COMMAND

## Examples of sudoers entries
	# User can run all commands
	john ALL=(ALL:ALL) ALL

	# User can run specific commands
	jane ALL=(ALL) /usr/bin/systemctl, /usr/bin/apt

	# Group can run all commands without password
	%admin ALL=(ALL) NOPASSWD: ALL

	# User can run commands as specific user
	bob ALL=(www-data) ALL

	# User can run commands on specific hosts
	alice webserver=(ALL) ALL

## Command aliases in sudoers
	Cmnd_Alias SERVICES = /usr/bin/systemctl start, /usr/bin/systemctl stop
	Cmnd_Alias NETWORKING = /usr/sbin/ifconfig, /usr/sbin/route
	username ALL=(ALL) SERVICES, NETWORKING

## User aliases in sudoers
	User_Alias ADMINS = john, jane, bob
	ADMINS ALL=(ALL) ALL

# Security Best Practices

- Always use `visudo` to edit sudoers file (validates syntax)
- Be specific with NOPASSWD entries (limit to specific commands when possible)
- Regularly audit sudo access: `sudo grep -i sudo /var/log/auth.log`
- Use command aliases for complex configurations
- Avoid using `ALL` in NOPASSWD rules when possible
- Set sudo timeout: `Defaults timestamp_timeout=5` in sudoers

# Common Privilege Escalation Checks

## Check for sudo permissions
	sudo -l

## Check for NOPASSWD entries
	sudo -l | grep NOPASSWD

## Find SUID binaries owned by root
	find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;

## Check sudoers file permissions
	ls -la /etc/sudoers

## View sudo logs
	grep sudo /var/log/auth.log
	grep sudo /var/log/secure

# Help output
```
sudo - execute a command as another user

usage: sudo -h | -K | -k | -V
usage: sudo -v [-ABknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-ABknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-ABbEHknPS] [-C num] [-D directory] [-g group] [-h host] [-p prompt] [-R directory] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-ABknS] [-C num] [-D directory] [-g group] [-h host] [-p prompt] [-R directory] [-T timeout] [-u user] file ...

Options:
  -A, --askpass                 use a helper program for password prompting
  -b, --background              run command in the background
  -B, --bell                    ring bell when prompting
  -C, --close-from=num          close all file descriptors >= num
  -D, --chdir=directory         change the working directory before running command
  -E, --preserve-env            preserve user environment when running command
      --preserve-env=list       preserve specific environment variables
  -e, --edit                    edit files instead of running a command
  -g, --group=group             run command as the specified group name or ID
  -H, --set-home                set HOME variable to target user's home dir
  -h, --help                    display help message and exit
  -h, --host=host               run command on host (if supported by plugin)
  -i, --login                   run login shell as the target user; a command may also be specified
  -K, --remove-timestamp        remove timestamp file completely
  -k, --reset-timestamp         invalidate timestamp file
  -l, --list                    list user's privileges or check a specific command; use twice for longer format
  -n, --non-interactive         non-interactive mode, no prompts are used
  -P, --preserve-groups         preserve group vector instead of setting to target's
  -p, --prompt=prompt           use the specified password prompt
  -R, --chroot=directory        change the root directory before running command
  -S, --stdin                   read password from standard input
  -s, --shell                   run shell as the target user; a command may also be specified
  -T, --command-timeout=timeout terminate command after the specified time limit
  -U, --other-user=user         in list mode, display privileges for user
  -u, --user=user               run command (or edit file) as specified user name or ID
  -V, --version                 display version information and exit
  -v, --validate                update user's timestamp without running a command
  --                            stop processing command line arguments
```
