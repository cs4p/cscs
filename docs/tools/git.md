# git
Tool description

https://git-scm.com/

# Installation
## MacOS
    brew install git
## Debian
    apt install git

## Common Tasks

### Configuration
Set your identity for all repositories on your machine:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Creating and Cloning
Initialize a new local repository:
```bash
git init
```
Clone an existing repository:
```bash
git clone https://github.com/user/repo.git
```

### Basic Workflow
Check the status of your files:
```bash
git status
```
Stage changes for the next commit:
```bash
git add file.txt       # Stage a specific file
git add .              # Stage all changes
```
Commit staged changes:
```bash
git commit -m "Brief description of changes"
```

### Branching
Create a new branch and switch to it:
```bash
git checkout -b feature-branch
# OR (newer syntax)
git switch -c feature-branch
```
Switch back to the main branch:
```bash
git switch main
```
Merge a branch into the current one:
```bash
git merge feature-branch
```

### Remote Collaboration
Download latest changes from remote (without merging):
```bash
git fetch origin
```
Update local branch with remote changes:
```bash
git pull origin main
```
Upload local commits to remote:
```bash
git push origin feature-branch
```

### Undoing Changes
Discard local changes in a file:
```bash
git restore file.txt
```
Unstage a file (keep the changes):
```bash
git restore --staged file.txt
```

## Note
zsh git plugin reference:
https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git

# Help output
```
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```

