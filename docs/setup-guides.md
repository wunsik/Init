# Local Tooling Setup (Mac)

## VSCode / Cursor
- Install Python + ESLint + Prettier extensions.
- Use workspace settings to format on save.

## Codex CLI
- Keep `CODEX.md` and `.codex/SYSTEM_PROMPT.md` loaded in context.
- Start tasks by moving files across `.codex/tasks/*`.

## Pre-commit
```bash
chmod +x scripts/pre-commit.sh
ln -sf ../../scripts/pre-commit.sh .git/hooks/pre-commit
```
