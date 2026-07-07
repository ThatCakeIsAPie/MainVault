---
title: Agentic Loops — Design Over Prompting (2026)
date: 2026-07-07
tags: [faleth, process, hermes, automation, agentic-ai]
type: principle
related:
  - "[[Research/raw/transcripts/lyle-x-share-2074424941286719706]]"
source: Anthropic Claude Code loops guide + Lyle X share
---

# Agentic Loops — Design Over Prompting (2026)

## Core definition

A **loop** is an agent repeating cycles of work until a **stop condition** is met — not a one-shot prompt.

**Shift:** prompting (2025) → **loop design** (2026): you specify *what repeats*, *what stops*, *what triggers*, and *who owns verification*.

## Four loop types (Anthropic / Claude Code)

| Type | You delegate | Stop / trigger | Best when |
|------|----------------|----------------|-----------|
| **Turn-based** | Verification (“the check”) | User prompt; model judges done or needs context | Exploration, short tasks; custom **skills** as verifiers |
| **Goal-based** | Stop condition (“done”) | `/goal` until objectively complete | You know what “done” looks like (tests green, PR merged, etc.) |
| **Time-based** | Schedule (“the trigger”) | `/loop`, `/schedule` intervals | Recurring maintenance (PR hygiene, polls, watchdogs) |
| **Proactive** | The prompt / routine | Composed skills + goals + dynamic workflows | Recurring, well-defined work; runs without you |

## Map to Lyle’s Hermes stack

| Claude loop | Hermes analogue |
|-------------|-----------------|
| Turn-based + skills | Main session **orchestrates**; `delegate_task` + **mandatory verify** (pytest, curl, read-back) — SOUL review loop |
| Goal-based | Kanban/goals with explicit KPI; “don’t stop until proof passes” |
| Time-based | `cronjob` (briefings, last30days, embed sync, watchdog scripts `no_agent`) |
| Proactive | Cron + `attach_to_session`, ambient X ingest, GBrain sync timer, GovCon pipeline *when* runway allows |

**Non-negotiable for Lyle:** subagent summaries are **not** evidence — loops must end on **tool-verified** stop conditions (already in SOUL).

## Faleth / Three Ps

- **Process** bedrock: compress manual steering into **repeatable loops** with clear stop rules.
- **Pull** (purpose): loops should serve VXE cash timing and agency-respecting systems — not infinite agent theater.
- **Push**: use loops to survive **~1 month hell fulfillment** without becoming the bottleneck.

## Open application

- Faleth CRM: goal-based loop = intake card → delegate → pytest/curl until green.
- LTD: time-based reminders + turn-based distillate QA on transcripts.
- Do **not** confuse “more agent turns” with leverage — **delete** loops that don’t move a named KPI.

## References

- Anthropic: [Getting started with loops](https://claude.com/blog/getting-started-with-loops)
- Ingest: [[Research/raw/transcripts/lyle-x-share-2074424941286719706]]