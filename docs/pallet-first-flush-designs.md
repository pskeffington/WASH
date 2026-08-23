# Pallet-Scale First-Flush Designs

## Purpose

This document freezes two first-flush prototype families for the elevated pallet rain collector:

- **FF-M1** — simple manual-cleanout standpipe;
- **FF-F1** — floating-ball standpipe that reduces remixing after the first-flush chamber fills.

Both are gravity-fed and sized for the small catchment area of a single pallet module. Neither design creates a potable-water claim. Collected water remains **experimental and non-potable by default** unless the complete water-contact, treatment, testing, and use-classification pathway is independently validated.

## System position

```text
ELEVATED PALLET CATCHMENT
        ↓
GUTTER
        ↓
COARSE SCREEN
        ↓
TRANSFER TEE
        ├── FIRST-FLUSH CHAMBER
        ↓
GRAVITY FLOW TO BARREL / CISTERN
```

The transfer tee must remain above the storage inlet. The first-flush chamber may extend downward below the tee, but the route from the tee to storage must remain continuously descending.

## Why the volume is small

A nominal 48 x 40 in pallet at about 15 degrees has a horizontal projected area of about 12.9 ft2. One inch of rainfall represents about 8 gallons of theoretical incident water on that area.

A full residential-roof first-flush rule should therefore not be copied directly onto one pallet. The initial test matrix remains:

```text
0.25 gal
0.50 gal
1.00 gal
```

These values are experimental settings. The preferred volume must be selected from observed runoff quality, days since prior rain, dust, animal exposure, vegetation, and intended use.

## Pipe-volume calculation

For a cylindrical chamber:

```text
V = pi * (ID/2)^2 * L
```

Use **actual inside diameter**, not nominal pipe size, for final dimensions.

Approximate Schedule 40 reference values are:

```text
2 in nominal PVC: ~0.17 gal/ft
3 in nominal PVC: ~0.38 gal/ft
4 in nominal PVC: ~0.66 gal/ft
```

Approximate chamber lengths:

| Target volume | 2 in nominal | 3 in nominal | 4 in nominal |
|---|---:|---:|---:|
| 0.25 gal | ~17 in | ~8 in | ~5 in |
| 0.50 gal | ~35 in | ~16 in | ~9 in |
| 1.00 gal | ~69 in | ~31 in | ~18 in |

These values are design approximations; fittings and end geometry can change usable volume.

# FF-M1 — Manual-Cleanout Standpipe

## Objective

FF-M1 is the minimum-parts reference design. It intentionally favors simplicity, visibility, and repairability over automation.

## Architecture

```text
FROM SCREENED GUTTER
        ↓
      TEE ─────────────→ TO STORAGE
        │
        │
        │ FIRST-FLUSH STANDPIPE
        │
        │
      CLEANOUT CAP / VALVE
```

At the start of rainfall, runoff falls into the empty standpipe. After the chamber fills to the tee elevation, subsequent runoff proceeds toward storage.

## Reference configuration

For the first build:

```text
chamber: 3 in nominal PVC
nominal test volume: 0.5 gal
straight chamber length: ~16 in starting value
bottom: removable cleanout cap or valve
upper connection: sanitary tee / wye / equivalent low-loss branch
```

The actual filled volume should be measured with a graduated container after assembly rather than assumed from nominal dimensions.

## Reset options

### FF-M1A — manual reset

The chamber remains closed during rainfall. After the event, the operator drains and rinses it.

Advantages:

- fewest parts;
- easiest function to understand;
- no small bleed hole to clog;
- first-flush volume remains fixed during the storm.

Disadvantages:

- depends on user reset;
- forgotten reset means the next storm may bypass effective first flush.

### FF-M1B — controlled slow drain

A very small drain path empties the chamber after rain.

This variant should not be treated as automatically superior. The bleed rate must be tested so that the chamber does not substantially empty while rainfall is still occurring.

Required test:

```text
fill chamber completely
measure time to drain
repeat after adding representative fine debris
```

If the drain clogs easily or empties too rapidly, revert to FF-M1A.

## FF-M1 acceptance gate

```text
[ ] chamber is empty before test
[ ] initial runoff fills chamber before substantial storage inflow
[ ] no uncontrolled leakage from cleanout
[ ] chamber volume is measured, not nominally assumed
[ ] chamber can be opened and cleaned without dismantling collector
[ ] reset method is obvious to user
[ ] tee-to-storage line remains continuously descending
```

# FF-F1 — Floating-Ball Standpipe

## Objective

FF-F1 adds a floating ball inside the first-flush chamber. As the chamber fills, the ball rises toward a seat near the upper chamber, reducing exchange between retained dirty water and later runoff.

