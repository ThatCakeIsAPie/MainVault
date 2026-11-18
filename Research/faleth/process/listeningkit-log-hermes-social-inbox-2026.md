---
title: ListeningKit log as a Hermes social inbox (2026)
created: 2026-11-12
updated: 2026-11-12
type: principle
tags: [ai, software, infrastructure, open-source, systems, leverage]
sources:
  - raw/transcripts/lyle-x-share-2120940613726265419.md
confidence: medium
---

# ListeningKit log as a Hermes social inbox (2026)

## Signal

matt. (@matthewsoldit) launched **log**, an open-source local CLI and MCP server from ListeningKit, and pointed Nous Research at the repo. The pitch is that an AI agent can read and answer the user's own social inboxes — especially X DMs and X Chat, plus Discord, Slack, and Instagram — in the user's voice, with sends held until the user says yes. He says he built it so he could "play video games" instead of doing "boring outbound work." ^[raw/transcripts/lyle-x-share-2120940613726265419.md]

A community Hermes plugin, **listeningkit-log**, is already in the official plugin catalog (merged Nov 12, 2026, version 0.1.0, Hermes `>=0.23.1`, catalog marked for Windows). It does not bundle log. It starts the user's own `logMcp` process and adds inbox and outreach skills. Writes are marked untrusted, so Hermes asks before anything is sent, and unattended cron cannot send. ^[raw/transcripts/lyle-x-share-2120940613726265419.md]

## How it talks to the platforms

This is not official OAuth. log signs in by reusing session cookies or a local browser login, then talks to each platform through reverse-engineered internal APIs (the announcement credits @treg_ai, @subquadratic, and @morluto; a catalog test reported X as `directApi (twikit)`). Commands that change something stay a dry run until `--live` is added. Account data lives in `~/.logCli` on the machine. Reddit and LinkedIn were only "session check" at retrieval. Facebook uses a browser. Optional hosted keys (SubQ, Jina, AssemblyAI, voice cloning) are separate from the core local install. ^[raw/transcripts/lyle-x-share-2120940613726265419.md]

That clashes with an existing house preference: prefer **owned OAuth + a ledger** over opaque scrapers. See [[faleth/process/hermes-cloud-and-x-mcp-2026]].

## Lyle's take

> This looks very interesting. Curious if it is useful for our Hermes setup

## Hermes-fit verdict: maybe

It is a real Hermes plugin, and it is aimed at the Windows Desktop setup Lyle already runs. It would **add** a social inbox and outbound layer, especially X DMs and X Chat, which the hosted X MCP page still treats as an open question. It would **not** replace Hermes as the workhorse, Opus as the orchestrator, DeepSeek on the Sparks, or the official Hermes messaging gateways. Official Discord and Slack paths should stay first where they already work.

Reasons to take it seriously:

- The catalog entry is merged, the plugin is Windows-first, and a PowerShell installer exists.
- Dry-run by default, plus Hermes approval on writes, is the right shape for a tool that can send as Lyle.
- The gap it claims to fill — X DMs and X Chat from Hermes, plus a voice check on drafts — is a real gap.

Reasons to go slow:

- Cookie and unofficial-API access is a ToS and account-ban risk, and it goes against the OAuth preference already on the X MCP page.
- The live tool set comes from whatever log version is installed, not from the plugin's pinned commit, so the catalog pin does not freeze the code that talks to X.
- In the launch thread, one reviewer warned that the public log repo may have leaked internal setup detail, and that optional Twenty CRM telemetry is on by default. Those claims were not checked here, but they are a hygiene flag.
- The product is built for outbound social selling. That is not the current VXE-first calendar, and the existing Hermes page already warns against opening a second agent-ops rabbit hole during cash-timing months.

### What adopting it would take

On the Windows Hermes box, with Hermes at least 0.23.1: install log locally, sign in only the accounts worth the risk, then install and enable `listeningkit-log`. Start with a session check and dry-run reads. Leave the MCP server untrusted. Do not turn on live sends, and do not put this in cron, until a read-only pass looks right. Do not paste session cookies into a chat, a vault page, or a shared profile. If official X MCP later covers DMs under OAuth, prefer that for X and keep log only for platforms official tools cannot reach.

This was not installed or tested on Lyle's machine here.

## Related

- Raw: [[raw/transcripts/lyle-x-share-2120940613726265419]]
- Repo: https://github.com/matthewdonsemail-lab/log
- Plugin: https://github.com/deepmroot/listeningkit-log
- [[faleth/process/hermes-cloud-and-x-mcp-2026]]
- [[faleth/process/messaging-ui-as-agent-operating-surface-2026]]
- [[faleth/content/hermes-grok-x-content-machine-2026]]
- [[faleth/process/hermes-bot-mode-persistent-profiles-2026]]
