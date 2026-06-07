# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-14] create | Wiki initialized
- Domain: General (AI/ML, business, philosophy, technology, theology, whatever comes up)
- Location: /home/lylecole4/Documents/Main Vault/Research/
- Structure created with SCHEMA.md, index.md, log.md
- Directories: raw/ (articles, papers, transcripts, assets), entities/, concepts/, comparisons/, queries/
- Tag taxonomy: 6 top-level categories (Technology, Business, People & Orgs, Research, Philosophy, Meta)

## [2026-05-16] ingest | Claude Memory (External AI Memory)
- Source: External AI Memory/Claude Memory.md
- Raw saved: raw/transcripts/claude-memory-2026-05-16.md
- Created: entities/lyle-cole.md
- Created: concepts/five-step-sequencing-model.md
- Created: concepts/faleth-capital-economic-philosophy.md
- Updated: index.md (3 pages total)

## [2026-05-16] create | Akash Hermes Deployment Plan
- Plan: Plans/akash-hermes-deployment.md
- Goal: Deploy full Hermes Agent (gateway + CLI) to Akash Network
- 8 tasks: Dockerfile, config bundle, SSH keys, build/push, SDL, deploy, SSH config, verify

## [2026-05-16] update | Akash Hermes Deployment Plan — Simplified
- Discovered official nousresearch/hermes-agent:latest Docker image (1.2M+ pulls)
- Eliminated need for custom Dockerfile, Docker installation, SSH setup
- Updated plan: paste SDL into Akash Console, replace API keys, deploy
- Persistent 50GB volume at /opt/data for all user data
- CLI access via Akash Console web shell (no SSH needed)

## [2026-05-18] create | LTD Amway First-Principles Extraction (small-scale test)
- Extracted 1 foundational principle + 3 offshoot principles from LTD Amway Info Sessions and related notes
- Created: concepts/network-marketing-as-leadership-development-system.md (foundational)
- Created: concepts/mentorship-compression-through-proven-paths.md
- Created: concepts/sweat-equity-as-primary-selection-mechanism.md
- Created: concepts/asset-creation-over-linear-income.md
- Updated: index.md (added 4 new concept pages)
- Approach: Hierarchical first-principles with reference weighting
- Source area: Business/LTD Amway/Info Sessions (2024–2026)

## [2026-05-18] create | Contribution Over Wage Compensation principle
- Extracted from Faleth Capital core frameworks
- Created: concepts/contribution-over-wage-compensation.md
- Source: Business/Faleth Capital/The Contribution Framework.md
- Updated: processed-sources.md and index.md

## [2026-05-21] update | Concepts folder restructured for clarity
- Created foundational/ and offshoots/ subfolders under Research/concepts/
- Moved 3 core foundational principles into foundational/
- Moved 7 recurring situational/offshoot principles into offshoots/
- Updated index.md to reflect the new hierarchical organization
- No content changes to the principles themselves; this is purely structural for better navigation and distinction between foundational vs. contextual patterns

## [2026-05-21] create | New offshoot principles from full Info Sessions processing
- Created: offshoots/systems-and-duplication-as-leverage.md
- Created: offshoots/persistent-consistent-action.md
- Created: offshoots/networking-and-connection-skills.md
- Updated foundational/network-marketing-as-leadership-development-system.md with expanded Related Principles section and updated References
- Added cross-links between foundational and offshoots layers
- Updated index.md with new pages and folder organization
## [2026-05-21] create | Conferences & Events Full Processing Complete
- Completed full processing of all major LTD Amway Conferences & Events notes
- Created 4 new offshoot principles from conference content:
  - Purpose and Vision as Focusing Mechanisms
  - Traditions and Experiences Build Real Teams
  - Master Once, Then Duplicate
  - Environment Design and Standards of Excellence
- Strengthened existing hierarchy with higher-signal vision, culture, and duplication patterns
- Updated processed-sources.md to mark as FULL PROCESSING COMPLETE
- No new foundational principles; offshoots significantly expanded

## [2026-06-04] ingest | New 2026 Info Sessions (Tyler Sheridan, Dale Jones, Justin Gorby)
- Processed recent 2026 Info Sessions notes post-2026-05-18 extraction
- Created: offshoots/awareness-as-agent-for-change.md (Johari Window, blind spots, self-awareness)
- Created: offshoots/systems-building-through-training-and-delegation.md (leverage via developing others)
- Created: offshoots/character-assessment-through-fruit-inspection.md (evaluate by observable fruit/results)
- Updated index.md with 3 new offshoot pages and bumped page count/date
- Sources: Business/LTD Amway/Info Sessions/2026/ (multiple files from Mar-Jun 2026)
- Reinforced existing network marketing leadership, mentorship, and systems principles with fresh examples
## [2026-06-04] update | LTD Amway full corpus principle review
- Reviewed 98 LTD Amway notes across Info Sessions, Conferences & Events, and Others folders against existing wiki principles
- Confirmed overall principle hierarchy as directionally sound
- Created 6 new offshoot principles:
  - offshoots/faith-anchored-action-and-obedience.md
  - offshoots/identity-and-belief-drive-behavior.md
  - offshoots/pipeline-abundance-through-repetition.md
  - offshoots/family-legacy-as-mission-multiplier.md
  - offshoots/calendar-as-proof-of-priorities.md
  - offshoots/honor-edification-and-communication-rhythm.md
