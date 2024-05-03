# bopscrk
Targeted-attack wordlist creator: introduce personal info related to target, combines every word and transforms results into possible passwords. The lyricpass module allows to search lyrics related to artists and include them to the wordlists.

https://github.com/r3nt0n/bopscrk

# Installation
    pip install bopscrk


# Examples

## Run interactive mode
    bopscrk -i

# Advanced usage
## Customizing behaviour using .cfg file
In bopscrk.cfg file you can specify your own charsets and enable/disable options:

`
threads: number of threads to use in multithreaded operations
extra_combinations (like (john, doe) => 123john, john123, 123doe, doe123, john123doe doe123john) are enabled by default. You can disable it in the configuration file in order to get more focused wordlists.
separators_chars: characters to use in extra-combinations. Can be a single char or a string of chars, e.g.: !?-/&(
separators_strings: strings to use in extra-combinations. Can be a single string or a list of strings space-separated, e.g.: 123 34!@
leet_charset: characters to replace and correspondent substitute in leet transforms, e.g.: e:3 b:8 t:7 a:4
recursive_leet: enables a recursive call to leet_transforms() function to get all possible leet transforms (disabled by default). WARNING: enabled with huge --max parameters (e.g.: greater than 18) could take even days. Can be true or false.
remove_parenthesis: remove all parenthesis in lyrics found before any transform
take_initials: produce words based on initial of each word in lyric phrases found (if enabled with remove_parenthesis disabled, it can produce useless words)
artist_split_by_word: split artist names and add each word as a new one
lyric_split_by_word: same with lyrics found
artist_space_replacement: replace spaces in artist names with chars/strings defined in charset
lyric_space_replacement: same with lyrics found
space_replacement_chars: characters to insert instead of spaces inside an artist name or a lyric phrase. Can be a single char or a string of chars, e.g.: !?-/&(
space_replacement_strings: strings to insert instead of spaces inside an artist name or a lyric phrase. Can be a single string or a list of strings space-separated, e.g.: 123 34!@
Some transforms have extensive charsets preincluded. To use it instead of the basic ones, just comment and uncomment the corresponding lines (It's important to comment the original one, if you let two lines with the same keyname uncommented, it will throw an error: AttributeError: 'bool' object has no attribute 'split').
`
Parameters configuration examples

Combine all the words using dots as separator, and same using commas
separators_chars=.,
Convert all "a/A" occurrences into "4" and all "e/E" occurrences into "3"
leet_charset=a:4 e:3

# Help output
```
  -h, --help         show this help message and exit
  -i, --interactive  interactive mode, the script will ask you about target
  -w                 words to combine comma-separated (non-interactive mode)
  --min              min length for the words to generate (default: 4)
  --max              max length for the words to generate (default: 32)
  -c, --case         enable case transformations
  -l, --leet         enable leet transformations
  -n                 max amount of words to combine each time (default: 2)
  -a , --artists     artists to search song lyrics (comma-separated)
  -o , --output      output file to save the wordlist (default: tmp.txt)
  -C , --config      specify config file to use (default: ./bopscrk.cfg)
  --version          print version and exit

```

