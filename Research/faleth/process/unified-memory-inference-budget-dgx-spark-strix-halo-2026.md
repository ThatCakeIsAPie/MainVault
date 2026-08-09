---
title: Unified-Memory Inference Budget — DGX Spark, RTX Spark, and Strix Halo
created: 2026-07-30
updated: 2026-08-09
type: principle
tags: [ai, llm, inference, hardware, systems]
sources:
  - research/raw/transcripts/lyle-x-share-2082629254731440546.md
  - raw/x-bookmarks/2026-07-30/2082629254731440546.md
  - raw/x-bookmarks/2026-07-30/2082909527515779164.md
  - raw/articles/2026-07-31-waste-inference-engine-readme.md
  - raw/x-bookmarks/2026-08-02/2083705845670650195.md
confidence: medium
---

# Unified-Memory Inference Budget — DGX Spark, RTX Spark, and Strix Halo

## Principle

A model that technically fits in unified memory may still be operationally unusable. Budget the complete serving system, not just the weight file:

> **weights + KV cache + draft/MTP model + runtime workspace + operating-system reserve + concurrent-session reserve < usable unified memory**

Context is not free. Long context and concurrency expand KV cache; speculative decoding consumes additional memory; runtimes need workspace; and the operating system still expects to remain conscious. MoE sparsity reduces how many parameters are *activated for compute per token*, but it does not make inactive experts disappear: conventional runtimes keep them memory-resident, while storage-tier designs must still make them reachable within the latency budget. Filling nearly all memory with weights converts an expensive inference box into a very sophisticated swap demonstrator.

## Storage-tier MoE serving — WASTE proof point

WASTE demonstrates an important exception to the assumption that all expert weights must be memory-resident: keep the shared model trunk in RAM, arrange each expert as a single aligned record, stream only routed experts from internal NVMe, and use remaining RAM as a bounded expert cache. Its published Kimi K3 proof point converts the complete 2.78T-parameter model into a 982 GiB container and runs it on a 64 GB MacBook Pro at roughly **0.32–0.34 tok/s**. The measured deployment uses a 46.24 GB RAM budget, including a 17.56 GB expert cache; the engine reports a 29.05 GiB minimum at 4K context, but treats 64 GB and fast internal NVMe as the practical floor. [[raw/x-bookmarks/2026-07-30/2082909527515779164]] [[raw/articles/2026-07-31-waste-inference-engine-readme]]

This changes **feasibility**, not necessarily **usability**. K3 reads about 17 GB of experts per token, and the published laptop result is closer to an offline private oracle than an interactive Hermes worker. More RAM also did not monotonically help: larger cache budgets pushed the operating system into paging and made decoding slower despite higher cache-hit rates. The transferable rule is therefore broader than unified memory: budget **resident trunk + one routed working set + useful cache + OS headroom**, then validate the storage path and latency target. “It generated a sentence” is a systems milestone, not a production SLA.

## DGX Spark operator signal

A single DGX Spark operator reports an empirical **~80 GB maximum weight target** on a 128 GB system, leaving roughly **35–45 GB** for KV cache, speculative decoding, runtime overhead, and context. The post reports:

- **Laguna S 2.1 NVFP4:** 67 GB; claimed ~35 tok/s with a dFlash drafter and up to 45 tok/s on sustained code.
- **Qwen 3.5 122B-A10B NVFP4:** 74 GB; claimed ~35 tok/s using MTP.
- **StepFun 3.7 Flash Q4:** 108 GB; reported slow with little headroom, while the NVFP4 build reportedly failed to load and wedged the machine twice.

These are practitioner measurements, not controlled benchmarks. Preserve the heuristic; reproduce the numbers before depending on them. [[research/raw/transcripts/lyle-x-share-2082629254731440546]] [[raw/x-bookmarks/2026-07-30/2082629254731440546]]

### DeepSeek V4 Flash quantization ladder (2026-08-02)

