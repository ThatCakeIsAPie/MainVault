---
title: MAGI-2 Open MoE Video Generation (2026)
created: 2026-08-15
updated: 2026-08-15
type: concept
tags: [ai, ml, open-source, architecture, inference, hardware]
sources:
  - raw/x-bookmarks/26-08-14/2088152335008571532.md
confidence: medium
---

# MAGI-2 Open MoE Video Generation (2026)

## Durable idea

**Activated-parameter marketing is not a local-inference budget.** Sand.ai's MAGI-2 Preview is a real 100B-class open video model, but 6B active per token does not make a 114B / ~307 GB stack a DGX Spark or consumer-GPU workflow.

## What shipped

@SandAI_HQ bookmarked MAGI-2 Preview as an open-source ultra-fine-grained MoE video model: **114B total parameters, ~6B activated per token**. The 2026-08-05 tech report and the Apache-2.0 inference repo back the launch copy. [[raw/x-bookmarks/26-08-14/2088152335008571532]]

Inspected official materials:

| Layer | Stated fact |
| --- | --- |
| Architecture | Single-stream text + video + audio Transformer (MagiHuman interface), not Magi-1 autoregressive chunking |
| Sparse core | MagiMoE: multi-head latent ultra-fine-grained MoE |
| Shape | 40 layers; middle 36 MoE; 4 boundary layers dense; width 3,072 |
| Routing | 12 heads × 256-d; 256 experts per head; Top-6 per head (72 experts/token) |
| Generation | T2V and I2V; **10-second clips only** |
| Pipeline | `magi2_preview` low-res denoise, then `magi2_refiner` to 1080p (generated 1088×1920) |
| Steps | Preview is **not step-distilled**: 100 preview + 5 refiner steps |
| Inference hardware | **8 NVIDIA Hopper GPUs** |
| Weights | Hugging Face `sand-ai/MAGI-2-preview`, ~307 GB complete tree (preview 228 GB + Qwen3.5-27B text encoder 56 GB + refiner 14 GB + VAEs) |

The launch tweet's “100% open-source” line is truncated in the X API payload and is marketing language. Code is Apache-2.0. Weight license still needs a dedicated check before any Faleth use.

## Why 6B active does not mean “fits locally”

This is the same residency rule as [[faleth/process/unified-memory-inference-budget-dgx-spark-strix-halo-2026]]:

1. **Inactive experts still occupy disk and usually memory.** Sparse compute cuts FLOPs, not the 228 GB preview transformer plus 56 GB text encoder.
2. **Video tokens are long.** Even with Head Parallel, the published inference path stages preview and refiner around 80 GB Hopper cards. A 128 GB Spark is the wrong class.
3. **The current preview is slow by design.** Until the distilled checkpoint exists, wall-clock is dominated by the 100-step preview.
4. **Duration is a product constraint.** 10 seconds is not a long-form production system.

Treat MAGI-2 as a **research-scale open video foundation**, not as the next MiniMax H3 experiment on Lyle's current boxes.

## Contrast with the local video path

[[faleth/process/local-minimax-h3-video-generation-tradeoffs-2026]] is about accepted-result cost on consumer or workstation GPUs. MAGI-2 is the opposite pole: more capacity, native audio-video in one backbone, and a documented 8× Hopper requirement. Do not mix the two into one “open video model” shopping list.

Ownership still matters ([[faleth/process/local-model-ownership-agency-2026]]). Owning MAGI-2 weights without Hopper-class serving is a trophy download.

## Faleth take

- Watch the promised **distilled** preview. That is when inference cost becomes discussable.
- Do not commission hardware against 6B-active headlines.
- If Faleth ever needs open video generation this season, keep measuring accepted clips on the H3 / LTX path, not MAGI-2.
- Re-check the Hugging Face license before any commercial or client use.

## Open questions

- What is the actual weight license, not the code license?
- What quality does 6B-active MagiMoE hold on motion, physics, identity, and A/V sync versus H3, Wan, LTX, and closed APIs?
- When the distilled checkpoint lands, what is wall-clock and VRAM on 8×H100 versus any smaller topology?
- Does Sand.ai publish scaling curves that actually connect parameter count to those quality axes, or only architecture feasibility?

## Sources

[1] https://x.com/SandAI_HQ/status/2088152335008571532 — official MAGI-2 Preview launch post
[2] https://sand.ai/blog/magi-2-preview — MAGI-2 Preview tech report (2026-08-05)
[3] https://github.com/SandAI-org/MAGI-2-preview — Apache-2.0 inference code
[4] https://huggingface.co/sand-ai/MAGI-2-preview — published weight tree
