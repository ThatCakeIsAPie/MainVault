---
title: Faleth CRM Iteration Inbox
created: 2026-06-22
status: active
tags:
  - faleth
  - crm
  - iteration
  - product-intake
---

# Faleth CRM Iteration Inbox

Purpose: this is the shared source of truth for rapid Faleth CRM iteration. Lyle can dump rough observations while using the backend CRM; Delta triages them into bounded work items, delegates safe parallel work, and verifies before marking anything done.

## How Lyle Uses This

Fastest path: send Delta a message that starts with one of these phrases:

- `CRM tweak:`
- `CRM bug:`
- `CRM feature:`
- `CRM note:`
- `Faleth CRM:`

Useful but optional details:

```text
Screen:
What I saw:
What I expected:
How bad: low / medium / high / blocking
Evidence: screenshot, URL, ticket ID, or rough description
```

You do **not** need to organize the thought first. Dump the observation. Delta handles the sorting, because apparently we are trying to remove friction rather than worship paperwork.

## Operating Rules

1. Raw observations go under **Raw Dump** first unless they are already clear enough to triage.
2. Delta converts each dump into one or more atomic cards.
3. Work items touching the same files/domain logic should not be delegated in parallel.
4. Subagent completion is not proof. Delta must verify with real evidence: tests, seed, curl, SQL, build, or Playwright as appropriate.
5. Verified work gets summarized in **Verified / Done** with the proof that passed.
6. Product/UX judgment questions that need Lyle's taste go under **Needs Lyle Decision** instead of being guessed.

## Intake Template

```text
### YYYY-MM-DD — Short title
- Status: Raw Dump
- Type: bug | tweak | feature | investigation | UX
- Area: backend | frontend | seed | admin UI | workflow | payout | customer | auth | docs
- Priority: low | medium | high | blocking
- Screen / route:
- What Lyle saw:
- Expected behavior:
- Evidence:
- Triage notes:
- Parallel safety:
- Verification required:
```

## Raw Dump

Use this for messy observations that have not been decomposed yet.

## Triaged / Ready for Agent

Work here should have clear scope, acceptance criteria, and verification.

## In Progress

Track delegated work here only after a worker has been assigned.

### 2026-06-22 — Display subsidiary COF rate and make labor pool use subsidiary COF × gross profit
- Status: Interrupted / needs verification
- Type: feature
- Area: backend | frontend | seed | admin UI | payout
- Priority: high
- Screen / route: Org hierarchy / subsidiaries; ticket payout previews
- What Lyle saw: COF rate is not actually visible in the org view for subsidiaries; labor pool preview needs to follow subsidiary COF economics.
- Expected behavior: Each subsidiary shows its COF rate in org view. Default COF rate is 20% of gross margin. Ticket labor pool preview = subsidiary COF rate × ticket gross profit. Node payout previews are calculated from that labor pool.
- Evidence: Telegram feature request, 2026-06-22.
- Triage notes: Existing code has `ContributionConfig.cof_rate`, seed/defaults often use 30%, and payout preview already has a labor-pool calculation path; implementation should make the 20% default consistent and verify node payouts derive from the new labor pool.
- Interruption note: The Telegram gateway was OOM-killed during build/verification at 2026-06-22T19:42Z, so the delegate session did not finish cleanly. Repo has dirty changes and must be reviewed/verified before this can be treated as done.
- Parallel safety: Single worker only; touches payout economics + org display.
- Verification required: Backend tests for default/config math, frontend build, API sanity on preview/dev data showing COF rate displayed in org data and payout preview labor pool/node payouts using 20%.

## Needs Lyle Decision

Questions where taste, business logic, or product intent matters more than code correctness.

## Verified / Done

Completed only after Delta independently verifies the result.

## Parked / Later

Ideas worth keeping, but not worth interrupting current iteration.
