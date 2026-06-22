---
title: OKF Compatibility
created: 2026-06-22
updated: 2026-06-22
type: summary
tags: [meta, framework]
sources: []
---

# OKF Compatibility (v0.1 mapping)

Concise map between this vault's **Research wiki** conventions and [Open Knowledge Format](https://github.com/google/open-knowledge-format) (OKF) v0.1 ideas. Full vault includes non-Research notes (Business/, Personal/) that are Markdown-first but not fully schema-governed.

## What already aligns

| OKF concept | This vault |
|-------------|------------|
| **Documents as Markdown** | All notes are `.md`; Research wiki is the structured subset |
| **YAML frontmatter** | Required on Research wiki pages per [[SCHEMA]] |
| **`type` field** | Required: `entity`, `concept`, `principle`, `comparison`, `query`, `summary`, etc. |
| **Recommended metadata** | `title`, `created`, `updated`, `tags`, optional `sources`, `confidence`, `contested` |
| **Graph edges** | Obsidian `[[wikilinks]]` (minimum 2 outbound on wiki notes); GBrain adds typed links on sync |
| **Provenance** | `sources:` in wiki frontmatter; raw/ uses `source_url`, `ingested`, `sha256` |
| **Catalog** | [[index]] as human TOC; GBrain as machine index |

## Gaps vs OKF v0.1 (honest)

- **Global OKF manifest** — No single `okf.json` at vault root; rules live in [[SCHEMA]] + this doc.
- **Uniform types outside Research/** — Business/Personal notes use mixed naming (title case, spaces) without enforced `type`.
- **Stable IDs** — Slugs are path/filename based, not UUIDs; OKF-style immutable ids not used.
- **Structured relations** — Wikilinks are untyped; GBrain can add `link_type` but vault files do not require it.
- **Validation gate** — `_tools/validate_vault.py` reports warnings only (exit 0); not blocking CI yet.
- **Binary / media OKF bundles** — Assets exist under `raw/` but no OKF package layout.

## Next steps (low-risk)

1. Run validator periodically; track [[VALIDATION-REPORT]] trends.
2. Backfill raw/ frontmatter on transcripts missing `source_url` or `sha256`.
3. Keep [[SOURCE-MANIFEST]] current as connectors land.
4. Optionally add vault-root `okf.manifest.yaml` later if tooling expects it — fields can mirror [[SCHEMA]].

## Validator scope

Read-only scan excludes `.obsidian/`, `.git/`, `_tools/`. Checks Research wiki frontmatter, raw/ provenance fields, wikilink count, best-effort link resolution, and secret-pattern warnings (no secret values printed).