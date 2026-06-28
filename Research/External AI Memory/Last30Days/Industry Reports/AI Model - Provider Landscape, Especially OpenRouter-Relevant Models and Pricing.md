# AI Model / Provider Landscape, Especially OpenRouter-Relevant Models and Pricing

Purpose: rolling industry report informed by daily Last30Days debriefs. This file captures the distilled direction of the industry over time, not merely daily notes.

## Current Direction
- The model market is a routing and caching market: select by task, context, price, latency, cache behavior, multimodal needs, and reliability.
- OpenRouter-style aggregation makes cheap long-context models practical for triage/extraction/drafting, while premium models remain useful for final reasoning and high-stakes review.
- Compound/router products such as Fusion need separate cost accounting because headline placeholder rows do not equal effective cost.
- Prompt-cache and response-cache visibility should become part of every recurring agent workflow budget.

## Major Shifts to Watch
- Promotional cache pricing and cheap large-context models are becoming decisive for agent loops and recurring research jobs.
- Provider/model churn remains high; workflows need fallbacks rather than hard dependency on any one free or discounted model.
- Activity/cost dashboards, cache-hit rate, provider reliability, and routing telemetry are becoming operational infrastructure.
- Chinese/open models continue pressuring pricing and expanding viable cheap-agent choices.

## Faleth Relevance
- Maintain a Faleth/OpenRouter routing policy: cheap model for classification/extraction, mid-tier for drafting, premium cached model for final reasoning/review, multimodal only when required.
- Log model ID, provider, input/output tokens, cache read/write, response-cache hit, cost, workflow, and quality outcome.
- Use budget caps for compound models and recurring agents; do not assume OpenRouter Fusion placeholder pricing is meaningful.

