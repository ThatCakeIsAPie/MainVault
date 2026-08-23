---
title: Hermes Cloud + Hosted X MCP (agent stack, 2026)
created: 2026-07-10
updated: 2026-08-17
type: principle
tags: [ai, software, infrastructure, open-source, leverage, systems]
sources:
  - research/raw/x-bookmarks/2026-07-10/2074878754485043333.md
  - research/raw/x-bookmarks/2026-07-10/2071752389183647758.md
  - research/raw/x-bookmarks/2026-07-11/2070053292474773772.md
  - research/raw/x-bookmarks/2026-07-13/2076047289756561711.md
  - research/raw/x-bookmarks/2026-07-13/2076277722083463480.md
  - raw/x-bookmarks/2026-07-12/2076345051198984637.md
  - raw/x-bookmarks/2026-07-30/2082854011460518352.md
  - raw/articles/2026-07-31-hermes-flightplan-2-always-on-cloud.md
  - raw/transcripts/lyle-nous-cloud-vs-hetzner-2026-08-17.md
confidence: medium
---

# Hermes Cloud + Hosted X MCP (agent stack, 2026)

## Signals

1. **NousResearch — Hermes Agent in the Cloud:** pick model + server size; live in ~60s; org multi-agent with access controls and unified billing via Nous Portal.
2. **XDevelopers — Hosted X MCP:** MCP-compatible tools (Grok, Cursor, etc.) connect to the X API / docs with minimal setup (`docs.x.com/tools/mcp`).
3. **Unofficial Hermes mobile “battlestation” (beta, @demi_hl):** start agent tasks from phone; switch models per turn (opus/gpt/grok/local); jump chats/repos/boards/sessions; attach camera/media; pets/usage/skills. Directionally confirms **mobile operator surface** for Hermes, not only desktop/CLI.
4. **Mid-run steering:** `/steer` can deliver guidance after the next tool call instead of interrupting and restarting a run; a quoted post says this behavior can be selected as the default message-send mode rather than interrupt or queue.
5. **Wearable control experiment:** an independent smartwatch app demonstrates sending `/steer` guidance to Hermes. Source code was not yet released in the bookmarked post, so treat this as a product-direction signal, not deployable infrastructure.

## Distillation

| Layer | Product move | Operator implication |
|-------|--------------|----------------------|
| Runtime | Hosted Hermes | Agent capacity becomes **SKU + seat**, not only self-host ops |
| Context | Hosted X MCP | Real-time social graph as a **first-class tool** for any MCP client |
| Stack shape | Cloud agent + social MCP | Personal AI ops converge on **portal billing + OAuth scopes + tool policies** |

## One runtime, multiple operator surfaces

The Flightplan #2 implementation makes the hosted topology concrete: one persistent Hermes Cloud workspace can expose a locked-down Discord lane for ambient chat while Hermes Desktop connects to the same instance as a remote coding backend. Sessions and tool execution remain server-side; the channels are front doors, not separate brains. This is the durable architecture signal: separate **runtime continuity** from **operator interface**, then add each interface under its own authentication and authority boundary. [[raw/x-bookmarks/2026-07-12/2076345051198984637]] [[raw/articles/2026-07-31-hermes-flightplan-2-always-on-cloud]]

The article's July 2026 walkthrough reports browser provisioning, a persistent `/opt/data` workspace, dashboard-managed channels/configuration, Nous OAuth for Desktop, and no SSH requirement for ordinary operation. Flightplan prices ($0.32/$0.59/$1.12 running, $0.06 stopped) are dated. Portal info on 2026-08-17: Small/Medium/Large **$0.29 / $0.56 / $1.09 per running day**, stopped **$0.03/day**, still excluding inference and tools. Cloud remains preview. [[raw/transcripts/lyle-nous-cloud-vs-hetzner-2026-08-17]]

Hermes Desktop's visible subagent activity is likewise more than UI polish. Showing each delegated agent's live status and context turns parallelism into an inspectable operating surface, which lowers supervision cost and makes failed or wandering work easier to catch. The video is product evidence of observability, not evidence that spawning more agents automatically improves outcomes. [[raw/x-bookmarks/2026-07-30/2082854011460518352]] [[faleth/process/agent-swarm-coordination-context-economics-2026]]

## Faleth take (Lyle)

- **Already running Hermes self-hosted/VPS path** with xurl OAuth and bookmark cron. Cloud SKU is a **fallback / team path**, not a forced migration while solo.
- **2026-08-17 switch check:** HermesDelta is a Hillsboro **CPX21**. US list after the June 2026 hike is **$37.49/mo** (was $13.99). Cloud Large 24/7 is **$32.70** plus inference. Lyle’s real argument is idle billing + first-party ops, not the Small $8.70 headline. Official meter is Running vs Stopped, not “no chat.” Marketing says scale-to-zero; that is unverified. Honcho/GBrain/Faleth still do not fit the Cloud container. If the invoice is the pain and he wants the stack, EU CX is the cheap self-host move. If he wants them to eat systemd, Cloud is the product.
- **X MCP** validates the ambient-learning architecture: bookmarks + STEAL ingest + agent tools over the same API surface. Prefer **owned OAuth + ledger** over opaque scrapers.
- **GovCon/VXE priority still wins calendar.** Cloud convenience is leverage only if it reduces babysitting; do not open a second agent-ops rabbit hole during cash-timing hell month.
- **Steering is the useful primitive:** keep long jobs alive while correcting direction at tool boundaries. The smartwatch is merely one interface; the durable value is cheap, non-destructive operator intervention.
- Map to loop design: hosted product simplifies **time-based / proactive** loops; verification still local to Lyle’s SOUL rules ([[faleth/process/agentic-loops-design-2026]]).

## Open questions

- Exact current HermesDelta invoice vs EU CX33 / US CPX after the June 2026 Hetzner hike.
- Cost vs self-host for multi-model + long jobs.
- Data residency / client-work isolation on multi-tenant cloud agents.
- Whether hosted X MCP scopes match bookmark/DM needs or remain read-heavy.

## Provenance

- Bookmarks 2026-07-08 (Hermes Cloud), 2026-06-30 (X MCP); batch 2026-07-10; mobile app beta bookmark 2026-07-11; steering/default-mode and smartwatch signals ingested 2026-07-13.
- Raws: [[research/raw/x-bookmarks/2026-07-10/2074878754485043333]], [[research/raw/x-bookmarks/2026-07-10/2071752389183647758]], [[research/raw/x-bookmarks/2026-07-11/2070053292474773772]], [[research/raw/x-bookmarks/2026-07-13/2076047289756561711]], [[research/raw/x-bookmarks/2026-07-13/2076277722083463480]]

## Related

- [[faleth/process/hermes-agent-long-horizon-codebases-2026]]
- [[faleth/content/hermes-grok-x-content-machine-2026]]
- [[faleth/process/agentic-loops-design-2026]]
