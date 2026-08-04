---
title: Delta Phone Interface — Grok Voice over Hermes
created: 2026-07-14
updated: 2026-07-31
type: principle
tags: [ai, infrastructure, software, systems, leverage]
sources:
  - research/raw/articles/2026-07-14-xai-grok-voice-agent-builder.md
  - raw/x-bookmarks/2026-07-26/2081408374315602338.md
  - research/raw/transcripts/lyle-x-share-2082339029375426914.md
  - raw/x-bookmarks/2026-07-29/2082339029375426914.md
  - raw/x-bookmarks/2026-07-29/2082509593280688317.md
  - research/raw/transcripts/lyle-x-share-2082864345520722221.md
  - raw/x-bookmarks/2026-07-29/2082430003460166142.md
  - raw/x-bookmarks/2026-07-30/2082864166960877718.md
  - raw/x-bookmarks/2026-07-29/2082570290828304553.md
  - raw/articles/2026-07-31-audio8-tts-preview-readme.md
confidence: high
---

# Delta Phone Interface — Grok Voice over Hermes

## Thesis

xAI's Voice Agent Builder materially collapses the **presence + conversation** layers of Lyle's JARVIS vision. It supplies a live speech-to-speech agent, a phone number, SIP, call transfer, remote MCP/custom tools, guardrails, and observability. Hermes should remain the **brain and hands**: identity, memory, vault/GBrain/Honcho context, subagent delegation, and real tool execution.

The correct design is not “replace Delta with Grok Voice.” It is:

> **Grok Voice is Delta's ears and mouth; Hermes is Delta's operating system.**

## What changed from the 2026-07-09 assessment

The earlier recommendation assumed assembling telephony plus a realtime provider such as Twilio/Vapi/Bland or custom Grok Voice code. Voice Agent Builder now packages most of that commodity plumbing:

- dedicated number or bring-your-own SIP;
- inbound phone sessions;
- realtime duplex voice;
- transfer/handoff;
- custom functions and remote MCP;
- call logs, transcripts, guardrails, and observability.

That means a useful prototype is no longer “build a telephony platform.” It is primarily **build a narrow, secure Hermes bridge and prove the interaction model**.

## Recommended v0 architecture

1. **Phone edge — xAI Voice Agent Builder**
   - Dedicated number.
   - Delta voice/personality instructions.
   - Realtime conversation, interruption/turn detection, and call control.

2. **Narrow bridge — HTTPS tool endpoint**
   - Prefer a purpose-built remote MCP or custom-function bridge over exposing the entire Hermes tool universe.
   - Initial tool surface:
     - `ask_delta(message, conversation_id)` — send a toolful request into a persistent Hermes session.
     - `start_delta_task(goal, conversation_id)` — delegate longer work without blocking the call.
     - `check_delta_task(task_id)` — retrieve status/result.
   - Authenticate every request; scope by explicit allowlist; log calls and enforce timeouts/idempotency.

3. **Hermes brain**
   - Use the existing authenticated OpenAI-compatible API server on the VPS (`/v1/chat/completions` or Sessions API).
   - Preserve one Hermes conversation/session per phone caller or per Lyle-only line.
   - Hermes performs vault, Honcho/GBrain, browser, terminal, cron, and subagent work under its normal policies.

4. **Return path**
   - Short work returns synchronously to the voice agent.
   - Long work returns an acknowledgement plus task ID; the call continues while Hermes delegates.
   - Completion can be spoken if the call remains active, sent through Telegram, or trigger an outbound callback later.

5. **Human handoff**
   - xAI `refer` transfers the phone call to a human/PSTN/SIP destination.
   - This is distinct from a **work handoff** to Hermes; both should be explicit tools so the agent does not confuse “transfer the caller” with “delegate the task.”

## Why not expose Hermes directly as MCP?

Hermes can run as an MCP server with `hermes mcp serve`, but current Hermes documentation says that server mode is **stdio-only**. xAI requires a reachable remote HTTP MCP endpoint. More importantly, exporting Hermes' full toolset to a realtime voice model would be reckless: a misunderstood sentence should not become `terminal`, file mutation, email, or CRM side effects at conversational latency.

A thin bridge gives:

- a tiny attack surface;
- explicit tool schemas;
- bounded authority;
- stable session routing;
- asynchronous task semantics;
- audit logs and revocation;
- freedom to change the internal Hermes model/provider without rebuilding the phone edge.

## Existing infrastructure confirmed 2026-07-14

- Hermes gateway is running on the VPS.
- The Hermes API Server is enabled and listening locally on `127.0.0.1:8642`.
- An unauthenticated probe correctly returned HTTP 401, confirming bearer-key enforcement.
- xAI OAuth is available to Hermes, but Voice Agent Builder/API billing and credentials may still require configuration in the xAI console.
- The API server is intentionally local-only; the bridge should remain the only public ingress rather than exposing port 8642 directly.

## Voice as a mobility and capture interface

Alex Finn's field report adds a separate use case from telephony: **continuous voice access to an always-on headquarters computer** while walking, driving, or moving between places. The durable mechanism is not human-sounding speech. It is converting otherwise awkward, screenless time into project briefing, idea capture, drafting, decomposition, and delegated execution.

