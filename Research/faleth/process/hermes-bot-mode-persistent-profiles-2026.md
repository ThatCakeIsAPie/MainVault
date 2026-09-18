---
title: Hermes Bot Mode Persistent Profiles
created: 2026-08-14
updated: 2026-08-14
type: principle
tags: [ai, software, infrastructure, systems, leverage]
sources:
  - raw/x-bookmarks/26-08-13/2088003994904113614.md
confidence: medium
---

# Hermes Bot Mode Persistent Profiles (2026)

## Thesis

> **Sessions are disposable threads. Bots are named teammates with identity, a job, their own memory, and the ability to talk to each other.**

Teknium's 2026-08-13 launch treats Bot Mode as an alternative to sessions mode: one chat per agent profile, with job, description, profile picture, and inter-bot messaging. Screenshots on the Desktop app show a New Agent form ("named teammate with its own memory, skills, and chat") and a Developer bot briefing a testing-focused `mr-tester` profile. The public beta was announced as one day.

## First-principles split

| Mode | Persistence | Job | Failure if confused |
|------|-------------|-----|---------------------|
| **Session** | Conversation history | Whatever this thread is | Identity reset; operator re-explains the role |
| **Bot / profile** | Named role + memory + skills | A standing job (inbox, tests, ops) | A zoo of unused mascots |
| **Child / delegate** | Mid-flight transcript | One bounded task | Fire-and-forget until a victory speech |

Bot Mode is the missing **identity layer** between chat threads and [[faleth/process/hermes-subagent-orchestra-2026|subagent orchestra]]. Orchestra is how a parent steers a child mid-run. Bot Mode is how specialized agents keep a name, a job, and a mailbox when the thread ends.

## Product claims worth keeping

1. **One chat per profile** — staffing, not tab sprawl.
2. **Job + description + picture** — the interface is a person-shaped slot, not a settings panel.
3. **Own memory and skills** — role identity should not collapse into the operator's global context.
4. **Bots message bots** — coordination is a first-class action, not a human copy-paste ritual.
5. **Desktop surface** — this is a productized cockpit on Hermes Agent Desktop, not only CLI profiles.

That maps onto the same stack already running as Delta: Telegram is the operator surface; profiles, skills, cron, and delegates are the named teammates; Honcho / vault / GBrain are the memory layers. See [[faleth/process/messaging-ui-as-agent-operating-surface-2026]].

## Faleth / Delta application

- Keep **one personal agent** (Delta) as the cockpit. Spin specialized bots only when a standing job exists: tests, vault hygiene, GovCon research, inbox triage.
- Do not create bots because the sidebar looks like a team. Unused named agents are costume.
- Inter-bot talk is useful only if the parent still **verifies outcomes**. A tester bot saying the suite passed is not proof.
- VXE cash timing stays primary. Bot Mode is how Delta staffs recurring operator jobs, not a new product identity.

## Contested / open

- Whether a fleet of named bots beats one strong personal agent with skills and cron for Lyle's actual load.
- How profile memory should partition against Honcho, vault principles, and session search without becoming a fourth babysat store.
- One-day public beta is a launch window, not a stability claim.

## Related

- [[raw/x-bookmarks/26-08-13/2088003994904113614]]
- [[faleth/process/messaging-ui-as-agent-operating-surface-2026]]
- [[faleth/process/hermes-subagent-orchestra-2026]]
- [[faleth/process/hermes-agent-long-horizon-codebases-2026]]
- [[faleth/process/agentic-loops-design-2026]]
- [[faleth/process/owner-manages-agent-manager-not-the-work-2026]]
