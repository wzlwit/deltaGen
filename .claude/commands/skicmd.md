# /skicmd

Downloads and installs skills/commands/hooks from a remote GitHub repository.

## Parameters

- **$1** (optional): Skill path in `folder/name` format (e.g. `repos/iniGit`). If omitted, prompt to install all available components.
- **$2** (optional): GitHub repo URL (default: `https://github.com/wzlwit/zwClue`)

## Usage

```
/skicmd                              # install all components from repo
/skicmd repos                        # install all items in repos/
/skicmd repos/                       # install all items in repos/ (same)
/skicmd repos/iniGit                 # install a specific skill
/skicmd repos/iniGit https://github.com/user/repo   # from a custom repo
```

## Instructions

1. Parse the arguments from the user's input:
   - First argument (optional): skill path — can be `folder/name` (specific item), `folder` or `folder/` (all items in folder), or omitted (all components).
   - Second argument (optional): GitHub repo URL. Default: `https://github.com/wzlwit/zwClue`.

2. **If $1 is missing** — install all components:
   a. Use `gh api repos/{owner}/{repo}/git/trees/main?recursive=1` to get the full file tree.
   b. Filter the tree for `.md` files under `skicmd/` (skills/commands) and `hooks/` (hooks).
   c. Present the user with a list of all available components grouped by type.
   d. Ask the user which components to install — all of them, or let them pick specific ones.
   e. For each selected component, proceed with steps 4–10 below.

3. **If $1 is a folder only** (no `/name` segment, or ends with `/`, e.g. `repos` or `repos/`) — install all items in that folder:
   a. Use `gh api repos/{owner}/{repo}/git/trees/main?recursive=1` to get the file tree.
   b. Filter for `.md` files under `skicmd/{folder}/`.
   c. Present the list and ask the user which to install — all or pick specific ones.
   d. For each selected component, proceed with steps 4–10 below.

4. **If $1 is `folder/name`** — install a specific component:
   - Extract the **name** (last segment) from the path. Example: `repos/iniGit` → name is `iniGit`.

5. Construct the raw download URL:
   - From: `https://github.com/{owner}/{repo}`
   - To: `https://raw.githubusercontent.com/{owner}/{repo}/main/skicmd/{folder/name}.md`
   - Example: `https://raw.githubusercontent.com/wzlwit/zwClue/main/skicmd/repos/iniGit.md`
   - For hooks, use the `hooks/` prefix instead of `skicmd/`.

6. Download the file using `curl -fSs <url>`. If the download fails, report the error and stop.

7. Show the user a preview: display the component name and the first 5 lines of the downloaded content.

8. Ask the user where to install:
   - **Project** — `.claude/commands/{name}.md` (for skills/commands) or `.claude/hooks/{name}` (for hooks) in the current working directory
   - **Global** — `~/.claude/commands/{name}.md` or `~/.claude/hooks/{name}`

9. If a file already exists at the target path, warn the user and ask for confirmation before overwriting.

10. Create the target directory if needed (`mkdir -p`), write the file, and confirm the installed path.
