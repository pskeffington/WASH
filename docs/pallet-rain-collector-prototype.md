# Pallet Rain Collector Prototype

## Purpose

This prototype converts a standard wooden pallet into a small freestanding rainwater catchment system for low-resource settings where barrels or cisterns may be available but roof repair, gutter replacement, or structural modifications are not affordable.

The system is intentionally modular, resident-buildable, gravity-fed, and compatible with salvaged structural materials. Collected water is **non-potable by default** unless the entire contact path, treatment train, and resulting water quality are independently validated.

## Core architecture

```text
sealed pallet catchment
        -> low-edge gutter
        -> removable debris screen
        -> first-flush diverter
        -> barrel / cistern inlet
        -> storage
        -> overflow to safe drainage
```

A single 4 ft x 4 ft pallet provides approximately 16 ft2 of catchment area. One inch of rain over that surface corresponds to about 10 gallons before system losses and roughly 8 gallons at an illustrative 80% recovery efficiency.

## Pallet structure

### Recommended geometry

- standard pallet or equivalent wood frame;
- approximately 4 ft x 4 ft collector surface;
- 10-20 degree operating slope;
- free-standing rear support or A-frame brace;
- lower edge kept sufficiently high to permit gravity drainage into the gutter and storage inlet.

The wood should primarily provide structure. A separate waterproof skin should provide the water-contact surface.

### Catchment skin

Candidate prototype surfaces include:

- EPDM or pond-liner membrane;
- heavy polyethylene sheet;
- known-material roofing membrane;
- other intact waterproof liner appropriate to the intended use.

Unknown paints, treated wood, old roofing coatings, or chemically contaminated sheet material should not be assumed suitable for drinking-water contact.

The liner should extend beyond the wood edge, be mechanically secured with washers/battens rather than relying only on staples, and drain continuously toward the gutter without low pockets.

## Corrected pipe logic

The hydraulic path should preserve gravity flow and avoid unnecessary traps or undersized transitions.

```text
CATCHMENT
   ↓
GUTTER
   ↓
COARSE SCREEN
   ↓
VERTICAL DROP / TEE
   ├── first-flush standpipe
   └── overflow path to barrel after diverter fills
                ↓
          BARREL INLET
                ↓
             STORAGE
                ↓
            OVERFLOW
```

### Gutter

For one pallet:

- approximately 4 ft long;
- split PVC, bent metal, or conventional gutter section;
- minimum slope around 1/8 in per ft toward outlet;
- avoid flat sections that retain sediment or water.

A 2-3 in nominal gutter is generally adequate for a single pallet prototype, but the actual capacity must be checked where very intense rainfall is expected.

### Downpipe

A 2 in nominal downpipe is a useful low-cost starting point because it provides much greater flow capacity and debris tolerance than small hose.

The path from gutter to diverter should be:

```text
short
smooth
continuously descending
accessible for cleaning
```

Avoid unnecessary elbows and horizontal dead legs.

## First-flush fill logic

The first-flush diverter should be treated as a storage volume that captures the first dirty runoff from the catchment surface.

A simple configuration uses a vertical capped standpipe attached below a tee.

```text
                 to barrel
                    →
              ┌─────┴─────┐
roof/pallet → │     T     │
              └─────┬─────┘
                    │
                    │ first-flush standpipe
                    │
                    │
                    ● slow drain / cleanout
```

### Dry start

Before rainfall:

- standpipe is empty;
- barrel path is open above the tee;
- slow drain at the bottom is closed enough that the first runoff accumulates faster than it escapes.

### Initial rainfall

The first contaminated runoff enters the standpipe and fills it from the bottom upward.

```text
water level ↑
```

This initial volume captures dust, pollen, debris, animal waste, atmospheric deposition, and other material accumulated on the collector between rains.

### Diverter full

Once the standpipe reaches its design volume, additional runoff rises to the tee elevation and is routed toward the barrel.

The hydraulic logic therefore becomes:

```text
first water → fill diverter
later water → barrel
```

No pump or active valve is required in the simplest design.

### Reset after rainfall

A small controlled drain at the bottom should empty the first-flush standpipe slowly after rainfall stops.

The reset time should be long enough that the diverter does not empty significantly during the storm but short enough that it is ready before the next event.

This is preferable to a permanently sealed pipe that must be manually emptied after every rainfall.

A removable bottom cap or cleanout should still be provided for sediment removal.

