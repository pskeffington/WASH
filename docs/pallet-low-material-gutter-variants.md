# Pallet Low-Material Gutter Variants

## Purpose

This document defines two interchangeable gutter architectures for the pallet rain collector:

```text
G-L1 = folded-liner trough
G-P1 = split-PVC gutter
```

The goal is to reduce dependence on purpose-built gutter products while preserving simple gravity flow, inspectability, repairability, and compatibility with locally available materials.

Collected water remains **experimental and non-potable by default** unless the entire water-contact, treatment, testing, and use-classification pathway is separately validated.

## Design requirements shared by both variants

Each gutter must:

- accept runoff from the full low edge of the pallet collector;
- remain continuously sloped toward one outlet;
- preserve the elevated gravity-feed chain;
- avoid standing water after a simple flush test;
- tolerate coarse debris without immediate blockage;
- be removable or repairable with ordinary tools;
- avoid requiring paint, spray coating, or sealing of the pallet itself;
- remain outside unnecessary structural load paths;
- discharge into the screen / first-flush assembly without an uphill section.

Reference hierarchy:

```text
collector low edge
    > gutter body
    > gutter outlet
    > screen / transfer tee
    > storage inlet
```

Starting gutter slope:

```text
~1/8 in per ft toward outlet
```

This is a prototype starting value, not a universal minimum.

---

# G-L1 Folded-Liner Trough

## Concept

The collector liner extends beyond the pallet's low edge and is folded into a supported trough. This eliminates a separate gutter body.

```text
LINER OVER PALLET
       ↓ runoff
  ------------------
                  \
                   \
                    \____ folded liner trough
                         \____ outlet
```

## Materials

- same liner used for catchment surface, if sufficient excess length exists;
- one or more support battens / slats / wire / rope / simple brackets;
- end dams or folded end closures;
- outlet fitting or formed low-point discharge;
- optional removable mesh screen at outlet.

## Geometry

Reference low edge:

```text
40-48 in depending pallet orientation
```

Liner extension beyond low edge:

```text
starting range: 6-10 in
```

Form a trough approximately:

```text
2-4 in deep
2-4 in open width
```

Dimensions remain experimental and should be scaled to expected rainfall intensity and available liner stiffness.

## Support methods

Possible support methods:

- scrap wood batten under the outer lip;
- rope or wire support line;
- salvaged angle or bracket;
- second strip of liner acting as sling;
- simple drilled hanger points outside the primary flow surface.

Avoid puncturing the hydraulic low point where possible.

## Outlet methods

### GL1-A formed corner outlet

Slope trough toward one corner and form a narrow discharge into a pipe or funnel.

Advantages:

- fewest fittings;
- easy to fabricate.

Risks:

- corner may sag;
- localized wear;
- difficult to screen if too narrow.

### GL1-B bulkhead outlet

Install a mechanical outlet fitting through reinforced liner near the low end.

Advantages:

- cleaner pipe connection;
- easier to screen and service.

Risks:

- requires fitting;
- puncture/seal quality becomes important.

## Failure modes

Track:

- liner sagging;
- ponding between supports;
- edge tearing;
- folded end leakage;
- outlet tear propagation;
- UV embrittlement;
- debris accumulation in a shallow trough;
- progressive deformation after repeated storms.

## Acceptance test

Use a measured bucket or simulated-rain input.

Pass if:

```text
[ ] runoff enters trough across full low edge
[ ] no large bypass behind trough
[ ] no standing pool remains after drain-down
[ ] outlet remains continuously gravity-descending
[ ] trough does not collapse under expected short-duration flow
[ ] screen/outlet can be cleaned without removing whole liner
```

---

# G-P1 Split-PVC Gutter

## Concept

A section of PVC pipe is split longitudinally and used as a half-round gutter.

```text
full PVC pipe
     ↓ cut lengthwise
   _________
 /           \
|             |
 \___________/

use one half as gutter
```

## Materials

- straight PVC section approximately equal to pallet low-edge length;
- brackets, straps, wire, rope, or scrap-wood supports;
- outlet adapter or shaped end transition;
- removable screen.

## Starting size

For a one-pallet prototype:

```text
3-4 in nominal PVC starting range
```

