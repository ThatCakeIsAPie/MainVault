---
title: Lyle Nous Cloud vs Hetzner check
created: 2026-08-17
type: raw
source_url: https://portal.nousresearch.com/cloud
related:
  - https://portal.nousresearch.com/info
  - https://hermes-agent.nousresearch.com/docs/integrations/nous-portal
---

# 2026-08-17 — Nous Cloud vs HermesDelta

Lyle sent https://portal.nousresearch.com/cloud and said he was thinking of switching Delta over because it is a better rate than Hetzner.

## Official Cloud SKUs (portal info, 2026-08-17)

Prices exclude inference and tool usage. Running = compute + storage. Stopped = storage only, $0.03/day. Preview. Deploy needs $10 credit or an active subscription (info page still says $2 to start).

| Size | RAM | vCPU | Concurrent sessions | Running / day | ~30-day |
|---|---:|---:|---:|---:|---:|
| Small | 1 GB | 2 | 5 | $0.29 | $8.70 |
| Medium | 2 GB | 4 | 10 | $0.56 | $16.80 |
| Large | 4 GB | 8 | 20 | $1.09 | $32.70 |

Older Flightplan #2 listed $0.32 / $0.59 / $1.12 running and $0.06 stopped. Do not reuse those as current.

## What Cloud actually is

First-party hosted Hermes Agent on a dedicated instance. Dashboard-managed. Persistent workspace at `/opt/data`. No SSH for ordinary operation. Isolated hardened container. Inference and Tool Gateway bill separately on the same credit. Product is a thin managed agent runtime, not a general VPS.

## Live HermesDelta snapshot (this session)

- Host: HermesDelta, Hetzner vServer, Hillsboro OR, `5.78.226.169`
- Fedora 44, 3 vCPU AMD EPYC-Rome, 3.7 GiB RAM, 4 GiB swap (~0.9 GiB used), 75G disk (~24G used)
- Resident: Hermes ~545 MiB; postgres family ~375 MiB; fastapi ~166 MiB; bun ~118 MiB
- Docker: Honcho (api/deriver/postgres/redis), GBrain postgres `:55432`, Faleth CRM postgres `:55433`
- Also: Tailscale, systemd crons/backups, vault, projects

## Transfer boundary

Headline $/day is for a locked-down Hermes container. It is not a price for this box. Large (4 GB) matches RAM class only if you delete Honcho, GBrain, Faleth DB, Docker, and most of the 24G working set. Hillsboro Hetzner has no cheap CX/CAX SKUs; US CPX is why the VPS feels expensive. EU CX would be the cheap self-host comparison, not Cloud Small.

## Lyle's refinement (same session)

He wants the switch because Hetzner raised rates, Cloud bills $1.09 only while running and $0.03 idle, and first-party Hermes Cloud is built for this agent.

Live box matches **CPX21 in hil-dc1** (3 vCPU / 4 GB / 80 GB). After the 15 June 2026 hike, US list is **$13.99 → $37.49/mo**. Unknown whether this instance still has legacy pricing.

Marketing on /cloud says the agent “scales to zero when idle.” Official /info prices are **Running vs Stopped instance**, billed as a daily UTC charge, excluding inference. Those are not the same claim. Telegram polling cannot sleep on a normal VPS; Cloud may use webhooks internally. Unverified whether an online instance with no chat is $0.03 or $1.09.

If Running is pro-rated by hour (Flightplan said hourly), Large at 8 working hours/day is ~$11.50/mo compute. If any Running stamps the whole day, Large is ~$32.70 — close to new CPX21. Inference extra either way.

## Decision this session

Do not treat Cloud as a drop-in for Honcho + GBrain + Faleth. The billing argument is open: it wins only if idle actually hibernates and Lyle accepts a thinner runtime, or keeps a cheap box for the DBs.
