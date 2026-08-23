# Pallet Rain Collector Durability Cycle Protocol

## Purpose

This protocol defines how to evaluate repeated weathering, use, and maintenance effects on the pallet rain collector before the design is treated as field-ready.

The goal is not to assign an assumed service life. The goal is to determine which components fail first, whether failure is visible before hydraulic or structural loss, and whether repair remains low-cost and locally achievable.

The collector remains **experimental and non-potable by default** unless the complete water-contact, treatment, testing, and use-classification pathway is separately validated.

## Durability doctrine

```text
CHEAP WEAR LAYERS SHOULD FAIL BEFORE MAJOR STRUCTURE
        ↓
FAILURE SHOULD BE VISIBLE
        ↓
REPAIR SHOULD REQUIRE COMMON TOOLS
        ↓
THE SYSTEM SHOULD RETURN TO SERVICE WITHOUT FULL REBUILD
```

The prototype should prefer:

```text
liner adjustment
screen cleaning
gutter realignment
fastener tightening
brace replacement
```

over:

```text
full pallet replacement
barrel replacement
major plumbing reconstruction
```

## Components under test

Track each component independently:

### D1 - pallet / wood frame

Observe:

- checking and splitting;
- joint loosening;
- rot initiation;
- fungal growth;
- insect damage;
- localized crushing at supports;
- distortion / warping;
- loss of screw or bolt holding power;
- racking under hand load.

Do not introduce paint, stain, spray sealant, or coating as a routine durability intervention. The wood remains structural material; the replaceable liner remains the water-contact / waterproof layer.

### D2 - liner

Observe:

- puncture;
- edge tearing;
- abrasion at battens and fasteners;
- UV embrittlement;
- sagging;
- loss of tension;
- wrinkle formation;
- ponding;
- outlet tear propagation;
- leakage to pallet wood.

### D3 - fasteners and attachment points

Observe:

- screw withdrawal;
- nail loosening;
- washer pull-through;
- batten splitting;
- corrosion;
- strap stretch;
- clip failure;
- progressive edge peel.

### D4 - gutter

For G-L1 folded-liner trough:

- sagging;
- support creep;
- fold deformation;
- edge tearing;
- retained water;
- outlet distortion.

For G-P1 split-PVC:

- cracking;
- rotation;
- support failure;
- sharp-edge abrasion;
- outlet blockage;
- slope loss.

### D5 - first-flush assembly

Observe:

- chamber leakage;
- drain blockage;
- sediment accumulation;
- float sticking if FF-F1 used;
- seat fouling;
- reset time drift;
- cap / cleanout damage.

### D6 - support and footing

Observe:

- settlement;
- tilt;
- foot movement;
- erosion;
- ballast displacement;
- anchor loosening;
- loss of collector-to-storage gravity head.

### D7 - storage interface

Observe:

- inlet leakage;
- lid deformation;
- overflow restriction;
- vent blockage;
- fitting loosening;
- barrel movement;
- footing settlement.

## Baseline measurements

Before cycling, record:

```text
build ID
pallet dimensions
collector angle
H1 low edge
H2 gutter outlet
H3 transfer tee
H4 storage inlet
frame diagonal dimensions
support spacing
liner type / thickness if known
liner installed area
gutter type
first-flush type
storage type
all fastener types and counts
```

Photograph or sketch:

- front;
- side;
- underside;
- low-edge gutter;
- first-flush assembly;
- support feet;
- storage inlet / overflow.

## Accelerated bench cycle

One cycle represents a simplified wet-load-dry-maintenance sequence.

### Cycle step A - dry inspection

Check:

```text
frame movement
fastener looseness
liner tension
gutter alignment
support settlement
```

### Cycle step B - simulated rain

Run enough water to wet the entire collector and exercise:

```text
liner → gutter → screen → first flush → storage → overflow
```

Include at least one short high-rate pour during every fifth cycle.

### Cycle step C - saturated hold

Keep the collector wet long enough to inspect:

- liner sag;
- leakage;
- gutter deformation;
- joint movement;
- support settlement.

Initial bench hold:

```text
30-60 min
```

This is an internal test interval, not a service-life equivalence claim.

### Cycle step D - drain-down

Allow full gravity drainage.

Pass condition:

```text
no substantial standing water remains in collector or gutter
```

Record retained pockets.

### Cycle step E - dry period

Allow the assembly to dry naturally or under controlled ambient conditions.

Do not heat wood or liner aggressively in a way that creates unrealistic damage.

### Cycle step F - handling perturbation

Apply ordinary service disturbance:

- clean screen;
- open first-flush cleanout;
- touch / inspect gutter;
- lightly push frame by hand;
- operate any isolation fittings.

The objective is to include wear from maintenance, not only rainfall.

## Initial cycle schedule

```text
0 cycles = baseline
5 cycles = early inspection
10 cycles = first checkpoint
25 cycles = intermediate checkpoint
50 cycles = extended bench checkpoint
```

Do not claim that 50 bench cycles equal a fixed number of field months or years.

## Field durability schedule

Once deployed, inspect at:

```text
installation
first rain
first heavy rain
30 days
90 days
180 days
365 days
```

Also inspect after:

- strong wind;
- hail if relevant;
- freezing weather;
- flooding / erosion;
- visible impact damage;
- extended dry periods before reuse.

## Gravity-head retention gate

Durability includes hydraulic geometry.

At every checkpoint record:

```text
H1
H2
H3
H4
```