A 2 in section may be too shallow once split for debris tolerance and high-intensity rainfall, so it should not be the primary reference gutter size without testing.

## Mounting

The split PVC should be supported at multiple points so it does not rotate or flatten under load.

Possible supports:

- wood cleats;
- wire loops;
- pipe straps;
- carved cradle blocks;
- rope suspension with anti-roll restraint.

## Outlet methods

### GP1-A end-cap outlet

Use an end cap with outlet drilled/fitted near the bottom.

### GP1-B open-end funnel

Slope the half-pipe directly into a larger funnel or tee.

### GP1-C reduced outlet fitting

Use a mechanical reducer only if it does not create a debris choke point.

## Failure modes

Track:

- cut edge sharpness damaging liner;
- gutter rotation;
- local flattening;
- outlet blockage;
- debris bridging;
- cracks from aged PVC;
- poor support spacing;
- standing water due insufficient slope.

## Acceptance test

Pass if:

```text
[ ] gutter remains stable during bucket test
[ ] no reverse slope or retained water
[ ] outlet does not back up before first-flush assembly
[ ] cut edges do not abrade or puncture liner
[ ] debris screen is removable
[ ] support method is understandable and repairable
```

---

# Comparative Selection Matrix

| Criterion | G-L1 Folded Liner | G-P1 Split PVC |
|---|---:|---:|
| Manufactured parts required | very low | low |
| Uses same liner as catchment | yes | no |
| Requires rigid pipe stock | no | yes |
| Debris tolerance | moderate | moderate-high |
| Repairability | high if liner available | high if PVC available |
| Puncture risk | moderate | low-moderate |
| Shape stability | low-moderate | high |
| Ease of outlet fitting | moderate | high |
| Weight | very low | low |
| Likely lowest cash cost | G-L1 | site-dependent |
| Best where rigid scrap pipe exists | no | yes |
| Best where only sheet/liner material exists | yes | no |

Do not freeze a preferred design until both variants are tested under the same simulated-rain input.

## Comparative bench protocol

Build one G-L1 and one G-P1 on otherwise equivalent pallet collectors.

Use the same:

- pallet size;
- collector angle;
- liner material;
- low-edge height;
- rainfall input;
- first-flush assembly;
- storage inlet geometry.

Measure:

```text
input water volume
captured water volume
water retained after drain-down
spill/bypass volume
peak visible water depth in gutter
cleaning time
repair time
new-material cost
salvaged-material fraction
```

Primary decision metrics:

```text
hydraulic recovery
standing-water fraction
maintenance burden
new-material cost
failure frequency
```

## Simple hydraulic stress test

Use staged bucket tests rather than only gentle flow.

Suggested sequence:

```text
T1 = low flow
T2 = moderate continuous pour
T3 = short high-rate pour
T4 = debris-loaded repeat
```

Debris challenge may use a controlled small quantity of leaves or inert surrogate material. Do not use hazardous contaminants.

Fail if:

- water routinely bypasses the gutter;
- trough/gutter collapses;
- outlet backs water into the collector;
- reverse slope appears;
- support detaches;
- standing water remains in substantial pockets;
- the transfer path loses gravity descent.

## Recommended prototype order

```text
1. Build G-L1 first where liner material is abundant.
2. Build G-P1 as the rigid comparison.
3. Run same-input bench tests.
4. Measure repairability after deliberate minor damage.
5. Select by local material availability, not aesthetics.
```

## Sketch requirements

Future sketches should show both variants as **interchangeable low-edge modules** beneath the elevated pallet collector.

Do not depict:

- painted gutters attached directly to painted pallet wood as the waterproofing strategy;
- flat gutters without fall;
- gutter outlet below storage inlet with an uphill transfer line;
- unsupported folded liner hanging freely under water load;
- split PVC with sharp cut edges contacting the liner without protection.

## Current freeze status

```text
G-L1 folded-liner trough: DESIGN FROZEN FOR BENCH BUILD
G-P1 split-PVC gutter: DESIGN FROZEN FOR COMPARATIVE BENCH BUILD
preferred gutter architecture: NOT YET FROZEN
```

The preferred field design should be selected from measured performance and locally available materials rather than assumed superiority.