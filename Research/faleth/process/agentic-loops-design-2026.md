---
title: Agentic Loops — Design Over Prompting (2026)
created: 2026-07-07
updated: 2026-08-03
tags: [ai, software, systems, operations, framework]
type: principle
sources:
  - raw/transcripts/lyle-x-share-2074424941286719706.md
  - raw/x-bookmarks/2026-08-02/2084065915004747888.md
  - raw/x-bookmarks/2026-08-01/2083458624202944694.md
confidence: medium
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

## Harness reliability is model leverage (Hermes signal, 2026-08-02)

Hermes' maintainer reported a batch of tool-layer improvements developed with NVIDIA NeMo Relay: recovery from zero-match and multiline search failures, deduplication of truncated reads, clearer sandbox hints, more efficient skill viewing, and better wait/status behavior. The accompanying benchmark graphic describes hard A/B testing across two models and deliberately error-inducing tasks, with lower tool-error incidence, wall-clock time, and token use after the fixes. These are maintainer-reported results from a launch graphic rather than an independently reproducible benchmark, so the exact percentages should remain provisional.

The durable point is stronger than any one number: **agent capability is model × harness reliability**. A smarter prompt cannot recover tokens and turns wasted because the tool interface is ambiguous or brittle. Better recovery paths, smaller schemas, and explicit status semantics disproportionately expand what weaker or local models can complete. That connects loop design to [[faleth/process/frontier-model-cost-speed-tradeoff-2026]] and [[faleth/process/local-model-ownership-agency-2026]]: optimize the execution substrate before paying indefinitely for a larger brain.

## Node workflows as observability, not ceremony

A short visual demo represented UI implementation, code review, and a visual judge as separate nodes, exposing each node's files changed, token use, runtime, and verdict. The useful pattern is not "boxes make agents better." It is that a graph can make dependencies, parallel review, and stop conditions inspectable: implementation emits a diff; review emits non-blocking findings; the visual judge checks a pixel-difference threshold and emits a final match verdict.

Use node views when they reveal state that would otherwise be hidden across parallel agents. Keep the executable workflow file-native and testable where possible, consistent with [[faleth/process/file-native-agent-canvases-2026]]. If the diagram becomes a second source of truth or adds manual wiring without improving diagnosis, delete the diagram. We have enough enterprise spaghetti already.

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
- Hermes efficiency announcement: [[raw/x-bookmarks/2026-08-02/2084065915004747888]]
- Node-workflow demo: [[raw/x-bookmarks/2026-08-01/2083458624202944694]]