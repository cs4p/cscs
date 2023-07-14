#!/bin/bash

# For ParrotOS
#disable language package
echo 'Acquire::Languages "none";' | sudo tee /etc/apt/apt.conf.d/99disable-translations

apt update
apt upgrade -y
apt autoremove -y

#setup flatpak
apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
apt install -y gnome-software-plugin-flatpak

# install Google Chrome
flatpak install flathub com.google.Chrome

#setup 1password at this point

# setup zsh as default shell
apt install zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# Restore MATE settings
# to backup MATE settings run
# dconf dump / > my_dconf
# to load settings from the backup
dconf load / < my_dconf

# install security tools
apt install parrot-tools-full


# Install tailscale
#Add Tailscale’s package signing key and repository:
curl -fsSL https://pkgs.tailscale.com/stable/debian/bullseye.noarmor.gpg | sudo tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
curl -fsSL https://pkgs.tailscale.com/stable/debian/bullseye.tailscale-keyring.list | sudo tee /etc/apt/sources.list.d/tailscale.list
#Install Tailscale:
sudo apt update
sudo apt install -y tailscale
#Connect your machine to your Tailscale network and authenticate in your browser:
sudo tailscale up
#You’re connected! You can find your Tailscale IPv4 address by running:
tailscale ip -4

#Install SSH server
apt install openssh-server
systemctl enable ssh

#Install jetbrains tools
cd /opt/
wget https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.28.1.15219.tar.gz -o ~/Downloads/jetbrains-toolbox.tar.gz
sudo tar -xvzf ~/Downloads/jetbrains-toolbox.tar.gz
# Rename the folder (not mandatory but it's easier for later use)
sudo mv jetbrains-toolbox jetbrains
#Open JetBrains Toolbox
jetbrains/jetbrains-toolbox