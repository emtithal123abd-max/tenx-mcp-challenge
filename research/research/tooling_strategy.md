# Tooling Strategy (MCP + Swarm)

## Dev tooling vs runtime skills
- Dev tooling (MCP servers) helps me build/debug locally (telemetry, analysis).
- Runtime skills are what the Chimera agent uses during operation (trend fetch, post gen, publish).

## MCP usage
- Keep Tenx MCP connected for session telemetry (“black box recorder”).
- Prefer tool calls through MCP instead of ad-hoc scripts where possible.

## Swarm execution model
- Planner: turns campaign goals into tasks.
- Workers: execute skills (fetch trends → generate post → publish plan).
- Judge: validates outputs against `/specs` + safety rules before publish.

## Guardrails
- Specs-first: no implementation without reading `/specs`.
- No secrets in repo (`.env` never committed).
- CI must run tests on push/PR to keep behavior stable.
