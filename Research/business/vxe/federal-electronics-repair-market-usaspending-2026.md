---
title: Federal electronics-repair market size (USASpending, FY2021–FY2026 YTD)
created: 2026-08-30
updated: 2026-08-30
type: summary
tags: [business, strategy, operations]
confidence: high
---

# Federal electronics-repair TAM (USASpending)

Pulled 2026-08-30 from USASpending.gov API. Dollars are **obligated transaction amounts**, not IDIQ ceilings and not outlays.[1][6]

**Headline (in-scope repair, not new-buy):** PSC **J058 + J059** obligated **$8,937,996,625.77** across full FY2021–FY2025 (**$1,787,599,325.15** per year average). FY2026 through 2026-08-30 is **$938,350,300.28** more (incomplete year).[1]

That is the TAM figure VXE should use for “federal electronics repair / electronics maintenance.” Do not add PSC 58/59 product buys into it.

## Query (reproducible)

API: `POST https://api.usaspending.gov/api/v2/search/spending_over_time/` with `"group": "fiscal_year"`.[1]

Shared time window:

- `time_period`: `start_date` **2020-10-01**, `end_date` **2026-08-30**
- No keywords. PSC/NAICS codes only.

| Slice | `psc_codes` / `naics_codes` | What it is |
|---|---|---|
| **Core (TAM)** | `J058`, `J059` | Maint/repair/rebuild of comms/detection/coherent-radiation equipment (J058) and electrical/electronic equipment components (J059).[4] |
| J058 only | `J058` | Comms / radar / EW-class equipment repair.[4] |
| J059 only | `J059` | Electrical/electronic component repair.[4] |
| Adjacent, **not** in TAM | `J016` | Aircraft components and accessories repair — engines, accessories, not electronics-only.[4] |
| Adjacent, **not** in TAM | `J070` | ADP equipment/software maintenance.[4] |
| Adjacent, **not** in TAM | `J066` | Instruments and laboratory equipment maintenance.[4] |
| Adjacent, **not** in TAM | `K058`, `K059` | **Modification** of the same 58/59 equipment families, not repair.[4] |
| New-buy contrast | `58` | Product group 58 (communication, detection, coherent radiation equipment) — **buy**, not repair.[1] |
| New-buy contrast | `59` | Product group 59 (electrical/electronic components) — **buy**, not repair.[1] |
| NAICS check | `811210`, `811211`, `811212`, `811213`, `811219` | Electronic and precision equipment repair NAICS family. 811211/212/213/219 show `year_retired` 2022; 811210 is current.[5] |

Agency / recipient breakouts: `POST /api/v2/search/spending_by_category/` with `category` `awarding_agency` or `recipient`, same core PSC filter.[2]

Award counts: `POST /api/v2/search/spending_by_award_count/` , same core PSC filter. `spending_level` returned `awards`.[3]

Set-aside overlays (core PSC, same dates):

- Small-business bundle `set_aside_type_codes`: `SBA`, `SBP`, `8AN`, `8A`, `HS3`, `SDVOSBC`, `SDVOSBS`, `WOSB`, `EDWOSB`, `HZC`, `HZS`
- SDVOSB only: `SDVOSBC`, `SDVOSBS`

USASpending.gov Advanced Search equivalent: Fiscal Years 2021–2026, PSC J058 and J059, Award Type contracts + IDVs.[6]

PSC titles match Acquisition.gov PSC Manual (current archive April 2025).[8] Census NAICS 2022 search UI did not return a parseable 811210 definition in static HTML on this pull; NAICS titles above are from USASpending NAICS autocomplete.[5][7]

SAM.gov opportunity volume was **not** sized. Unauthenticated `api.sam.gov` opportunities search returned HTTP 404. Do not invent a solicitation count.

## Core PSC J058+J059 — obligated by FY

Source: `spending_over_time`, `psc_codes=["J058","J059"]`.[1]

| FY | Aggregated obligations | Contract obligations | IDV obligations |
|---:|---:|---:|---:|
| 2021 | 1,873,690,141.90 | 1,872,283,820.41 | 1,406,321.49 |
| 2022 | 1,673,690,891.91 | 1,668,589,637.98 | 5,101,253.93 |
| 2023 | 1,770,830,200.93 | 1,765,299,700.56 | 5,530,500.37 |
| 2024 | 1,588,667,555.72 | 1,584,008,441.59 | 4,659,114.13 |
| 2025 | 2,031,117,835.31 | 2,026,809,802.09 | 4,308,033.22 |
| 2026 YTD (through 2026-08-30) | 938,350,300.28 | 932,663,889.60 | 5,686,410.68 |
| **FY21–25 sum** | **8,937,996,625.77** | | |
| **FY21–25 average** | **1,787,599,325.15** | | |
| FY21–FY26 YTD sum | 9,876,346,926.05 | | |

