# Project Chimera Rules (Cursor-compatible)

- Specs-first: specs in /specs define scope and contracts.
- TDD-first: write/keep tests in /tests before implementation.
- No secrets: NEVER cogit add .cursor/rules/project_rules.md
git commit -m "Add Cursor rules file for Chimera"
git push origin main
mmit .env, API keys, tokens, credentials.
- Prefer small skills: each skill has clear input/output and is testable.
- Log + audit: design assumes audit logs for tool calls and publishing.
- HITL: publishing actions require human review/approval gate.
