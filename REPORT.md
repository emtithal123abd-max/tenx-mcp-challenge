# Day 3 — Project Chimera (Minimal Submission)

## What I built
A minimal, spec-first repo layout for “Project Chimera”: an autonomous influencer network (AI swarm) design with CI, specs, and skill plug-in contracts.

## Repo Structure
- research/: definitions + risks + success criteria
- specs/: SRS + architecture
- skills/: skill interface contract (plug-in design)
- tests/: minimal test documentation (CI-ready)
- .github/workflows/main.yml: CI on push/PR
- CLAUDE.md: agent operating rules (prime directive + security)

## CI
CI is set up via GitHub Actions to run on push/PR. It installs pytest and runs tests (non-blocking for MVP).

## Notes on Practical Constraints
- No API keys committed; secrets handled via .env locally only.
- Design supports future expansion: more skills, real platform posting, and metric feedback loops.
