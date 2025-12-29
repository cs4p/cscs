# Oh My Zsh
Oh My Zsh is an open-source, community-driven framework for managing your Zsh configuration. It comes bundled with thousands of helpful functions, helpers, plugins, and themes.

* https://github.com/ohmyzsh/ohmyzsh
* https://ohmyz.sh/

# Installation
## MacOS / Linux
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
## Alternative: wget
    sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
## Manual Installation
    git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

# Configuration

## Enable plugins
Edit `~/.zshrc` and add plugins to the plugins array:

    plugins=(git docker kubectl python)

## Change theme
Edit `~/.zshrc` and set the theme:

    ZSH_THEME="robbyrussell"

## Update Oh My Zsh
    omz update

## Reload configuration
    source ~/.zshrc

# Popular Plugins

## Built-in Plugins

### git
Provides aliases and functions for Git commands

    # Already enabled by default
    plugins=(git)

### docker
Adds auto-completion for Docker commands

    plugins=(docker docker-compose)

### kubectl
Adds auto-completion for kubectl commands and aliases

    plugins=(kubectl)

### sudo
Press ESC twice to add sudo to the current command

    plugins=(sudo)

### web-search
Search directly from terminal (google, bing, github, etc)

    plugins=(web-search)
    # Usage: google "search term"

### extract
Extract any archive with a single command

    plugins=(extract)
    # Usage: extract archive.tar.gz

### z
Jump to frequently used directories

    plugins=(z)
    # Usage: z project

### history
Aliases for history commands

    plugins=(history)
    # h - show history
    # hs - search history

### colorize
Syntax highlighting for common commands

    plugins=(colorize)

### command-not-found
Suggests packages to install when command is not found

    plugins=(command-not-found)

### copypath
Copy current path to clipboard

    plugins=(copypath)
    # Usage: copypath

### copyfile
Copy file contents to clipboard

    plugins=(copyfile)
    # Usage: copyfile filename

### python
Python aliases and virtual environment helpers

    plugins=(python pip)

### nvm
Node Version Manager integration

    plugins=(nvm)

### rust
Rust development aliases

    plugins=(rust)

## Third-Party Plugins

### zsh-autosuggestions
Suggests commands as you type based on history

    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    plugins=(zsh-autosuggestions)

### zsh-syntax-highlighting
Fish-like syntax highlighting for Zsh

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    plugins=(zsh-syntax-highlighting)

### zsh-completions
Additional completion definitions

    git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
    plugins=(zsh-completions)

### fzf
Fuzzy finder integration

    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    ~/.fzf/install
    plugins=(fzf)

# Popular Themes

## Built-in Themes

### robbyrussell (default)
Minimal and fast theme

    ZSH_THEME="robbyrussell"

### agnoster
Popular theme with Git status and virtual env info (requires Powerline fonts)

    ZSH_THEME="agnoster"

### powerlevel10k (third-party)
Most popular theme with extensive customization

    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    ZSH_THEME="powerlevel10k/powerlevel10k"
    # Run configuration wizard:
    p10k configure

### avit
Clean theme with Git info

    ZSH_THEME="avit"

### bira
Two-line theme with time, user, and Git info

    ZSH_THEME="bira"

### jonathan
Minimalist theme with Git status

    ZSH_THEME="jonathan"

### refined
Simple and clean Git-focused theme

    ZSH_THEME="refined"

### spaceship (third-party)
Minimalistic theme with Git, Node, Docker info

    git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
    ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
    ZSH_THEME="spaceship"

### pure (third-party)
Minimal and fast async prompt

    git clone https://github.com/sindresorhus/pure.git "$ZSH_CUSTOM/themes/pure"
    ln -s "$ZSH_CUSTOM/themes/pure/pure.zsh-theme" "$ZSH_CUSTOM/themes/pure.zsh-theme"
    ZSH_THEME="pure"

# Example Configuration

    # Path to your oh-my-zsh installation.
    export ZSH="$HOME/.oh-my-zsh"
    
    # Set name of the theme to load --- if set to "random", it will
    # load a random theme each time oh-my-zsh is loaded, in which case,
    # to know which specific one was loaded, run: echo $RANDOM_THEME
    # See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
    ZSH_THEME="half-life"
     
    # Uncomment one of the following lines to change the auto-update behavior
    # zstyle ':omz:update' mode disabled  # disable automatic updates
    zstyle ':omz:update' mode auto      # update automatically without asking
    # zstyle ':omz:update' mode reminder  # just remind me to update when it's time
    
    # Uncomment the following line to enable command auto-correction.
    ENABLE_CORRECTION="true"
    
    # Which plugins would you like to load?
    # Standard plugins can be found in $ZSH/plugins/
    # Custom plugins may be added to $ZSH_CUSTOM/plugins/
    # Example format: plugins=(rails git textmate ruby lighthouse)
    # Add wisely, as too many plugins slow down shell startup.
    plugins=(1password asdf aliases alias-finder common-aliases command-not-found docker git nmap pip python sudo themes tailscale)
    
    source $ZSH/oh-my-zsh.sh
    
    # User configuration
    
    zstyle ':omz:plugins:alias-finder' autoload yes # disabled by default
    zstyle ':omz:plugins:alias-finder' longer yes # disabled by default
    zstyle ':omz:plugins:alias-finder' exact yes # disabled by default
    zstyle ':omz:plugins:alias-finder' cheaper yes # disabled by default
    
    # Set personal aliases, overriding those provided by oh-my-zsh libs,
    # plugins, and themes. Aliases can be placed here, though oh-my-zsh
    # users are encouraged to define aliases within the ZSH_CUSTOM folder.
    # For a full list of active aliases, run `alias`.
    #
    # Example aliases
    alias zshconfig="vim ~/.zshrc"
    alias ohmyzsh="vim ~/.oh-my-zsh"
    alias git_config_list="git config -l --show-origin --show-scope"
    
    # Add asdf shims to PATH
    export PATH="${ASDF_DATA_DIR:-$HOME/.asdf}/shims:$PATH"
    
    export PATH=$PATH:$HOME/go/bin



# Useful Commands

## List all themes
    ls ~/.oh-my-zsh/themes/

## List all plugins
    ls ~/.oh-my-zsh/plugins/

## Preview theme
    omz theme use <theme-name>

## Disable Oh My Zsh
    omz disable

## Enable Oh My Zsh
    omz enable

## Uninstall Oh My Zsh
    uninstall_oh_my_zsh

## Show plugin info
    omz plugin info <plugin-name>

# Tips

- Keep plugins minimal for better performance
- Use `zsh-syntax-highlighting` as the last plugin in the list
- Install Powerline fonts for best theme compatibility: https://github.com/powerline/fonts
- Use `source ~/.zshrc` after making changes to reload configuration
- Backup your `.zshrc` before major changes
- Check plugin documentation: `~/.oh-my-zsh/plugins/<plugin-name>/README.md`

# Common Aliases (from git plugin)

    gst = git status
    ga = git add
    gcmsg = git commit -m
    gp = git push
    gl = git pull
    gco = git checkout
    gcb = git checkout -b
    glog = git log --oneline --decorate --graph
    gdiff = git diff
