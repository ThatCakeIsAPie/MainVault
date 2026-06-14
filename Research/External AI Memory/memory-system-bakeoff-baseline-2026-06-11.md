# Memory System Bakeoff Baseline — 2026-06-11

## Purpose
Evaluate whether AgentMemory remains useful compared with Honcho and GBrain over the next month. Lyle wants set-and-forget usefulness, inspectability, portability, and low babysitting.

## Baseline status

### Hermes built-in memory
    
    Memory status
    ────────────────────────────────────────
      Built-in:  always active
      Provider:  (none — built-in only)
    
      Installed plugins:
        • byterover  (requires API key)
        • hindsight  (API key / local)
        • holographic  (local)
        • honcho  (API key / local)
        • mem0  (API key / local)
        • openviking  (API key / local)
        • retaindb  (API key / local)
        • supermemory  (requires API key)
    

### AgentMemory
    ┌  agentmemory status
    │
    ◆  Connected — v0.9.18 at http://localhost:3111
    │
    ◇  agentmemory ──────────────────────────────────────────────────────────────╮
    │                                                                            │
    │  Health:       ✓ healthy                                                   │
    │  Sessions:     0                                                           │
    │  Observations: 0                                                           │
    │  Memories:     1                                                           │
    │  Graph:        0 nodes, 0 edges                                            │
    │  Circuit:      closed                                                      │
    │  Heap:         30 MB                                                       │
    │  Uptime:       335522s                                                     │
    │  Viewer:       http://localhost:3113                                       │
    │                                                                            │
    │  Provider:     ✗ noop (no key)                                             │
    │  Embeddings:   bm25-only                                                   │
    │  Flags:                                                                    │
    │    ✗ GRAPH_EXTRACTION_ENABLED         Knowledge graph extraction           │
    │    ✗ CONSOLIDATION_ENABLED            Memory consolidation                 │
    │    ✗ AGENTMEMORY_AUTO_COMPRESS        LLM-powered observation compression  │
    │    ✗ AGENTMEMORY_INJECT_CONTEXT       In-conversation context injection    │
    │                                                                            │
    ├────────────────────────────────────────────────────────────────────────────╯

### GBrain
    Pages:     72
    Chunks:    116
    Embedded:  0
    Links:     101
    Tags:      37
    Timeline:  3
    
    By type:
      concept: 20
      note: 18
      principle: 16
      entity: 9
      query: 4
      comparison: 4
      analysis: 1

Doctor top issues summary:
    status: warnings
    health_score: 40
    top_issues:
    - brain_score — Brain score 43/100 (embed 0/35, links 25/25, timeline 0/15, orphans 8/15, dead-links 10/10)
    - embed_staleness — 116 stale chunks (small backlog)
    - embedding_column_registry — Active column 'embedding' is 0.0% populated. Search quality silently degraded on un-embedded chunks. Fix: gbrain embed --column embedding --stale (write-side support v2) OR gbrain config set search_embedding_column embedding
    - embeddings — No embeddings yet. Run: gbrain embed --stale
    - graph_coverage — Entity link coverage 0%, timeline 0% (9 entity pages). Run: gbrain extract all
    - jsonb_integrity — Could not check JSONB integrity
    - pack_upgrade_available — Active pack: gbrain-base@1.0.0+7bd490ab. Successor available: gbrain-base-v2@1.0.0+b9bebaa4. Preview: `gbrain onboard --check --explain`
    - pgvector — Could not check pgvector extension

### Honcho
    SDK installed: yes (honcho-ai).
    Hermes honcho config scaffolded at /root/.hermes/honcho.json but disabled because no Honcho API key or self-hosted server is configured.
    Docker is not installed, making local self-host non-trivial on this VPS.

## GBrain import baseline
- Imported: /home/lylecole4/Documents/Main Vault/Research
- Pages: 72
- Chunks: 116
- Links: 101
- Timeline entries: 3
- Embeddings: 0 (no provider configured; keyword/BM25 baseline only)
- Search mode: conservative

## 2026-06-14 wiring update

Lyle asked to wire the stack properly after discovering GBrain had not been ingesting the full vault.

### Obsidian / LLM Wiki
- Human-readable source of truth remains `/home/lylecole4/Documents/Main Vault`.
- Research wiki control files exist at `Research/SCHEMA.md`, `Research/index.md`, and `Research/log.md`.
- Current vault scale observed during wiring: 325 Markdown notes / 1172 total files in Main Vault; 80 Markdown notes in Research.

### GBrain
- Registered durable source: `obsidian` → `/home/lylecole4/Documents/Main Vault`.
- Source is federated, so default cross-source GBrain retrieval can hit the vault.
- Full sync imported 318 Obsidian Markdown pages into GBrain.
- Post-sync GBrain stats: 403 pages, 1239 chunks, 354 links, 55 tags, 6 timeline entries.
- Embeddings remain disabled because no OpenAI/Voyage embedding key is configured in the GBrain environment; current retrieval is keyword/BM25 + available rerank/search behavior, not fully vector-backed.
- Important operational caveat: `gbrain serve` over MCP can hold the PGLite lock. Large syncs should stop Hermes gateway / GBrain MCP first, then restart gateway after sync.

### Hermes MCP
- `agentmemory` MCP is enabled and `hermes mcp test agentmemory` discovered 7 tools.
- `gbrain` MCP is enabled and available in live Hermes sessions, but `hermes mcp test gbrain` caused an OOM kill during this wiring attempt. Live GBrain tool calls still worked afterward. Treat `hermes mcp test gbrain` as expensive on this VPS unless memory is increased.

### AgentMemory
- AgentMemory service is active as systemd user service.
- MCP tools available: recall, save, sessions, smart_search, export, audit, governance_delete.
- Recall quality should be evaluated by actual retrieval usefulness, not assumed from the service being active.

### Honcho
- Honcho local server at `http://127.0.0.1:8000` returned health `{"status":"ok"}`.
- Hermes memory provider is `honcho`; status reports provider available.
- Honcho remains configured in stable tools-only mode (`recallMode=tools`, `writeFrequency=turn`) because earlier hybrid/context modes caused Python SIGABRT on CLI exit.

### Automation
- Added systemd user timer `gbrain-obsidian-sync.timer`.
- Schedule: daily around 04:10 UTC with up to 10 minutes randomized delay.
- Script: `/root/.hermes/scripts/gbrain-obsidian-sync.sh`.
- Script behavior: stop Hermes gateway to release GBrain/PGLite lock, sync `obsidian` source without embeddings, extract links/timeline, log stats, then restart gateway.
- Log file: `/root/.hermes/logs/gbrain-obsidian-sync.log`.

## Evaluation criteria for 2026-07-11
- Which layer was actually used without manual babysitting?
- Which layer improved answers/workflows?
- Which layer was inspectable/editable?
- Which layer handled project/business/source-of-truth knowledge best?
- Which layer handled live user/project profile best?
- Did AgentMemory accumulate useful operational memories or remain mostly empty?
- Should AgentMemory be removed, retained as explicit operational memory, or replaced by Honcho/GBrain?
