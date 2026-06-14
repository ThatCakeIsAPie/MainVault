# AI Model / Provider Landscape, Especially OpenRouter-Relevant Models and Pricing

Purpose: rolling industry report informed by daily Last30Days debriefs. This file captures the distilled direction of the industry over time, not merely daily notes.

## Current Direction
- The model market is becoming a routing problem, not a single-best-model problem. OpenRouter-style aggregation makes it practical to select models by task, cost, latency, cache economics, context length, and reliability.
- OpenRouter is adding higher-order routing products such as compound/panel models, making prompt caching and panel composition central to effective price.
- Cheap/open high-performing models are increasingly credible for classification, extraction, draft generation, and coding assistance; premium models should be reserved for high-stakes reasoning/review.
- Prompt caching and effective price are becoming central to long-context agent economics.
- Premium long-context agent models are getting powerful but expensive; stable reusable context plus cache-aware prompt design is now an operating discipline, not a nerd tax footnote.
- Provider dashboards and activity analytics are becoming part of the model-selection loop: usage-weighted cost, cache-hit rate, and provider reliability matter as much as headline benchmark scores.
- Cache-aware routing now matters at the model-selection level: some credible long-context models have cache-read prices that radically change effective cost for repeated research, agent loops, and standing system prompts.

## Major Shifts to Watch
- OpenRouter model availability/deprecation churn, especially free/cheap models and image/video-adjacent providers.
- Cache-hit-rate visibility, cache read/write pricing, context-window pricing cliffs, and provider-specific cache rules.
- Independent verification of new open-weight benchmark claims.
- Reliability differences under tool use, long context, structured output, and coding-agent workloads.
- Whether Chinese/open models continue gaining traffic share among builders due to price/performance.

## Faleth Relevance
- Create a Faleth/OpenRouter routing policy: cheap model for classification/extraction, mid-tier model for draft generation, premium cached model for final reasoning and review, multimodal only when required.
- Track actual cost and quality per workflow: daily research, GovCon parsing, proposal drafting, FRR marketing content, and Hermes agent tasks.
- Avoid building workflows around volatile free models unless fallback routing exists.
- Use expensive 1M-context models only when the problem actually requires long-horizon synthesis, coding, or ambiguous reasoning.

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
