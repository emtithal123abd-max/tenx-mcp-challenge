# Skills (Agent Plug-ins)

This repo models an "AI swarm" as multiple skill modules.

## Skill Interface (Minimal Contract)
Each skill should define:
- Name
- Purpose
- Inputs (required/optional)
- Outputs
- Failure modes / retries
- Logging behavior

## Current Skills (Folder-based)
- skill_fetch_trends/
- skill_generate_post/
- skill_publish_social/

## Expected Pipeline (High level)
Goal → fetch_trends → generate_post → publish_social → (future: review + evaluate)
