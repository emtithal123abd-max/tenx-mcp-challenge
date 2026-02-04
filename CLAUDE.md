# Project Chimera – Agent Rules (Day 3)

## Prime directive
- Specs in `/specs` are the source of truth. Read them before changing anything.

## Workflow rules
- Prefer smallest change that satisfies the spec.
- Always update docs/tests when behavior changes.
- Keep changes reviewable and commit often.

## Security rules
- NEVER commit `.env` or API keys.
- Use `.env.example` only.
- Do not log secrets.

## Engineering rules
- Add or update tests when adding new interfaces.
- Do not directly call external APIs in “business logic”; assume tools/resources are accessed through MCP boundaries.
