# AI Model / Provider Landscape, Especially OpenRouter-Relevant Models and Pricing

Purpose: rolling industry report informed by daily Last30Days debriefs. This file captures the distilled direction of the industry over time, not merely daily notes.

## Current Direction
- The model market is a routing and caching market: select by task, context, price, latency, cache behavior, multimodal needs, and reliability.
- OpenRouter-style aggregation makes cheap long-context models practical for triage/extraction/drafting, while premium models remain useful for final reasoning and high-stakes review.
- **GPT-5.6 tiering (Sol / Terra / Luna)** on OpenAI + OpenRouter (Jul 9–10, 2026) codifies a three-layer everyday stack: flagship long-horizon agentic (Sol $5/$30), balanced everyday/agent mid-tier (Terra $2.50/$15, marketed near GPT-5.5 quality at ~half cost), and high-volume cheap (Luna $1/$6).
- Compound/router products such as Fusion need separate cost accounting because headline placeholder rows do not equal effective cost.
- Prompt-cache and response-cache visibility should become part of every recurring agent workflow budget (OpenAI notes more predictable prompt caching / cache breakpoints on GPT-5.6).
- **MCP-native routing** on aggregators (OpenRouter-class) is becoming the default interface for agent tool loops—not a side integration.
- Provider **service tiers** (`flex` / `priority`) and per-endpoint price, latency, throughput, and uptime are becoming machine-readable routing inputs; a model ID alone no longer describes the operational service being bought.
- **Effort controls and premium speed variants** are now explicit routing dimensions: Claude Opus 5 standard versus Fast makes latency value and supervision savings part of accepted-result economics, not merely a model-family choice.
- Cheap coding/agent workers such as **poolside/laguna-xs-2.1** and **meituan/longcat-2.0** matter for cron/volume economics, but must be benchmarked on accepted-result cost. The July 21 removal of **tencent/hy3:free** confirms that promotional free routes cannot be treated as durable dependencies.
- Daily full-ID snapshots and pricing checks are now mandatory operational evidence: catalog removals are exactly auditable, and DeepSeek V3.2's July 15 cache-price jump shows why cheap-worker assumptions must expire automatically.
- Free routes are opportunistic capacity, not durable infrastructure: July 20 removed six free endpoints at once, reinforcing preflight checks and paid fallback requirements.

## Major Shifts to Watch
- Promotional cache pricing and cheap large-context models are becoming decisive for agent loops and recurring research jobs.
- Provider/model churn remains high; workflows need fallbacks rather than hard dependency on any one free or discounted model.
- Activity/cost dashboards, cache-hit rate, provider reliability, and routing telemetry are becoming operational infrastructure.
- Chinese/open models continue pressuring pricing and expanding viable cheap-agent choices.
- **Usage mix can shift faster than catalog churn**—OpenRouter token share moving toward Chinese/open routes even when model count is flat (social telemetry).
- **Tiered frontier families** (Sol/Terra/Luna pattern) will force explicit Hermes routing policies, not a single “default model.”

## Faleth Relevance
- Maintain a Faleth/OpenRouter routing policy: cheap model for classification/extraction (HY3:free / Luna / Laguna), mid-tier for drafting/orchestration (Terra A/B vs Sonnet 5 / GPT-5.5), premium for final reasoning/review (Sol / GPT-5.5 / Sonnet 5), multimodal only when required.
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

