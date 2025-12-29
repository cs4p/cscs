# HashID

Identify the different types of hashes used to encrypt data and provides the corresponding Hashcat mode and JohnTheRipper format.

* https://github.com/psypanda/hashID

# Installation

## MacOS / Debian (Using pip)
```bash
pip install hashid
```

## Debian (Using apt)
```bash
apt install hashid
```

# Examples

## Identify a single hash
```bash
hashid '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'
```

## Identify a hash and show Hashcat and JohnTheRipper modes
```bash
hashid -mj '$racf$*AAAAAAAA*3c44ee7f409c9a9b'
```

## Identify hashes from a file
```bash
hashid hashes.txt
```

# Help output
```
usage: hashid.py [-h] [-e] [-m] [-j] [-o FILE] [--version] INPUT

Identify the different types of hashes used to encrypt data

positional arguments:
  INPUT                    input to analyze (default: STDIN)

options:
  -e, --extended           list all possible hash algorithms including salted
                           passwords
  -m, --mode               show corresponding Hashcat mode in output
  -j, --john               show corresponding JohnTheRipper format in output
  -o FILE, --outfile FILE  write output to file
  -h, --help               show this help message and exit
  --version                show program's version number and exit

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

```