- Rebuilt index.md to include all existing concept pages and corrected total page count
- Updated raw/processed-sources.md
## [2026-06-04] update | Identity and belief principle strengthened
- Captured Lyle's Tony Robbins identity-as-thermostat note as raw/transcripts/lyle-tony-robbins-identity-thermostat-2026-06-04.md
- Updated offshoots/identity-and-belief-drive-behavior.md with external corroboration and identity set-point framing
## [2026-06-04] update | Heart shift framing added to identity and faith principles
- Captured Lyle's religion-vs-relationship / heart-shift note as raw/transcripts/lyle-heart-shift-religion-vs-relationship-2026-06-04.md
- Updated offshoots/identity-and-belief-drive-behavior.md with theological framing: behavior downstream from heart
- Updated offshoots/faith-anchored-action-and-obedience.md to distinguish changed-heart obedience from mere behavior compliance
## [2026-06-04] create | Theological horticulture heart-upstream identity note
- Captured Lyle's theological horticulture metaphor as raw/transcripts/lyle-theological-horticulture-heart-upstream-identity-2026-06-04.md
- Updated offshoots/identity-and-belief-drive-behavior.md with root-before-fruit and heart-upstream-of-identity framing
- Updated offshoots/faith-anchored-action-and-obedience.md with the apple-tree metaphor
- Created query synthesis: queries/heart-upstream-of-identity-theological-horticulture.md
## [2026-06-04] update | Religion terminology clarified
- Captured Lyle's clarification that "religion" means behavior collection/external compliance in this context, contrasted with relationship with Christ
- Created raw/transcripts/lyle-religion-as-behavior-collection-churchianity-2026-06-04.md
- Updated queries/heart-upstream-of-identity-theological-horticulture.md with terminology section
- Updated offshoots/faith-anchored-action-and-obedience.md and offshoots/identity-and-belief-drive-behavior.md with church-ianity distinction

## [2026-06-06] ingest | Trust, Effective Effort, Factory; Tyler Sheridan notes completion
- Processed new raw source: raw/transcripts/Trust_Effective_Effort_and_The_Factory.md
- Processed completed note updates: Business/LTD Amway/Info Sessions/2026/2026-06-04 Tyler Sheridan.md
- Created: concepts/offshoots/trust-as-coordination-infrastructure.md
- Created: concepts/offshoots/factory-over-product-thinking.md
- Updated: concepts/offshoots/systems-and-duplication-as-leverage.md
- Updated: concepts/offshoots/systems-building-through-training-and-delegation.md
- Updated: concepts/offshoots/asset-creation-over-linear-income.md
- Updated: concepts/offshoots/contribution-over-wage-compensation.md
- Updated: index.md (31 pages total)
- Note: Tyler Sheridan notes mainly reinforced existing LTD principles; new raw source introduced the strongest novel frames.

## [2026-06-06] update | Wiki utilization upgrade: entities, comparisons, queries
- Audited wiki structure and confirmed concept-heavy distribution
- Updated SCHEMA.md to allow `type: principle` and expanded tag taxonomy to match useful existing tags
- Created entity anchors: entities/faleth-capital.md, entities/ltd-amway.md, entities/amway.md, entities/tyler-sheridan.md, entities/dale-jones.md, entities/alex-hormozi.md, entities/robert-kiyosaki.md, entities/tony-robbins.md
- Updated: entities/lyle-cole.md and concepts/foundational/five-step-sequencing-model.md to repair dangling links
- Created comparison pages: comparisons/faleth-capital-vs-ltd-amway.md, comparisons/contribution-compensation-vs-wage-compensation.md, comparisons/mentorship-vs-consulting.md, comparisons/factory-thinking-vs-product-thinking.md
- Created query syntheses: queries/how-ltd-amway-functions-as-leadership-incubator.md, queries/faleth-capital-operating-philosophy.md, queries/trust-as-root-of-business-systems.md
- Rebuilt index.md with sections for entities, concepts, comparisons, and queries
- Purpose: shift wiki from concept pile toward cross-linked knowledge map / strategic second brain