Verify:

```text
H1 > H2 > H3 > H4
```

If settlement or warping removes continuous gravity descent, the module is not accepted even if the structure remains standing.

## Structural movement measurement

Record simple diagonal dimensions across the support frame.

Define:

```text
rack_change = |diagonal_A - baseline_A|
            + |diagonal_B - baseline_B|
```

Use this as an internal trend metric rather than a universal structural limit.

Also record visible looseness under a standardized hand-push check:

```text
0 = no obvious movement
1 = minor movement
2 = noticeable movement / service required
3 = unstable / remove from service
```

## Liner condition scale

```text
L0 = intact; no service needed
L1 = cosmetic wrinkles / minor tension adjustment
L2 = localized abrasion or small repair required
L3 = active leak / tear; replace or repair before use
L4 = widespread degradation; liner rejected
```

## Wood condition scale

```text
W0 = sound
W1 = weathering only
W2 = localized split / loose joint; repair required
W3 = rot, crushing, major joint degradation; remove from service
W4 = unsafe frame; reject
```

Paint or coating is not an authorized method for moving a W3/W4 component back to W0/W1.

## Gutter condition scale

```text
G0 = drains fully
G1 = minor alignment adjustment
G2 = local sag / retained water; repair
G3 = repeated bypass / structural gutter failure; replace
```

## First-flush condition scale

```text
F0 = fills and resets correctly
F1 = cleaning required
F2 = reset time / float movement degraded; service
F3 = first runoff no longer isolated; remove from service until repaired
```

## Support / footing condition scale

```text
S0 = stable
S1 = minor settlement; geometry retained
S2 = measurable tilt / head loss; re-level
S3 = unstable / erosion / overturning risk; remove from service
```

## Failure visibility requirement

Preferred failure modes should be observable without specialized instruments.

Examples:

- sagging liner;
- standing water;
- loose brace;
- leaning frame;
- gutter spill;
- blocked overflow;
- first-flush chamber not draining;
- visible leak.

A hidden failure that sends untreated first-flush water to storage or defeats raw/clean separation is higher priority than cosmetic wood aging.

## Repair classification

### DR1 - immediate no-cost adjustment

Examples:

- retension liner;
- reposition screen;
- clear debris;
- re-seat gutter support.

### DR2 - low-cost replaceable part

Examples:

- replace screen;
- replace small section of hose;
- replace fastener / washer;
- replace first-flush drain fitting.

### DR3 - structural repair

Examples:

- sister brace;
- replace pallet slat;
- replace foot block;
- add diagonal brace.

### DR4 - component replacement

Examples:

- replace liner;
- replace gutter body;
- replace full first-flush assembly;
- replace pallet frame.

Track labor and cash for every repair.

## Durability performance metrics

### Repair frequency

```text
repairs / 10 cycles
```

and later:

```text
repairs / field month
```

### Maintenance burden

```text
maintenance minutes / cycle
```

or:

```text
maintenance minutes / month
```

### Cost accumulation

```text
cumulative repair dollars
```

### Hydraulic retention

```text
measured collection efficiency at checkpoint /
baseline collection efficiency
```

### Downtime

```text
hours or days unavailable due to repair
```

## Acceptance gates

### D-G0 Baseline

Complete measurements and condition documentation before cycling.

### D-G1 Five-cycle survival

Pass if:

- no structural instability;
- gravity head retained;
- no major liner tear;
- gutter remains functional;
- first flush still separates initial runoff.

### D-G2 Ten-cycle serviceability

Pass if:

- all required maintenance can be completed with ordinary tools;
- no DR4 replacement is required unless the part was deliberately damaged for testing;
- collection efficiency has not materially collapsed.

### D-G3 Twenty-five-cycle repairability

Pass if:

- observed failures remain predominantly DR1-DR3;
- support settlement can be corrected;
- no hidden contamination pathway has emerged.

### D-G4 Fifty-cycle extended bench gate

Pass if:

- structural frame remains serviceable or repairable;
- liner failure mode is visible before gross leakage;
- gutter and first-flush systems remain maintainable;
- cumulative repair burden remains compatible with the low-resource objective.

### D-G5 Field checkpoint gate

Field-readiness should not be declared until at least repeated real-rain observations exist and the 30/90/180/365-day inspection framework is active.

## Stop-use conditions

Immediately remove the collector from service for repair if:

- frame becomes unstable;
- support settlement removes gravity descent;
- liner tear causes uncontrolled contact with suspect structural materials or large capture loss;
- first-flush separation fails;
- overflow is blocked;
- barrel/cistern shifts or footing becomes unstable;
- raw water is accidentally connected to a treated-water path.

## Field durability log

```text
build ID:
date:
cycle count / field age:
weather since prior inspection:

wood condition W0-W4:
liner condition L0-L4:
gutter condition G0-G3:
first flush F0-F3:
support S0-S3:

H1:
H2:
H3:
H4:

gravity path retained: yes/no
standing water observed: yes/no
leaks: yes/no
frame movement score 0-3:
maintenance minutes:
repair class DR1-DR4:
repair cash cost:
parts replaced:
notes:
```

## Current freeze status

```text
durability protocol: FROZEN FOR BENCH USE
5 / 10 / 25 / 50 cycle checkpoints: ACTIVE
30 / 90 / 180 / 365 day field checkpoints: ACTIVE
paint/coating as pallet preservation: NOT RECOMMENDED
service-life claim: NOT YET ESTABLISHED
```
