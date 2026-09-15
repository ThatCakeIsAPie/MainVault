---
title: Brainstorm Team — CRM vs Faleth canon discrepancies (2026-09-15)
created: 2026-09-15
type: raw
tags: [faleth, crm, brainstorm-team]
sources: [Brainstorm Team room; FalethCapitalBackend review]
---

# Brainstorm Team dump — CRM vs nine-doc canon (2026-09-15)

Room ask: @Faleth @Coder check backend CRM vs overall design; surface discrepancies for Lyle approve / deny / clarify.

## Already aligned (per Faleth)
- Layer 2 = COF × gross margin (default 20%)
- Office fee true-up = max(5% rev, ⅓ OP)
- Total Portfolio = A−L from GL
- Office rollup as investments in subs
- Phase 4 payroll spine: weekly Layer 2 batches (`computed → lead_reviewed → process → mark-paid`), GL COF accrual/clear, Payroll tab (mark-paid still manual; don’t double-run weekly payroll + ticket→GL labor for same dollars)

## Open product-law calls for Lyle
1. **Subsidiary gain share base** — Canon: 20% of OP *parallel* with office fee. CRM: 20% of *after-fee* OP. Biggest math miss. → Fix CRM if approved.
2. **Office 20/30/50 + management fee** — Canon: 20% total pool growth to team first; investors pay perf fee only (20% of their growth share); office keeps share+fees then 30% Class B dividends / rest retained. CRM: hardcoded 2% AUM mgmt fee + 20/30/50 framing ≠ Financial Framework.
3. **Office fee split 14% exec / 6% mentor / 80% pool** — in Governance/Financial; not in CRM.
4. **Equity layer mostly missing** — Class B mint/burn at book, cash-vs-mint on gain share, MCA pool %, dilution, Class A: stubs/zeros (Person MCA shell). Sequencing vs next priority.
5. **Anti-gaming book value** — Canon A−L−unrealized. CRM plain GL A−L. Open PR #5 on Accounting Overview (A−L−unrealized) — merge or rework pending Lyle.
6. **Floor** — floor_cents + advance cap weeks exist; newcomer grant + soft-credit clearing incomplete.
7. **Governance** — elections, calibration, peaceful fork: not in CRM (config only).

## Coder framing
- 1–3 → bounded CRM PRs if Lyle says fix CRM
- 5 → PR #5 direction if approved
- 4 / 6 / 7 wait on priority

## Payroll clarification (Lyle ask)
Payroll function is started (Phase 4 spine); not full Contribution floor law or auto payment rails yet.