## Running Source Debrief Notes
### 2026-06-08
- Web search found OpenRouter’s model and pricing pages as current sources. Search snippets said the models page listed DeepSeek V3.1 Nex-N1 with June 8 relevance and that pricing covers 400+ models / 60+ providers with platform fees and free model options ([OpenRouter models](https://openrouter.ai/models), [OpenRouter pricing](https://openrouter.ai/pricing)).
- X signal said OpenRouter updated its Pricing tab with live cache-hit rates and historical traffic, making effective price more visible for long-context / repeated-context agent usage ([OpenRouter pricing update](https://x.com/OpenRouter/status/2063504950429147376)).
- X signal also mentioned newly added free image models: `sourceful/riverflow-v2.5-pro:free` and `sourceful/riverflow-v2.5-fast:free` ([NetCyberseo OpenRouter note](https://x.com/NetCyberseo/status/2063681087407272201)).

### 2026-06-09
- OpenRouter web snippets reported June 8 blog/activity around model tests, compliance/human-oversight features, DeepSeek V3.1 Nex-N1 availability, Riverflow V2.5 notices, and current models/pricing pages ([OpenRouter blog](https://openrouter.ai/blog), [OpenRouter models](https://openrouter.ai/models), [OpenRouter prompt caching docs](https://openrouter.ai/docs/guides/best-practices/prompt-caching)).
- X signal said Nex-N2-Pro/mini and DeepSeek V3.1 are drawing builder attention for price/performance, open weights, benchmark claims, quantization/local-running experiments, and OpenRouter availability ([Nex-N2 signal](https://x.com/HonorestV5/status/2063878280806367685), [OpenRouter/free Nex signal](https://x.com/mr_r0b0t/status/2064086767750271269), [DeepSeek V3.1 signal](https://x.com/ssuhjo/status/2064095796606157194)).
- Signal strength: medium. Strong current chatter; some benchmarks are self-reported and web details are snippet-level.

### 2026-06-10
- OpenRouter’s official API model endpoint was checked directly. It listed `anthropic/claude-fable-5` with 1,000,000 context, 128,000 max completion tokens, and pricing equivalent to **$10/M input, $50/M output, $1/M cache read, $12.50/M cache write** ([OpenRouter models API](https://openrouter.ai/api/v1/models), [Claude Fable 5 page](https://openrouter.ai/anthropic/claude-fable-5)).
- The same official API check listed `minimax/minimax-m3` at about **$0.30/M input, $1.20/M output, $0.06/M cache read** with very large context/token limits ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- X signal reported cache-hit-rate visibility in OpenRouter pricing and builder discussion around Chinese-model price/performance share ([cache visibility signal](https://x.com/ainews_24_7/status/2063600862925320426), [Chinese-model traffic signal](https://x.com/kokasync/status/2064446387555860506)).
- Signal strength: strong for official pricing; medium for social interpretation.

### 2026-06-11
- X signal reported OpenRouter launched **Activity Explorer** for spend, token usage, cache hit rates, agents, models, users, providers, and trends ([OpenRouter Activity Explorer X post](https://x.com/OpenRouter/status/2064732886750699961)).
- OpenRouter also reported Fable seeing roughly twice the usage volume of Opus 4.8 in a recent comparison; treat this as provider-reported social signal, not an independent benchmark ([OpenRouter Fable usage X post](https://x.com/OpenRouter/status/2064788002606309723)).
- Official API check listed 338 models. Recent entries included `anthropic/claude-fable-5` and `~anthropic/claude-fable-latest` dated 2026-06-09 at **$10/M input, $50/M output, $1/M cache read, $12.50/M cache write**, plus `nvidia/nemotron-3-ultra-550b-a55b` dated 2026-06-04 at **$0.50/M input, $2.50/M output, $0.15/M cache read** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- Signal strength: strong for official pricing/API evidence; medium for usage interpretation.

### 2026-06-12
- Official OpenRouter API inspection returned 337 models. Recent relevant entries included `anthropic/claude-fable-5` at 1M context and **$10/M input, $50/M output, $1/M cache read, $12.50/M cache write**; `qwen/qwen3.7-plus` at 1M context and **$0.32/M input, $1.28/M output, $0.064/M cache read**; `minimax/minimax-m3` at ~1.05M context and **$0.30/M input, $1.20/M output, $0.06/M cache read**; `anthropic/claude-opus-4.8` at 1M context and **$5/M input, $25/M output, $0.50/M cache read**; and `google/gemini-3.5-flash` at ~1.05M context and **$1.50/M input, $9/M output, $0.15/M cache read** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- X signal found no major new model announcement in the last 24 hours; OpenRouter’s current operational story remains Activity Explorer/cache telemetry and visible cache-hit rates ([OpenRouter Activity Explorer](https://x.com/OpenRouter/status/2064730079872381392), [pricing/cache tab signal](https://x.com/OpenRouter/status/2063504950429147376)).
- Signal strength: strong for official API pricing; medium for cache-usage/social interpretation.

### 2026-06-13
- Official OpenRouter API inspection again returned 337 models. Relevant entries included `anthropic/claude-opus-4.8` at **$5/M input, $25/M output, $0.50/M cache read, $6.25/M cache write**; `openai/gpt-5.5` at **$5/M input, $30/M output, $0.50/M cache read**; `qwen/qwen3.7-plus` at **$0.32/M input, $1.28/M output, $0.064/M cache read**; `deepseek/deepseek-v4-pro` at **$0.435/M input, $0.87/M output, $0.003625/M cache read**; and `x-ai/grok-4.20` at **$1.25/M input, $2.50/M output, $0.20/M cache read** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- Fresh X/current discussion reinforced prompt caching as the key cost lever and cache-aware prompt structuring as an operating practice ([cache implementation signal](https://x.com/vela_gao/status/2065459874348384512), [cache savings signal](https://x.com/akashgohil10/status/2065319124201574691)).
- Signal strength: strong for official API pricing; medium for real-world cache-savings interpretation. Faleth should design standing prompts and agent loops so stable prefixes can actually be cached.

### 2026-06-14
- OpenRouter launched/discussed **Fusion** (`openrouter/fusion`), a server-side compound model/panel workflow priced as the sum of underlying model calls plus OpenRouter fees; OpenRouter explicitly noted its cost comparison included cache hits ([Fusion launch](https://x.com/OpenRouter/status/2065856860435988482), [cache-inclusive comparison note](https://x.com/OpenRouter/status/2065864932155920534)).
- Official OpenRouter API inspection returned 337 models. Relevant entries included `openrouter/fusion` with placeholder negative pricing fields, `moonshotai/kimi-k2.7-code` at **$0.75/M input, $3.50/M output, $0.16/M cache read**, `anthropic/claude-fable-5` at **$10/M input, $50/M output, $1/M cache read, $12.50/M cache write**, `qwen/qwen3.7-plus` at **$0.32/M input, $1.28/M output, $0.064/M cache read**, `minimax/minimax-m3` at **$0.30/M input, $1.20/M output, $0.06/M cache read**, and `deepseek/deepseek-v4-flash` at **$0.09/M input, $0.18/M output, $0.02/M cache read** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- Signal strength: strong for API pricing, medium for Fusion quality/cost claims. Faleth should test Fusion only on bounded synthesis tasks with budget caps.

### 2026-06-19
- Official OpenRouter API inspection returned 341 models. Selected rows: `openai/gpt-5.5` at **$5/M input, $30/M output, $0.50/M cache read**; `openai/gpt-5.5-pro` at **$30/M input, $180/M output**; `anthropic/claude-opus-4.5` at **$5/M input, $25/M output, $0.50/M cache read, $6.25/M cache write**; `google/gemini-3-pro-image` at **$2/M input, $12/M output, $0.20/M cache read, $0.375/M cache write**; `openrouter/fusion` still exposed placeholder negative pricing fields ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- X/current signal discussed Opus/GPT-5.5 cost tradeoffs, prompt caching, and routing/Fusion strategies; treat social pricing claims as secondary to the API ([OpenRouter cost signal](https://x.com/AndreBuckingham/status/2067748188602200074), [Fusion/routing signal](https://x.com/kirillk_web3/status/2067602480620536078)).
- Signal strength: strong for official API pricing; medium for social cost/quality interpretation. Faleth should separate provider prompt caching, OpenRouter response caching, and compound-model call costs in logs.

### 2026-06-20
- OpenRouter X signal highlighted stackable workspace inference budgets with different reset periods, while current discussion stressed prompt/KV caching and provider pinning to preserve cache hits ([OpenRouter budget signal](https://x.com/OpenRouter/status/2068068872180080644), [cache/cost signal](https://x.com/fmontes/status/2068094806295797938), [provider-routing/cache signal](https://x.com/packers_owner_j/status/2067986345608331422)).
- Official OpenRouter API inspection returned 340 models. Selected rows: `openai/gpt-5.5` **$5/M input, $30/M output**; `openai/gpt-5.5-pro` **$30/M input, $180/M output**; `anthropic/claude-fable-5` **$10/M input, $50/M output**; `anthropic/claude-opus-4.8` **$5/M input, $25/M output**; `x-ai/grok-4.20` **$1.25/M input, $2.50/M output** with 2M context; `google/gemini-2.5-pro` **$1.25/M input, $10/M output**; `openrouter/fusion` still showed placeholder negative pricing fields ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- Signal strength: strong for API pricing; medium for social cache commentary. Faleth should attach budgets to workflows/agents and track cache/provider routing explicitly.

### 2026-06-21
- X search found no major official OpenRouter announcement in the strict window, but social discussion continued around prompt caching and subscription/API cost tradeoffs ([cache/cost discussion](https://x.com/BuildFastWithAI/status/2068199086952763469), [subscription-cost discussion](https://x.com/tyrtyre201/status/2068341425905815949)).
- Official OpenRouter API inspection returned 340 models. Selected current rows included `anthropic/claude-opus-4.8` **$5/M input, $25/M output, $0.50/M cache read, $6.25/M cache write**; `x-ai/grok-4.20` **$1.25/M input, $2.50/M output, $0.20/M cache read** with 2M context; `google/gemini-2.5-pro` **$1.25/M input, $10/M output, $0.125/M cache read**; `moonshotai/kimi-k2.7-code` **$0.612/M input, $3.069/M output, $0.1296/M cache read**; `openrouter/fusion` still exposed placeholder negative pricing fields ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- Signal strength: strong for API pricing; medium for social cache commentary. Continue logging provider, cache, response-caching, and workflow-budget fields separately.

### 2026-06-22
- Official OpenRouter API inspection returned 340 models. Selected rows: `google/gemini-3.1-flash-image` / Nano Banana 2 **$0.50/M input, $3/M output**; `google/gemini-3-pro-image` / Nano Banana Pro **$2/M input, $12/M output, $0.20/M cache read, $0.375/M cache write**; `anthropic/claude-fable-5` **$10/M input, $50/M output, $1/M cache read, $12.50/M cache write**; `qwen/qwen3.7-plus` **$0.32/M input, $1.28/M output, $0.064/M cache read**; `x-ai/grok-4.3` **$1.25/M input, $2.50/M output, $0.20/M cache read**; `openai/gpt-5.5` **$5/M input, $30/M output, $0.50/M cache read**; `deepseek/deepseek-v4-flash` **$0.09/M input, $0.18/M output, $0.02/M cache read** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- X/current discussion reinforced cheap-model adoption/security concern, routing as moat, response/prompt-caching economics, and billing friction ([cheap-model risk](https://x.com/kiyohero/status/2068844828792885431), [routing/harness signal](https://x.com/0xrwu/status/2068834437001781737), [billing friction](https://x.com/HelloCalcaas/status/2068828348495634454)). Signal strength: strong for official pricing; medium for social interpretation.

### 2026-06-23
- Official OpenRouter API inspection returned 340 models. Recent relevant rows included `google/gemini-3.1-flash-image` / Nano Banana 2 at **$0.50/M input, $3/M output**; `google/gemini-3-pro-image` / Nano Banana Pro at **$2/M input, $12/M output**; `moonshotai/kimi-k2.7-code` at about **$0.68/M input, $3.41/M output**; `qwen/qwen3.7-plus` at **$0.32/M input, $1.28/M output**; `anthropic/claude-opus-4.8` at **$5/M input, $25/M output**; and `anthropic/claude-fable-5` at **$10/M input, $50/M output** ([OpenRouter models API](https://openrouter.ai/api/v1/models)).
- X/current discussion compared OpenRouter Fusion with Sakana Fugu as compound/orchestrator systems. Treat this as medium-confidence social signal; Fusion's API row still exposes placeholder negative pricing, so effective cost must be logged as underlying model calls plus platform economics, not headline placeholder pricing.
### 2026-06-24
- Official OpenRouter API fetch returned 339 models at 2026-06-24T11:02Z; selected rows included Claude Opus 4.8 at $5/M input and $25/M output, Grok 4.20 at $1.25/M and $2.50/M, Qwen3.7 Plus at $0.32/M and $1.28/M, DeepSeek V4 Flash at $0.09/M and $0.18/M, Kimi K2.7 Code at $0.74/M and $3.50/M, Gemini 3.1 Flash Image at $0.50/M and $3/M, and Fusion with placeholder negative pricing ([OpenRouter API](https://openrouter.ai/api/v1/models)). X signal highlighted AntLing/Ring 2.6 promotional cache prices and Nex N2 Pro paid transition with cached prompt pricing ([AntLing/Ring](https://x.com/SakethR93178495/status/2069326928549380524), [Nex N2 Pro](https://x.com/NexEcosystem/status/2069386516737216543)). Signal strength: strong for API, medium for X pricing claims.

### 2026-06-27
- Official API returned **339** models; Lyle-relevant pricing unchanged: Grok 4.20 **$1.25/$2.50** (cache read $0.20/M), Opus 4.8 **$5/$25**, GPT-5.5 **$5/$30**, DeepSeek V4 Flash **$0.09/$0.18**; recent adds include **sakana/fugu-ultra** and **z-ai/glm-5.2**; Fusion still placeholder -1 ([OpenRouter API](https://openrouter.ai/api/v1/models)). X: model-wave + **OpenRouter MCP** routing ([OpenRouter MCP](https://x.com/OpenRouter/status/2070630667663163875)). Signal strength: strong (API), medium (social).
### 2026-06-28
- Official API **2026-06-28T11:01Z**: **339** models; Grok 4.20 **$1.25/$2.50** (cache read $0.20/M), Opus 4.8 **$5/$25**, GPT-5.5 **$5/$30**, DeepSeek V4 Flash **$0.09/$0.18**; Fusion placeholder -1; newest tail includes sakana/fugu-ultra, z-ai/glm-5.2 ([API](https://openrouter.ai/api/v1/models)). Jun 27 blog on open-weight agentic production ([blog](https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/)). Signal: strong (API).
