# Pallet Collector Barrel / Cistern Manifold

## Purpose

This document defines the storage-side architecture for one or more pallet rain collectors feeding existing barrels or cisterns in low-resource settings.

The design objective is to preserve:

- gravity flow;
- modular expansion;
- simple isolation for repair;
- visible overflow behavior;
- separation between raw and treated water paths;
- compatibility with existing barrels/cisterns where their prior use is known or otherwise acceptable for the intended research use.

Collected water remains **experimental and non-potable by default** unless the complete water-contact, treatment, testing, and use-classification pathway is separately validated.

## Core rule

```text
COLLECTORS
    ↓
FIRST FLUSH
    ↓
RAW STORAGE ONLY
    ↓
OPTIONAL TREATMENT
    ↓
SEPARATE CLEAN STORAGE
```

Do not connect a raw rainwater collector manifold directly into a container designated as validated treated-water storage.

## Reference architectures

### M-S1 Single collector / single barrel

```text
PALLET
  ↓
FIRST FLUSH
  ↓
BARREL A
  ↓
OVERFLOW
```

This is the minimum reference system.

### M-P2 Two collectors / parallel barrels

```text
PALLET 1 ──→ FF1 ──→ BARREL A

PALLET 2 ──→ FF2 ──→ BARREL B
```

Advantages:

- failures remain isolated;
- simple troubleshooting;
- easy side-by-side prototype comparison;
- no shared manifold required.

### M-C2 Two collectors / common raw-storage manifold

```text
PALLET 1 ─→ FF1 ─┐
                  ├─→ COMMON RAW INLET HEADER ─→ BARREL A
PALLET 2 ─→ FF2 ─┘                         └──→ BARREL B
```

Use only after single-module hydraulics are verified.

## Storage-level strategy

Two low-resource arrangements are acceptable for bench comparison.

### Independent-fill barrels

Each collector feeds a dedicated barrel.

```text
collector A → barrel A
collector B → barrel B
```

Preferred when:

- fittings are scarce;
- storage vessels differ in size or condition;
- maintenance capacity is limited;
- water-quality experiments require source separation.

### Equalized barrel bank

Multiple barrels are connected near their lower sidewalls through a common equalization line.

```text
      inlet
        ↓
    BARREL A
       │
       ├──────── equalization line ────────┐
       │                                    │
    BARREL B                            BARREL C
```

This can make multiple barrels behave as one larger reservoir, but it also couples failures and contamination.

For the first fieldable architecture, **independent-fill barrels are preferred** until the equalization line has been bench-tested.

## Raw / clean separation

The system must distinguish physically and visually between:

```text
RAW RAINWATER STORAGE
```

and:

```text
TREATED / VALIDATED STORAGE
```

Recommended separation methods:

- different containers;
- different outlet heights or fittings;
- clear labels;
- no shared equalization line;
- no gravity return path from clean storage to raw storage;
- no common open lid or transfer bucket.

A treatment stage, if later added, should create a one-way process:

```text
RAW BARREL
   ↓
TREATMENT
   ↓
CLEAN BARREL
```

not:

```text
RAW ↔ CLEAN
```

## Gravity inlet manifold

For a common header, every inlet branch must remain gravity-descending.

Reference hierarchy:

```text
collector gutter
    > first-flush tee
    > collector branch line
    > common header
    > barrel inlet
```

Avoid low loops that trap stagnant water.

### Header diameter

For one or two pallet modules, use a header at least as large as the largest feeder branch unless bench testing demonstrates a smaller size remains non-restrictive.

Prototype starting point:

```text
collector branch: ~1.5-2 in
common header: ~2 in or larger
```

Do not treat these as universal design minima; actual rainfall intensity and debris loading must be tested.

## Barrel inlet interface

Preferred features:

- closed or closable lid;
- screened inlet;
- screened vent;
- inlet above maximum stored waterline;
- removable connection for cleaning;
- no open funnel permanently exposed to insects and debris.

## Isolation logic

Every barrel in a multi-barrel bank should be capable of being isolated without disabling all collectors where practical.

Possible methods:

- branch valve;
- removable union;
- capped tee;
- flexible-hose disconnect;
- independent overflow reroute.

Design goal:

```text
one failed barrel ≠ total system failure
```

## Overflow architecture

Overflow is mandatory.

### Individual overflow

Each barrel has its own overflow line.

Advantages:

- simple;
- failures visible;
- no dependence on common header.

### Cascading overflow