For Delta, this supports a broader interface test: the phone line should make useful work possible away from a desk without pretending every task belongs in voice. Voice is strongest for intent capture, review, prioritization, and starting asynchronous jobs; exact code review, dense comparison, and irreversible actions should still return to a screen or explicit confirmation. The post's claim of four voice hours outperforming eight desk hours is an anecdote, not a benchmark. [[raw/x-bookmarks/2026-07-26/2081408374315602338]]

This complements [[faleth/process/demonstration-to-skill-capture-2026]]: narration can expose intent and tacit judgment, while Hermes converts that input into durable artifacts and verifiable work.

## Native Hermes real-time voice path — 2026-07-29

Hermes now streams generated replies into TTS sentence-by-sentence across CLI, TUI, and Desktop. True chunked providers—ElevenLabs, Gemini, OpenAI, and xAI—can begin yielding PCM audio after the first complete clause; Edge and other synchronous providers still benefit from sentence-level playback instead of waiting for the full answer. [[research/raw/transcripts/lyle-x-share-2082339029375426914]]

This creates a cheaper and simpler **personal Delta voice interface** than the phone architecture above:

- **Hermes Desktop on Lyle's computer** supplies the microphone, speaker, and conversational surface.
- **The existing VPS Hermes backend** retains the same sessions, identity, tools, GBrain/Honcho/vault access, cron jobs, and delegation.
- **Streaming TTS** makes long, toolful answers feel conversational rather than producing a finished audio memo after the work is over.
- **Telegram remains the asynchronous mobile surface.** It can return voice files, but Telegram does not provide the continuous PCM playback channel needed for true barge-in conversation.

The two architectures therefore serve different mobility envelopes:

1. **Desktop/CLI voice:** personal, lowest complexity, best for office/home brainstorming, directing work, reviewing results, and narrating thought loops.
2. **Phone/SIP voice:** works while driving or away from a computer, but still needs a narrow remote bridge, telephony controls, and stricter confirmation boundaries.

The correct sequence is now: prove native Hermes Desktop voice first; add phone/SIP only if Lyle repeatedly needs voice access away from the Desktop machine. This deletes a rather heroic amount of telephony engineering before proving the behavior is valuable.

### Local wake-word activation

Hermes now also supports an optional, locally detected wake word that opens a new voice session in the CLI, TUI, or Desktop app. Combined with streaming TTS, this closes two different latency gaps: the wake word removes the manual start action, while streamed speech reduces the delay before Delta begins answering. Detection is off by default, which is the correct boundary for an always-listening interface. [[raw/x-bookmarks/2026-07-29/2082509593280688317]]

This strengthens the case for testing the native desktop path before building telephony. The immediate experiment is mundane but decisive: enable wake-word activation on one trusted machine, measure false activations and successful hands-free task starts for a week, and keep irreversible actions behind explicit confirmation. A voice interface that awakens elegantly but mishears file deletion is merely Clippy with initiative.

### Current stack fit

The VPS currently has local faster-whisper `base` for STT, `voice.auto_tts: true`, ffmpeg, ONNX Runtime, three AMD EPYC vCPUs, 3.7 GiB RAM, and no NVIDIA GPU. The configured TTS provider remains `xai`, but Lyle's xAI subscription is no longer available; Kokoro is not yet installed. At inspection, roughly 2.0 GiB RAM was available and 2.0 GiB swap was already occupied, so any local voice service must be benchmarked alongside the live gateway rather than congratulated for merely starting.

## Local-first speech edge — Kokoro + faster-whisper (2026-07-30)

Audio8-TTS Preview is technically impressive: 601,159,424 parameters, 11 languages, zero-shot voice cloning, a bundled 44.1 kHz codec, Apache 2.0 licensing, and a reported English Seed-TTS WER of 1.506. Its official README identifies a DualAR architecture, a 2,048-position packed text/audio context, and a recommended CUDA-capable GPU. It is roughly seven times larger than Kokoro-82M. Those extra capabilities do not improve the primary Delta requirement enough to justify becoming the default on the current CPU-only VPS. The benchmark is first-party and the release is explicitly a preview, so production latency and pronunciation still require direct testing. [[raw/x-bookmarks/2026-07-29/2082430003460166142]] [[raw/x-bookmarks/2026-07-30/2082864166960877718]] [[raw/articles/2026-07-31-audio8-tts-preview-readme]]

Kokoro better matches the actual job:

- 82 million parameters;
- eight languages and 54 fixed voices in v1.0;
- Apache-licensed weights;
- StyleTTS2/ISTFTNet decoder with no diffusion;
- ONNX packaging around 300 MB full or 80 MB quantized;
- CPU-oriented deployments and third-party EPYC benchmarks reporting faster-than-real-time aggregate generation;
- no voice-cloning complexity when Delta should sound like one stable character anyway.

The minimal private speech path is:

> microphone or Telegram voice → faster-whisper `base` → Hermes/Delta → Kokoro-82M → speaker or Telegram voice bubble

