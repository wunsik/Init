# AI Engineering Harness

Production-ready, Git-first workspace for AI-assisted software development using OpenAI Codex, Cursor, CLI agents, and future orchestration bots.

## Goals
- Solo + small-team workflows
- Durable AI memory and decision logging
- Reusable role-based agents and procedural skills
- Repeatable orchestration with review/test/deploy gates
- Mac-friendly local development with Docker fallback

## Quick Start
```bash
cp .env.example .env
make bootstrap
make up
make test
```

## Repository Conventions
- `apps/`: product UIs and client applications
- `services/`: backend services and APIs
- `contracts/`: API and event schemas
- `.codex/agents`: role definitions and boundaries
- `.codex/skills`: reusable procedures
- `.codex/orchestration`: machine-readable workflow plans
- `_workspace/`: ephemeral artifacts, drafts, generated outputs

See `CODEX.md` for operational rules and `docs/adr` for architecture decisions.
