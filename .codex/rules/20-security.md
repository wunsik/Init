# Security & Secrets Rules
- Load sensitive values from `.env` only.
- Commit only `.env.example`.
- Sanitize and validate request payloads.
- Avoid shell command interpolation with untrusted inputs.
