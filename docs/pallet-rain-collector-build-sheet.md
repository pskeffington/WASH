# Pallet Rain Collector Build Sheet

## Purpose

This build sheet converts the pallet rain collector concept into a reproducible one-module field build. It is intended for low-resource settings where suitable storage may already exist, roof modification is unaffordable or unsafe, and salvaged wood is more available than purpose-built rainwater infrastructure.

Collected water remains **experimental and non-potable by default** unless the complete water-contact, treatment, testing, and use-classification pathway is separately validated.

## Reference module

```text
1 salvaged pallet or equivalent wood frame
1 replaceable waterproof liner
1 elevated support frame
1 low-edge gutter
1 debris screen
1 first-flush diverter
1 gravity transfer line
1 existing barrel / cistern
1 overflow path
```

Reference pallet geometry:

```text
nominal pallet: 48 x 40 in
collector angle: 10-20 deg
nominal starting angle: 15 deg
low-edge height above grade: 42-48 in starting range for a typical 55-gal drum
```

The actual storage inlet controls final elevation. Do not raise the collector higher than required to preserve gravity flow.

## Functional dimensional chain

The build is accepted only when this vertical relationship exists:

```text
LOW EDGE OF CATCHMENT
        >
GUTTER OUTLET
        >
SCREEN / TRANSFER TEE
        >
BARREL / CISTERN INLET
```

The first-flush branch may extend below the transfer tee. It must not create an uphill return path to storage.

Measure and record:

```text
H1 = low catchment edge above grade
H2 = gutter outlet above grade
H3 = transfer tee centerline above grade
H4 = storage inlet centerline above grade
```

Acceptance condition:

```text
H1 > H2 > H3 > H4
```

with visible continuous fall in all connecting plumbing.

## Material hierarchy

### Structural materials

Prefer locally available or salvaged material where structurally sound:

- pallet;
- scrap lumber;
- braces;
- screws / bolts / washers;
- blocks, stones, or stable rubble footing outside the water-contact path;
- stakes, anchors, or ballast where required.

### Water-contact materials

Use a distinct controlled layer for the rainwater path:

- intact replaceable liner or membrane;
- gutter or folded liner trough;
- screen;
- transfer pipe;
- first-flush assembly;
- known-use storage container where possible.

### No-paint rule

Do **not** specify painting, staining, spraying, sealing, or coating the pallet as a normal waterproofing or preservation step.

Design intent:

```text
WOOD = STRUCTURE
LINER = WATERPROOF / WATER-CONTACT SURFACE
```

If a pallet is structurally unsuitable without a coating, it should be repaired, reassigned to a non-critical role, or rejected rather than made acceptable by an unknown surface treatment.

## Nominal one-pallet BOM

### Required

- 1 x structurally acceptable pallet, measured before build;
- liner sized at least several inches beyond pallet perimeter for fastening and drainage folds;
- 2-4 support legs or equivalent braced support structure;
- diagonal bracing sufficient to prevent racking;
- broad feet, blocks, or stable footing;
- fasteners with washers or battens for liner retention;
- approximately 40-48 in gutter or folded liner trough;
- coarse removable mesh screen;
- gravity transfer pipe or hose of adequate diameter;
- tee or equivalent branch for first flush;
- first-flush standpipe or removable collection vessel;
- closed or closable barrel/cistern inlet;
- overflow line.

### Optional / site-dependent

- second pallet used as base or rear bracing;
- anchors or ballast;
- insect mesh at barrel vent;
- cleanout fitting;
- flow indicator or simple transparent section;
- graduated sight tube for storage measurement;
- sampling tap for experimental water-quality work.

## Build sequence

### B0 - select pallet

Record:

```text
length
width
condition
visible markings
odor / residue check
rot / insect damage
repair requirements
```

Reject structurally unsafe or visibly contaminated pallets.

### B1 - repair structure

- replace or reinforce missing non-critical boards as needed;
- tighten loose joints;
- remove protruding nails from working surfaces;
- add diagonal bracing where required;
- do not use paint or coating as a substitute for structural repair.

### B2 - establish support height

Place the barrel/cistern first and measure its inlet height.

Set collector support height so:

```text
gutter outlet > transfer tee > storage inlet
```

A typical 55-gallon drum may place the collector low edge around 42-48 in above grade, but field geometry controls.

### B3 - set collector angle

Start near 15 degrees from horizontal.

Verify:

- water drains completely to the low edge;
- no deep liner pockets remain;
- frame remains stable;
- wind exposure is acceptable;
- horizontal projected area remains useful.

### B4 - install liner

