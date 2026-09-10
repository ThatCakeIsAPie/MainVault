---
title: Simplified Technical English as an LLM Documentation Constraint (2026)
created: 2026-07-19
updated: 2026-07-19
type: principle
tags: [ai, llm, skills, systems, standards]
sources:
  - research/raw/x-bookmarks/26-07-18/2078492579511906771.md
confidence: medium
---

# Simplified Technical English as an LLM Documentation Constraint (2026)

## Principle

A concrete style standard can constrain an LLM more reliably than vague requests to “sound human” or “avoid AI slop.” The bookmarked claim recommends **ADS-STE100 Simplified Technical English** as the writing constraint for technical documentation.

The actionable mechanism is broader than this specific standard: replace aesthetic complaints with an inspectable specification. A named standard gives the model rules to follow and gives the reviewer something more objective than vibes—humanity's most overworked quality-assurance framework.

## Working pattern

For technical documentation, ask the model to:

1. follow ADS-STE100 Simplified Technical English;
2. prefer short, direct sentences and unambiguous instructions;
3. preserve required technical terms rather than decorating them with synonyms;
4. flag places where strict simplification would change meaning;
5. run a final compliance pass against the selected rules.

Treat this as a hypothesis to test, not a universal guarantee. The source is a high-engagement practitioner claim, not a controlled comparison, and the exact prompt and evaluation criteria were not supplied.

## Faleth / Delta implication

Use a defined language constraint when producing SOPs, agent runbooks, GovCon fulfillment instructions, and operator-facing documentation. Pair it with [[faleth/process/agentic-loops-design-2026]] for an explicit review loop and [[faleth/process/ai-as-sparring-partner-house-method-2026]] for human verification. The KPI is lower ambiguity and fewer operator errors—not merely prose that wins a beauty contest.

## Related

- [[faleth/process/anthropic-prompting-craft-deleted-lecture-2026]]
- [[faleth/process/agentic-loops-design-2026]]
- [[faleth/process/ai-as-sparring-partner-house-method-2026]]

## Provenance

- Bookmark: [[research/raw/x-bookmarks/26-07-18/2078492579511906771]]
- Source: [@geogristle on X](https://x.com/geogristle/status/2078492579511906771), bookmarked in the 2026-07-19 daily batch.
