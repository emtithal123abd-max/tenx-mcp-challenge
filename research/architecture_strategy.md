# Architecture Strategy — Project Chimera (Minimal)

## Goal
Define a minimal architecture for an AI “swarm” that can:
1) fetch trends
2) generate posts
3) output a publish plan

## Core idea: skill pipeline
Input: platform + niche + language + constraints  
Pipeline:
fetch_trends → generate_post → publish_social

## Components
- **Specs**: `/specs` is source of truth (functional + technical)
- **Skills**: `/skills/*` implement each stage
- **Tests**: validate interfaces and basic behavior
- **CI**: GitHub Actions runs tests on push/PR

## Data flow (minimal)
User request → TrendFetcher returns trend list → PostGenerator creates drafts → Publisher formats plan (stub)

## Why this design
- Small, testable, extendable
- Matches “agent swarm” style: modular workers + shared contract
## Diagram (Mermaid)

```mermaid
flowchart LR
  A[Campaign Goal] --> B[skill_fetch_trends]
  B --> C[skill_generate_post]
  C --> D[Review Step (future/Judge)]
  D --> E[skill_publish_social (stub)]
  E --> F[Artifacts + Logs]
