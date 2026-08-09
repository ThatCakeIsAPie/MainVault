---
title: ParaNetics tri-pole propulsion — technical due diligence
created: 2026-08-09
updated: 2026-08-09
type: research
tags:
  - electric-motors
  - aviation
  - propulsion
  - due-diligence
source_url: https://www.paranetics.com/
status: preliminary-public-evidence
---

# ParaNetics tri-pole propulsion — technical due diligence

## Executive conclusion

ParaNetics appears to have a real, patented electromagnetic geometry and multiple physical prototypes, but the publicly available evidence does **not** establish the claimed commercial performance. The hardware is best understood as a permanent-magnet synchronous/BLDC-style external-rotor or circumferential fan motor with a proprietary multi-pole field-shaping arrangement—not a new source of energy.

The company claims 96–98% efficiency, 25–30% torque gains, 30% or greater thrust improvement, passive cooling, and fault-tolerant triple redundancy.[1][2] Those figures are not accompanied publicly by a complete dyno report, torque-speed curve, efficiency map, test conditions, motor mass, continuous thermal limit, electrical operating point, uncertainty statement, or named independent laboratory.

**Commercial assessment:** interesting prototype/IP opportunity; not yet a specifiable propulsion product based on public evidence.

## What kind of motor is it?

The propulsion patent places permanent magnets around the outside of the fan-blade housing and drives that rotating housing with stationary magnetic-field generators.[4] Functionally, this is a circumferential or rim-driven external-rotor permanent-magnet motor integrated with a ducted fan, although ParaNetics distinguishes it from conventional rim-drive motors.[1]

The core patent describes a magnetic field pattern with three spatial poles—north–south–north or the inverse—created by a particular magnetic structure.[3]

The motor arranges many such field generators around a circular path and electronically commutates them so the permanent-magnet rotor is successively attracted and repelled.[1][3][4]

The key novelty is therefore **field geometry and packaging**, not altered electromagnetic laws. Permanent magnets provide flux, windings and the controller create a traveling field, and electrical input is converted into torque through ordinary electromagnetic interaction.

## What is genuinely plausible

- A distributed rim/circumference motor can create high low-speed torque because torque equals tangential force times radius.
- Distributed windings and a large exterior surface can improve passive heat rejection.
- Integrating the rotor into the fan rim can remove a central shaft/gearbox and potentially reduce hub blockage.
- Counter-rotating stages can recover swirl and reduce net reaction torque when properly aerodynamically designed.
- A multiphase or multi-sector winding/controller arrangement can tolerate some electrical faults.
- Ducted fans can outperform an equal-diameter open propeller in static thrust under suitable geometry, although the duct also adds drag and weight in forward flight and performance is highly sensitive to tip clearance.[8]

These are legitimate engineering possibilities. None, however, proves that this implementation beats optimized existing aerospace motors on total system mass, efficiency, noise, or thrust.

## Claims and evidence status

| Claim | Public support | Assessment |
|---|---|---|
| 96–98% efficiency | Company whitepaper says prototype testing demonstrated it.[2] | Plausible as a **peak motor-only** figure, but unverified and undefined. |
| 25–30% torque gain | Company whitepaper; no baseline or raw curve.[2] | Not decision-grade. Must specify equal current, copper loss, mass, active volume, temperature, and speed. |
| 30%+ thrust gain | Company whitepaper attributes this to the circumferential ducted architecture.[2] | Cannot be assigned to the motor without matched fan testing over an operating envelope. |
| Passive cooling | Company claim.[2] | Plausible at low power; continuous thermal-soak data absent. |
| Triple redundancy | Three independently controlled propulsion sections in one unit.[2] | Electrical redundancy, not necessarily system redundancy: bearings, fan ring, structure, blades, duct, and some wiring remain common-mode risks. |
| Six or seven prototypes | Company says six built and a seventh planned for Q4 2025; site whitepaper later says seven working prototypes.[2][5] | Physical prototypes appear credible; maturity and test rigor remain unclear. |
| Preliminary third-party test | Company says an unnamed major technology company tested early versions.[5] | Not independently reviewable because the company, method, results, and report are undisclosed. |
| Patent protection | Granted U.S. patents cover the tri-pole field generator and integrated fan propulsion arrangement.[3][4] | Valid evidence of patentability, not evidence of efficiency or commercial readiness. |

## Major technical concerns

### 1. The public “373 W = 1 HP” statement is physically unacceptable as written

The whitepaper says its push-pull interaction means “373 W = 1 HP,” while also acknowledging that efficiency cannot exceed 100%.[2] One mechanical horsepower is approximately 745.7 W. At 373 W electrical input, a device could produce at most 0.5 hp even at impossible 100% efficiency. The statement may intend to compare magnetic force at a chosen geometry rather than actual shaft power, but it must not be used as a power claim.

### 2. “Conventional motors use only one side of the magnetic field” is misleading

The patents argue conventional motors utilize only 50% of the available magnetic field because an outward-facing pole is “unused.”[3][4] Real PM machines use closed magnetic circuits: the air gap, rotor iron, stator teeth/back iron, magnets, and leakage paths all participate in the flux circuit.[9] Field concentration and leakage reduction can improve torque density, but adding an accessible third pole does not automatically double usable magnetic energy or halve watts per horsepower.

