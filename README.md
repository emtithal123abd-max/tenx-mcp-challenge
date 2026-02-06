# TenX MCP Challenge — Day 3 (Project Chimera)

This repository contains:
- **Challenge 2:** `trp1-ai-artist/` (AI content generation exploration + artifacts)
- **Day 3:** Project Chimera scaffolding (spec-first agent swarm design)

## Day 3 Deliverables (Chimera)
- `research/` — research notes + architecture strategy
- `specs/` — source-of-truth requirements
- `skills/` — skill interface contracts (agent plug-ins)
- `tests/` — minimal interface + contract tests
- `.github/workflows/main.yml` — CI on push/PR
- `Dockerfile`, `Makefile`, `.coderabbit.yaml`, `CLAUDE.md`

## How to run locally
```bash
pytest -q
```md
## Day 2 Submission
- Report: see `REPORT.md`
- Run tests: `pytest -q`
- CI: `.github/workflows/main.yml` runs on push/PR
- Specs are source of truth: `/specs`