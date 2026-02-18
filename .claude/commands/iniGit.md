# /iniGit

Initializes a git repository in the current working directory with standard defaults.

## What It Does

1. Run `git init`
2. Create a `.gitignore` with common defaults
3. Create an initial commit

## .gitignore Defaults

```
# Dependencies
node_modules/
vendor/

# Environment
.env
.env.local
.env.*.local

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Build output
dist/
build/
out/

# Logs
*.log
```

## Usage

Run `/iniGit` in any project root to initialize a git repo with sensible defaults.

## Instructions

1. Run `git init` in the current working directory
2. Create a `.gitignore` file with the defaults listed above
3. Stage all files with `git add -A`
4. Create an initial commit with message: `Initial commit`

If git is already initialized (`.git/` exists), warn the user and do nothing.
