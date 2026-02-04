# Project Chimera — Functional Spec (Minimal)

## Purpose
Build an autonomous influencer network (“AI swarm”) that can:
1) detect or accept trends/topics,
2) generate platform-specific content,
3) run review/safety checks,
4) output publish plans and artifacts,
5) evaluate results and iterate.

## Users
- Operator (human): sets goals, monitors outputs, controls policies.
- Agents (system): execute tasks under constraints.

## Functional Requirements
FR1: Accept a campaign goal (topic, audience, tone, platform).
FR2: Produce at least one draft per platform template.
FR3: Run review step (policy + factuality checklist).
FR4: Export artifacts (md/json + media placeholders).
FR5: Track runs with timestamps + inputs.
FR6: Support multiple skills/agents that can be swapped.

## Acceptance Criteria
- Repo contains research/, specs/, skills/, tests/, docs/, and CI workflow.
- CLAUDE.md contains agent rules + security rules.
- REPORT.md explains what was built and how to run checks/tests.
