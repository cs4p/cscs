# Homebrew Tips

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
    brew install mas
    brew install maccy
    brew install --cask the-unarchiver
    brew install rsync
    brew install htop

## Docker/Container Management
Recommend using colima as a simple command line replacement for docker:
    
    brew install colima     
    brew install docker     
    brew install docker-compose     
    brew install docker-buildx
    brew install docker-clean

## Claude
    brew install claude
    brew install claude-code or curl -fsSL https://claude.ai/install.sh | bash
    brew install claude-devtools

## Development
    brew install uv
    brew install asdf
    brew install gh
    brew install node
    brew install oven-sh/bun/bun or curl -fsSL https://bun.com/install | bash 
    
## Terraform
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform

## Security
    brew install nmap
    brew install ffuf
    brew install gobuster
    brew install hashcat
    brew install masscan
    brew install netcat
    brew install nikto
    brew install theharvester

# Additional Apps
    brew install --cask anylist 
    brew install --cask backblaze
    brew install --cask balenaetcher
    brew install --cask cyberduck
    brew install --cask discord
    brew install --cask grandperspective
    brew install --cask hush
    brew install --cask jetbrains-toolbox
    brew install --cask postman
    brew install --cask setapp
    brew install --cask signal
    brew install --cask slack
    brew install obsidian

# Apps can be installed from the App Store using MAS
    FriendlyStreaming - mas install 553245401
    SiteSucker - mas install 442168834
    TheCamelizer - mas install 1532579087

## Kubernetes
    brew install kubecm
    brew install kubernetes-cli
    brew install minikube
    brew install helm
    brew install kubectl
    

## Special use case
    brew install big-mean-folder-machine
    brew install handbrake-app
    brew install osxphotos <-- May not be working  
    brew install ffmpeg
    brew install openvpn

## Set up tailscale
    brew install tailscale

To start tailscale now and restart at login:

    brew services start tailscale
    
Note: You may have to run this command as root depending on your setup

Login to the tailscale network:

    tailscale login

# Get homebrew to work with zscalar
    ls /opt/homebrew/etc/openssl@3/certs
    cp ~/Documents/Zscaler\ Root\ CA.cer /opt/homebrew/etc/openssl@3/certs



