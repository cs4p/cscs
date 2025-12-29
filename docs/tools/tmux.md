# Tmux

Tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.

* https://github.com/tmux/tmux
* https://github.com/tmux/tmux/wiki

# Installation

## MacOS
```bash
brew install tmux
```

## Debian
```bash
sudo apt install tmux
```

# Examples

## Sessions

### Start a new session
```bash
tmux new -s my-session
```

### Detach from session
`Ctrl+b` then `d`

### List sessions
```bash
tmux ls
```

### Attach to a session
```bash
tmux attach-session -t my-session
# OR
tmux a -t 0
```

## Panes

### Split horizontally
`Ctrl+b` then `"`

### Split vertically
`Ctrl+b` then `%`

### Navigate between panes
`Ctrl+b` then `Arrow Keys`

# Help output
```
usage: tmux [-2CluvV] [-c shell-command] [-f file] [-L socket-name] [-S socket-path] [command [flags]]
```

