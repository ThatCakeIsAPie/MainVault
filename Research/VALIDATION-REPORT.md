---
title: Validation Report
created: 2026-06-22
updated: 2026-06-22
type: summary
tags: [meta, framework]
sources: []
---

# Vault Validation Report

**Date:** 2026-06-22  
**Tool:** `_tools/validate_vault.py` (read-only, exit 0)  
**Vault:** `/home/lylecole4/Documents/Main Vault`

## Interpretation

Refreshed pass after validator noise reduction (metadata docs skip unresolved-link checks; inline/fenced code stripped before wikilink extraction). **352** markdown files scanned; **37** findings (35 warnings, 2 info). No secret-scan hits.

Remaining gaps are substantive, not self-referential: **raw/transcripts** provenance fields still need backfill (19), **unresolved wikilinks** (14) mostly audio recording embeds and title-case Business/Research links that do not match slug-style note names, plus three **frontmatter** gaps on Research Ideas/Plans and one **wikilinks** threshold warning on a plan note with no outbound links.

**Top categories:** raw_frontmatter (19), unresolved_link (14), frontmatter (3), wikilinks (1).

Optional follow-ups: add source_url / ingested / sha256 on transcript raw notes; align display-title links to existing slugs (e.g. five-step sequencing model, Faleth Capital entity); use embed syntax for audio assets if resolution warnings are unwanted.

---

# Vault Validation Report (tool output)

**Vault:** `/home/lylecole4/Documents/Main Vault`
**Files scanned:** 352
**Issues:** 37

## Summary by severity

- **info:** 2
- **warning:** 35

## Summary by category

- **raw_frontmatter:** 19
- **unresolved_link:** 14
- **frontmatter:** 3
- **wikilinks:** 1

## Sample issues

- [warning] **unresolved_link** — `Business/Ideas/2026-06-08 - GovCon Opportunity Radar.md`: Unresolved wikilink target: [[Daily Industry Landscape Debrief - 2026-06-08]]
- [warning] **unresolved_link** — `Business/LTD Amway/Info Sessions/2026/2026-06-11 Ethan Ellenberg.md`: Unresolved wikilink target: [[Recording 20260611220952.m4a]]
- [warning] **unresolved_link** — `Business/LTD Amway/Info Sessions/2026/2026-06-18 Nic Oshodi.md`: Unresolved wikilink target: [[Recording-20260618-220245-16k-32k.mp3]]
- [warning] **unresolved_link** — `Business/LTD Amway/Others/2026/2026-06-13 Josh Gordon Men's Night Owl.md`: Unresolved wikilink target: [[Recording-20260613-16k-32k.mp3]]
- [warning] **frontmatter** — `Research/Ideas/Faleth Capital — System Overview & Takeaways.md`: Missing or empty frontmatter key: title
- [warning] **frontmatter** — `Research/Ideas/Faleth Capital — System Overview & Takeaways.md`: Missing or empty frontmatter key: updated
- [warning] **frontmatter** — `Research/Plans/akash-hermes-deployment.md`: Missing YAML frontmatter
- [warning] **wikilinks** — `Research/Plans/akash-hermes-deployment.md`: Fewer than 2 wikilinks (found 0)
- [warning] **unresolved_link** — `Research/concepts/foundational/faleth-capital-economic-philosophy.md`: Unresolved wikilink target: [[Faleth Capital]]
- [warning] **unresolved_link** — `Research/entities/lyle-cole.md`: Unresolved wikilink target: [[Five-Step Sequencing Model]]
- [warning] **raw_frontmatter** — `Research/raw/processed-sources.md`: Missing or empty raw field: source_url, ingested, sha256
- [info] **raw_frontmatter** — `Research/raw/transcripts/2026-04-06 — Theological Reflection.md`: No frontmatter on raw note
- [warning] **raw_frontmatter** — Multiple `Research/raw/transcripts/*.md`: Missing source_url / ingested / sha256 (2026-06-11 through 2026-06-19 batch)
- [warning] **raw_frontmatter** — `Research/raw/transcripts/claude-memory-2026-05-16.md`: Missing or empty raw field: source_url
- [info] **raw_frontmatter** — `Research/raw/transcripts/Trust_Effective_Effort_and_The_Factory.md`: No frontmatter on raw note

_(Full machine run: `python3 _tools/validate_vault.py . --format markdown`)_