### 2026-06-29
- Official API **2026-06-29**: **339** models; Lyle stack pricing unchanged (Grok 4.20, GPT-5.5, Opus 4.7, DeepSeek V4 Flash, Fusion placeholder) ([API](https://openrouter.ai/api/v1/models)). **GPT-5.6 Sol** preview announced but not in catalog yet ([OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/)). X agent-volume narrative on OpenRouter—social-level ([milkroaddaily](https://x.com/milkroaddaily/status/2071262095795257754)). Signal: strong (API), medium (preview).

### 2026-06-30
- Official API pull: **338** models; Lyle-relevant pricing **stable**—Grok 4.20 **$1.25/$2.50** (cache read **$0.20/M**), GPT-5.5 **$5/$30**, Opus 4.7 **$5/$25**, DeepSeek V4 Flash **$0.09/$0.18** (cache **$0.02/M**); Fusion placeholder pricing; **no gpt-5.6 / grok-composer IDs** in catalog ([API](https://openrouter.ai/api/v1/models)). Newest `created` entries include **sakana/fugu-ultra** (Jun 30) and Gemini image models (Jun 23). X: OpenRouter cited for near-zero agent experimentation ([0xJeff](https://x.com/0xJeff/status/2071881103409901807)). Signal: strong (API), medium (social).

### 2026-07-01
- Official API **2026-07-01**: **338** models; Lyle stack **stable**—Grok 4.20, GPT-5.5, DeepSeek V4 Flash cache economics unchanged; **`anthropic/claude-sonnet-5`** newest Anthropic listing (**$2/$10**, cache read **$0.20/M**); Fusion placeholder; no grok-composer in catalog ([API](https://openrouter.ai/api/v1/models)). OpenRouter June open-weight insights + X on agent routing/volume share ([blog](https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/), [OpenRouter Sonnet 5](https://x.com/OpenRouter/status/2072020173872325088)). Signal: strong (API), medium (social).

### 2026-07-02
- Official API **2026-07-02**: **338** models; **`anthropic/claude-fable-5`** confirmed **$10/$50/M** (cache read **$1/M**); Sonnet 5 and Lyle core IDs unchanged; Fusion placeholder ([API](https://openrouter.ai/api/v1/models)). X on Fable redeploy/routing (**secondary to API**) ([Fable chatter](https://x.com/i/status/2072405997289877846)). Signal: strong (API), medium (social).

### 2026-07-03
- Official API **2026-07-03**: **340** models; **new `poolside/laguna-xs-2.1`** agentic coding model **$0.06/$0.12/M** plus **`:free`** variant (**262K** ctx, Jul 2 created stamp); Sonnet 5 **$2/$10/M**, GPT-5.5 **$5/$30/M**, DeepSeek V3.2 **$0.23/$0.34/M**; Fusion placeholder negatives ([API](https://openrouter.ai/api/v1/models)). X: open-weight/Chinese models dominate token economics; planner+judge vs cheap worker routing ([GotoNathan](https://x.com/GotoNathan/status/2072681740439617922), [stretchcloud Fusion cost](https://x.com/stretchcloud/status/2072632626268037373)). Signal: strong (API), medium (social).

### 2026-07-04
- Official API **2026-07-04**: **340** models—**stable vs prior day**; Lyle stack pricing unchanged; **Poolside Laguna XS 2.1** still newest paid coding entry; Fusion placeholder negatives ([API](https://openrouter.ai/api/v1/models)). OpenRouter **Jun 30** blog item on **DeepSeek V4 agentic token share** ([blog](https://openrouter.ai/blog/all/)). Signal: strong (API), weak (24h catalog delta).

### 2026-07-05
- Official API **2026-07-05**: **340** models, **26** free variants—**stable**; Lyle stack + Laguna XS 2.1 pricing unchanged; Fusion placeholder negatives ([API](https://openrouter.ai/api/v1/models)). X: **Chinese-model token share** growth on OpenRouter and **LongCat 2.0 / “Alpha”** leaderboard chatter—**social-level** ([token share](https://x.com/ddkarakullukcu/status/2073722739924312212), [LongCat](https://x.com/JulianGoldieSEO/status/2073723031344849225)). Signal: strong (API), medium (usage narrative).

### 2026-07-06
- Official API **2026-07-06**: **340** models—**stable**; Lyle stack unchanged (Sonnet 5 **$2/$10/M**, GPT-5.5 **$5/$30/M**, DeepSeek V3.2 **$0.23/$0.34/M**, Laguna XS 2.1 **$0.06/$0.12/M**); **26** free variants; Fusion placeholder negatives ([API](https://openrouter.ai/api/v1/models)). X: OpenRouter **MCP routing** promo (up to **24×** savings cited) plus **GLM-5.2** / **Fugu Ultra** pricing chatter—**social-level** until API IDs appear ([OpenRouter](https://x.com/OpenRouter/status/2073811537567867029), [GLM](https://x.com/grok/status/2073565912179847296), [Fugu](https://x.com/PonderoAI/status/2073772739827990624)). Signal: strong (API), medium (MCP narrative).

### 2026-07-07
- Official API **2026-07-07**: **343** models (**+3**); **new** `tencent/hy3` **$0.20/$0.80/M** and **`tencent/hy3:free`**; **`sakana/fugu-ultra`** listed **$5/$30/M**; Lyle stack pricing **unchanged** ([API](https://openrouter.ai/api/v1/models)). X: Chinese-model **volume share** on OpenRouter—**social-level** ([thread](https://x.com/thehypedotnews/status/2074244462478303740)). Signal: strong (API delta); medium (usage narrative).

### 2026-07-08
- Official API **2026-07-08**: **343** models—**stable**; Lyle stack unchanged; **`tencent/hy3:free`** still **$0/$0** per API ([API](https://openrouter.ai/api/v1/models)). X: **`hy3:free`** promo chatter (Jul 21 end cited—**social-level**) ([HY3](https://x.com/i/status/2074766296596525121)). Signal: strong (API); medium (promo narrative).

### 2026-07-09
- Official API **2026-07-09**: **343** models—**stable**; Lyle stack unchanged (`claude-sonnet-5` **$2/$10/M**, `gpt-5.5` **$5/$30/M**, `deepseek-v3.2` **$0.23/$0.34/M**, `laguna-xs-2.1` **$0.06/$0.12/M**, `hy3:free` **$0/$0**); **`deepseek/deepseek-v4-flash`** **$0.09/$0.18/M** ([API](https://openrouter.ai/api/v1/models)). X: **agentic token share** and **HY3:free** tool-calling recommendations—**social-level** ([TeksCreate](https://x.com/TeksCreate/status/2075116705102061722), [SingularLab](https://x.com/SingularLabNews/status/2075161901558886498)). Signal: strong (API); medium (usage narrative).

### 2026-07-10
- Official API **2026-07-10**: **347** models (**+4** vs 343 on 2026-07-09). **New GPT-5.6 family:** `openai/gpt-5.6-sol`/`sol-pro` **$5/$30/M**, `terra`/`terra-pro` **$2.50/$15/M**, `luna`/`luna-pro` **$1/$6/M** (~1.05M ctx, created 2026-07-09) ([API](https://openrouter.ai/api/v1/models), [OpenAI Sol](https://openai.com/index/previewing-gpt-5-6-sol/), [OR X](https://x.com/OpenRouter/status/2075271807855452196)).
- Lyle stack: Sonnet 5 **$2/$10/M**, GPT-5.5 **$5/$30/M**, DeepSeek V3.2 **~$0.21/$0.32/M** (slightly down), Laguna XS 2.1 **$0.06/$0.12/M**, `tencent/hy3:free` **$0/$0**, DeepSeek V4 Flash **$0.09/$0.18/M**.
- Practical routing frame: Terra as everyday/agent mid-tier experiment vs Sonnet 5 / GPT-5.5; Luna/HY3/Laguna for volume; Sol for hard long-horizon only.
- Signal: **strong** (full API + official pricing).

### 2026-07-13
- Official API **2026-07-13 ~11:01 UTC**: **345 models**, net **-2** versus Jul 10; exact removed IDs were not reconstructable from the prior compact snapshot. Lyle stack stable: Sonnet 5 **$2/$10/M** (cache **$0.20**), GPT-5.5 **$5/$30/M** (cache **$0.50**), DeepSeek V3.2 **$0.2145/$0.32175/M** (cache **$0.02145**), Laguna XS 2.1 **$0.06/$0.12/M** plus `:free`; GPT-5.6 Sol/Terra/Luna and `hy3:free` stable ([API](https://openrouter.ai/api/v1/models)). Fresh FT RSS headline on enterprise Chinese-model adoption reinforces price pressure but is **snippet-level**. Signal: **strong** (API), **medium** (cost narrative).

### 2026-07-14
- Official API **~11:01 UTC**: **344 models**, net **-1**; today's full 344-ID snapshot establishes the baseline for exact future deltas, but yesterday's removed ID cannot be reconstructed. Lyle stack pricing remains stable. Official service-tier docs expose `flex`/`priority` and per-endpoint price, latency, throughput, and uptime; route policy should therefore log endpoint/service tier as well as model ID ([API](https://openrouter.ai/api/v1/models), [service tiers](https://openrouter.ai/docs/guides/features/service-tiers), [endpoint API](https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model)). Signal: **strong**.

### 2026-07-15
- Official API **~11:04 UTC**: **343 models**; exact full-ID diff found **0 additions** and removal of `sao10k/l3.1-70b-hanami-x1`. DeepSeek V3.2 changed to **$0.269/$0.40/M** with **$0.1345/M cache read** (about **+25.4%/+24.3%/+527%** vs Jul 14); Sonnet 5, GPT-5.5, and Laguna XS 2.1 base prices remain stable. OpenRouter MCP added task insights, filters, and provider pinning ([API](https://openrouter.ai/api/v1/models), [MCP update](https://x.com/OpenRouter/status/2077131714678435994)). Signal: **strong**.

### 2026-07-16
- Official API **~11:02 UTC**: **342 models**; exact full-ID diff found **0 additions** and removal of `arcee-ai/coder-large`. Lyle stack pricing is unchanged: Sonnet 5 **$2/$10/M** (cache **$0.20**), GPT-5.5 **$5/$30/M** (cache **$0.50**), DeepSeek V3.2 **$0.269/$0.40/M** (cache **$0.1345**), Laguna XS 2.1 **$0.06/$0.12/M** (cache **$0.03**) plus `:free` ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**; retain coder-route fallback.

### 2026-07-17
- Official API **~11:00 UTC**: **344 models**; exact full-ID diff found additions `moonshotai/kimi-k3` and `meta/muse-spark-1.1`, with **no removals**. Kimi K3: 1,048,576 context, text+image input, **$3/$15/M**, cache **$0.30/M**. Muse Spark 1.1: 1,048,576 context, text/image/video/file/audio input, **$1.25/$4.25/M**, cache **$0.15/M**. Lyle's Sonnet 5 / GPT-5.5 / DeepSeek V3.2 / Laguna prices are unchanged ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**; benchmark Muse for multimodal triage and Kimi for long-horizon work before routing changes.

### 2026-07-18
- Official API **~11:00 UTC**: **344 models**, but exact diff found additions `thinkingmachines/inkling` and `openrouter/auto-beta` plus removals `meta-llama/llama-3.2-11b-vision-instruct` and `nvidia/llama-3.3-nemotron-super-49b-v1.5`. Inkling: 1,048,576 context, text/image/audio input, **$1/$4.05/M**, cache **$0.17/M**. Auto Router Beta: 2M context and task-aware routing with placeholder pricing; selected-route cost must be logged. Core-stack pricing unchanged ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**; flat counts conceal fallback churn.

### 2026-07-19
- Official API **~11:00 UTC**: **344 models** with exact full-ID diff of **0 additions / 0 removals**. Core stack remains unchanged: Sonnet 5 **$2/$10/M** (cache **$0.20**), GPT-5.5 **$5/$30/M** (cache **$0.50**), DeepSeek V3.2 **$0.269/$0.40/M** (cache **$0.1345**), Laguna XS 2.1 **$0.06/$0.12/M** (cache **$0.03**) plus `:free`. Kimi K3 news is continuing reaction; benchmark it before routing changes ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**.

### 2026-07-20
- Official API **~11:01 UTC**: **338 models**, exact diff **0 additions / 6 removals**. Removed free routes: Dolphin Mistral Venice, Llama 3.2 3B, Llama 3.3 70B, Hermes 3 405B, Qwen3 Coder, and Qwen3 Next 80B. Core stack remains unchanged: Sonnet 5 **$2/$10/M** (cache **$0.20**), GPT-5.5 **$5/$30/M** (cache **$0.50**), DeepSeek V3.2 **$0.269/$0.40/M** (cache **$0.1345**), Laguna XS 2.1 **$0.06/$0.12/M** (cache **$0.03**) plus `:free` ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**; assign paid fallbacks and preflight every free dependency.

### 2026-07-21
- Official API **~11:01 UTC**: **338 models**, exact diff **+1 / -1**. Added `meituan/longcat-2.0` (131,072 context, **$0.30/$1.20/M**); removed `tencent/hy3:free`. Core-stack pricing is unchanged. Remove HY3 from fallback assumptions and benchmark LongCat against Laguna on accepted-result cost before routing changes ([API](https://openrouter.ai/api/v1/models), [LongCat](https://openrouter.ai/meituan/longcat-2.0)). Signal: **strong**.

### 2026-07-22
- Official API **~11:01 UTC**: **342 models**, exact diff **+4 / -0**. Added `google/gemini-3.6-flash` **$1.50/$7.50/M**, `google/gemini-3.5-flash-lite` **$0.30/$2.50/M**, `poolside/laguna-s-2.1` **$0.10/$0.20/M**, and `poolside/laguna-s-2.1:free`. Core-stack pricing is unchanged. Benchmark Flash-Lite for extraction, Flash for general/multimodal work, and Laguna S against XS/LongCat on accepted-result cost ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**.

### 2026-07-23
- Official API **~11:01 UTC**: **342 models**, exact full-ID diff **0 additions / 0 removals**. Core stack remains stable: Sonnet 5 **$2/$10/M** (cache **$0.20**), GPT-5.5 **$5/$30/M** (cache **$0.50**), DeepSeek V3.2 **$0.269/$0.40/M** (cache **$0.1345**), and Laguna XS 2.1 **$0.06/$0.12/M** (cache **$0.03**) plus `:free` ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**; continue accepted-result benchmarks before rerouting.

### 2026-07-24
- Official API **~11:01 UTC**: **343 models**, exact full-ID diff **+1 / -0**. Added `inclusionai/ling-3.0-flash:free`; core-stack pricing remains unchanged. Treat Ling as opportunistic bounded capacity and benchmark structured output, tool use, latency, availability, and accepted-result cost against Gemini 3.5 Flash-Lite and Laguna XS while retaining a paid fallback ([API](https://openrouter.ai/api/v1/models)). Signal: **strong**.

### 2026-07-25
- Official API **~11:01 UTC**: **345 models**, exact full-ID diff **+2 / -0**. Added `anthropic/claude-opus-5` (**$5/$25/M**, cache read **$0.50/M**, 1M context) and `anthropic/claude-opus-5-fast` (**$10/$50/M**, cache read **$1/M**, 1M context). Core-stack pricing remains unchanged. Benchmark standard Opus 5 against GPT-5.5/Sonnet 5 first; Fast requires measured latency value before paying 2× ([Anthropic](https://www.anthropic.com/news/claude-opus-5), [API](https://openrouter.ai/api/v1/models)). Signal: **strong**.
