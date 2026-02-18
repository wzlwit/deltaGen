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

2. **Fetch `meta.md`** from the repo to get the component registry:
   - Construct the URL: `https://raw.githubusercontent.com/{owner}/{repo}/main/meta.md`
   - Download using `curl -fSs <url>`. If it fails, fall back to `gh api repos/{owner}/{repo}/git/trees/main?recursive=1` and filter for files under `skicmd/` and `hooks/` (exclude `.claude/`).
   - Parse the folder structure from `meta.md` to identify all available components and their paths.

3. **If $1 is missing** — install all components:
   a. Use the parsed structure from `meta.md` to list all available components grouped by category.
   b. Ask the user which components to install — all of them, or let them pick specific ones.
   c. For each selected component, proceed with steps 5–11 below.

4. **If $1 is a folder only** (no `/name` segment, or ends with `/`, e.g. `repos` or `repos/`) — install all items in that folder:
   a. Use the parsed structure from `meta.md` to list items in that folder.
   b. Present the list and ask the user which to install — all or pick specific ones.
   c. For each selected component, proceed with steps 5–11 below.

5. **If $1 is `folder/name`** — install a specific component:
   - Extract the **name** (last segment) from the path. Example: `repos/iniGit` → name is `iniGit`.

6. Construct the raw download URL:
   - From: `https://github.com/{owner}/{repo}`
   - To: `https://raw.githubusercontent.com/{owner}/{repo}/main/skicmd/{folder/name}.md`
   - Example: `https://raw.githubusercontent.com/wzlwit/zwClue/main/skicmd/repos/iniGit.md`
   - For hooks, use the `hooks/` prefix instead of `skicmd/`.

7. Download the file using `curl -fSs <url>`. If the download fails, report the error and stop.

8. Show the user a preview: display the component name and the first 5 lines of the downloaded content.

9. Ask the user where to install:
   - **Project** — `.claude/commands/{name}.md` (for skills/commands) or `.claude/hooks/{name}` (for hooks) in the current working directory
   - **Global** — `~/.claude/commands/{name}.md` or `~/.claude/hooks/{name}`

10. If a file already exists at the target path, warn the user and ask for confirmation before overwriting.

11. Create the target directory if needed (`mkdir -p`), write the file, and confirm the installed path.

12. **Check for duplicates**: After installation, check if a component with the same name exists in both project (`.claude/commands/` or `.claude/hooks/`) and global (`~/.claude/commands/` or `~/.claude/hooks/`) locations. If a duplicate is found, warn the user and ask if they want to remove the other copy to avoid conflicts.
