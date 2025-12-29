# hashid
Identify the different types of hashes used to encrypt data


[link to tool]

# Installation
## MacOS
    brew install tool
## Debian
    apt install hashid
## Script
    pip install hashid

# Examples

`$ ./hashid.py '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'`
`Analyzing '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'`
`[+] Wordpress ≥ v2.6.2`
`[+] Joomla ≥ v2.5.18`
`[+] PHPass' Portable Hash`

`$ ./hashid.py -mj '$racf$*AAAAAAAA*3c44ee7f409c9a9b'`
`Analyzing '$racf$*AAAAAAAA*3c44ee7f409c9a9b'`
`[+] RACF [Hashcat Mode: 8500][JtR Format: racf]`

`$ ./hashid.py hashes.txt`
`--File 'hashes.txt'--`
`Analyzing '*85ADE5DDF71E348162894C71D73324C043838751'`
`[+] MySQL5.x`
`[+] MySQL4.1`
`Analyzing '$2a$08$VPzNKPAY60FsAbnq.c.h5.XTCZtC1z.j3hnlDFGImN9FcpfR1QnLq'`
`[+] Blowfish(OpenBSD)`
`[+] Woltlab Burning Board 4.x`
`[+] bcrypt`
`--End of file 'hashes.txt'--`

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




