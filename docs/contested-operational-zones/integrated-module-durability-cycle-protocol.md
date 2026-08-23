# Integrated Module Durability-Cycle Protocol

## Purpose

This pass converts the current analytical durability assessment into a repeatable bench and field test protocol for the integrated household alternative-water module.

The protocol exercises the system as a coupled assembly rather than testing only individual parts.

Target subsystems:

```text
COLLECTOR
FIRST FLUSH
RAW STORAGE
BARREL MANIFOLD
PRETREATMENT
HEALTH-CRITICAL FILTER
CLEAN STORAGE
STATUS / LOCKOUT SYSTEM
RUBBLE PAD / LOAD SPREADER
```

The purpose is to identify wear, drift, hidden failure, operator burden, and maintenance demand before any deployment claim is made.

---

## 1. Durability objectives

Measure whether repeated use causes degradation in:

- structural stability;
- hydraulic function;
- liner integrity;
- first-flush performance;
- barrel/manifold isolation;
- filter flow and integrity;
- clean-storage protection;
- status/lockout hardware;
- setup/stow repeatability;
- maintenance burden.

Durability is not simply “still works.”

The system should remain:

```text
FUNCTIONAL
+
INSPECTABLE
+
FAIL-VISIBLE
+
REPAIRABLE
```

---

## 2. Test levels

### D0 — component check

Single operation of each subsystem.

### D1 — 10-cycle bench screen

Minimum early prototype test.

### D2 — 30-cycle repeated-use test

Captures moderate wear and operator repetition.

### D3 — 100-cycle durability target

Intended to expose recurring failure modes before field freeze.

### D4 — seasonal field exposure

Outdoor operation across real rain, dust, temperature, wind, and handling.

No simulated test substitutes for D4.

---

## 3. One durability cycle

One complete cycle consists of:

```text
1. SET UP / INSPECT
2. SIMULATED OR REAL RAIN EVENT
3. FIRST-FLUSH OPERATION
4. RAW BARREL FILL
5. MANIFOLD TRANSFER / ISOLATION
6. PRETREATMENT
7. HEALTH-CRITICAL FILTER OPERATION
8. CLEAN STORAGE FILL
9. DISPENSE
10. DRAIN / RESET / STOW OR RETURN TO READY
```

Record every intervention required to complete the cycle.

---

## 4. Collector durability

Inspect each collector before and after every test block.

Record:

- frame movement;
- fastener loosening;
- liner stretching;
- puncture;
- abrasion;
- pooling;
- gutter detachment;
- screen clogging;
- ballast shift;
- guy-line shift;
- dimensional change.

### Collector failure classes

#### DC-1 minor

- cosmetic wear;
- small adjustment required;
- no water-contact breach.

#### DC-2 moderate

- gutter realignment;
- screen replacement;
- loose fastener;
- small repairable liner abrasion not through-water-path.

#### DC-3 critical

- structural instability;
- liner puncture into contaminated substrate;
- major gutter failure;
- collector collapse.

DC-3 triggers RED or GRAY status depending pathway impact.

---

## 5. Setup / stow test

For modular collectors intended to be moved or stowed:

Repeat:

```text
deploy
secure
inspect
stow
redeploy
```

Measure:

- setup time;
- stow time;
- number of tools;
- number of people;
- fastener wear;
- alignment drift;
- liner damage;
- user errors.

Target:

```text
no critical damage after 10 setup/stow cycles
```

before advancing to D2.

---

## 6. Rain-event simulation

Use clean test water for hydraulic durability work.

Simulate at least three event intensities:

```text
LOW
MODERATE
HIGH
```

Do not claim these represent site storm statistics unless calibrated.

Observe:

- surface drainage;
- gutter capacity;
- splash;
- first-flush capture;
- overflow;
- structural movement;
- barrel fill behavior.

---

## 7. First-flush durability

For FF-M1:

Repeat manual switching/reset.

Track:

- valve/diverter wear;
- chamber leakage;
- user reset errors;
- incomplete drain;
- difficult operation.

For FF-F1:

Track:

- float sticking;
- seat fouling;
- incomplete closure;
- leak past seat;
- drain/reset behavior.

Minimum bench target:

```text
10 successful sequential resets
```

before integration.

Preferred pre-field target:

```text
30 successful cycles
```

without hidden bypass.

---

## 8. Barrel fill / drain cycling

