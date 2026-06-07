# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an [Obsidian](https://obsidian.md/) knowledge vault — a collection of interconnected Markdown notes. There are no build systems, tests, or compiled artifacts.

## Structure

```
Main Vault/
├── Business/
│   ├── Faleth Capital/   ← family office: governance docs, equity framework, constitution
│   └── LTD Amway/
└── Personal/
    ├── Church/
    ├── Ideas/
    └── Journal/
```

All notes are plain Markdown (`.md`) files using title-case names with spaces (e.g., `Faleth Capital Constitution.md`).

### Cross-referencing

Business documents heavily cross-reference each other using wikilinks with anchors (e.g., `[[Faleth Capital Constitution#Article IV: The Equity System|Article IV]]`). When editing or creating notes that relate to existing documents, maintain these links — they are load-bearing for navigation in Obsidian.

### Obsidian-specific syntax

- `[[wikilinks]]` — internal links between notes
- `[[Note#Heading|Alias]]` — links to a specific heading with display text
- `#tags` — for categorization
- YAML frontmatter — note metadata/properties
- `![[embeds]]` — to embed other notes or assets

Configuration lives in `.obsidian/` (plugin settings, workspace state, hotkeys) — avoid editing these directly unless the user asks.

## Business Context Files

Each business under Faleth Capital has an AI Reference file. When a business comes up in conversation, read its reference file before responding.

| Business | Reference File | When to load |
|---|---|---|
| Free Range Repair | `Business/Faleth Capital/Free Range Repair/AI Context/Free Range Repair — AI Reference.md` | Any mention of Free Range Repair, device repair, or FRR |
| LibreTech | `Business/Faleth Capital/LibreTech/AI Context/LibreTech — AI Reference.md` | Any mention of LibreTech or the brother's defense company |
| VXE | `Business/Faleth Capital/VXE (partner)/AI Context/VXE — AI Reference.md` | Any mention of VXE, Leonard, or government contracts |
| Faleth Capital (governance) | `Business/Faleth Capital/Faleth Capital Constitution.md` | Questions about equity, ownership structure, or family office |
| Faleth Capital (compensation) | `Business/Faleth Capital/The Contribution Framework.md` | Questions about comp plans, COF, profit share, or point systems |

The AI Context folders may also contain individual `.txt` source files with additional detail. If the reference file points to a specific `.txt` file for more depth, read it.

## Installed Community Plugins

- **Templater** — template automation with `<% %>` syntax for dynamic note creation
- **Calendar** — calendar view for daily notes
- **Terminal** — in-app terminal access
- **Docxer** — document export
