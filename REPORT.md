# Project Chimera — Day 2 Independent Work (GitHub Link Report Submission)

## 0) What I’m submitting
This GitHub repository contains a **spec-first, eval-ready scaffold** for “Project Chimera: Autonomous Influencer Network”.
It includes:
- `/specs` — functional + technical scope (source of truth)
- `/skills` — skill contracts (plug-in design)
- `/tests` — tests (TDD-first; runnable via CI)
- `.github/workflows/main.yml` — CI (runs tests on push/PR)
- `CLAUDE.md` — agent rules + security (no secrets)

Repo link: https://github.com/emtithal123abd-max/tenx-mcp-challenge  
Direct report link: `REPORT.md` in repo root

---

## 1) Research & Domain Analysis (evidence of readings)

### 1.1 a16z — “The Trillion Dollar AI Code Stack” (my synthesis)
**Key idea:** AI development is becoming a multi-layer stack (models → infra → tooling → apps). The durable value is in **repeatable workflows** and **production reliability**, not one-off prompting.
**What that means for Chimera:** Chimera should be built as a **pipeline with contracts** (specs + tests) so multiple agents can safely collaborate and iterate without breaking behavior.

### 1.2 OpenClaw — “Agent Social Network”
**Key idea:** Agents should act like services in a network: discoverable, capability-declared, and interoperable through consistent interfaces.
**What that means for Chimera:** Chimera needs clear “skill” interfaces (trend fetch, post generate, publish) so other agents/tools can call them reliably.

### 1.3 MoltBook — “Social Media for Bots”
**Key idea:** Bot-to-bot social systems create risks (spam, manipulation, identity abuse). Governance requires identity, audit logs, rate limits, and safety enforcement.
**What that means for Chimera:** Chimera must maintain auditability (what was posted, why, by whom/which agent), and should include a Human-in-the-Loop checkpoint before publishing.

### 1.4 Project Chimera SRS (Autonomous Influencer Network)
**Key idea:** Chimera is an agentic system using MCP tools, parallel workers (swarm), governance (planner/worker/judge), and a clear operating model.
**What that means for Chimera:** Architecture should explicitly define roles, state storage, and how tasks progress from “trend” → “draft” → “review” → “publish”.

---

## 2) Architecture (complete, including database strategy)

### 2.1 Agent pattern
I use a **Planner → Worker(s) → Judge** pattern:
- **Planner** breaks a campaign goal into tasks.
- **Workers** execute tasks via skills (fetch trends, generate draft, propose schedule).
- **Judge** validates outputs against specs + safety rules and triggers HITL when needed.

### 2.2 Human-in-the-Loop (HITL)
HITL happens at the **Judge** stage:
- Auto-approve only high-confidence outputs
- Route uncertain/risky content for human review
- Require review for sensitive topics and publishing actions

### 2.3 Database strategy (explicitly addressing prior feedback)
Chimera needs durable state for:
- campaigns, trend snapshots, generated drafts, publishing jobs, audit logs

**Proposed storage: PostgreSQL + Redis**
- **PostgreSQL** (system of record): relational integrity, queries, reporting, auditability
- **Redis** (optional): queueing + short-lived coordination for swarm tasks

Why this choice:
- Strong consistency and relationships matter (campaign → trend → draft → publish → outcome)
- Audit logs must be durable and queryable

### 2.4 Minimal data model (draft)
```mermaid
erDiagram
  CAMPAIGN ||--o{ TREND_SNAPSHOT : collects
  TREND_SNAPSHOT ||--o{ CONTENT_DRAFT : inspires
  CONTENT_DRAFT ||--o{ PUBLISH_JOB : schedules
  PUBLISH_JOB ||--o{ AUDIT_LOG : logs

  CAMPAIGN { string campaign_id string goal datetime start_at }
  TREND_SNAPSHOT { string snapshot_id string campaign_id string source datetime created_at }
  CONTENT_DRAFT { string draft_id string snapshot_id string text float confidence string status }
  PUBLISH_JOB { string job_id string draft_id string platform datetime scheduled_at string status }
  AUDIT_LOG { string log_id string entity_type string entity_id string action datetime created_at }
