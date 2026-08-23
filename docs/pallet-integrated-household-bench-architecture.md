# Integrated Pallet Household Bench Architecture

## Purpose

This document combines the pallet collector, gutter, first-flush unit, raw storage, overflow, instrumentation, and durability requirements into one integrated bench architecture.

The purpose is to test the complete low-cost rainwater module as a system rather than as isolated components.

Collected water remains **experimental and non-potable by default** unless the complete water-contact, treatment, testing, and use-classification pathway is separately validated.

## Integrated reference system

```text
ELEVATED SALVAGED PALLET FRAME
        ↓
REPLACEABLE LINER
        ↓
G-L1 OR G-P1 GUTTER
        ↓
REMOVABLE COARSE SCREEN
        ↓
FF-M1 OR FF-F1 FIRST FLUSH
        ↓
GRAVITY TRANSFER LINE
        ↓
RAW BARREL / CISTERN
        ↓
INDEPENDENT OVERFLOW
```

No pump is required for the reference architecture.

## Fixed interface contract

Each module must preserve the same interfaces so components can be exchanged without redesigning the whole system.

### I1 Collector to gutter

Requirements:

- full low edge drains toward gutter;
- no major bypass behind liner;
- gutter can be removed independently;
- no paint/coating is used as the waterproof interface.

### I2 Gutter to screen

Requirements:

- outlet remains accessible;
- removable screen does not create severe flow restriction;
- flow remains gravity-descending.

### I3 Screen to first flush

Requirements:

- first-flush chamber receives initial runoff before storage;
- chamber can be cleaned;
- later runoff transitions to storage without requiring a pump.

### I4 First flush to storage

Requirements:

```text
transfer tee > storage inlet
```

and no low-loop trap is permitted.

### I5 Storage to overflow

Requirements:

- overflow elevation defines maximum storage level;
- overflow capacity must not be obviously smaller than the inlet path without test evidence;
- discharge goes to a safe erosion-resistant location.

## Reference geometry

Nominal pallet:

```text
48 x 40 in
```

Nominal collector angle:

```text
15 deg starting point
```

Reference vertical chain:

```text
H1 = low collector edge
H2 = gutter outlet
H3 = transfer tee
H4 = storage inlet
```

Acceptance condition:

```text
H1 > H2 > H3 > H4
```

Typical starting point for a 55-gallon drum:

```text
H1 ≈ 42-48 in above grade
```

The actual barrel/cistern geometry controls final dimensions.

## Bench configuration A

Minimum-parts architecture:

```text
pallet
+ liner
+ G-L1 folded-liner trough
+ coarse screen
+ FF-M1 manual first flush
+ independent 55-gal barrel
```

This is the **primary affordability baseline**.

## Bench configuration B

Rigid-hydraulic comparison:

```text
pallet
+ liner
+ G-P1 split-PVC gutter
+ coarse screen
+ FF-F1 floating-ball first flush
+ independent 55-gal barrel
```

This is the **manufactured-component comparison**.

## Instrumentation points

### P0 Rain input

Measure:

```text
simulated rainfall volume
or
measured field rainfall depth
```

### P1 Collector runoff

Optional measurement point immediately before gutter for controlled bench tests.

### P2 Gutter outlet

Measure or observe:

- spill/bypass;
- retained water;
- outlet backup.

### P3 First-flush chamber

Record:

```text
selected chamber volume
fill completion time
reset time
sediment / visible contamination
```

### P4 Storage inlet

Record:

```text
start of storage inflow
backup occurrence
leakage
```

### P5 Storage volume

Record before and after each test.

### P6 Overflow

Record:

```text
overflow onset
overflow continuity
backup during full-storage condition
```

## System mass-balance test

For each controlled bench test:

```text
V_input = V_firstflush
        + V_storage
        + V_overflow
        + V_retained
        + V_spill
        + V_unmeasured_loss
```

Calculate:

```text
mass_balance_error = V_input - measured outputs
```

and:

```text
recovery_efficiency = V_storage / potential collectable input
```

The exact denominator must be documented so first-flush diversion is not accidentally counted as a hydraulic failure.

## Integrated test sequence

### T0 Dry inspection

Verify:

