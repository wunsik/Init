# ADR-0001: AI Harness Directory Structure
Date: 2026-05-08
Status: Accepted

## Context
We need repeatable AI-assisted workflows without mixing temporary artifacts and long-term memory.

## Decision
Adopt split layout:
- `.codex/` for AI runtime definitions and memory
- `_workspace/` for ephemeral generated artifacts
- `contracts/` for API/event source-of-truth

## Consequences
- Better auditability and lower prompt token waste.
- Onboarding improves through explicit roles and skills.
