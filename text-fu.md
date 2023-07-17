# Tools and tips for manipulating text from the command line
* awk
  * https://www.shortcutfoo.com/app/dojos/awk/cheatsheet
* tr
* cut 
  * -d to set the Delimiter
  * -f select fields
* grep 
  * add $ to match end of line
  * 'grep -v' - return anyline that does not match the criteria
  * -B# return # lines before matching line
* sed
* ps
  * ps -auxwwf


# Examples #
Store your local IP in a variable

    ip a | grep tun0$ | awk '{print2}' | awk -F / '{print $1}' | xclip selection clipboard

Extract users' login names and shells from the system passwd(5) file as “name:shell” pairs:

    cut -d : -f 1,7 /etc/passwd

Show the names and login times of the currently logged-in users:

    who | cut -c 1-16,26-38

Create a list of the words in file1, one per line, where a word is taken to be a maximal string of letters.

    tr -cs "[:alpha:]" "\n" < file1

Translate the contents of file1 to upper-case.

    tr "[:lower:]" "[:upper:]" < file1

(This should be preferred over the traditional UNIX idiom of “tr a-z A-Z”, since it works correctly in all locales.)

Strip out non-printable characters from file1.

    tr -cd "[:print:]" < file1

Remove diacritical marks from all accented variants of the letter ‘e’:

    tr "[=e=]" "e"

substitute a comma at the end of a file with nothing 

    sed s/,$//g