### 3. The efficiency claim is not uniquely exceptional

A 96–98% peak motor efficiency is excellent, but modern aerospace motor drives already publish figures in this range. H3X, for example, lists 180 kW continuous at 13 kg and 96.5% peak efficiency for its HPDM-180 integrated motor drive.[6] ParaNetics has not published comparable continuous power, motor/controller mass, dimensions, speed, torque, cooling, bus voltage, or efficiency-map data.

At 100 kW mechanical output, 98% versus 96.5% efficiency changes heat loss from about 3.63 kW to 2.04 kW. That matters, but only if measured across the actual mission profile and achieved without excess motor, controller, duct, or structural mass.

### 4. Motor efficiency is not propulsive efficiency

A motor can be 98% efficient while the full battery-to-thrust system performs poorly. The complete chain includes inverter losses, wiring, bearings, motor, fan aerodynamics, duct drag, inlet distortion, blade clearance, and installation effects. NASA testing shows that duct benefits vary with operating condition and that clearance can materially erode thrust and efficiency.[8]

### 5. No public performance envelope

The site shows running prototypes and partial-power demonstrations, but I found no public document containing:

- torque versus RPM;
- continuous and peak shaft power;
- DC voltage/current and inverter waveform;
- motor and controller mass;
- efficiency map across load and speed;
- winding and magnet temperatures during thermal soak;
- thrust versus electrical power and airspeed;
- acoustic spectrum and test geometry;
- vibration/bearing-life results;
- fault-injection results;
- named independent test laboratory and uncertainty budget.

## Minimum evidence to request

Ask for a **signed test report or raw time-series data**, not another slide deck.

1. **Dynamometer report** using direct electrical-input and mechanical-output measurement. IEC 60034-2-1 defines recognized methods based on input electrical power and output from measured torque and rotational speed.[7]
2. Torque-speed and power-speed curves from zero to maximum RPM.
3. Efficiency map across the usable envelope, not only the best point.
4. Continuous rating: at least 30–60 minutes at rated power with winding, magnet, bearing, controller, and ambient temperatures.
5. Peak rating and allowable duration, followed by recovery/cooldown requirements.
6. Exact mass breakdown: motor active materials, fan/rotor, bearings, duct, inverter/controller, and cooling hardware.
7. DC bus voltage, RMS/peak phase current, power factor, switching frequency, and controller efficiency.
8. Test article serial number, prototype revision, calibration certificates, sensor uncertainty, sample rate, and raw data.
9. Matched A/B comparison against a named commercial motor at equal shaft power, speed, cooling condition, and system mass.
10. For thrust claims: diameter, blade geometry, tip clearance, RPM, air density, inlet condition, airspeed/advance ratio, electrical input, thrust, and test-cell correction.
11. Fault-injection demonstration for each claimed redundant sector plus common-mode failure analysis.
12. Patent-to-product mapping showing which prototype actually implements each claimed feature.

## Suggested question to send ParaNetics

> Please provide the latest third-party test report and raw data for the Version 6 or 7 propulsion unit. We need the test article configuration, DC input voltage/current/power, shaft torque, RPM, mechanical output power, efficiency calculation, motor/controller/fan masses, winding and magnet temperatures, cooling conditions, uncertainty bounds, and full torque-speed/efficiency maps. For the claimed 25–30% torque and 30% thrust gains, please identify the comparator and confirm that input power, diameter, speed, thermal condition, and total system mass were controlled. Please also clarify whether the stated 96–98% efficiency is motor-only, inverter-to-shaft, or DC-bus-to-thrust.

## Decision rule

Do not reject the company because the idea is unconventional. Reject—or pause—any procurement, licensing valuation, or aircraft-sizing decision until ParaNetics supplies repeatable measured data with units, baselines, and uncertainty.

A live bench demonstration is useful, but the decisive artifact is a calibrated **input-power → torque × angular-speed** dataset and a thermal soak. If they cannot produce that after seven prototypes, the missing data is itself the answer.

## Sources

[1] https://www.paranetics.com/electric-motors — ParaNetics Electric Propulsion
[2] https://www.paranetics.com/_files/ugd/d383a2_0699b3f11708431590db1017535dbf1d.pdf — ParaNetics Version 7.0 Motor Whitepaper
[3] https://patents.google.com/patent/US10937582B2/en — US10937582B2 - Magnetic fields
[4] https://patents.google.com/patent/US11476026B2/en — US11476026B2 - Magnetic propulsion system
[5] https://www.paranetics.com/about-us — About ParaNetics
[6] https://www.h3x.tech/products/hpdm-180 — H3X HPDM-180
[7] https://webstore.iec.ch/en/publication/67756 — IEC 60034-2-1:2024
[8] https://ntrs.nasa.gov/api/citations/20020052231/downloads/20020052231.pdf — NASA Performance Study of a Ducted Fan System
[9] https://info.ornl.gov/sites/publications/Files/Pub57470.pdf — ORNL Real-Time Flux Control in PM Motors
