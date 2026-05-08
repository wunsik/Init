# Skill: generate-openapi-schema
Purpose: Generate and validate OpenAPI schema from service code.
Inputs: app entrypoint, schema output path.
Required context: FastAPI app module.
Execution steps: run schema export script, lint schema, publish JSON.
Output expectations: versioned schema artifact.
Validation checklist: valid JSON, path parity, component refs resolve.