- isolate rainwater from direct contact with pallet wood where practical;
- extend liner beyond edges;
- use battens, clips, washers, rope, or broad-load fasteners;
- avoid puncture-prone sharp fasteners in the flow surface;
- form a clean low edge feeding the gutter.

### B5 - install gutter

Acceptable prototype variants:

- split PVC;
- conventional gutter section;
- bent sheet gutter;
- supported folded-liner trough.

Starting gutter slope:

```text
~1/8 in per ft toward outlet
```

Verify no retained pools remain after a bucket test.

### B6 - install screen and first flush

Place removable coarse screen before the storage inlet.

Initial first-flush test volumes:

```text
0.25 gal
0.5 gal
1.0 gal
```

Do not freeze one volume until local contamination and rainfall observations justify it.

### B7 - connect storage

- keep transfer path continuously descending;
- enter storage through a screened/closed interface where practical;
- do not require lifting or pumping of collected water;
- ensure barrel/cistern remains stable when empty and full.

### B8 - install overflow

Overflow must:

- leave storage near maximum intended water level;
- have capacity comparable to the inlet path;
- discharge away from foundations and unstable slopes;
- terminate in an erosion-resistant area.

## Pre-use hydraulic test

Run a simulated-rain or bucket test before field operation.

Verify:

```text
[ ] liner drains to gutter
[ ] gutter drains to outlet
[ ] screen does not cause immediate backup
[ ] first-flush chamber fills first
[ ] later water reaches storage
[ ] no reverse slope in transfer line
[ ] no leakage at storage inlet
[ ] overflow functions when storage is full
```

## Structural acceptance test

Before use:

```text
[ ] pallet passes salvage gate
[ ] support frame is independently stable
[ ] structure does not rack under hand pressure
[ ] feet do not slide under normal handling
[ ] diagonal bracing is present where needed
[ ] collector low edge remains above storage inlet
[ ] liner attachment does not peel from a corner
[ ] no paint/coating has been added as a routine collector treatment
[ ] anchors/ballast do not block drainage or create major trip hazards
```

## Field data sheet

Record for each storm:

```text
site:
date:
pallet dimensions:
collector angle:
H1 low edge:
H2 gutter outlet:
H3 transfer tee:
H4 storage inlet:
rainfall depth:
first-flush volume:
storage before:
storage after:
overflow observed: yes/no
visible debris/turbidity:
leaks:
frame movement:
liner damage:
maintenance performed:
```

## Performance calculation

Projected catchment area:

```text
A_projected = A_surface * cos(theta)
```

Theoretical captured volume:

```text
V_theoretical = 0.623 * A_projected * rainfall_inches
```

Collection efficiency:

```text
eta = measured captured volume / V_theoretical
```

For a nominal 48 x 40 in pallet at 15 degrees:

```text
A_surface = 13.33 ft2
A_projected ~= 12.88 ft2
V_theoretical ~= 8.0 gal per inch
```

An 80% recovery assumption would correspond to about 6.4 gal/in, but measured data should replace this assumption.

## Cost and accessibility tracking

For each build, record:

```text
new-material cost
salvaged-material fraction
build labor-hours
repair labor-hours
replacement liner cost
first-flush hardware cost
storage cost if not already available
```

Primary low-resource metric:

```text
liters collected / dollar of new material
```

Secondary metrics:

```text
liters / labor-hour
$/ft2 of new catchment
maintenance minutes / storm-month
```

## Build acceptance decision

### ACCEPT FOR FIELD PROTOTYPE

All of the following are true:

- structurally stable;
- gravity-feed geometry confirmed;
- liner and gutter drain completely;
- first flush functions;
- storage inlet and overflow function;
- no routine paint/coating treatment introduced near the pallet/water path;
- water remains correctly classified as experimental/non-potable unless separately validated.

### REPAIR AND RETEST

Use when:

- frame is repairable;
- gravity head is insufficient;
- gutter retains water;
- liner attachment is weak;
- first flush fails to separate initial runoff;
- overflow is undersized or poorly routed.

### REJECT

Use when:

- pallet is structurally unsafe;
- contamination is obvious or strongly suspected;
- support cannot be stabilized with simple local means;
- gravity transfer cannot be achieved without unsafe elevation;
- storage is unsuitable or of unknown hazardous prior use.

## Prototype objective

The target is a field-reproducible module with this logic:

```text
SALVAGED WOOD
     +
MINIMAL NEW HARDWARE
     +
CONTROLLED LINER
     +
LOWEST SAFE ELEVATION
     +
GRAVITY FLOW
     +
EXISTING STORAGE
     =
LOW-COST INDEPENDENT RAIN CATCHMENT
```
