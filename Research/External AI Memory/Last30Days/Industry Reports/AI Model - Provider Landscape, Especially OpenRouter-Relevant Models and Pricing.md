# AI Model / Provider Landscape, Especially OpenRouter-Relevant Models and Pricing

Purpose: rolling industry report informed by daily Last30Days debriefs. This file captures the distilled direction of the industry over time, not merely daily notes.

## Current Direction
- The model market is becoming a routing problem, not a single-best-model problem. OpenRouter-style aggregation makes it practical to select models by task, cost, latency, cache economics, context length, and reliability.
- Cheap/open high-performing models are increasingly credible for classification, extraction, draft generation, and coding assistance; premium models should be reserved for high-stakes reasoning/review.
- Prompt caching and effective price are becoming central to long-context agent economics.

## Major Shifts to Watch
- OpenRouter model availability/deprecation churn, especially free/cheap models and image/video-adjacent providers.
- Cache-hit-rate visibility, cache read/write pricing, context-window pricing cliffs, and provider-specific cache rules.
- Independent verification of new open-weight benchmark claims.
- Reliability differences under tool use, long context, structured output, and coding-agent workloads.

## Faleth Relevance
- Create a Faleth/OpenRouter routing policy: cheap model for classification/extraction, mid-tier model for draft generation, premium cached model for final reasoning and review, multimodal only when required.
- Track actual cost and quality per workflow: daily research, GovCon parsing, proposal drafting, FRR marketing content, and Hermes agent tasks.
- Avoid building workflows around volatile free models unless fallback routing exists.

## Running Source Debrief Notes
### 2026-06-08
- Web search found OpenRouter’s model and pricing pages as current sources. Search snippets said the models page listed DeepSeek V3.1 Nex-N1 with June 8 relevance and that pricing covers 400+ models / 60+ providers with platform fees and free model options ([OpenRouter models](https://openrouter.ai/models), [OpenRouter pricing](https://openrouter.ai/pricing)).
- X signal said OpenRouter updated its Pricing tab with live cache-hit rates and historical traffic, making effective price more visible for long-context / repeated-context agent usage ([OpenRouter pricing update](https://x.com/OpenRouter/status/2063504950429147376)).
- X signal also mentioned newly added free image models: `sourceful/riverflow-v2.5-pro:free` and `sourceful/riverflow-v2.5-fast:free` ([NetCyberseo OpenRouter note](https://x.com/NetCyberseo/status/2063681087407272201)).

### 2026-06-09
- OpenRouter web snippets reported June 8 blog/activity around model tests, compliance/human-oversight features, DeepSeek V3.1 Nex-N1 availability, Riverflow V2.5 notices, and current models/pricing pages ([OpenRouter blog](https://openrouter.ai/blog), [OpenRouter models](https://openrouter.ai/models), [OpenRouter prompt caching docs](https://openrouter.ai/docs/guides/best-practices/prompt-caching)).
- X signal said Nex-N2-Pro/mini and DeepSeek V3.1 are drawing builder attention for price/performance, open weights, benchmark claims, quantization/local-running experiments, and OpenRouter availability ([Nex-N2 signal](https://x.com/HonorestV5/status/2063878280806367685), [OpenRouter/free Nex signal](https://x.com/mr_r0b0t/status/2064086767750271269), [DeepSeek V3.1 signal](https://x.com/ssuhjo/status/2064095796606157194)).
- Signal strength: medium. Strong current chatter; some benchmarks are self-reported and web details are snippet-level.
