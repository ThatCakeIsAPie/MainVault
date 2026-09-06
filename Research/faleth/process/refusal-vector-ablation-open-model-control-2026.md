---
title: Refusal-Vector Ablation and Open-Model Control (2026)
created: 2026-07-26
updated: 2026-07-26
type: principle
tags: [ai, ml, llm, alignment, open-source, infrastructure, ethics]
sources:
  - raw/x-bookmarks/26-07-24/2080607945071686030.md
  - raw/x-bookmarks/26-07-25/2081134153970688251.md
confidence: medium
contested: true
---

# Refusal-Vector Ablation and Open-Model Control (2026)

## Durable idea

Open weights turn model alignment from a vendor-controlled behavior into an inspectable deployment choice. Tools such as **OBLITERATUS** probe hidden states for refusal-associated directions, then project or steer away from those directions. This is more precise than the bookmarked phrase “identifies the exact weights”: refusal can involve directions and subspaces distributed across layers, and removal quality must be measured rather than presumed. ^[raw/x-bookmarks/26-07-24/2080607945071686030.md]

The project exposes a Gradio interface, CLI, Python API, permanent weight projection, and reversible inference-time steering. Its public README describes checks such as refusal rate, perplexity, coherence, and KL divergence, but those are project claims and mechanisms—not independent proof that broad capabilities remain intact. [Project repository](https://github.com/elder-plinius/OBLITERATUS)

A second bookmark says Hermes packages a native optional skill at `official/mlops/obliteratus`, reducing the operational friction from research code to an agent-accessible workflow. That packaging claim was not installed or exercised during this ingest. ^[raw/x-bookmarks/26-07-25/2081134153970688251.md]

## Why it matters

1. **Ownership becomes behavioral control.** [[faleth/process/local-model-ownership-agency-2026]] is not merely about privacy or avoiding API rent; access to weights permits direct intervention in model behavior.
2. **Alignment is less robust than interface-level refusals imply.** If a compact representational intervention can substantially change refusal behavior, deployment safety cannot rely only on model post-training.
3. **Evaluation is the real product.** The useful loop is probe → intervene → benchmark refusal and capability → inspect regressions—not “uncensor” → declare victory. This matches [[faleth/process/agentic-loops-design-2026]]: verification, not tool completion, is the stop condition.
4. **Reversibility matters.** Inference-time steering or adapters are safer experimental surfaces than irreversible weight surgery because the baseline can be restored and compared.

## Faleth / Hermes decision rule

Do not install this merely because it exists; novelty is not a business priority, despite the internet’s heroic efforts to make every GitHub repo feel like destiny. Use it only for a defined local-model research need: mechanistic interpretability, red-team baselines, or recovering legitimate capability blocked by blunt refusal behavior. Keep the model isolated, benchmark against the original, record the exact method and strength, and retain external policy and tool-level controls around any deployment.

This is complementary to [[faleth/process/zero-data-retention-ai-procurement-control-2026]]: privacy controls govern where sensitive data travels, while weight-level interventions govern what an owned model will do. Neither replaces authorization, sandboxing, logging, or human accountability.

## Open questions

- How much do refusal-removal methods degrade reasoning, calibration, or harmless-boundary discrimination on the exact target model?
- Do extracted refusal directions generalize across architectures, or are they model- and dataset-specific?
- Can reversible steering provide enough control without creating permanent modified checkpoints?
- Has the Hermes skill pinned, audited, and sandboxed the upstream implementation and its optional telemetry?

## Sources and links

- [[raw/x-bookmarks/26-07-24/2080607945071686030]] — OBLITERATUS discovery claim.
- [[raw/x-bookmarks/26-07-25/2081134153970688251]] — Hermes optional-skill claim.
- [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) — public project repository inspected 2026-07-26.
- Related: [[faleth/process/frontier-model-cost-speed-tradeoff-2026]]