```text
[ ] pallet salvage gate passed
[ ] support stable
[ ] H1 > H2 > H3 > H4
[ ] liner secure
[ ] no paint/coating specified near pallet/water path
[ ] gutter removable
[ ] screen removable
[ ] first flush serviceable
[ ] barrel stable
[ ] overflow routed safely
```

### T1 Low-flow rain simulation

Objective:

- verify continuous drainage;
- confirm no reverse slope;
- confirm first-flush filling logic.

### T2 Moderate-flow rain simulation

Objective:

- measure gutter behavior;
- observe screen loading;
- confirm transition from first flush to storage.

### T3 High-rate short-duration simulation

Objective:

- identify gutter bypass;
- identify first-flush or inlet backup;
- test structural movement under wet load.

### T4 Full-storage overflow test

Objective:

- fill storage to overflow elevation;
- continue inflow;
- confirm overflow handles continued collector input;
- verify water does not back up toward first flush or gutter.

### T5 Debris challenge

Use a controlled small quantity of leaves or inert surrogate debris.

Objective:

- verify removable screen function;
- measure cleaning time;
- identify blockage locations.

### T6 Post-test drain-down

Pass if:

- no substantial standing water remains in gutter or transfer line;
- first flush resets as designed;
- collector returns to stable dry geometry.

## Integrated acceptance gates

### H-G0 Geometry

Pass if:

```text
H1 > H2 > H3 > H4
```

and continuous gravity descent is visually confirmed.

### H-G1 Structural

Pass if:

- frame remains stable;
- support does not rack excessively;
- no footing movement threatens gravity geometry.

### H-G2 Hydraulic

Pass if:

- runoff enters gutter;
- first flush captures initial water;
- later runoff reaches storage;
- no uncontrolled backup occurs.

### H-G3 Overflow

Pass if full-storage inflow exits through overflow without uncontrolled upstream flooding.

### H-G4 Maintenance

Pass if a resident can:

- clean screen;
- service first flush;
- inspect gutter;
- tighten accessible fasteners;
- inspect liner;
- verify overflow;

using ordinary tools.

### H-G5 Cost

Track:

```text
new cash cost
salvage fraction
labor-hours
```

Current one-pallet target excluding storage/treatment:

```text
<= $40 new cash
stretch target <= $25
```

### H-G6 Durability entry

Integrated system must enter the 5 / 10 / 25 / 50 cycle durability protocol without redesigning core interfaces.

### H-G7 Water-use boundary

Raw collected water remains correctly labeled and isolated from any treated-water storage.

## Bench comparison matrix

| Variable | Configuration A | Configuration B |
|---|---|---|
| gutter | G-L1 folded liner | G-P1 split PVC |
| first flush | FF-M1 | FF-F1 |
| pallet | same reference geometry | same reference geometry |
| liner | same material where possible | same material where possible |
| barrel | same size/type where possible | same size/type where possible |
| collector angle | same | same |
| hydraulic head | same target | same target |

Primary comparison metrics:

```text
captured volume
spill/bypass
retained water
maintenance time
repair time
new-material cost
failure count
```

## Failure isolation

A failure should be traceable to one module:

```text
collector
liner
gutter
screen
first flush
transfer line
storage inlet
overflow
support
```

Do not treat total system underperformance as one undifferentiated failure.

## Sketch contract for integrated system

Future integrated sketches must show:

- elevated pallet collector;
- visible support / bracing;
- replaceable liner;
- interchangeable gutter module;
- removable screen;
- first-flush branch;
- continuous downhill gravity transfer;
- low stable barrel/cistern;
- independent overflow;
- explicit RAW / NON-POTABLE prototype label;
- no paint/coating recommendation near the pallet.

## Current integrated freeze status

```text
Configuration A: FROZEN FOR BENCH BUILD
Configuration B: FROZEN FOR COMPARATIVE BENCH BUILD
interface contract I1-I5: FROZEN
integrated hydraulic gates H-G0 through H-G7: ACTIVE
field deployment claim: NOT YET ESTABLISHED
```

## Next evidence required

Before promoting the architecture beyond bench status, collect:

- actual build cost;
- actual build time;
- measured hydraulic recovery;
- gutter comparison data;
- first-flush comparison data;
- overflow stress-test result;
- 5 / 10 / 25 / 50 cycle durability observations;
- field rain observations;
- maintenance burden;
- water-quality observations appropriate to the intended use classification.
