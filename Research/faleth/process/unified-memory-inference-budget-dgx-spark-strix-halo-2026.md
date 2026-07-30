---
title: Unified-Memory Inference Budget — DGX Spark and Strix Halo
created: 2026-07-30
updated: 2026-07-30
type: principle
tags: [ai, llm, inference, hardware, dgx-spark, strix-halo, systems]
sources:
  - research/raw/transcripts/lyle-x-share-2082629254731440546.md
confidence: medium
---

# Unified-Memory Inference Budget — DGX Spark and Strix Halo

## Principle

A model that technically fits in unified memory may still be operationally unusable. Budget the complete serving system, not just the weight file:

> **weights + KV cache + draft/MTP model + runtime workspace + operating-system reserve + concurrent-session reserve < usable unified memory**

Context is not free. Long context and concurrency expand KV cache; speculative decoding consumes additional memory; runtimes need workspace; and the operating system still expects to remain conscious. MoE sparsity reduces how many parameters are *activated for compute per token*, but it does not magically remove the expert weights that must remain resident. Filling nearly all memory with weights converts an expensive inference box into a very sophisticated swap demonstrator.

## DGX Spark operator signal

A single DGX Spark operator reports an empirical **~80 GB maximum weight target** on a 128 GB system, leaving roughly **35–45 GB** for KV cache, speculative decoding, runtime overhead, and context. The post reports:

- **Laguna S 2.1 NVFP4:** 67 GB; claimed ~35 tok/s with a dFlash drafter and up to 45 tok/s on sustained code.
- **Qwen 3.5 122B-A10B NVFP4:** 74 GB; claimed ~35 tok/s using MTP.
- **StepFun 3.7 Flash Q4:** 108 GB; reported slow with little headroom, while the NVFP4 build reportedly failed to load and wedged the machine twice.

These are practitioner measurements, not controlled benchmarks. Preserve the heuristic; reproduce the numbers before depending on them. [[research/raw/transcripts/lyle-x-share-2082629254731440546]]

## DGX Spark deployment policy

For one 128 GB DGX Spark:

1. Start with **60–75 GB of weights**; treat 80 GB as a soft ceiling, not a purchasing guarantee.
2. Prefer models and quantizations native to the NVIDIA stack—especially validated NVFP4 artifacts—when quality is acceptable.
3. Measure memory after loading the intended context length and speculative-decoding configuration, not at an empty prompt.
4. Reserve explicit headroom for Hermes, the model server, monitoring, and at least one realistic concurrent job.
5. Reject any setup that survives only at short context or after closing every other process.

## Strix Halo translation

The **budgeting principle transfers; the model recipe does not automatically transfer**.

Strix Halo is an AMD unified-memory system with a different software and kernel ecosystem. DGX-specific NVFP4 artifacts and CUDA/TensorRT-LLM paths should not be assumed to run efficiently—or at all—on Strix Halo. The practical Strix path is more likely to use **GGUF with llama.cpp/Vulkan/ROCm-compatible builds** or another runtime explicitly proven on the exact APU and operating system.

For a 128 GB Strix Halo machine:

1. Keep the same conservative starting envelope: **roughly 60–75 GB of weights**, then benchmark upward.
2. Confirm how much RAM the OS, firmware/UMA allocation, and runtime make available to the GPU path.
3. Prefer a known-good GGUF quantization over an NVIDIA-native format whose theoretical size looks attractive.
4. Benchmark prompt processing, generation speed, long-context degradation, power draw, and thermal stability separately.
5. Do not copy DGX token-per-second claims across architectures. Same nominal memory capacity does not mean equivalent kernels, bandwidth utilization, or speculative-decoding support.

## Procurement rule

Choose **hardware + model + quantization + runtime + context target + concurrency target** as a single package. Before buying either machine, require a reproducible benchmark for the exact intended Hermes workload:

- coding executor;
- research/summarization worker;
- embeddings or retrieval;
- number of concurrent agents;
- target context window;
- acceptable tokens per second;
- quality floor against the current cloud model;
- watts and completed-job cost.

The local box should absorb stable, high-volume work while frontier cloud models retain planning, hard judgment, and overflow. Ownership is useful; forcing every workload onto owned hardware is merely cloud lock-in wearing a homemade hat.

## First commissioning sequence

1. Install and validate one conservative model below the memory ceiling.
2. Record idle memory, loaded-weight memory, first-token latency, prompt-processing speed, generation speed, and power.
3. Increase context in fixed steps and record KV-cache growth.
4. Add speculative decoding only after the baseline is stable.
5. Run the actual Hermes executor workload and compare accepted completed jobs—not synthetic tok/s alone.
6. Add concurrency last; stop when tail latency or quality becomes operationally worse than cloud overflow.

## Related

- [[faleth/process/frontier-model-cost-speed-tradeoff-2026]]
- [[faleth/process/local-model-ownership-agency-2026]]
- [[faleth/process/member-gated-compute-mesh-for-sovereign-agents-2026]]
