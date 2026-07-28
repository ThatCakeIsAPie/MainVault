---
type: source
status: reviewed
date: 2026-07-22
source_url: https://github.com/block/buzz
source_repo: block/buzz
source_commit: 6d04d27
latest_release_checked: v0.4.22
retrieved_at: 2026-07-22
related: ["[[research/faleth/process/buzz-sovereign-agent-workspace-analysis-2026]]"]
tags: [raw, github, buzz, block, agents, nostr, collaboration, self-hosted]
---

# Source Notes — Block Buzz

## Repository identity

- Repository: [block/buzz](https://github.com/block/buzz)
- License: Apache-2.0
- Inspected commit: `6d04d27`
- Latest release at inspection: [`v0.4.22`](https://github.com/block/buzz/releases/tag/v0.4.22), published 2026-07-21
- GitHub API snapshot: 3,806 stars, 287 forks, 315 open issues; repository created 2026-03-06
- Main implementation: Rust relay/services, TypeScript/React/Tauri desktop and web clients, Flutter mobile client

## Repository claim

Buzz describes itself as:

> A workspace where humans and agents build together, on a relay you own.

The product is a self-hostable collaboration workspace built on Nostr event structures. Humans, agents, workflows, messages, reactions, approvals, canvases, media, and git events share one identity model, one event log, and one search surface.

## Core architecture

- Central self-hosted relay is the source of truth.
- Nostr NIP-01 event format is used on the wire.
- Every action is represented as a signed event with an author public key, event kind, tags, content, hash, and Schnorr signature.
- Relay handles authentication, authorization, persistence, fan-out, full-text search indexing, audit, and workflow triggers.
- Postgres stores events and search data.
- Redis supports pub/sub, presence, and typing.
- S3/MinIO stores media through Blossom-compatible primitives.
- Community/tenant boundary is derived from the request host; unknown hosts fail closed.
- Custom capabilities generally enter as new event kinds rather than bespoke service APIs.

The deployment is centralized even though the event protocol and identity scheme are portable. Buzz explicitly does not operate as a P2P gossip network.

## Agent architecture

Buzz treats agents as workspace members rather than bot integrations:

- Agents have their own Nostr keypairs and identities.
- Channel membership scopes agent access.
- Agent actions produce the same signed/audited event shape as human actions.
- `buzz-cli` provides JSON-in/JSON-out operations designed for agent tool calls.
- `buzz-acp` bridges relay events and @mentions to ACP-compatible agents such as Goose, Codex, Claude Code, and Buzz's own agent.
- `buzz-agent` is a deliberately small ACP agent loop.
- `buzz-dev-mcp` provides shell, file editing, todo, and image tools through MCP.
- ACP separates agent clients from agent implementation; MCP separates agents from tools.
- Each concurrent agent session gets isolated MCP server instances and context.

The agent vision explicitly favors minimality, auditability, bounded processes/output/history, protocol-native composition, and honest failure.

## Collaboration primitives

Buzz currently claims working support for:

- stream channels, forums, DMs, canvases, media, search, and audit log;
- Tauri desktop client;
- agent-first CLI and ACP harness;
- YAML workflows triggered by messages, reactions, schedules, and webhooks;
- git hosting and NIP-34 git events;
- persona packs and agent teams;
- WebSocket Opus huddles;
- relay-gated shared AI compute.

In progress or planned:

- workflow approval executor persistence/resume;
- fuller mobile clients;
- push notifications;
- branch/project binding, merge coordinator, NIP-34 issues, and web-of-trust reputation.

The vision docs clearly distinguish implemented features from designed features.

## Branch as room

The forge vision models a feature branch as a collaboration channel containing:

- request and discussion;
- patches;
- CI outcomes;
- agent reviews;
- human approvals;
- merge event;
- final archived rationale.

The channel becomes the durable record of why the code exists rather than leaving rationale fragmented across chat, issue trackers, CI systems, and pull-request pages.

Some supporting git hosting and event infrastructure works today, while project binding, merge coordination, issues, and reputation are described as future forge-layer work.

## Agent activity feed

The activity-feed design compresses agent activity into:

> agent did [verb] to [object] → [outcome]

Key principles:

- semantic action rather than transport implementation;
- outcome first;
- update a running action in place;
- render idle, silence, and timeout rather than going dark;
- elevate failures and consequential writes;
- suppress low-value reads and heartbeats;
- polished summaries by default, raw truth on demand;
- progressive disclosure rather than raw transcript flooding.

The design goal is to make delegation supervisable without forcing humans to read every tool payload.

## Security and sovereignty notes

Positive properties:

- per-human and per-agent keys;
- channel-scoped membership;
- signed events;
- hash-chain audit log;
- tenant derivation before handlers observe data;
- fail-closed unknown hosts;
- portable identity and protocol formats;
- agent authorization can be contained and revoked independently.

Important caveats:

- The relay remains a central trust and availability boundary.
- DMs are server-readable; end-to-end encryption is only a future consideration.
- At-rest encryption is delegated to the storage layer.
- Self-hosting requires operating Postgres, Redis, object storage, relay, clients, identity/key handling, and upgrades.
- Workflow approvals are not fully executable/resumable yet.
- Several forge capabilities are vision rather than shipping implementation.
- The system is young and rapidly changing.

## Local inspection scope

The repository was shallow-cloned and its README, architecture, agent vision, project vision, activity-feed vision, contributor guidance, test guide, Cargo workspace, and repository metadata were inspected. Buzz was not built or deployed during this review; implementation-status claims above are sourced from the repository's own current documentation and code structure rather than an independent live-system acceptance test.
