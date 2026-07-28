---
type: article
source: x-article
source_url: https://x.com/i/article/2080052071097663488
shared_post: https://x.com/jack/status/2080056638820450400
author: jack (@jack)
published_at: 2026-07-22T22:25:22Z
retrieved_at: 2026-07-23T00:44:07Z
article_id: "2080052071097663488"
status_id: "2080056638820450400"
cover_image: https://pbs.twimg.com/media/HN3WeN-X0AAKYrK.jpg
related: ["[[research/raw/sources/block-buzz-2026-07-22]]", "[[research/faleth/process/buzz-sovereign-agent-workspace-analysis-2026]]", "[[research/faleth/process/member-gated-compute-mesh-for-sovereign-agents-2026]]"]
tags: [x-ingest, lyle-x-share, raw, article, buzz, block, agents, context, sovereignty]
---

# Why We're Buzzing

## Article

yesterday we released buzz. it's an open source workspace that puts people, agents, conversations, and code on the same level, behind one cryptographic identity system. we built it to reduce our dependency on slack and github, and we're sharing it so anyone can do the same.

the biggest problem it solves is context. teams today spread their work across a chat tool, a code host, a CI system, and now a pile of ever-changing agent tools. every seam loses information...and agents feel it the most. they can't help with what they can't see.

we felt this earlier than most. block is rebuilding itself to be an intelligence. goose, the agent substrate we built and open sourced at the start of 2025, works across the company every day, and the deeper we go the more the seams between tools become the limit. buzz solves a lot of the problems we experienced.

buzz stores everything as a signed event on a relay you host yourself. every message, patch, review, workflow step, and approval. one record, one search. people and agents get the same kind of identity: their own keys, channels, and an audit trail. an agent on buzz is an equal member of the team. it can search history, open repos, send patches, review code, run workflows, and edit canvases. everything it does is signed and attributable, which builds trust and accountability.

a few principles we held:

self-sovereign: run your own relay. own your domain and your data. carry your keys anywhere.

open: apache 2.0, built on nostr, model agnostic. harnesses for goose, codex, and claude code. no lock-in, including to us.

one context: a feature branch becomes a channel. patches, CI results, review, and the merge decision live in the same thread as the conversation that shaped them. code review becomes a conversation with a permanent record.

it's early! channels, threads, DMs, canvases, media, search, the audit log, workflows, and the desktop app work today. full git hosting is being wired up. mobile and push are coming. approval gates are partially built. each workspace runs through a single relay, so federation between relays is the clearest path to the full decentralization our design points to.

the bigger work is ahead: tighter scoping for agents so they can operate in workspaces where some things stay private, a hosted option for teams that don't want to run infrastructure, token efficiency (we've done a lot of work here), and an ecosystem of workflows and agents on the open spec. agents that can transact feels like a natural place for us to take it next.

we believe buzz is truly social AI. the category so far has meant people chatting with AI companions, AI filling human feeds or chats, or agents talking to each other while people watch. people and agents as equal members of the same network doing work together feels like the first interesting and durable version.

we're going to run more and more of block on buzz. that's the first test we care about. the second is whether it's useful to you. it's all open. come build with us!

https://buzz.xyz

https://github.com/block/buzz

## Provenance

The article body was extracted from the server-rendered article entity embedded in the public X status page. X API metadata returned the article title and identifier; the article content was not available through the exposed X API operation or logged-out article route directly.

## Distilled claim

Block is building Buzz because the seams among chat, code hosting, CI, and agent tools destroy organizational context. Buzz treats people and agents as equal, attributable members operating over one self-hosted signed event record. The intended end state is a self-sovereign organizational intelligence with portable identity, unified context, scoped agents, open workflows, and eventually transaction-capable agents.
