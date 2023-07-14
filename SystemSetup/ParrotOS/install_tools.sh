#!/bin/bash

# For ParrotOS
#disable language package
echo 'Acquire::Languages "none";' | sudo tee /etc/apt/apt.conf.d/99disable-translations

apt update
apt upgrade -y
apt autoremove -y

#Install 1Password
curl https://downloads.1password.com/linux/debian/amd64/stable/1password-latest.deb
sudo dpkg -i 1password-latest.deb

#synapse
sudo apt install synapse

#zsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

#jetbrains
sudo mkdir /opt/jetbrains
sudo chown dan:dan /opt/jetbrains
curl https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.28.1.15219.tar.gz
tar -xzvf jetbrains-toolbox-1.28.1.15219.tar.gz
mv jetbrains-toolbox-1.28.1.15219/jetbrains-toolbox /opt/jetbrains

#setup flatpak
apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
apt install -y gnome-software-plugin-flatpak

# install Google Chrome
flatpak install flathub com.google.Chrome

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

#Install SSH server
apt install openssh-server
systemctl enable ssh

#Install txeh - cli for managing /etc/hosts
curl https://github.com/txn2/txeh/releases/download/v1.4.0/txeh_arm64.deb