A second operator report adds a useful boundary test for **DeepSeek V4 Flash 0731** (284B total / 13B active MoE) in CUDA-enabled llama.cpp on one 128 GB Spark. The reported ladder is **UD-IQ3_XXS at 104 GB fully GPU-resident**, **IQ3_S at 116 GB too tight**, both 128 GB Q3 variants OOM, and the 162 GB Q8 build unable to fit. This does not invalidate the conservative 60–80 GB commissioning envelope: it shows that a 104 GB model can technically load when the intended KV cache and workload fit the remaining memory, while roughly 116 GB leaves too little operating room. [[raw/x-bookmarks/2026-08-02/2083705845670650195]]

The practical distinction is **safe operating target versus maximum loadable artifact**. Use 60–80 GB when buying for flexible context, concurrency, speculative decoding, and co-resident services; test larger artifacts only as workload-specific exceptions with measured KV growth and failure behavior.

## DGX Spark deployment policy

For one 128 GB DGX Spark:

1. Start with **60–75 GB of weights**; treat 80 GB as a soft ceiling, not a purchasing guarantee.
2. Prefer models and quantizations native to the NVIDIA stack—especially validated NVFP4 artifacts—when quality is acceptable.
3. Measure memory after loading the intended context length and speculative-decoding configuration, not at an empty prompt.
4. Reserve explicit headroom for Hermes, the model server, monitoring, and at least one realistic concurrent job.
5. Reject any setup that survives only at short context or after closing every other process.

## RTX Spark translation (2026-08-09)

The flagship RTX Spark and DGX Spark occupy essentially the same **model-fit class** on NVIDIA's published headline specifications: up to 6,144 Blackwell CUDA cores, a 20-core Grace CPU, up to 1 PFLOP FP4 compute, and up to 128 GB unified memory.[1][2] For an inference workload that is supported and given a 128 GB RTX Spark configuration, the same conservative **60–80 GB weight envelope** should transfer.

The products are not yet operationally interchangeable. DGX Spark is a shipping, dedicated Linux AI appliance with a documented 128 GB at 273 GB/s, 1 TB or 4 TB NVMe, 10 GbE, and ConnectX-7 networking for multi-node scaling.[3] RTX Spark is a fall-2026 Windows-on-Arm platform spanning laptops and compact desktops; NVIDIA has not published one fixed power limit, memory bandwidth, storage, networking specification, or official price because OEM configurations will vary.[1][2]

### Decision split

- Choose **DGX Spark** when the job is a dedicated, always-on Linux/Hermes inference node; mature CUDA containers, predictable thermals, 10 GbE/ConnectX clustering, and deployment certainty matter more than acquisition cost.
- Prefer a **128 GB RTX Spark desktop** when it can replace the daily PC as well as the AI box; Windows creation, gaming, ComfyUI, and local-agent use are first-class goals; and independent benchmarks confirm that the OEM's sustained power and cooling preserve near-DGX performance.
- Treat an **RTX Spark laptop** as portability-first. The same capacity can determine what models load, but a thin chassis may not sustain the same throughput as a desktop AI appliance. Do not infer sustained parity from the shared “1 PFLOP” peak figure.
- Keep the software-risk distinction explicit: RTX Spark has native CUDA and vendor commitments from ComfyUI, Adobe, llama.cpp, and others, but Windows-on-Arm application, Python-wheel, custom-node, driver, and emulation compatibility must be proven on the shipping systems.[2]

DGX Spark currently lists at **$4,699** from NVIDIA.[4] RTX Spark pricing is not official. For Lyle's present cash-timing season, there is no reason to pay the DGX premium before the fall RTX desktop configurations, prices, sustained benchmarks, and software compatibility are known—unless a paid workload immediately requires the DGX Linux appliance.

### Clusterability is workload-specific

