---
title: Delta Phone Interface — Grok Voice over Hermes
created: 2026-07-14
updated: 2026-07-29
type: principle
tags: [ai, infrastructure, software, systems, leverage]
sources:
  - research/raw/articles/2026-07-14-xai-grok-voice-agent-builder.md
  - raw/x-bookmarks/2026-07-26/2081408374315602338.md
  - research/raw/transcripts/lyle-x-share-2082339029375426914.md
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

### Current stack fit

The VPS currently has local faster-whisper `base` for STT, `voice.auto_tts: true`, and `tts.provider: xai`; Hermes resolves the new `XAIStreamer` through xAI OAuth. Because xAI subscription availability may change, the reliable zero-cost fallback is Edge TTS: it is not raw-PCM streaming, but Hermes still starts speaking sentence-by-sentence. A paid ElevenLabs or OpenAI key is only justified after native voice becomes a daily interface and lower first-word latency is measurably valuable.

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
