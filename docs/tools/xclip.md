# xclip
xclip is a command-line utility that provides an interface to the X Window System clipboard. It allows you to copy and paste text between the terminal and graphical applications.

* https://github.com/astrand/xclip
* https://linux.die.net/man/1/xclip

# Installation
## MacOS
    # Use pbcopy/pbpaste instead (built-in)
    # Or install xclip via:
    brew install xclip
## Debian
    apt install xclip

# Examples

## Copy text to clipboard
	echo "text" | xclip -selection clipboard

## Copy file contents to clipboard
	xclip -selection clipboard < file.txt

## Paste from clipboard
	xclip -selection clipboard -o

## Copy command output to clipboard
	ls -la | xclip -selection clipboard

## Copy file path to clipboard
	pwd | xclip -selection clipboard

## Short form using aliases (recommended)
	# Add to ~/.bashrc or ~/.zshrc:
	alias xc='xclip -selection clipboard'
	alias xp='xclip -selection clipboard -o'

	# Then use:
	echo "text" | xc
	xp

## Copy primary selection (middle-click paste)
	echo "text" | xclip

## Paste from primary selection
	xclip -o

## Copy to both clipboard and primary
	echo "text" | tee >(xclip) | xclip -selection clipboard

## Copy multiple lines to clipboard
	cat << EOF | xclip -selection clipboard
	Line 1
	Line 2
	Line 3
	EOF

## Copy screenshot path to clipboard
	import screenshot.png && echo "screenshot.png" | xclip -selection clipboard

## Clear clipboard
	echo -n | xclip -selection clipboard

## Monitor clipboard changes
	while true; do xclip -o -selection clipboard; sleep 1; done

## Copy SSH public key to clipboard
	cat ~/.ssh/id_rsa.pub | xclip -selection clipboard

## Copy current directory path
	pwd | xclip -selection clipboard

## Copy last command output
	!! | xclip -selection clipboard

# MacOS Equivalents

## Copy to clipboard (MacOS)
	echo "text" | pbcopy

## Paste from clipboard (MacOS)
	pbpaste

## Copy file contents (MacOS)
	pbcopy < file.txt

# Common Use Cases

## Copy grep results
	grep "pattern" file.txt | xclip -selection clipboard

## Copy find results
	find . -name "*.txt" | xclip -selection clipboard

## Copy IP address
	ip addr show | grep "inet " | awk '{print $2}' | xclip -selection clipboard

## Copy current Git branch
	git branch --show-current | xclip -selection clipboard

## Copy base64 encoded file
	base64 file.bin | xclip -selection clipboard

## Copy without newline
	echo -n "text" | xclip -selection clipboard

# Help output
```
Usage: xclip [OPTION] [FILE]...
Access an X server selection for reading or writing.

  -i, -in          read text into X selection from standard input or files
                   (default)
  -o, -out         print the selection to standard out (generally for piping
                   to a file or program)
  -f, -filter      when xclip is invoked in the in mode with output level set
                   to silent (the defaults), the filter option will cause xclip
                   to print the text piped to standard in back to standard out
                   unmodified
  -r, -rmlastnl    when the last character of the selection is a newline
                   character, remove it. Newline characters that are not the
                   last character in the selection are not affected. If the
                   selection does not end with a newline character, this option
                   has no effect. This option is useful for copying one-line
                   output
  -l, -loops       number of X selection requests (pastes into X applications)
                   to wait for before exiting, with a value of 0 (default)
                   causing xclip to wait for an unlimited number of requests
                   until another application (possibly another invocation of
                   xclip) takes ownership of the selection
  -t, -target      specify a particular data format using the given target atom.
                   With -o the special target atom name "TARGETS" can be used
                   to get a list of valid target atoms for this selection.
                   For more information about target atoms refer to ICCCM
                   section 2.6.2
  -d, -display     X display to use (e.g. "localhost:0"), xclip defaults to
                   the value in $DISPLAY if this option is omitted
  -h, -help        usage information
      -selection   selection to access ("primary", "secondary", "clipboard" or
                   "buffer-cut")
      -version     version information
      -silent      fork into the background to wait for requests, no
                   informational output, errors only (default)
      -quiet       show informational messages on the terminal and run in the
                   foreground
      -verbose     provide a running commentary of what xclip is doing
      -noutf8      operate in legacy (i.e. non UTF-8) mode for backwards
                   compatibility (Use this option only when really necessary,
                   as the old behavior was broken)

xclip reads text from standard in or files and makes it available to other
X applications for pasting as an X selection (traditionally with the middle
mouse button). It reads from all files specified, or from standard in if no
files are specified. xclip can also print the contents of a selection to
standard out with the -o option.

Examples:
  Copy file contents to clipboard:
    cat file | xclip -selection clipboard

  Copy command output to clipboard:
    ls | xclip -selection clipboard

  Paste from clipboard:
    xclip -selection clipboard -o

  Copy to primary selection (middle-click):
    echo "text" | xclip

Report bugs to <astrand@lysator.liu.se>
```