```text
BARREL A overflow → BARREL B
BARREL B overflow → safe drainage
```

Potential benefit:

- fills first barrel before second.

Risks:

- upstream blockage can cause backup;
- barrel A may overflow before B if transfer is undersized;
- contamination and maintenance become coupled.

### Common overflow header

Multiple overflows discharge into one larger drain line.

Use only when the header is sized and tested for simultaneous flow.

## Preferred prototype overflow

For the first one- and two-barrel builds:

```text
INDEPENDENT BARREL OVERFLOWS
```

are preferred because they are easiest to inspect and least likely to hide failure.

## Barrel footing

A full 55-gallon barrel contains approximately 460 lb / 209 kg of water before adding barrel mass.

A full 200-L drum contains approximately 200 kg / 441 lb of water.

Therefore:

- keep barrels low;
- use broad stable footing;
- avoid narrow elevated stands unless independently engineered;
- keep settlement uniform across manifolded barrels;
- ensure fittings are not carrying structural load.

## Equalization-line caution

An equalization line near barrel bottoms can balance water levels, but creates several coupled hazards:

- one leaking barrel can drain multiple barrels;
- one contaminated barrel can contaminate the bank;
- sediment can settle into the common line;
- mismatched barrel elevations can induce uneven loading;
- service requires isolation valves or caps.

Therefore the equalized bank remains a **secondary prototype lane**, not the default low-income deployment architecture.

## Recommended first field architecture

```text
PALLET A
  ↓
FF-A
  ↓
BARREL A
  ↓
independent overflow

PALLET B
  ↓
FF-B
  ↓
BARREL B
  ↓
independent overflow
```

Advantages:

- no common inlet manifold;
- no shared contamination path;
- no shared failure point;
- easiest to build from mismatched salvaged barrels;
- easiest to compare collection performance.

## Shared-manifold development gate

Move to a common inlet header only after:

```text
[ ] one-pallet hydraulics pass
[ ] first flush passes
[ ] barrel inlet does not back up
[ ] overflow passes full-storage test
[ ] branch disconnection is understood
[ ] common header can be cleaned
[ ] no reverse-slope pockets exist
```

## Barrel prior-use gate

Before connecting any recovered barrel or cistern, record:

```text
prior contents known? yes/no
visible residue? yes/no
strong chemical odor? yes/no
physical damage? yes/no
lid intact? yes/no
inlet modifiable? yes/no
overflow possible? yes/no
```

Reject from water-storage research where previous contents were hazardous, unknown and suspicious, or where contamination cannot reasonably be excluded for the intended use.

Do not recommend paint, coatings, or sealants as a way to convert an unsuitable barrel into acceptable water storage.

## Hydraulic bench test

For each architecture:

1. start with empty storage;
2. simulate collector inflow;
3. confirm first-flush branch behavior;
4. confirm inlet does not back up;
5. continue until storage reaches overflow elevation;
6. confirm overflow handles continued inflow;
7. isolate one barrel if applicable;
8. repeat flow test.

Record:

```text
inflow rate
time to first-flush completion
time to barrel inflow
maximum header water depth
backup occurrence
overflow onset
overflow capacity
leaks
isolation success
```

## Sketch requirements

Future sketches should show:

- collector above barrel inlet;
- separate first-flush branch per collector unless a shared design is explicitly under test;
- independent raw storage labels;
- overflow exiting each barrel or clearly sized common overflow;
- no raw-to-clean cross connection;
- barrels sitting low on broad stable footing;
- branch isolation where a common manifold is shown.

Do not depict:

- barrels elevated unnecessarily to receive water;
- open-top storage as the default;
- untreated rainwater feeding a clean-water tank directly;
- lower equalization manifolds without isolation provisions;
- paint/coating as a barrel rehabilitation method.

## Current freeze status

```text
M-S1 single collector / single barrel: DESIGN FROZEN
M-P2 independent parallel barrels: DESIGN FROZEN FOR FIELD PROTOTYPE
M-C2 common raw inlet header: DESIGN FROZEN FOR BENCH TEST
bottom equalized barrel bank: RESEARCH LANE ONLY
raw / clean separation: REQUIRED
```

## Design principle

The storage architecture should preserve the same philosophy as the pallet collector:

```text
MODULAR
+
GRAVITY DRIVEN
+
LOW TO GROUND
+
INDEPENDENTLY REPAIRABLE
+
VISIBLE FAILURE
+
NO RAW/CLEAN CROSS-CONNECTION
```
