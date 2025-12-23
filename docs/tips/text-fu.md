# Tools and tips for manipulating text from the command line

## awk
https://www.shortcutfoo.com/app/dojos/awk/cheatsheet

awk is a powerful text processing tool that scans files line by line and performs actions on patterns. It's particularly useful for extracting and manipulating columnar data, calculating values, and generating formatted reports. Each line is automatically split into fields (columns) that can be accessed using $1, $2, etc., making it ideal for processing structured text like logs, CSV files, and command output.

## tr

tr (translate) is a command-line utility that translates, deletes, or squeezes characters from standard input and writes the result to standard output. It's commonly used for character-by-character transformations like converting case, removing specific characters, replacing characters with others, or compressing repeated characters. Unlike awk or sed, tr operates on individual characters rather than lines or patterns, making it ideal for simple character substitution tasks.

## cut 

cut is a command-line utility that extracts sections from each line of input, typically from files or standard input. It's designed for working with delimited data (like CSV or TSV files) or fixed-width columns, allowing you to select specific fields or character ranges from structured text. Unlike awk which is more powerful and flexible, cut is simpler and faster for straightforward column extraction tasks.

### Useful flags
  * -d to set the Delimiter
  * -f select fields

## grep 

grep (global regular expression print) is a command-line utility that searches for patterns in text. It processes input line by line and prints lines that match a specified pattern or regular expression. It's one of the most commonly used tools for filtering and searching through files, command output, or logs, making it essential for quickly finding specific information in large amounts of text data.

### Useful flags
  * add $ to match end of line
  * 'grep -v' - return anyline that does not match the criteria
  * -B# return # lines before matching line

## sed

sed (stream editor) is a command-line utility for modifying text.

## ps

ps (process status) is a command-line utility that displays information about running processes on a system.

### Useful flags
  * ps -auxwwf


# Examples #
## Store your local IP in a variable

    ip a | grep tun0$ | awk '{print2}' | awk -F / '{print $1}' | xclip selection clipboard

## Extract users' login names and shells from the system passwd(5) file as “name:shell” pairs:

    cut -d : -f 1,7 /etc/passwd

## Show the names and login times of the currently logged-in users:

    who | cut -c 1-16,26-38

## Create a list of the words in file1, one per line, where a word is taken to be a maximal string of letters.

    tr -cs "[:alpha:]" "\n" < file1

## Translate the contents of file1 to upper-case.

    tr "[:lower:]" "[:upper:]" < file1

(This should be preferred over the traditional UNIX idiom of “tr a-z A-Z”, since it works correctly in all locales.)

## Strip out non-printable characters from file1.

    tr -cd "[:print:]" < file1

## Remove diacritical marks from all accented variants of the letter ‘e’:

    tr "[=e=]" "e"

## substitute a comma at the end of a file with nothing 

    sed s/,$//g

## Get all urls from a page

    curl -s $target | grep -Eo '(href|src)=".*"' | sed -r 's/(href|src)=//g' | tr -d '"' | sort 

