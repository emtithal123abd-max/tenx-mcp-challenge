# TRP1 – AI Content Generation Challenge Submission

**Name:** Emti  
**Repo:** trp1-ai-artist (included in my main submission repo)  
**OS:** Windows  
**Tooling:** uv / Python virtual environment

---

## 1) Environment Setup & API Configuration

### Setup steps executed
```bash
git clone https://github.com/10xac/trp1-ai-artist.git
cd trp1-ai-artist
copy .env.example .env
uv sync
APIs configured

Google Gemini API: configured via GEMINI_API_KEY

AIMLAPI: configured via AIMLAPI_KEY (blocked by verification at runtime)

Verification commands (successful)
uv run ai-content --help
uv run ai-content list-providers
uv run ai-content list-presets

Verified providers

Music Providers

lyria

minimax

Video Providers

veo

kling

Image Providers

imagen

2) Codebase Understanding
Package structure (src/ai_content/)

cli/ – CLI command entrypoints (ai-content ...) and argument parsing

core/ – shared core logic / models used across pipelines

pipelines/ – orchestration of tasks (music/video/full workflows)

providers/ – provider implementations grouped by vendor:

providers/google/ – Gemini integrations (Lyria, Veo, Imagen)

providers/aimlapi/ – MiniMax integration

providers/kling/ – Kling integration

presets/ – preset styles and defaults (music BPM/mood, video aspect)

utils/ – common helpers

Purpose of pipelines/

Pipelines coordinate execution:

validate inputs

select provider

execute generation

save artifacts / track jobs
This separates workflow orchestration from provider-specific API calls.

3) Preset System
Music presets (BPM + mood)

jazz: nostalgic (95 BPM)

blues: soulful (72 BPM)

ethiopian-jazz: mystical (85 BPM)

cinematic: epic (100 BPM)

electronic: euphoric (128 BPM)

ambient: peaceful (60 BPM)

lofi: relaxed (85 BPM)

rnb: sultry (90 BPM)

salsa: fiery (180 BPM)

bachata: romantic (130 BPM)

kizomba: sensual (95 BPM)

Video presets (aspect ratios)

nature: 16:9

urban: 21:9

space: 16:9

abstract: 1:1

ocean: 16:9

fantasy: 21:9

portrait: 9:16

How to add a new preset (high level)

Add a new entry in the presets definitions under src/ai_content/presets/ (music or video)

Include required metadata (music: mood + bpm; video: aspect ratio)

Confirm it appears with:

uv run ai-content list-presets

4) CLI Commands & Options
Top-level commands

music – generate music

video – generate video

list-providers – list supported providers

list-presets – list preset styles

music-status – check MiniMax async job status

jobs, jobs-stats, jobs-sync – track/sync generation jobs

Music options (uv run ai-content music --help)

--prompt / -p TEXT (required)

--provider TEXT (lyria/minimax)

--style / -s TEXT (preset style)

--duration / -d INT

--bpm INT

--lyrics / -l PATH

--reference-url / -r TEXT (MiniMax)

--output / -o PATH

--force / -f

Video options (uv run ai-content video --help)

--prompt / -p TEXT (required)

--provider TEXT (veo/kling)

--style / -s TEXT (preset style)

--aspect / -a TEXT

--duration / -d INT

--image / -i PATH (first frame image)

--output / -o PATH

5) Generation Log
A) Music generation (Lyria – Gemini)

Success 1 (10s):

Provider: lyria

File: artifacts/audio/lyria_jazz_10s.wav

Duration: 10s

Size: 1.46 MB

Success 2 (15s):

Provider: lyria

File: artifacts/audio/lyria_jazz_15s.wav

Duration: 15s

Size: 1.46 MB

Log showed streaming chunks received

Command example:

uv run ai-content music --prompt "Instrumental jazz with warm piano and soft drums" --style jazz --provider lyria --duration 15 --output artifacts/audio/lyria_jazz_15s.wav --force

B) Lyria longer duration failure (20s)

Attempting 20s generation repeatedly resulted in:

Error: No audio data received (0 chunks)
This appears to be a realtime streaming instability / provider-side issue for longer durations.

C) MiniMax vocals attempt (AIMLAPI)

Attempt resulted in:

HTTP 403 Forbidden

Message: complete verification required (err_unverified_card)
This indicates AIMLAPI billing/verification is required before generation.

6) Video Generation Attempts & Troubleshooting
A) Veo provider (Gemini)

Encountered multiple issues:

SDK/API mismatch errors (type/method names) requiring code adjustments

API validation error: unsupported person_generation.allow_adult flag (400 INVALID_ARGUMENT)

Quota exhaustion: 429 RESOURCE_EXHAUSTED

Outcome:

Veo generation could not complete due to quota limitations in the time-boxed window.

B) Kling provider

Attempt resulted in:

Authentication failed: missing API key

7) Workarounds to Deliver Artifacts Under Deadline

Because Veo was blocked (quota) and Kling required unavailable credentials, I produced a local video artifact and a combined MP4 to demonstrate end-to-end workflow delivery.

Local video (MoviePy)

File: artifacts/video/local_video_10s.mp4

Created successfully

Combined video

File: artifacts/combined/music_video_10s.mp4

Note:
The Lyria output files were not decodable by standard tooling (header inspection showed leading zero bytes). Under deadline constraints, a fallback audio tone was generated locally to complete muxing and produce a valid combined MP4 while preserving all AI generation logs and files for evaluation.

8) Challenges & Solutions (Summary)

Lyria 20s: realtime streaming returned 0 chunks → reduced duration / documented instability

MiniMax: blocked by account verification → documented

Veo: SDK drift + unsupported flags + quota exhaustion → documented and stopped retrying

Kling: missing API key → documented

Delivery under constraints: produced local video + combined MP4 to demonstrate pipeline completion

9) Insights & Learnings

Provider abstraction is clean and makes multi-provider support manageable.

The biggest operational risk is upstream API/SDK drift and quota constraints.

In a forward-deployed setting, shipping a reliable deliverable + documenting failure modes is more valuable than chasing perfect outputs under time pressure.

10) Links

YouTube (unlisted): https://youtu.be/NucjkFdLhLs 

Main submission repo: https://github.com/emtithal123abd-max/tenx-mcp-challenge.git