# Setup autoupdate
    brew tap domt4/autoupdate
    brew autoupdate start
    brew autoupdate status
    brew autoupdate delete
    brew autoupdate --start 43200 --upgrade --cleanup

# Useful formulas & Casks
## Must Have
    brew install meetingbar
    brew install --cask 1password
    brew install --cask platypus
    brew install tree
    brew install wget
    brew install osxphotos
    brew install mas
    brew install maccy

## Development
    brew install python@3.12
    brew install asdf
    brew install gh
    
## Security
    brew install nmap
    brew install ffuf
    brew install gobuster
    brew install hashcat
    brew install masscan
    brew install netcat
    brew install nikto
    brew install theharvester

## Kubernetes
    brew install kubecm
    brew install kubernetes-cli
    brew install minikube

## Special use case
    brew install big-mean-folder-machine
    brew install handbrake-app
    

## Setup tailscale
    brew install tailscale

To start tailscale now and restart at login:

    brew services start tailscale
    
Note: You may have to run this command as root depending on your setup

Login to the tailscale network:

    tailscale login



# Get homebrew to work with zscalar
    ls /opt/homebrew/etc/openssl@3/certs
    cp ~/Documents/Zscaler\ Root\ CA.cer /opt/homebrew/etc/openssl@3/certs