Split (FY21–25): J058 **$3,492,591,459.93** (avg **$698,518,291.99**); J059 **$5,445,405,165.84** (avg **$1,089,081,033.17**). The two codes add to the core sum (no double-count in the combined query).[1]

Award inventory overlapping this window: **13,288** contracts and **891** IDVs.[3]

## Repair vs new-buy

Do **not** treat product PSC 58/59 as repair TAM. Same window, obligated:[1]

| Slice | FY21–25 sum | FY21–25 average |
|---|---:|---:|
| Repair J058+J059 | 8,937,996,625.77 | 1,787,599,325.15 |
| New-buy PSC 58 | 74,481,698,465.30 | 14,896,339,693.06 |
| New-buy PSC 59 | 16,916,428,845.50 | 3,383,285,769.10 |

New-buy 58 ran about **8.3×** the core repair TAM over FY21–25. Mixing them would inflate TAM by nearly an order of magnitude.

## What is *not* electronics-repair TAM (but sits next door)

| Slice | FY21–25 average obligated | Why it is out |
|---|---:|---|
| J016 aircraft components repair | 2,940,485,905.77 | Airframe/engine/accessory mix; not an electronics code.[4] |
| J066 instruments/lab maintenance | 260,362,739.63 | Broader than electronics.[4] |
| J070 ADP maintenance | 75,060,345.12 | IT hardware/software; FY21 $192.4M collapsing to FY26 YTD **negative** $2.17M (deobligations). Unstable as a TAM add-on.[1] |
| K058+K059 modification | 620,658,814.25 | Modification, not repair/rebuild.[4] |
| NAICS 8112 family | 2,940,837,951.75 | Includes medical-equipment repair and other precision repair; VA/HHS share jumps vs PSC core. 811210 alone is $0 in FY21–22 (code not yet used), then $494.3M / $1.354B / $1.593B in FY23–25.[1][5] |

## Agencies (core J058+J059, FY21 through FY26 YTD)

`spending_by_category` awarding_agency, same filter. Period total **$9,876,346,926.05**.[2]

| Agency | Obligated |
|---|---:|
| Department of Defense | 8,984,373,547.61 |
| Department of Homeland Security | 299,506,011.77 |
| Department of Veterans Affairs | 220,681,197.65 |
| Department of Transportation | 128,118,524.61 |
| Department of Commerce | 61,706,602.25 |
| Social Security Administration | 34,534,374.06 |
| Department of Justice | 31,440,077.01 |
| Department of the Treasury | 15,533,317.07 |
| Department of State | 15,219,919.97 |
| Department of Agriculture | 15,175,111.20 |
| General Services Administration | 14,909,080.23 |
| Department of Health and Human Services | 13,507,863.19 |

DoD is **90.97%** of core-period dollars. Top 12 agencies are **99.58%**. This is a DoD depot/avionics-electronics maintenance market with a thin civilian tail (DHS radios, VA biomedical/electronics, DOT).[2]

## Recipients (core, same period) — OEM / depot concentration

Top 15 recipients obligated **$5,298,922,697.30** (**53.65%** of period). Top 5 **$3,446,220,425.36** (**34.89%**).[2]

| Recipient | Obligated |
|---|---:|
| L3HARRIS TECHNOLOGIES, INC. | 1,213,372,900.42 |
| RAYTHEON COMPANY (UEI MZK8TCNF24G2) | 816,574,225.06 |
| SERCO INC | 615,526,587.07 |
| SCIENTIFIC RESEARCH CORPORATION | 457,745,818.15 |
| TCOM, L.P. | 343,000,894.66 |
| NORTHROP GRUMMAN SYSTEMS CORP (D9SJDK872X57) | 322,240,072.03 |
| SCIENCE APPLICATIONS INTERNATIONAL CORPORATION | 290,817,448.56 |
| BAE SYSTEMS TECHNOLOGY SOLUTIONS & SERVICES INC. | 276,925,988.15 |
| CHUGACH TECHNICAL SOLUTIONS LLC | 193,674,753.37 |
| L3 TECHNOLOGIES, INC. | 151,870,960.33 |
| RAYTHEON COMPANY (UEI GMBYU6KAN9J3) | 137,443,515.70 |
| MOTOROLA SOLUTIONS, INC. | 132,973,793.20 |
| NORTHROP GRUMMAN SYSTEMS CORPORATION (E4X3BLZPPPX3) | 117,825,030.10 |
| JOHNSON CONTROLS BUILDING AUTOMATION SYSTEMS, LLC | 115,679,419.01 |
| KBR WYLE SERVICES, LLC | 113,251,291.49 |

