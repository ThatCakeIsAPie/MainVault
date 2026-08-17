---
title: Book-to-Skill Compilation for Agent Knowledge
created: 2026-08-08
updated: 2026-08-08
type: principle
tags: [ai, llm, software, open-source, skills, systems, leverage]
sources:
  - raw/x-bookmarks/2026-08-07/2085761587550519420.md
confidence: medium
---

# Book-to-Skill Compilation for Agent Knowledge

## Principle

A long book or PDF should not be flattened into one giant prompt. The more durable pattern is to **compile the source into a navigable skill**: a lean routing file, chapter-level references loaded on demand, and practical retrieval aids such as a glossary or cheatsheet.

Hermes Agent's `/learn` command now incorporates the open-source `book-to-skill` approach. Teknium's August 7 announcement says a user can point `/learn` at a book or PDF and generate a comprehensive technical skill. The [official Hermes skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) describes the corresponding structure: a compact `SKILL.md`, index, and on-demand chapter reference files. [[raw/x-bookmarks/2026-08-07/2085761587550519420]]

## Why the architecture matters

Long-source ingestion has two different jobs:

1. **Evidence extraction:** recover faithful text and structure from the source.
2. **Operational compilation:** reorganize that evidence so an agent can find and apply the right section without loading the whole corpus.

The first job depends on [[faleth/process/ocr-gated-pdf-ingestion-pipelines-2026]] and [[faleth/process/local-multiformat-document-to-markdown-ingestion-2026]]. The second turns the normalized source into a procedure-oriented retrieval surface. Confusing these stages produces polished skills built on broken extraction—the agentic equivalent of laminating a typo.

## Acceptance criteria

A generated book skill should be treated as a draft until it passes:

- **Coverage:** major chapters, definitions, warnings, examples, and exceptions are represented.
- **Traceability:** generated guidance points back to the source section or page.
- **Retrieval:** realistic questions route to the correct reference file without loading everything.
- **Fidelity:** summaries do not invent mechanisms or quietly remove caveats.
- **Utility:** the skill improves execution on representative tasks, not merely answers trivia about the book.
- **Maintainability:** the routing layer stays small enough to inspect and chapter files can be updated independently.

## Faleth / Delta application

Use book-to-skill compilation for stable, technical material that will recur across work: FAR/DFARS guidance, proposal methodology, manufacturing references, specialized software manuals, and operating playbooks. Keep source artifacts immutable, run extraction quality checks first, then test the generated skill against actual work.

This complements [[faleth/process/demonstration-to-skill-capture-2026]]: books compile explicit knowledge, while demonstrations capture tacit operator judgment. A serious agent stack needs both.

## Evidence limits

The bookmark and documentation establish the feature and intended architecture, not that every book will convert cleanly. Scanned pages, tables, equations, copyright boundaries, contradictory chapters, and domain-specific notation still require source-aware validation.

## Related

- [[faleth/process/ocr-gated-pdf-ingestion-pipelines-2026]]
- [[faleth/process/local-multiformat-document-to-markdown-ingestion-2026]]
- [[faleth/process/demonstration-to-skill-capture-2026]]
- [[faleth/process/self-writing-vault-operating-loop-2026]]