## First-flush volume

For a 16 ft2 pallet collector, the first-flush volume can be much smaller than the values used for full residential roofs.

Initial prototype values should be treated experimentally. A practical small test range is approximately:

```text
0.25 gal
0.5 gal
1.0 gal
```

The preferred setting depends on:

- days since previous rain;
- local dust and pollen;
- bird/animal exposure;
- collector material;
- tree cover;
- intended end use.

The repository should compare first-flush volume against turbidity and other water-quality observations rather than assume one universal setting.

## First-flush standpipe sizing

For cylindrical pipe:

```text
V = pi * r^2 * L
```

Approximate useful capacities:

- 2 in pipe contains about 0.16 gal per foot;
- 3 in pipe contains about 0.37 gal per foot;
- 4 in pipe contains about 0.65 gal per foot.

This means a compact diverter can be made with, for example:

```text
3 in x ~16 in ≈ 0.5 gal
4 in x ~18 in ≈ 1.0 gal
```

Actual inside diameter should be used for final calculations.

## Barrel inlet logic

The barrel inlet should remain above the maximum storage waterline and should preferably include:

- removable insect/debris screen;
- sealed lid interface;
- air vent protected by mesh;
- sufficient inlet diameter to avoid backing water into the diverter.

The inlet should not be placed through an open barrel lid where mosquitoes and debris can enter freely.

## Overflow logic

The barrel overflow is part of the hydraulic system, not an optional accessory.

Recommended overflow:

- approximately 1.5-2 in diameter where practical;
- positioned near the maximum desired storage elevation;
- discharge routed away from foundations and walking surfaces;
- terminate into a stable rock apron, vegetated swale, rain garden, or other safe drainage path where appropriate.

Overflow capacity should be at least comparable to inlet capacity so that a full barrel cannot cause water to back up through the catchment plumbing.

## Scaling logic

The smallest useful architecture is:

```text
1 pallet -> 1 barrel
```

Expansion can occur through either:

```text
multiple pallets -> common gutter -> one larger cistern
```

or:

```text
1 pallet -> 1 barrel
1 pallet -> 1 barrel
1 pallet -> 1 barrel
```

Separate modules are often easier to build and repair in low-resource settings.

### Approximate rainfall production

For a 4 ft x 4 ft collector:

```text
16 ft2 x 0.623 gal/ft2/in = ~10 gal/in theoretical
```

At an illustrative 80% recovery:

```text
~8 gal per inch of rainfall
```

Four pallet modules would therefore provide approximately 64 ft2 of catchment and about 32 gallons per inch at the same assumed recovery.

## Materials hierarchy

### Suitable structural reuse candidates

- sound pallets;
- scrap dimensional lumber;
- brackets;
- screws/bolts;
- masonry blocks or stones for stable footing.

### Water-contact caution

Avoid assuming that aged pallet wood, old paint, pressure-treated lumber, unknown membranes, or previously contaminated storage containers are potable-safe.

For experimental non-potable systems, structural reuse is encouraged while the water-contact layer remains separately controlled.

## Field measurements

Each prototype should record:

```text
catchment area
rainfall depth
first-flush volume
barrel volume before storm
barrel volume after storm
overflow occurrence
visible debris/turbidity
leakage observations
```

Calculate:

```text
collection efficiency = measured captured volume / theoretical rainfall volume
```

Theoretical rainfall volume is:

```text
V_theoretical = area * rainfall depth
```

using consistent unit conversion.

## Prototype gates

### P1 - structural

Pallet remains stable under rain and wind loading and drains without pooling.

### P2 - hydraulic

Gutter, screen, diverter, barrel inlet, and overflow pass a heavy simulated-rain test without backing up.

### P3 - first-flush

First runoff is measurably separated and diverter reliably resets after rainfall.

### P4 - collection efficiency

Measure actual versus theoretical captured rainfall over multiple storms.

### P5 - maintenance

Resident can clean screen, inspect liner, drain sediment, and service diverter without specialized tools.

### P6 - water-quality/use boundary

Collected water remains experimental/non-potable unless a separate validated water-contact, treatment, and testing pathway is established.

## Design principle

The prototype is intended to convert a common waste or low-value object into useful catchment area without requiring roof repairs or permanent alterations to an aging home:

```text
abundant wood structure
+ replaceable waterproof skin
+ simple gravity plumbing
+ existing storage
= modular micro-catchment
```
