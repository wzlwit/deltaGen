# /iniFolder

Initializes a standard folder structure in the current working directory.

## Created Structure

```
./src/
./tests/
./config/
./doc/
  plan/
  dev/
./scripts/
./assets/
```

## Usage

Run `/iniFolder` in any project root to scaffold the standard directory layout.

## Instructions

Create the following folder structure in the current working directory:

- `src/` — source code
- `tests/` — test files
- `config/` — configuration files
- `doc/` — project documentation root
  - `doc/plan/` — planning documents
  - `doc/dev/` — development documents
- `scripts/` — build, deploy, and utility scripts
- `assets/` — static assets (images, fonts, etc.)

Use `mkdir -p` to create all directories. Add a `.gitkeep` file in each leaf directory so git tracks them. Report what was created when done.
