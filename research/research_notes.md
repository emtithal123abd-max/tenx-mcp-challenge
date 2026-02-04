# Research Notes (Day 3) — Project Chimera

## CI (Continuous Integration)
CI is an automated pipeline that runs checks (tests, linting, build steps) whenever code is pushed or a pull request is opened. Goal: catch issues early and keep the repo always deployable.

## AI Swarm (working definition)
An “AI swarm” is a coordinated set of specialized AI agents (each with a narrow skill) that collaborate via a shared plan/state:
- Planner/Orchestrator: breaks work into tasks, assigns to agents
- Trend/Signal Agent: watches topics + extracts themes
- Content Agent: drafts posts/scripts
- Reviewer Agent: checks policy, tone, factuality
- Publisher Agent: schedules/posts content
- Evaluator Agent: measures performance + feedback loops

## Key Risks & Constraints
- Platform policy compliance (YouTube/TikTok/Instagram rules)
- Hallucinations / false claims
- Rate limits & quotas (Gemini/Veo etc.)
- Secrets management (never commit API keys)
- Reproducibility (logging prompts, configs, outputs)

## Minimal Success Criteria (for this 3-day challenge)
- Clear specs and architecture for the system
- Defined “skills” interface (how agents plug in)
- Tests folder with minimal checks
- CI workflow present and runs (even if tests are placeholders)
