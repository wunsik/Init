# Skill: create-fastapi-endpoint
Purpose: Add a validated FastAPI endpoint with tests and contract updates.
Inputs: route path, method, request/response models, acceptance criteria.
Required context: `services/api/app`, `contracts/openapi`.
Execution steps:
1) Define pydantic models.
2) Implement route handler + dependency wiring.
3) Add success/error tests.
4) Update OpenAPI contract example.
Output expectations: endpoint code, tests, curl sample.
Validation checklist: status codes, schema parity, deterministic tests.
