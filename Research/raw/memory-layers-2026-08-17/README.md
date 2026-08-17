---
title: Honcho + GBrain memory calcification
created: 2026-08-17
type: raw
tags: [memory, honcho, gbrain, archive]
---

# Honcho + GBrain memory layers (2026-08-17)

Snapshot taken 2026-08-17 20:38 UTC so these stores can be retired without losing the unique layer.

GBrain **pages are already the vault**. This folder is the *other* memory: Honcho profile/conclusions, plus any GBrain takes/facts/timeline that are not markdown pages.

## What is here

| File | What it is |
|---|---|
| [[honcho-card]] | Standing peer card Delta holds for Lyle |
| [[honcho-representation]] | Curated observations from Honcho |
| [[honcho-conclusions-lyle]] | All unique Delta→Lyle conclusions, newest first |
| `honcho-conclusions-full.jsonl` | Complete Honcho conclusion store (7,553 rows, all observer/observed pairs) |
| `honcho-conclusions-lyle-unique.json` | Machine copy of the Lyle-only set |
|| [[gbrain-snapshot]] | GBrain identity, empty takes/facts, table counts |
| [[gbrain-timeline]] | 56 GBrain timeline entries |

## What is not here

- The 1,884 GBrain wiki pages. Those already live under `Research/` and sync from git.
- Honcho chat message bodies (618 messages). Conclusions are the durable derived layer.
- Hermes built-in `MEMORY.md` / `USER.md`. Those stay in the agent home.

## Counts

- Honcho workspace: `faleth-memory-bakeoff`
- Conclusions total: 7,553
- Delta observing Lyle: 1712 unique
- Other pairs: Delta→Delta 2,173; Lyle→Delta 2,169; Lyle→Lyle 1,499 (in the jsonl only)
