---
title: Honcho and GBrain retired from HermesDelta
created: 2026-08-17
type: raw
---

# Honcho + GBrain retirement (2026-08-17)

Lyle asked to retire both on the agent before leaving Hetzner.

## Done

- `hermes memory off` — built-in MEMORY.md / USER.md only
- MCP server `gbrain` removed; `xapi` kept
- Cron `bab3a87dc850` (GBrain Research sync) paused
- User timer `gbrain-obsidian-sync` disabled
- `docker compose down` for `/opt/honcho` and `/opt/gbrain-postgres`
- Volumes kept: `honcho_pgdata`, `honcho_redis-data`, `gbrain-postgres_gbrain_postgres_data`
- Morning repo sync no longer calls `gbrain`
- DR backup skips pgdump when those containers are down
- SOUL.md protocol updated

## Not deleted

Compose files, `/opt/honcho`, `/opt/gbrain-postgres`, and named volumes. Faleth CRM Postgres is still running.

## After this chat

Gateway still has the old tools until `/restart`.