This localizes the **speech edge**, not the reasoning model. Hermes still uses its cloud planner/executor models and retains the VPS tools, vault, GBrain, Honcho, cron, and delegation stack. The win is eliminating cloud STT/TTS dependence, reducing recurring voice cost, and keeping raw speech away from another provider.

Hermes' official TTS documentation already supports the integration without a core fork: either point the OpenAI provider at an OpenAI-compatible Kokoro server through `tts.openai.base_url`, or register a custom command provider under `tts.providers`. A persistent OpenAI-compatible service is preferable for conversational use because it avoids reloading the model for every sentence and can preserve chunked playback. `Kokoro-FastAPI` is the obvious first adapter; a lightweight `kokoro-onnx` service is the fallback if the FastAPI image is too heavy for this VPS.

### Deployment sequence

1. Benchmark the existing faster-whisper `base` path on short real voice notes: end-of-speech-to-text latency and correction rate.
2. Run Kokoro persistently on the VPS and benchmark cold start, warm first-audio latency, real-time factor, peak RSS, and gateway impact.
3. Pick one fixed Delta voice and test Telegram voice bubbles through ffmpeg.
4. Test Hermes sentence-level streaming in Desktop/CLI.
5. If remote-server latency dominates live conversation, move only the speech service to the Desktop machine attached to the microphone and speakers; keep the Hermes brain on the VPS over the existing private connection.
6. Reconsider Audio8 only when multilingual zero-shot cloning becomes a real requirement or a GPU-capable edge box makes its latency acceptable.

### v0 acceptance gates

- STT accurately handles Lyle's normal speaking cadence without cloud fallback.
- Warm Kokoro generation is faster than playback and begins quickly enough to feel conversational.
- Combined Whisper + Kokoro load does not starve the Hermes gateway or force sustained swap churn.
- One stable voice sounds good enough for daily use; novelty is not a KPI.
- Telegram delivery and Desktop playback both work through the supported Hermes provider path.

### Resource envelope

Kokoro itself is small. The current `kokoro-onnx` release assets are approximately **115 MiB** for INT8 weights plus voices, **196 MiB** for FP16 plus voices, or **337 MiB** for FP32 plus voices. Runtime and API-wrapper overhead matter more than the weight file: lean ONNX deployments are commonly reported in the few-hundred-megabyte range, while PyTorch/FastAPI containers can require at least roughly 1.5–2 GiB free RAM and several gigabytes of disk for the full image and dependencies.

Practical tiers for the Delta speech edge:

- **Proof on the existing VPS:** 3 vCPU / 3.7 GiB RAM, INT8 ONNX, one voice stream, sequential STT then TTS. This should be attempted but is tight because the live host already uses swap.
- **Comfortable always-on service:** 4 vCPU / 8 GiB RAM / 10 GiB free disk. This leaves room for the Hermes gateway, faster-whisper `base`, Kokoro, ffmpeg, and short overlap without living in swap.
- **Desktop/edge ideal:** any recent 4+ core CPU with 8 GiB RAM. No GPU required. A modest GPU can reduce latency, but buying one for an 82M-parameter fixed-voice model would be performance art.

The lean implementation should start with a persistent INT8 `kokoro-onnx` service rather than the approximately 5 GB all-inclusive CPU Docker image. Upgrade the VPS only if measured first-audio latency, gateway contention, or swap pressure fails the acceptance gates.

This is the smallest credible local JARVIS loop. Audio8 can remain in the showroom until we actually need it; specifications are not a constitutional requirement to install every shiny model.

## v0 KPI

One inbound call where Lyle can naturally say:

> “Delta, research X, spin up a subagent to draft Y, and send the result to Telegram.”

Success means:

1. voice remains responsive;
2. Hermes receives the request with the correct identity/session;
3. the long task runs asynchronously;
4. the result arrives through Telegram;
5. no broad Hermes credentials or tools are exposed to xAI.

## Scope deletion

Do **not** start with Raspberry Pi wake words, multi-room audio, outbound callbacks, client-facing agents, or every Hermes tool. First prove the single personal inbound line. Revolutionary notion: test whether Lyle actually enjoys calling his computer before wiring the house like Stark Tower.

A Raspberry Pi + USB microphone + local-model Hermes appliance is a credible later packaging pattern, especially now that Hermes has local wake-word detection, but the bookmarked post is a proposal rather than a measured build report. It does not override the sequence above: validate the voice loop on existing hardware, measure latency and false activations, then move the proven edge onto a dedicated appliance if physical placement or privacy justifies it. [[raw/x-bookmarks/2026-07-29/2082570290828304553]]

## Cost envelope

At the published combined estimate of $0.06/minute:

- 10-minute call: $0.60
- 30-minute call: $1.80
- 60-minute call: $3.60
- 10 hours/month: $36.00

This excludes separately priced tools and any bring-your-own carrier costs.

## Related

- [[research/raw/articles/2026-07-14-xai-grok-voice-agent-builder]]
- [[faleth/process/hermes-cloud-and-x-mcp-2026]]
- [[Personal/Dream Compound Vision]]
