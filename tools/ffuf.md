# ffuf - Fuzz Faster U Fool 
A fast web fuzzer written in Go 

https://github.com/ffuf/ffuf

# Instalation
## MacOS 
    brew install ffuf
## go compiler installed
    go install github.com/ffuf/ffuf/v2@latest
(the same command works for updating)
## git
    git clone https://github.com/ffuf/ffuf ; cd ffuf ; go get ; go build

Ffuf depends on Go 1.16 or greater.

# Examples

## Basic fuzzing
    ffuf -w /path/to/wordlist -u https://target/FUZZ

## Search for subdomains ##
    ffuf -H "Host: FUZZ.example.com" -u http://example.com -c -mc 200 -w SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt -o sneakymailer.ffuf

# Help output
`
help output here
`