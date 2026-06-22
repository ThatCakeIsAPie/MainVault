---
title: Source Manifest
created: 2026-06-22
updated: 2026-06-22
type: summary
tags: [meta, framework]
sources: []
---

# Source Manifest

Human-readable inventory of where knowledge lives and how it flows into Lyle's second brain. **No secrets** — credentials and API keys belong in environment/config stores, not in notes.

## Primary human source

| System | Role | Location / access |
|--------|------|-------------------|
| **Obsidian vault** | Canonical human-readable notes, wikilinks, business/personal/research content | `/home/lylecole4/Documents/Main Vault` (Git repo, branch `main`) |
| **Research wiki** | Structured entities, concepts, comparisons, queries under `Research/` | Governed by [[SCHEMA]]; catalog in [[index]]; actions in [[log]] |

## Machine memory & search

| System | Role | Location / access |
|--------|------|-------------------|
| **GBrain** | Vector + graph brain over vault markdown; hybrid search, entities, takes | Source id `obsidian` → this vault path |
| **GBrain Postgres** | Dedicated pgvector store for embeddings/graph | Docker at `/opt/gbrain-postgres`, `127.0.0.1:55432` |
| **gbrain-obsidian-sync** | Incremental sync vault → GBrain | systemd timer `gbrain-obsidian-sync.timer` |

## Agent & session memory

| System | Role | Location / access |
|--------|------|-------------------|
| **Hermes memory** | Compact turn-injected preferences and environment context for Hermes Agent | Profile-scoped under `~/.hermes/` (default profile) |
| **AgentMemory** | Operational lessons, session observations, consolidation tiers | MCP tools; viewer `http://127.0.0.1:3113` |
| **Honcho** | Self-hosted tools-only profile memory (when enabled) | `/opt/honcho`, API `http://127.0.0.1:8000` |

## Cross-AI context

| System | Role | Location / access |
|--------|------|-------------------|
| **External AI Memory** | Exported context for Claude/other assistants (debriefs, bakeoff baselines) | `Research/External AI Memory/` |

## Planned / future connectors

Not yet wired as first-class ingest pipelines in this manifest:

- Gmail
- X (Twitter)
- GitHub
- Additional raw article/paper ingest automation

When a connector ships, add a row here with `source_url` / ingest path conventions and link from [[log]].

## Provenance chain (ideal)

1. **Raw** capture under `Research/raw/` with `source_url`, `ingested`, `sha256` when applicable.
2. **Wiki** synthesis pages with `sources:` in frontmatter and `[[wikilinks]]`.
3. **GBrain** sync for retrieval; Hermes/AgentMemory for operational recall across sessions.

See [[OKF-COMPATIBILITY]] for format alignment with Open Knowledge Format v0.1.