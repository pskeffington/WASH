# Pallet Rain Collector BOM and Lifecycle Cost Model

## Purpose

This document establishes the bill-of-materials and lifecycle-cost framework for one-, two-, and four-pallet rainwater collector systems.

The objective is not to claim one universal price. Local salvage availability, container availability, labor, and retail prices vary substantially. The model therefore separates:

```text
SALVAGED / EXISTING MATERIAL VALUE
+
NEW CASH PURCHASES
+
LABOR
+
REPLACEMENT / MAINTENANCE COST
```

The primary low-income design target is to minimize **new cash expenditure** while keeping the water-contact path controlled and the structure safe.

Collected water remains experimental and non-potable by default unless the water-contact, treatment, testing, and use-classification pathway is separately validated.

## Cost doctrine

```text
SALVAGE STRUCTURE WHERE SAFE
        ↓
BUY ONLY HEALTH / HYDRAULIC CRITICAL PARTS
        ↓
KEEP PARTS MODULAR
        ↓
REPLACE THE FAILED LAYER, NOT THE WHOLE SYSTEM
```

Do not treat painting, staining, spraying, or coating salvaged pallet wood as a required cost item or a normal preservation strategy.

## Reference price inputs

Reference U.S. retail checks on 2026-08-23 were used only to establish an order-of-magnitude benchmark for manufactured inputs. These prices are not procurement requirements and should be replaced with local prices before field budgeting.

Reference inputs:

```text
6 mil polyethylene sheeting, 10 ft x 25 ft: about $42.98 / 250 ft2
3 in PVC pipe, 10 ft: about $18.24
2 in PVC pipe, 10 ft: about $15.81
```

These references imply approximate material-allocation values of:

```text
6 mil sheet: ~$0.17/ft2
3 in PVC: ~$1.82/ft
2 in PVC: ~$1.58/ft
```

The reference prices are retail benchmarks, not evidence that those exact products are validated potable-water contact materials.

## One-pallet reference allocation

Nominal collector:

```text
pallet: 48 x 40 in
surface: 13.33 ft2
liner cut allowance: ~20-25 ft2 including edge folds / fastening margin
collector angle: ~15 deg
```

### Structural items

| Item | Quantity | Preferred source | New-cash target |
|---|---:|---|---:|
| pallet | 1 | salvaged | $0 |
| support legs / braces | as required | salvaged wood | $0 |
| footing / ballast | as required | local blocks / stone / rubble | $0 |
| structural fasteners | small lot | reuse where sound / buy | field price |

### Controlled water-path items

| Item | Approx. allocation | Reference cost logic |
|---|---:|---:|
| replaceable liner | 20-25 ft2 | ~$3.44-$4.30 at reference sheet price |
| gutter, G-L1 | same liner | incremental cost near zero if cut allowance sufficient |
| gutter, G-P1 | ~4 ft of 3 in PVC | ~$7.30 reference allocation |
| first-flush body | ~1.3 ft of 3 in PVC for ~0.5 gal test chamber | ~$2.40 reference allocation |
| transfer line | ~3 ft of 2 in PVC | ~$4.75 reference allocation |
| screen | small removable section | field price |
| tees / caps / outlet fittings | small set | field price |
| barrel inlet interface | 1 | field price |
| overflow connection | 1 | field price |

The G-L1 folded-liner variant can reduce the rigid gutter material requirement substantially.

## Baseline cash-cost bands

These are **planning bands**, not quotes.

### Scenario A - maximum salvage / existing storage

Assumptions:

- pallet free;
- supports and ballast salvaged;
- existing suitable barrel/cistern available;
- G-L1 folded-liner gutter;
- only liner, basic pipe/fittings, screen, and fasteners purchased.

Initial target:

```text
~$20-$40 new cash / module
```

This is the primary affordability architecture to test.

### Scenario B - moderate salvage

Assumptions:

- pallet free;
- some support lumber / fasteners purchased;
- G-P1 split-PVC gutter;
- first-flush and transfer plumbing purchased;
- existing barrel/cistern available.

Initial target:

```text
~$35-$70 new cash / module
```

### Scenario C - storage must also be purchased

Do not freeze a universal price because barrel/cistern pricing and availability vary widely. Track storage separately:

```text
collector cash cost
+
storage acquisition cost
```

This separation prevents an expensive new storage vessel from making the catchment architecture appear more expensive than it is.

## One-, two-, and four-pallet BOM scaling

### P1 - one pallet

```text
1 pallet
1 liner
1 gutter
1 first-flush unit
1 transfer line
1 barrel / cistern interface
1 overflow
```

Projected catchment at 15 deg:

```text
~12.88 ft2 horizontal area
~8.0 gal theoretical per inch rain
~6.4 gal/in at illustrative 80% recovery
```

### P2 - two independent modules

Preferred first scale-up:

```text
Pallet A → FF-A → Barrel A
Pallet B → FF-B → Barrel B
```

BOM roughly doubles, but shared purchases can reduce unit cost:

- one liner roll can supply multiple modules;
- one 10-ft PVC length can be divided among multiple first-flush bodies;
- fasteners / screen can be purchased in bulk;
- tools are reused.

Projected catchment:

```text
~25.8 ft2 horizontal area
~16.0 gal theoretical per inch
~12.8 gal/in at illustrative 80% recovery
```

### P4 - four independent modules

Reference resilience array:

```text
4 pallet collectors
4 first-flush units
2-4 storage vessels depending field configuration
independent overflow paths preferred initially
```

Projected catchment:

```text
~51.5 ft2 horizontal area
~32.1 gal theoretical per inch
~25.6 gal/in at illustrative 80% recovery
```

At this scale, purchased sheet and pipe should be costed from **whole-stock utilization**, not simply four times the one-module retail allocation.