These are OEM, depot, and large-integrator vehicles. A small GovCon supplier is not bidding the L3Harris/Raytheon/Northrop slice as a prime.

## Small GovCon vs mega-awards (core PSC)

Set-aside **type** filter, not “recipient is small.” Unrestricted wins by small firms are **outside** these numbers, so this is a **floor** on the coded small-business lane.[1]

| Filter | FY21–25 sum | FY21–25 average | Share of core FY21–25 |
|---|---:|---:|---:|
| Small-business set-aside bundle (see codes above) | 627,770,728.27 | 125,554,145.65 | 7.02% |
| SDVOSB set-aside only | 57,523,047.37 | 11,504,609.47 | 0.64% |

SDVOSB on these two PSCs is small in the five-year average (**~$11.5M/year**) but FY2026 YTD already shows **$18,363,105.66** — do not treat the five-year average as a cap without another pull.

In-scope for a small GovCon electronics-repair supplier: the set-aside slice, subcontracts under the primes above, and civilian-agency tails (DHS/VA/DOT), not the ~$1.8B headline as capturable prime share.

## Caveats (load-bearing)

1. **Obligated transactions ≠ IDIQ ceiling.** Core IDV obligations are **$1.4M–$5.7M per year** against **~$1.6–$2.0B** contract obligations. Using vehicle ceilings would inflate TAM. USASpending `spending_over_time` returned `"spending_level": "transactions"`.[1]
2. **No keyword search.** “Electronics repair” in description fields would mix new-buy, services, construction, and false positives. Size here is PSC/NAICS only.
3. **Multi-year vehicles.** Obligations post when funded. Award counts (13,288 contracts / 891 IDVs) are awards overlapping the window, not 13k new competitions per year.[3]
4. **Deobligations.** Negative IDV or contract amounts (J058 FY22–24 IDV; J070 FY26) are real in the API and pull the aggregate down.
5. **FY2026 is YTD** through 2026-08-30, with reporting lag. Do not annualize it into a full-year forecast from this pull.
6. **Set-aside codes undercount small-firm unrestricted wins** and can include large-firm participation on some vehicles. They are not a SAM.gov pipeline.
7. **NAICS 8112 is not a substitute for PSC J058/J059.** It is larger and dirtier (medical, mixed precision repair). Use it as a cross-check, not the TAM.
8. **SAM.gov opportunity volume** not included (API 404 without a usable public query). FPDS is already inside USASpending for this purpose.

## VXE take

Use **~$1.8B/year obligated** on J058+J059 as the federal electronics-repair TAM, **~$126M/year** coded small-business set-aside as the realistic prime-addressable band unless VXE is subcontracting the OEM/depot stack. Keep new-buy electronics (~$15B/year on PSC 58) in a separate column so TAM does not get inflated.

## See also

- [[business/vxe/full-time-transition-research-2026]]
- [[business/vxe/piee-solicitation-email-notifications-after-proposal-manager-activation]]

## Sources

[1] https://api.usaspending.gov/api/v2/search/spending_over_time — USASpending API spending_over_time
[2] https://api.usaspending.gov/api/v2/search/spending_by_category — USASpending API spending_by_category
[3] https://api.usaspending.gov/api/v2/search/spending_by_award_count — USASpending API spending_by_award_count
[4] https://api.usaspending.gov/api/v2/autocomplete/psc — USASpending PSC autocomplete
[5] https://api.usaspending.gov/api/v2/autocomplete/naics — USASpending NAICS autocomplete
[6] https://www.usaspending.gov — USASpending.gov
[7] https://www.census.gov/naics/?input=811210&year=2022&details=811210 — Census NAICS 2022 811210
[8] https://www.acquisition.gov/psc-manual — Acquisition.gov PSC Manual
