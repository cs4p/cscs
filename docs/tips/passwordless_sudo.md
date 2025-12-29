To set up passwordless `sudo` for a specific user, you need to modify the sudoers file. It is highly recommended to use the `visudo` command, as it checks for syntax errors before saving, preventing you from being locked out of administrative access.

Follow these steps:

1. **Open the sudoers file for editing:**
   Run the following command in your terminal:
```shell script
sudo visudo
```


2. **Add the passwordless rule:**
   Scroll to the end of the file and add the following line, replacing `username` with your actual Linux username:
```plain text
username ALL=(ALL) NOPASSWD: ALL
```


3. **Save and Exit:**
   * If `visudo` opened **Nano** (the default for many systems): Press `Ctrl + O`, then `Enter` to save, and `Ctrl + X` to exit.
   * If `visudo` opened **Vi/Vim**: Type `:wq` and press `Enter`.

### Alternative: Enable for a Group
If you want all users in the `sudo` group (common on Ubuntu/Debian) or the `wheel` group (common on CentOS/Fedora) to have passwordless access, find the line for that group and modify it:

* **For Ubuntu/Debian:**
  Change:
```plain text
%sudo   ALL=(ALL:ALL) ALL
```

  To:
```plain text
%sudo   ALL=(ALL:ALL) NOPASSWD: ALL
```


* **For CentOS/Fedora:**
  Change:
```plain text
%wheel  ALL=(ALL)       ALL
```

  To:
```plain text
%wheel  ALL=(ALL)       NOPASSWD: ALL
```


### Security Warning
Enabling passwordless `sudo` reduces the security of your system. Any process running under your user account will be able to execute commands with root privileges without verification. Ensure your account is protected by other means, such as SSH keys if accessing remotely.