Lyle's strongest RTX Spark thesis is **repeatable 128 GB unified-memory nodes**: begin with one useful local-LLM/creative machine, then add homogeneous nodes as demand grows. The intended acquisition sequence is options-based rather than speculative: the first 128 GB desktop must justify itself as the daily-PC replacement; additional nodes are funded only from strong VXE performance and only after the chosen OEM's ConnectX hardware, drivers, and distributed inference are verified. If shipping RTX Spark desktops lack a credible tightly coupled cluster path, the fallback is to keep one RTX Spark as the standalone daily PC/local-AI workstation and—only from later VXE surplus cash—build a separate ConnectX-equipped DGX Spark cluster for very large distributed models. This remains dreambuilding rather than a current procurement commitment. That is compelling for horizontal scaling—independent agents, batch requests, concurrent model servers, retrieval, embeddings, and separate image/video generations can be assigned by node with little inter-node communication.

Do not treat multiple RTX Spark boxes as one transparent pool of URAM. A two-node setup has **two 128 GB memory domains**, not one automatically coherent 256 GB GPU. Running one model across both requires a distributed runtime and explicit tensor or pipeline partitioning; on slower interconnects, single-request latency may stagnate or worsen even while aggregate throughput improves.[7]

RTX Spark networking appears to be an **OEM configuration choice**, not a settled platform-wide omission. The announced ASUS desktop documents **10 GbE** but no ConnectX-7/RDMA interface.[5] Conversely, HP displayed an unnamed RTX Spark mini-PC prototype with what reporters identified as two ConnectX-7 ports; HP has not named the unit or confirmed that those ports will survive into the retail specification.[8] Ten-gigabit Ethernet has a theoretical ceiling of 1.25 GB/s before protocol overhead. By contrast, each DGX Spark QSFP/ConnectX-7 port supports up to **200 Gb/s** or 25 GB/s—20 times the line rate—and NVIDIA provides direct multi-Spark clustering playbooks.[6] This distinction makes a ConnectX-equipped RTX Spark materially more valuable for sharding one large, communication-heavy model across nodes.

Therefore separate the procurement claims:

- **RTX Spark cluster:** potentially excellent price/capacity/efficiency for a distributed fleet of mostly independent workers; one node can fail or upgrade without retiring the fleet.
- **DGX Spark cluster:** stronger fit for one model or tightly coupled workload spanning nodes because the high-speed interconnect is part of the appliance.
- **Custom PC cluster:** not impossible and can exceed either platform with add-in 100/200 GbE or InfiniBand, but loses Spark's compact, homogeneous, low-power 128 GB unified-memory package and may cost more to make operationally equivalent.

The gating procurement requirement for RTX Spark is now explicit: buy only an OEM configuration with 128 GB memory, **ConnectX-7/QSFP if tightly coupled clustering is central** (10 GbE is acceptable for independent-worker scaling), Linux/container viability if required, and demonstrated multi-node inference. Treat claims of “clusterable” as incomplete until the benchmark states whether it measured **aggregate independent throughput, single-model capacity, or single-request latency**.

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
- [[faleth/process/llm-inference-serving-five-optimization-surfaces-2026]]

## Sources

[1] https://www.nvidia.com/en-us/products/rtx-spark — NVIDIA RTX Spark product page
[2] https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark — NVIDIA RTX Spark announcement
[3] https://docs.nvidia.com/dgx/dgx-spark/hardware.html — NVIDIA DGX Spark hardware overview
[4] https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark — NVIDIA DGX Spark marketplace listing
[5] https://www.asus.com/us/displays-desktops/mini-pcs/proart-mini-pc-series/proart-gr1x-mini-pc — ASUS ProArt GR1X RTX Spark desktop specifications
[6] https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html — NVIDIA DGX Spark ConnectX-7 clustering guide
[7] https://docs.vllm.ai/en/stable/serving/parallelism_scaling — vLLM parallelism and scaling guidance
[8] https://www.notebookcheck.net/Mac-challenger-Nvidia-RTX-Spark-HP-mini-PC-previewed-with-ConnectX-7-ports-up-to-128GB-RAM.1317028.0.html — HP RTX Spark prototype reportedly shown with ConnectX-7 ports