For each barrel:

Cycle through:

```text
0%
25%
50%
100%
50%
0%
```

Observe:

- vessel deformation;
- outlet leakage;
- lid movement;
- vent function;
- stand movement;
- deck deflection;
- valve wear.

At minimum, inspect after:

```text
cycle 1
cycle 10
cycle 30
cycle 100
```

where applicable.

---

## 9. Barrel-bank settlement monitoring

Measure deck elevations at fixed reference points.

Suggested points:

```text
NW
NE
SW
SE
CENTER
```

Record at:

- initial installation;
- first full load;
- 24 h;
- after 10 cycles;
- after simulated heavy rain;
- after 30 cycles;
- after 100 cycles.

Prototype alert:

```text
>10 mm unexpected corner-to-corner change
```

triggers inspection/re-leveling.

This remains an internal prototype alert, not a geotechnical criterion.

---

## 10. Manifold durability

Cycle every branch valve through:

```text
OPEN
CLOSED
DISCONNECT
RECONNECT
```

Track:

- valve leakage;
- coupling wear;
- hose cracking;
- fitting stress;
- manifold movement;
- cap loss;
- dead-leg accumulation.

At least once per test block, remove one barrel and continue operation with remaining vessels.

Pass condition:

```text
one-barrel removal does not disable bank
```

---

## 11. Flexible branch settlement test

Introduce a small controlled height change under one empty or partially filled barrel while maintaining safe support.

Observe whether the flexible branch:

- bends without kinking;
- avoids pulling on barrel fitting;
- avoids moving the manifold;
- remains leak-free.

Do not perform destabilizing tests on fully loaded unsafe structures.

---

## 12. Pretreatment durability

Track:

- settling volume;
- sludge accumulation;
- drain function;
- roughing-media clogging;
- bypass/channeling;
- cleaning frequency.

Record:

```text
maintenance events / 100 L
```

and:

```text
maintenance minutes / cycle
```

---

## 13. Filter durability

For the selected health-critical filter, use manufacturer or validation instructions where available.

Track:

- flow rate;
- head;
- cleaning events;
- integrity checks;
- housing leaks;
- seal condition;
- abnormal high-flow events;
- clogging.

Normalize flow:

```text
Q_n / Q_0
```

where:

- `Q_0` = commissioning baseline;
- `Q_n` = flow after cycle n.

An unexpected increase may indicate failure; a decrease may indicate fouling.

No generic threshold overrides product-specific guidance.

---

## 14. Filter maintenance cycle

At defined intervals:

1. change status to GRAY;
2. perform maintenance;
3. inspect seals/housing;
4. recommission;
5. measure flow;
6. complete required verification;
7. restore status only if criteria are met.

Track whether repeated opening/closing damages:

- threads;
- seals;
- housings;
- couplings;
- tamper marks.

---

## 15. Clean-storage durability

Cycle:

- fill;
- dispense;
- close;
- inspect;
- clean at defined intervals.

Track:

- lid fit;
- vent-screen condition;
- spigot leakage;
- outlet contamination;
- labeling durability;
- physical lockout function.

Clean-storage failures are health-critical even if the filter remains functional.

---

## 16. Status / lockout durability

Repeatedly exercise:

```text
GREEN
AMBER
RED
GRAY
```

Verify that:

- tags remain legible;
- cards stay attached;
- caps fit repeatedly;
- removed handles can be reinstalled;
- seals/ties remain available;
- operators can still recognize state after repeated use.

Minimum test:

```text
30 status changes
```

before field deployment.

---

## 17. Liner repair cycle

Deliberately use a sacrificial bench liner coupon or controlled non-health-critical panel for repair testing.

Do not puncture an active drinking-water prototype merely to test repair.

Test:

- patch adhesion;
- flexing after patch;
- repeated wet/dry exposure;
- leak recurrence;
- abrasion around patch.

Record whether patching can be performed with the expected field toolset.

---

## 18. Overflow and erosion durability

During high-flow events inspect:

- overflow conveyance;
- outlet erosion;
- rubble migration;
- standing water;
- splash toward clean components;
- undermining of barrel pad.

Any overflow that threatens structural support or contaminates clean components is a critical design failure.

---

## 19. Dust / fouling cycle

Use safe inert test dust only where appropriate for bench work.

Do not use hazardous demolition dust.

Evaluate:

