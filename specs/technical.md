# Project Chimera — Technical Spec (Minimal)

## CI (Continuous Integration)
CI automatically runs checks (tests/lint/build) on push/PR to keep the repo healthy.

## AI Swarm (Working Definition)
A coordinated set of specialized AI agents (“skills”) that collaborate via shared state:
- Orchestrator/Planner: breaks goals into tasks, assigns skills
- Trend Agent: finds topics
- Content Agent: drafts posts/scripts
- Reviewer Agent: checks safety/policy/facts
- Publisher Agent: schedules/posts (stub allowed)
- Evaluator Agent: measures metrics + suggests iteration

## Architecture (Minimal)
### Components
1) Orchestrator
- reads campaign goal
- selects skills in sequence
- stores run state + artifacts

2) Skills (plug-ins)
- fetch_trends → ranked topics
- generate_post → drafts
- publish_social → publish plan (stub ok)

3) Storage
- local artifacts/, logs/, or run outputs (implementation-specific)

### Data Flow
Goal → Trends → Draft → Review → Publish Plan → Metrics → Iteration

## Constraints / Risks
- No secrets committed (.env excluded)
- Hallucinations: require review step
- Rate limits/quotas
- Reproducibility: log prompts/configs/outputs
