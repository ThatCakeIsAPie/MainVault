---
type: principle
title: 'Hermes Subagent Orchestra: steer, stop, and watch live'
status: active
related:
  - research/raw/transcripts/lyle-x-share-2087986084592709814
  - research/faleth/process/messaging-ui-as-agent-operating-surface-2026
  - research/faleth/process/hermes-bot-mode-persistent-profiles-2026
sources:
  - 'https://x.com/Teknium/status/2087986084592709814'
  - raw/x-bookmarks/2026-08-13/2088003994904113614.md
effective_date: '2026-08-13'
updated: 2026-08-14
tags:
  - hermes
  - delegation
  - faleth
  - process
  - x-ingest
---

# Hermes Subagent Orchestra: steer, stop, and watch live

Teknium (2026-08-13): the parent agent can now **steer, end, and read live transcripts** of async sub-agents. Dispatch is no longer fire-and-forget until a summary lands.

## Mechanic

- **Spawn** returns child IDs.
- **List** is live telemetry, not a postmortem.
- **Steer** redirects at the next iteration boundary. In-flight tools are not cut. Same idea as `/steer`.
- **Stop** still returns partial work.
- Every `delegate_task` writes an append-only human-readable transcript you can tail.

The unpublished deep model of "how well the child is doing" is still the parent's judgment. The new surface just makes that judgment possible mid-flight.

Same-day **Bot Mode** is a different layer: standing named profiles that message each other, not live parent control of a spawned child. Use orchestra to steer a run; use [[faleth/process/hermes-bot-mode-persistent-profiles-2026]] when a role should persist after the thread ends.

## Faleth / Lyle application

This is the missing hand for the planner/executor rule Lyle already runs:

1. Parent does not wait blindly for a child's victory speech.
2. Parent can read the live log, then steer or kill.
3. Partial results beat silent death.
4. VXE cash work still comes first; this is how Delta supervises coding delegates, not a new product identity.

Use it. Do not spawn a fleet just because the dashboard looks like Wave Race.

## Related

- [[research/raw/transcripts/lyle-x-share-2087986084592709814]]
- [[research/faleth/process/messaging-ui-as-agent-operating-surface-2026]]
- [[faleth/process/hermes-bot-mode-persistent-profiles-2026]]
- [[raw/x-bookmarks/2026-08-13/2088003994904113614]]