- screen clogging;
- collector cleaning burden;
- first-flush demand;
- liner abrasion;
- turbidity change;
- filter loading.

Field environments should use naturally occurring dust exposure rather than artificial hazardous contaminants.

---

## 20. Transport / reassembly test

For systems intended to move:

1. drain;
2. disassemble modular sections;
3. package;
4. move short distance;
5. reassemble;
6. recommission.

Track:

- missing parts;
- broken fittings;
- setup errors;
- liner damage;
- seal damage;
- recommissioning time.

---

## 21. Failure injection tests

Use only harmless/safe simulations.

Simulate:

- missing status tag;
- closed manifold branch;
- harmless tracer in isolated raw barrel;
- partially clogged screen;
- loosened non-critical fitting;
- abnormal high-flow signal;
- overdue maintenance card.

Do not intentionally contaminate potable-research components with pathogens, toxic chemicals, or hazardous debris.

Success criterion:

```text
failure becomes visible before unsafe classification persists
```

---

## 22. Metrics

Track:

```text
cycles completed
critical failures / 100 cycles
minor repairs / 100 cycles
maintenance minutes / cycle
replacement parts / 100 cycles
litres processed before intervention
setup time
stow time
recommissioning time
flow drift
settlement drift
liner repairs
operator errors
```

---

## 23. Durability score

Internal scoring:

```text
5 = 100 cycles with no critical failure and low maintenance
4 = 30-100 cycles with manageable repair burden
3 = 10-30 cycles with no unresolved critical failure
2 = repeated moderate failures
1 = critical failures before 10 cycles
0 = unsafe / unusable
```

This is an internal maturity score, not a WHO/UNICEF rating.

---

## 24. Critical failure list

Any of the following stops the durability test until resolved:

```text
DF-1 structural instability
DF-2 liner breach into contaminated substrate
DF-3 hidden first-flush bypass
DF-4 raw-to-clean cross-connection
DF-5 manifold branch cannot isolate
DF-6 health-critical filter integrity failure
DF-7 clean storage contamination path
DF-8 lockout/status system cannot prevent normal dispensing after failure
DF-9 rubble-pad movement threatens barrel stability
DF-10 overflow undermines support or contaminates clean path
```

---

## 25. Test record

```text
SYSTEM ID: __________________
PROTOTYPE VERSION: __________
DATE STARTED: _______________
TESTER: _____________________

TARGET LEVEL:
[ ] D0
[ ] D1 - 10 cycles
[ ] D2 - 30 cycles
[ ] D3 - 100 cycles
[ ] D4 - field exposure

CYCLES COMPLETED: ___________

CRITICAL FAILURES: __________
MINOR REPAIRS: ______________
MAINTENANCE MINUTES: ________
PARTS REPLACED: _____________
LITRES PROCESSED: ___________

FLOW BASELINE: ______________
FLOW FINAL: _________________

SETTLEMENT MAX: __________ mm

LINER REPAIRS: ______________
STATUS/LOCKOUT FAILURES: _____

FINAL DURABILITY SCORE: _____/5

REQUIRED REDESIGN: __________
```

---

## 26. Advancement gates

### Advance D0 -> D1

All subsystems operate once without critical failure.

### Advance D1 -> D2

```text
10 cycles complete
zero unresolved critical failures
all isolation/lockout functions preserved
```

### Advance D2 -> D3

```text
30 cycles complete
repair burden acceptable
no recurring hidden-failure mode
```

### Advance D3 -> D4

```text
100 cycles or justified equivalent exposure
no unresolved critical failure
maintenance burden documented
```

---

## 27. Design decision

Durability is now treated as a measured evidence gate rather than a descriptive claim.

The integrated prototype should not be described as durable solely because it is mechanically simple.

The project must show:

```text
REPEATED OPERATION
+
MEASURED WEAR
+
REPAIR HISTORY
+
FAILURE VISIBILITY
+
MAINTENANCE BURDEN
```

before increasing maturity classification.

---

## 28. Next pass

Proceed to the **specific health-critical filter candidate freeze** using current product-level evidence and WHO/UNICEF evaluation sources where available.

The next file should compare exact candidate products or tightly defined product classes on:

- microbial evidence;
- gravity-head compatibility;
- flow;
- service life;
- cleaning;
- fail-visible behavior;
- cost;
- Gaza/logistics suitability;
- chemical limitations.
