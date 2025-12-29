# CeWL

CeWL (Custom Word List generator) is a ruby app that spiders a given URL to a specified depth, optionally following external links, and returns a list of words which can then be used for password crackers such as John the Ripper.

* https://github.com/digininja/CeWL
* https://digi.ninja/projects/cewl.php

# Installation

## MacOS / Debian
```bash
# Clone the repository
git clone https://github.com/digininja/CeWL.git
cd CeWL

# Install dependencies
gem install bundler
bundle install
```

## Docker
```bash
docker run -it --rm -v "${PWD}:/host" ghcr.io/digininja/cewl [OPTIONS] ... <url>
```

# Examples

## Generate wordlist from a website
```bash
cewl -w wordlist.txt https://example.com
```

## Generate wordlist with a minimum word length of 5
```bash
cewl -m 5 https://example.com
```

## Include email addresses in the output
```bash
cewl -e https://example.com
```

## Spider to a depth of 3
```bash
cewl -d 3 https://example.com
```

# Help output
```
CeWL 5.5.2 (Grouping) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
Usage: cewl [OPTIONS] ... <url>

    OPTIONS:
        -h, --help: Show help.
        -k, --keep: Keep the downloaded file.
        -d <x>,--depth <x>: Depth to spider to, default 2.
        -m, --min_word_length: Minimum word length, default 3.
        -o, --offsite: Let the spider visit other sites.
        --exclude: A file containing a list of paths to exclude
        --allowed: A regex pattern that path must match to be followed
        -w, --write: Write the output to the file.
        -u, --ua <agent>: User agent to send.
        -n, --no-words: Don't output the wordlist.
        -g <x>, --groups <x>: Return groups of words as well
        --lowercase: Lowercase all parsed words
        --with-numbers: Accept words with numbers in as well as just letters
        --convert-umlauts: Convert common ISO-8859-1 (Latin-1) umlauts (ä-ae, ö-oe, ü-ue, ß-ss)
        -a, --meta: include meta data.
        --meta_file file: Output file for meta data.
        -e, --email: Include email addresses.
        --email_file <file>: Output file for email addresses.
        --meta-temp-dir <dir>: The temporary directory used by exiftool when parsing files, default /tmp.
        -c, --count: Show the count for each word found.
        -v, --verbose: Verbose.
        --debug: Extra debug information.

        Authentication
        --auth_type: Digest or basic.
        --auth_user: Authentication username.
        --auth_pass: Authentication password.

        Proxy Support
        --proxy_host: Proxy host.
        --proxy_port: Proxy port, default 8080.
        --proxy_username: Username for proxy, if required.
        --proxy_password: Password for proxy, if required.

        Headers
        --header, -H: In format name:value - can pass multiple.

    <url>: The site to spider.

```

