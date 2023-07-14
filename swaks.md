# Swaks - Swiss Army Knife for SMTP
Swaks is a featureful, flexible, scriptable, transaction-oriented SMTP test tool \
https://github.com/jetmore/swaks
# Instalation
## MacOS
    brew install swaks
## Debian
    apt install swaks

# Example script to send email to a list of addresses
    while read email; do
      echo "[+] Sending email from $email"
        swaks --from support@sneakymailer.htb --to $email --header 'Subject: Register in the portal' --body 'http://10.10.14.129/pypi/register.php' --server sneakycorp.htb >/dev/null
    done < emails.txt