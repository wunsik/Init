# CODEX Workspace Operating Manual

## Priority Rules
1. Follow `.codex/SYSTEM_PROMPT.md`
2. Apply `.codex/rules/*.md` in lexical order
3. Execute active playbook from `.codex/playbooks/`
4. Use task lifecycle in `.codex/tasks/{todo,doing,blocked,done}`
5. Record decisions in `docs/adr/`

## Development Principles
- Make minimal, reversible commits.
- Separate orchestration from business logic.
- Keep AI context compact and versioned.
- Update contracts when API behavior changes.
- Add tests for new business logic.

## Standard Loop
1. Pick task file in `.codex/tasks/todo`.
2. Move to `doing` and append progress notes.
3. Implement with agent + skill pairing.
4. Run lint/tests.
5. Move task to `done` with evidence links.

## Memory Strategy
- Long-lived decisions: `docs/adr/` + `.codex/decisions/`
- Domain context: `.codex/context/`
- Temporary AI outputs: `_workspace/generated/`
- Prompt snippets: `.codex/prompts/`
