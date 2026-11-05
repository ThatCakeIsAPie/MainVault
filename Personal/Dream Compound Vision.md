# Dream Compound Vision

**Date:** June 2026  
**Status:** Pure dream-building / long-term vision

## Core Lifestyle Goal
- Total time freedom as a researcher, inventor, and engineer
- Run businesses remotely with minimal hands-on involvement
- Stay deeply present with family (sons can observe or participate in work)
- Maximum optionality and creative throughput

## Physical Compound
- **Location**: ~10-acre plot, slightly outside the city
- **Warehouse / Manufacturing Hub**: Full advanced manufacturing setup including CNC machines, lathes, mills, 3D printers, laser cutters, and robotic systems
- **Energy System**: Large commercial-grade solar array + massive battery storage capable of running the entire compound for a week+
- **Transportation Layer**:
  - Private airstrip with private jet + helicopter
  - Fleet of self-driving / autonomous vehicles
  - Short / medium / long distance mobility covered

## Central Compute System (The Brain)
- **One 8× RTX PRO 6000 (96GB) rack** that does double duty: run agents and LLMs, or pause the agents and use the cards for local cloud gaming with friends and family. Expand later by adding more racks. This beats the old plan of an 8× B200 AI rack plus an 8× RTX 5090 general rack.
- Lives in a small workshop barn on the compound — full of machines of all kinds, and also houses the personal compound server. Needs 240V power and a sealed, filtered server corner because of shop dust.
- High-speed networking throughout the property
- Permanent RAG/memory system for the AI (not limited by context windows)
- Can run multiple models or multiple instances of the same model simultaneously

### Full Cabinet Build (prices Nov 4, 2026)

**One server** — Supermicro AS-4125GS-TNRT (4U), $228,266.69
- CPUs: 2× AMD EPYC 9655 (192 cores / 384 threads)
- RAM: 1.5TB DDR5 (24× 64GB)
- GPUs: 8× RTX PRO 6000 96GB = 768GB GPU memory (Server Edition for rack fit, $16,566 each)
- Storage: 2TB NVMe + 24 open 2.5in bays
- Network: 2× 10Gb built-in + 2× 400G ConnectX-7
- Power: about 6kW

**Full cabinet** — 10 servers in one 42U rack
- 1,920 cores / 3,840 threads, 15TB RAM
- 80 GPUs, 7,680GB GPU memory
- About 60kW
- Rack is full: 40U of servers + 2U of switches

**Cabinet gear** — about $107k
- Rack: APC NetShelter SX 42U AR3340, $2,612
- Power: 4× Vertiv Geist 34.5kW 3-phase PDUs, $12,312
- Network: NVIDIA SN4700 400G switch $34,895; 20× ConnectX-7 400G cards $31,980; 20× 400G cables about $3,180
- Cooling: Motivair 60kW rear-door cooler, about $8,500 (est.); 20-ton air-cooled chiller (480V), $13,500
- Optional UPS: Eaton 93PM 60kW, $91,553 (too tight at full load)

**Totals**
- Servers: $2.28M
- Full cabinet: about $2.39M, or $2.48M with UPS
- Not included: management switch ($500–$1,500 est.), pumps/piping/install ($5k–$15k est.), barn 3-phase electrical service

## AI Agent Capabilities
- Always-on home security monitoring and response
- Visitor verification and delegation to personal security
- Integration with manufacturing hub (design → prototype → production)
- Robotic systems (e.g. Boston Dynamics-style Spot with arm) for physical tasks
- Remote access from anywhere via Tailscale or equivalent
- Family-integrated: sons can watch or get involved

## Additional Elements
- Guest house for private jet pilot + hostess (ideally a husband-wife team)
- Full self-driving / autonomous vehicle fleet
- Ability to spin up manufacturing jobs from the AI system ("make a prototype of this")
- Everything centrally managed and owned

## Vibe / Philosophy
- Modern Tony Stark workshop meets sovereign tech compound
- "Money is no object" dream building
- Maximum optionality and creative freedom while staying home with family
- The system should remove friction between having an idea and making it real

---

*This note was created from a long dream-building conversation. Feel free to expand, reorganize, or add details as the vision evolves.*

## Related principles

- [[offshoots/family-legacy-as-mission-multiplier]] — Compound as family-integrated mission, not isolated wealth display.
- [[offshoots/factory-over-product-thinking]] — Build the repeatable system (manufacturing + AI factory), not one-off projects.
- [[offshoots/asset-creation-over-linear-income]] — Assets and optionality over trading time for paychecks.
- [[foundational/five-step-sequencing-model]] — Sequence major commitments; compound vision is downstream of current sequencing.