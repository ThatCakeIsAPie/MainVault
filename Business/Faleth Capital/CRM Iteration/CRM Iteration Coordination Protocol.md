---
title: CRM Iteration Coordination Protocol
created: 2026-06-22
status: active
tags:
  - faleth
  - crm
  - agent-coordination
---

# CRM Iteration Coordination Protocol

This note defines how Delta coordinates rapid Faleth CRM iteration across multiple agent sessions/workers.

## Core Pattern

One orchestrator, many bounded workers.

- **Lyle**: dumps observations as quickly as he finds them.
- **Delta/orchestrator**: triages, dedupes, splits, prioritizes, assigns, and verifies.
- **Workers/subagents**: execute narrow scoped cards only.
- **Inbox note**: durable source of truth: [[Faleth CRM Iteration Inbox]].

## Card Quality Bar

A card is ready for implementation only when it has:

- A single clear problem or feature.
- Known screen/route or backend domain area.
- Acceptance criteria.
- Non-goals if scope could sprawl.
- Verification command/check.
- Parallel-safety note.

## Parallelization Rules

Safe to parallelize when cards touch clearly separate surfaces, for example:

- Admin UI layout only vs backend seed logic.
- Docs/reference update vs API test investigation.
- Playwright repro investigation vs unrelated endpoint bug.

Do not parallelize when cards likely touch the same files or invariants, for example:

- Two ticket detail UI changes.
- Two payout calculation changes.
- Seed workflow generation plus workflow event processor logic.
- Auth/session changes plus admin routing changes.

## Verification Menu

Use the smallest proof that actually verifies the claim:

- Backend health: `curl /health` against the correct preview port.
- Seed/data issue: rerun seed plus SQL counts.
- Admin UI change: `npm run build`; Playwright/screenshot when visual behavior matters.
- Domain logic: focused pytest plus seed/demo invariant check.
- Full confidence after multi-file work: seed + pytest + admin build + relevant preview check.

## Status Semantics

- **Raw Dump**: Lyle's rough observation, not yet actionable.
- **Triaged / Ready for Agent**: scoped enough to delegate.
- **In Progress**: worker assigned; not trusted yet.
- **Needs Lyle Decision**: product/taste/business choice required.
- **Verified / Done**: orchestrator independently checked it.
- **Parked / Later**: known, intentionally deferred.

## Related Project Context

- Repo: `/root/projects/FalethCapitalBackend`
- Repo context: `ai-context/`
- Development skill: `faleth-capital-backend-dev`
- Coordination skill: `kanban-coordination`