The ball is **not assumed to create a perfect hydraulic seal**. Its value must be demonstrated experimentally.

## Architecture

```text
FROM SCREENED GUTTER
        ↓
      TEE ─────────────→ TO STORAGE
        │
        │  upper seat / restriction
        │       ○  ← floating ball when full
        │
        │ FIRST-FLUSH CHAMBER
        │
        ○  ← ball when empty
        │
      CLEANOUT / RESET
```

## Ball-selection requirements

The ball must:

- float reliably in water;
- move freely through the chamber;
- be too large to enter downstream plumbing;
- not jam against pipe irregularities;
- be removable for cleaning;
- be of known material if water quality is being characterized.

A commercial first-flush ball or other purpose-appropriate float is preferable to an unknown salvaged object in the water-contact path.

## Seat geometry

The seat should restrict upward ball travel without creating an unacceptable bottleneck for storm flow.

Prototype checks:

```text
ball rises consistently
ball centers sufficiently to reduce remixing
runoff can still route toward storage after chamber fills
no ball entrapment blocks the entire collector
assembly can be opened for cleaning
```

Because locally sourced fittings vary, FF-F1 does not freeze one ball diameter or seat diameter before bench testing.

## Reference chamber

Use the same baseline chamber as FF-M1 for direct comparison:

```text
3 in nominal PVC
~0.5 gal measured volume
~16 in straight chamber starting length
```

This isolates the effect of the floating-ball mechanism rather than changing chamber volume at the same time.

## FF-F1 acceptance gate

```text
[ ] ball begins at chamber bottom
[ ] ball rises freely through repeated fill cycles
[ ] ball does not block the storage branch
[ ] later runoff reaches storage after chamber fills
[ ] retained first-flush water shows less visible remixing than FF-M1, if measurable
[ ] cleanout remains accessible
[ ] ball and chamber can be inspected without specialized tools
[ ] failure is visible and does not silently stop all collection
```

# Comparative bench protocol

Build FF-M1 and FF-F1 with the same approximate chamber volume.

Test at minimum:

```text
0.25 gal chamber setting
0.50 gal chamber setting
1.00 gal chamber setting
```

Where practical, expose both to the same simulated runoff.

Record:

```text
inflow rate
first-flush chamber measured volume
time until storage flow begins
volume reaching storage before chamber is nominally full
visible remixing / turbulence
leakage
reset time
clogging
cleaning time
operator errors
```

## Contamination-separation test

A safe visible tracer may be used during non-consumptive bench testing to compare separation performance.

Example logic:

```text
initial tracer-bearing runoff
        ↓
first-flush chamber
        ↓
subsequent clear simulated rainfall
```

Compare tracer carryover into the storage-side collection vessel between FF-M1 and FF-F1.

Any tracer experiment must remain separate from water intended for human or animal use.

# Hydraulic placement rules

The first-flush design must not violate the elevated pallet geometry.

Required vertical relationship:

```text
GUTTER OUTLET
      >
TRANSFER TEE
      >
STORAGE INLET
```

The standpipe extends downward from the tee and therefore does not need to remain above the storage inlet at its bottom.

Do not route water from the filled standpipe back upward to the barrel. The storage branch leaves at the tee and descends independently.

# Maintenance doctrine

The preferred design is the one residents can actually keep working.

Inspection after storms should include:

- screen condition;
- sediment in chamber;
- cleanout leakage;
- insect entry;
- ball movement for FF-F1;
- drain blockage if an automatic bleed is used;
- obvious cracks or UV damage;
- evidence that the chamber was reset before the next storm.

# Selection gate

## Prefer FF-M1 when

- fittings are scarce;
- users can reliably perform manual reset;
- visible simplicity is more valuable than partial automation;
- floating-ball components cannot be sourced consistently.

## Prefer FF-F1 when

- a reliable float and seat can be sourced;
- bench testing shows meaningful reduction in remixing;
- the mechanism remains easily serviceable;
- failure does not block the entire rainwater pathway.

## Do not advance either design when

- the chamber cannot be cleaned;
- storage receives substantial runoff before the intended first-flush volume is captured;
- reset is unreliable;
- the design creates reverse slope or hydraulic backup;
- locally available materials introduce unacceptable contamination concerns.

# Freeze status

```text
FF-M1: DESIGN FROZEN FOR BENCH BUILD
FF-F1: DESIGN FROZEN FOR COMPARATIVE BENCH BUILD
FIRST-FLUSH VOLUME: NOT YET FROZEN
```

The next evidence gate is empirical comparison of 0.25, 0.50, and 1.00 gallon settings under repeatable simulated-rain conditions.