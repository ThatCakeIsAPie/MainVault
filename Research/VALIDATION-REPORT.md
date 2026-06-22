---
title: Vault Validation Report
created: 2026-06-22
updated: 2026-06-22
type: meta
tags: [validation, okf, hygiene]
---

# Vault Validation Report

**Date:** 2026-06-22
**Vault:** `Main Vault` (Research wiki + OKF hygiene)
**Tool:** `_tools/validate_vault.py` (read-only; exit 0)

## Summary

| Metric | Value |
|--------|-------|
| Files scanned | 352 |
| Issues | 2 |
| Severity | info only |

### By category

- **raw_frontmatter:** 2 (info — notes without YAML provenance blocks)

## Interpretation

This pass cleared prior **warnings** from audio embeds, unresolved Research wikilinks, missing wiki frontmatter, and incomplete raw provenance on dated transcripts. Remaining items are **informational**: two legacy raw transcripts under `Research/raw/transcripts/` still lack frontmatter (`Theological Reflection`, `Trust_Effective_Effort_and_The_Factory`). No secrets, unresolved links, or wiki frontmatter gaps were reported on this run.

### Fixes applied (2026-06-22)

1. **Audio links** — Replaced `Recording 20260611220952.m4a` with `Recording-20260611-16k-32k.mp3` in info-session notes and transcripts; validator now resolves common audio asset basenames (`.mp3`, `.m4a`, `.wav`, `.ogg`, `.opus`).
2. **Wikilinks** — Aliased links to `faleth-capital`, `foundational/five-step-sequencing-model`, `lyle-cole`, and `2026-06-08-daily-industry-landscape-debrief`.
3. **Frontmatter** — Completed Research wiki fields on Faleth system overview and Akash Hermes deployment plan.
4. **Raw provenance** — Added `source_url`, `ingested`, and `sha256` on audio-backed and conversation-backed transcripts; excluded `processed-sources.md` from raw provenance requirements.

## Sample issues (current run)

- [info] **raw_frontmatter** — `Research/raw/transcripts/2026-04-06 — Theological Reflection.md`: No frontmatter on raw note
- [info] **raw_frontmatter** — `Research/raw/transcripts/Trust_Effective_Effort_and_The_Factory.md`: No frontmatter on raw note

## How to re-run

From vault root:

```bash
python3 _tools/validate_vault.py . --format text
python3 _tools/validate_vault.py . --format markdown --max-list 80
```