## Whole-stock utilization

A key low-income metric is waste from purchased stock.

Example: 10 x 25 ft liner sheet:

```text
250 ft2 purchased
```

If each pallet module consumes approximately 25 ft2 including folds and fastening margin:

```text
~10 nominal module cuts per sheet before cutting losses
```

Actual cutting layout should be field-tested because pallet dimensions vary.

Similarly, 10-ft PVC stock should be cut to minimize offcuts.

Record:

```text
purchased length
installed length
usable offcut length
waste length
```

## Salvage fraction

Track by component count and estimated replacement value.

### Simple component-count salvage fraction

```text
salvage_fraction_count = salvaged components / total components
```

### Better cost-weighted salvage fraction

```text
salvage_fraction_value = estimated value of salvaged inputs /
                         estimated value of all installed inputs
```

The cost-weighted value better reflects systems where a free pallet is large but inexpensive fittings dominate cash expenditure.

## Lifecycle cost

Initial build cost alone is insufficient.

Use:

```text
LCC_N = C_initial
      + sum(C_repair_year_i)
      + sum(C_replacement_year_i)
      + C_consumables
```

for an N-year observation period.

Do not assign an arbitrary long service life before field durability data exist.

For early prototypes, track actual cost cumulatively at:

```text
30 days
90 days
180 days
365 days
```

## Expected replacement classes

### Class R1 - frequent inspection / low-cost repair

- screen cleaning;
- loose fasteners;
- minor liner tension adjustment;
- first-flush cleaning;
- gutter realignment.

### Class R2 - replaceable wear layer

- liner;
- screen;
- flexible hose;
- small seals / gaskets;
- damaged outlet fitting.

### Class R3 - structural repair

- pallet board;
- brace;
- foot / support block;
- anchor.

### Class R4 - major component replacement

- barrel / cistern;
- entire pallet frame;
- full first-flush assembly.

Design preference:

```text
R1 / R2 failure
```

is preferable to:

```text
R4 failure
```

because wear should be concentrated in cheap replaceable components.

## Labor tracking

Record separately:

```text
salvage collection time
inspection time
repair time
initial build time
installation time
storm maintenance time
scheduled cleaning time
failure repair time
```

Do not assume volunteer or household labor is economically free. Report both:

```text
cash cost
```

and:

```text
labor-hours
```

so systems can be compared honestly across settings.

## Performance-normalized cost metrics

### Catchment capital intensity

```text
$/ft2 projected catchment
```

### Storage connection cost

```text
new cash collector cost / gallons of existing storage connected
```

This metric is only meaningful when storage already exists.

### Rain-event productivity

```text
liters collected per inch rain / dollar new cash
```

### Measured water productivity

After field data exist:

```text
measured liters collected / dollar new cash
```

### Lifecycle productivity

```text
cumulative liters collected / cumulative lifecycle dollars
```

### Labor productivity

```text
cumulative liters collected / cumulative labor-hour
```

## Illustrative affordability calculation

If a one-pallet module costs $30 in new cash and later measures 6.0 gal/in actual recovery:

```text
6.0 gal = 22.7 L per inch rain
```

Then event-normalized productivity is:

```text
22.7 L / $30 ≈ 0.76 L per dollar per inch of rain
```

This is not annual productivity. Annual value depends on rainfall distribution, storage capacity, overflow losses, withdrawals, maintenance, and downtime.

## Storage utilization gate

A collector should not be judged solely on maximum rainfall yield if connected storage is too small.

Track:

```text
potential capture
actual stored volume
overflow loss
resident withdrawal
unused storage capacity
```

Define:

```text
storage_utilization = actual stored volume / available storage capacity
```

and:

```text
overflow_fraction = overflow loss / theoretical collector yield
```

This allows the project to determine when adding another pallet is less useful than adding another barrel.

## Cost decision gate

### ACCEPT architecture for continued field work when

- new cash cost is documented;
- salvage assumptions are explicit;
- labor-hours are recorded;
- replaceable wear layers are identifiable;
- storage acquisition is separated from collector cost;
- no paint/coating expenditure is treated as necessary to make aged pallet wood acceptable;
- measured water yield can eventually be normalized against cost.

### REVISE when

- fittings dominate total cost unnecessarily;
- purchased stock creates high unusable waste;
- maintenance requires specialized consumables;
- storage cost overwhelms collector cost and an existing-storage pathway has not been evaluated;
- a small component failure requires replacement of the whole module.

## Field BOM record

```text
build ID:
date:
location:
pallet source:
storage already available: yes/no

component | qty | salvaged/new | cash cost | estimated replacement value | expected wear class

liner area purchased:
liner area installed:
pipe length purchased:
pipe length installed:
usable offcuts retained:

initial cash cost:
initial labor-hours:
30-day repair cost:
90-day repair cost:
180-day repair cost:
365-day repair cost:
cumulative water collected:
```

## Current cost target

The current research target for a **one-pallet collector excluding storage and treatment** is:

```text
maximum-salvage target: <= $40 new cash
stretch target: <= $25 new cash
```

These are internal design targets, not claims that every location can achieve them.

The two- and four-pallet arrays should demonstrate declining purchased cost per square foot through shared sheet stock, pipe stock, tools, and bulk hardware.

## Current freeze status

```text
BOM architecture: FROZEN FOR BENCH PROCUREMENT
retail reference inputs: SNAPSHOT ONLY
one-pallet <=$40 target: ACTIVE DESIGN GATE
storage cost: TRACK SEPARATELY
labor: TRACK SEPARATELY
lifecycle interval: 30 / 90 / 180 / 365 days
preferred gutter by cost: NOT YET FROZEN
```
