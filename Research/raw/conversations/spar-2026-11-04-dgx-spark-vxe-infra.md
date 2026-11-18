---
source: Spar distillate (conversation with Lyle, incl. his corrections)
author: Spar
date: 2026-11-04
ingested: 2026-11-04
sha256: f8a161d86ebea4cc74c37f6f00866e7cb3a4d14a937501362316bed8c1e99314
---
# Spar distillate — DGX Spark as VXE infrastructure (2026-11-04)

Source: Spar conversation with Lyle. Corrections from Lyle in a follow-up addendum are folded in below (do not treat overnight loops as the selling point).

## What changed
The Spark idea moved from fascination to a real consideration. When VXE gets paid, Lyle and his brother may buy one or two DGX Sparks to run open-weight models such as DeepSeek.

## Real driver (Lyle's corrections)
Overnight loops are NOT the selling point; they don't care about that.
The real driver is the cost curve:
- Already on ~$100/month Grok Bot plan; hit ~27–30% usage right after reset.
- Pays ~$200/month Claude and ~$100/month X → about $300/month total, and they still ration usage.
- Meeting their needs would soon take $400–$600/month.
- At about $600/month, a Spark "pays itself off in a year," maybe two.
- Put that subscription money toward financing a Spark, or buy outright.

## Planned setup
- Drop to about $50/month in subscriptions ($30 X plan + $20 Claude plan).
- Opus is the orchestrator that reviews the work and builds the plan.
- DeepSeek on the Sparks does the work.
- Hermes becomes the main workhorse on the Spark; Grok Bot is kept for what it's best at.
- Sparks would also replace the need for Grok Bot's virtual computer, possibly running work through a VM.
- He knows the Spark is ARM, not x86, and that this needs care.

## Workload
Main workload: VXE coding projects and apps that need lots of iterative changes. (Overnight agent loops were mentioned earlier but Lyle corrected: not the selling point.)

## Prior local experience
He has run local models before, but his old computer only fits a small Gemma, which is slow and not very smart. A couple of Sparks running a quantized model at about 40 tokens/sec would be "plenty," with a work queue that moves to the next job as soon as one finishes.

## Prices found (as of distillate day)
- NVIDIA lists 128 GB at $6,950, out of stock (launched at $3,999).
- New on eBay ~$7,700; used from ~$6,750.
- 64 GB partner models start at $4,999.
- Renting a Spark ~$0.79/hr.

## Open question
What tips it from "makes sense" to "do it" once VXE gets paid — a cash amount, or the subscription bill crossing a line.

## Vault touch
Touches Research/faleth/process/unified-memory-inference-budget-dgx-spark-strix-halo-2026.md — record Lyle's conclusions as his take, not external fact.
