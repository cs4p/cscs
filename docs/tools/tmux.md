#tmux

https://medium.com/hackernoon/a-gentle-introduction-to-tmux-8d784c404340

tmux is based around sessions. To start a new session in tmux, simply type tmux new in your terminal. 

All commands in tmux require the prefix shortcut, which by default is ctrl+b.

**ctrl+b d** - This will detach the current session and return you to your normal shell.

To check what sessions are active you can run: **tmux ls**

The tmux sessions will each have a number associated with them on the left-hand side (zero indexed as nature intended). This number can be used to attach and get back into this same session. For example, for session number 3 we would type:
`tmux attach-session -t 3`
or we can go to the last created session with:
`tmux a #`

To start a new session with a specific name we can just do the below:
`tmux new -s [name of session]`

To split a pane horizontally: `ctrl+b "`

To split pane vertically: `ctrl+b %`

To move from pane to pane: `ctrl+b [arrow key]`

tmux shortcuts & cheatsheet: https://gist.github.com/MohamedAlaa/2961058

tmux themes: https://github.com/jimeh/tmux-themepack

