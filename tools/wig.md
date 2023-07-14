# wig
WebApp Information Gatherer 

https://github.com/jekyc/wig

# Installation
## MacOS
    brew install tool
## Debian
    apt install tool
## Script
    curl http://example.com/script.sh

# Examples

## Example 1
    something

## Example 2
    something else

# Help output
```
usage: wig [-h] [-l INPUT_FILE] [-q] [-n STOP_AFTER] [-a] [-m] [-u] [-d]
           [-t THREADS] [--no_cache_load] [--no_cache_save] [-N] [--verbosity]
           [--proxy PROXY] [-w OUTPUT_FILE]
           [url]

WebApp Information Gatherer

positional arguments:
  url              The url to scan e.g. http://example.com

optional arguments:
  -h, --help       show this help message and exit
  -l INPUT_FILE    File with urls, one per line.
  -q               Set wig to not prompt for user input during run
  -n STOP_AFTER    Stop after this amount of CMSs have been detected. Default:
                   1
  -a               Do not stop after the first CMS is detected
  -m               Try harder to find a match without making more requests
  -u               User-agent to use in the requests
  -d               Disable the search for subdomains
  -t THREADS       Number of threads to use
  --no_cache_load  Do not load cached responses
  --no_cache_save  Do not save the cache for later use
  -N               Shortcut for --no_cache_load and --no_cache_save
  --verbosity, -v  Increase verbosity. Use multiple times for more info
  --proxy PROXY    Tunnel through a proxy (format: localhost:8080)
  -w OUTPUT_FILE   File to dump results into (JSON)