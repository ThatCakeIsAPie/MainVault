---
title: xAI Grok Voice Agent Builder — launch evidence
created: 2026-07-14
updated: 2026-07-14
type: source
tags: [xai, grok, voice-agent, telephony, mcp, hermes, jarvis]
source_url: https://x.ai/voice?campaign=voice-agent-builder-updates-email
announcement_url: https://x.ai/news/grok-voice-agent-builder
retrieved_at: 2026-07-14T15:56:12Z
confidence: high
---

# xAI Grok Voice Agent Builder — launch evidence

## Lyle context

Lyle shared the xAI Voice Agent Builder on 2026-07-14 because it appears to supply the missing live-voice and telephony shell for the previously discussed **JARVIS-style Delta**: call a dedicated number, converse naturally, let the voice layer hand work to Hermes, and support call transfers or handoffs.

## Verified product claims

Official xAI search results, Voice Agent API documentation, SIP documentation, and the xAI launch thread support the following:

- Voice Agent Builder launched in beta on 2026-07-01.
- No-code creation of Grok Voice agents with instructions, knowledge retrieval, tools, guardrails, call logs, and observability.
- A provisioned phone number is available; existing numbers can be connected through direct SIP.
- SIP routes PSTN, PBX, or contact-center calls into a realtime Voice Agent API session.
- Incoming calls produce a signed `realtime.call.incoming` webhook containing a `call_id`; the application joins the call over WebSocket.
- Call control includes `refer` for transfer to another PSTN or SIP destination and `hangup`.
- The realtime agent can use built-in search, document collections, custom JSON-schema functions, and remote MCP servers.
- Remote MCP configuration supports authorization tokens, custom headers, and an allowlist of exposed tools.
- The realtime voice channel is bidirectional over WebSocket and supports telephone-native G.711 codecs.

## Pricing observed 2026-07-14

- Realtime voice: **$0.05/minute** ($3/hour).
- xAI launch material says provisioned telephony adds **$0.01/minute**.
- Estimated combined provisioned-phone cost: **$0.06/minute**, **$3.60/hour**, before paid tools or any separate carrier/SIP costs.

## Sources

- [Voice Agent Builder](https://x.ai/voice)
- [Launch announcement](https://x.ai/news/grok-voice-agent-builder)
- [Voice Agent API](https://docs.x.ai/developers/model-capabilities/audio/voice-agent)
- [SIP Phone Calls](https://docs.x.ai/developers/model-capabilities/audio/voice-agent/sip)
- [xAI pricing](https://docs.x.ai/developers/pricing)
- [Official launch thread](https://x.com/SpaceXAI/status/2072342803787702422)

## Retrieval caveat

The x.ai landing page itself returned a Cloudflare block to the browser and the launch article returned HTTP 403 to a direct fetch. Claims above were cross-checked against xAI search snippets, official docs fetched successfully over HTTPS, and the official xAI launch thread. No blocked-page body was fabricated.
