# Skill: build-barcode-flow
Purpose: Implement barcode intake and validation workflow.
Inputs: barcode format rules, item payload contract.
Required context: `contracts/events`, `docs/business`.
Execution steps: parse/validate code, map SKU, emit event, log audit.
Output expectations: handler logic + event schema + tests.
Validation checklist: invalid barcode handling, duplicate scan behavior.
