# Integrated Household Module — BOM and Lifecycle Cost Model

## Purpose

This pass addresses the affordability gap identified in the UNICEF-aligned scorecard by defining a bill of materials (BOM) and lifecycle-cost model for the integrated household alternative-water module.

The model separates:

```text
LOCAL / SALVAGED STRUCTURE
CONTROLLED WATER-CONTACT MATERIALS
HEALTH-CRITICAL TREATMENT HARDWARE
SAFE STORAGE
TESTING / STATUS CONTROL
LABOR
REPLACEMENT / CONSUMABLES
```

The objective is to measure affordability rather than assume it.

This document intentionally does not freeze a single market price. Prices vary sharply by country, crisis conditions, aid channel, procurement scale, and local availability. Every deployment should replace placeholder values with actual local or procurement quotes.

---

# 1. Reference integrated module

Reference household architecture:

```text
4 x 4 ft modular rain collectors x 4
        ↓
screen + first flush
        ↓
raw barrel bank
        ↓
settling / roughing
        ↓
health-critical gravity filter
        ↓
disinfection if required
        ↓
clean barrel(s)
        ↓
controlled dispensing
```

The module is multi-source: rainwater is supplemental and seasonal rather than assumed to be the sole annual source.

---

# 2. Cost categories

Use six accounting buckets.

## C1 — local structural mass

Examples:

- pallets;
- rubble;
- timber;
- wire;
- masonry;
- load spreader;
- ballast containers.

## C2 — controlled water-contact path

Examples:

- liner;
- gutter;
- screen;
- first-flush vessel;
- food-compatible hose;
- known-use barrels;
- clean fittings.

## C3 — health-critical treatment

Examples:

- ceramic/UF/GDM element;
- filter housing;
- validated disinfection component;
- treatment-specific consumables.

## C4 — monitoring / fail-visible controls

Examples:

- turbidity tube;
- conductivity meter if used;
- microbial field tests;
- status tags;
- sampling ports;
- caps/lockouts.

## C5 — labor

Examples:

- collection and sorting of local materials;
- construction;
- cleaning;
- assembly;
- training;
- routine inspection;
- filter maintenance.

## C6 — lifecycle replacement

Examples:

- liner replacement;
- valve/hose replacement;
- filter element replacement;
- disinfectant replenishment;
- damaged barrels;
- test consumables.

---

# 3. Reference BOM — four-panel household module

The following quantities are engineering placeholders for cost capture. Local field builds may vary.

| Item | Qty | Category | Preferred source | Water-contact critical? | Replacement basis |
|---|---:|---|---|---|---|
| 4 x 4 ft pallet/scrap collector frames | 4 | C1 | local/salvaged | no | condition-based |
| Screened rubble / ballast | site-specific | C1 | local | no | rarely |
| Collector liner / membrane | ~6-8 m2 total + margin | C2 | controlled procurement | yes | UV/abrasion condition |
| Gutter / edge channel | ~8-10 m total | C2 | local/controlled | yes | damage/contamination |
| Debris screen | 4 collector outlets or common inlet | C2 | controlled/local | yes | damage/clogging |
| First-flush assembly | 1 per collector or common unit | C2 | controlled/local | yes | condition-based |
| Raw barrels ~200 L | 1-2 initially | C2 | known-use local | yes | condition/history |
| Clean barrels ~200 L | 1-2 | C2 | known-use controlled | yes | condition/history |
| Barrel lids / screened vents | 1 per barrel | C2 | controlled | yes | condition-based |
| Barrel isolation valves | 1 per barrel | C2 | controlled | yes | leak/function |
| Flexible barrel branches | 1 per barrel | C2 | controlled | yes | wear/contamination |
| Removable couplings/unions | 1 per barrel | C2 | controlled | yes | wear/damage |
| Raw manifold | 1 | C2 | controlled/local | yes | condition-based |
| Clean dispensing plumbing | 1 | C2 | controlled | yes | condition-based |
| Settling vessel | 1 | C2 | known-use local | yes | condition-based |
| Roughing filter housing | 1 | C2 | local/controlled | yes | condition-based |
| Graded filter media | as design requires | C3 | characterized local | yes | cleaning/replacement |
| Health-critical gravity filter | 1 | C3 | controlled/imported | yes | product-rated life |
| Disinfection component | optional/required by source | C3 | controlled | yes | method-specific |
| Sampling ports | S2/S5/S7 minimum | C4 | controlled | yes | condition-based |
| Status tags / lockout caps | 1 set | C4 | controlled/local | no | loss/damage |
| Turbidity measurement tool | 1 | C4 | controlled | no | long-life |
| Basic pH / conductivity tools | optional | C4 | controlled | no | calibration/replacement |
| Microbial field tests | per verification schedule | C4/C6 | controlled | no | recurring |
| Load-spreader deck | 1 | C1 | local | no | structural condition |
| Overflow/drainage materials | site-specific | C1/C2 | local | no/limited | erosion/damage |

---

# 4. Local-versus-import doctrine

The preferred cost strategy is:

```text
IMPORT PRECISION
SOURCE MASS LOCALLY
```

## Prefer local/salvaged where safe

- rubble;
- pallets;
- timber;
- structural brackets;
- masonry;
- ballast;
- non-water-contact framing.

## Prefer controlled procurement

- liner/water-contact membrane;
- clean hoses and fittings;
- known-use clean-storage vessel if local provenance is uncertain;
- health-critical filter;
- disinfection products/devices;
- microbial tests;
- critical sampling components.

The imported fraction should be measured by both **cost** and **mass/volume**.

---

# 5. Cost fields to capture

For every BOM item record:

```text
QTY
UNIT COST
LOCAL TRANSPORT
IMPORT / FREIGHT COST
LABOR HOURS
EXPECTED LIFE
REPLACEMENT INTERVAL
FAILURE RATE IF KNOWN
```

Then calculate:

```text
Installed cost
= materials + transport + initial labor

Annualized replacement cost
= replacement cost / service life

Annual operating cost
= consumables + routine labor + testing
```

---

# 6. First-year cost equation

Let:

- `C_struct` = structural/local material cost;
- `C_contact` = controlled water-contact material cost;
- `C_treat` = treatment component cost;
- `C_test` = initial monitoring/testing kit;
- `C_labor0` = initial build/training labor;
- `C_transport` = procurement/logistics cost.

Then:

```text
C_year1 = C_struct + C_contact + C_treat
        + C_test + C_labor0 + C_transport
        + C_consumables_year1
        + C_maintenance_year1
```

---

# 7. Multi-year lifecycle cost

For an analysis period `N` years:

```text
C_lifecycle(N)
= C_initial
+ sum(C_replacement_y)
+ sum(C_consumables_y)
+ sum(C_maintenance_y)
+ sum(C_testing_y)
```

For simple field comparisons, discounting may be omitted if the goal is operational screening rather than formal economic evaluation.

If long-duration financial analysis is performed, state the discount rate explicitly.

---

# 8. Cost-per-litre normalization

Two denominators should be kept separate.

## Collection cost per litre

```text
C_collection/L
= collection-system lifecycle cost
  / measured collected volume
```

## Treatment cost per litre

```text
C_treatment/L
= treatment-system lifecycle cost
  / measured treated volume
```

## Integrated cost per litre

```text
C_integrated/L
= total system lifecycle cost
  / verified usable water delivered
```

Do not divide by theoretical rainfall yield or manufacturer-rated throughput when actual field output is available.

---

# 9. Throughput reference

The UNICEF emergency HWTS design benchmark used elsewhere in this repo corresponds approximately to:

```text
5 people
x 2.5 L/person/day
= 12.5 L/day
≈ 4,560 L/year
```

Therefore the treatment lane should be modeled at multiple annual throughputs:

```text
LOW:      2,000 L/year
TARGET:   4,560 L/year
HIGH:     7,500 L/year
```

This captures intermittent use, benchmark household use, and modest margin.

---

# 10. Illustrative cost scenarios

Use three procurement scenarios rather than one false-precision estimate.

## S1 — high local reuse

Assumptions:

- pallets, rubble, framing, and some barrels locally available;
- only liner, fittings, filter, status hardware, and tests are externally procured;
- local labor/community assembly available.

Expected behavior:

```text
lowest capital cost
highest dependence on material screening / QA
```

## S2 — controlled humanitarian kit

Assumptions:

- collector structure still local;
- liner, barrels, fittings, filter, and monitoring components controlled/procured;
- standardized assembly kit.

Expected behavior:

```text
higher capital cost
lower contamination uncertainty
better replicability
```

## S3 — fully standardized module

Assumptions:

- most structural and water-contact components procured as a kit;
- limited salvage dependence.

Expected behavior:

```text
highest capital/logistics burden
highest repeatability
```

---

# 11. Cost ranges should be field-entered

For every line item use:

```text
LOW
BASE
HIGH
```

Example table structure:

| Item | Qty | Low | Base | High | Source/date |
|---|---:|---:|---:|---:|---|
| Controlled liner | | | | | |
| Known-use barrel | | | | | |
| Valve/fitting set | | | | | |
| Health-critical filter | | | | | |
| Test kit | | | | | |

Do not reuse stale procurement data without a date/source.

---

# 12. Labor model

Labor should not be treated as free merely because community members perform it.

Track:

## Build labor

- rubble screening;
- pad construction;
- collector framing;
- liner installation;
- gutter/first flush;
- barrel plumbing;
- filter installation;
- labeling/training.

## Routine labor

- collector cleaning;
- first-flush reset;
- filter inspection;
- storage cleaning;
- testing;
- documentation.

Normalize as:

```text
labor-hours / 1,000 L delivered
```

and:

```text
maintenance-hours / household-month
```

---

# 13. Replacement model

Each component should be assigned one of three replacement classes.

## R-A — condition-based structural

Examples:

- pallet/frame;
- rubble pad;
- load spreader.

Replace when damaged or unsafe.

## R-B — scheduled / wear component

Examples:

- liner;
- hose;
- valve;
- screen;
- seals.

Replace on defined inspection/wear criteria.

## R-C — health-critical rated life

Examples:

- ceramic element;
- membrane;
- disinfection cartridge/device consumable.

Use exact validated product life or measured field life.

---

# 14. Hidden-cost checklist

Include costs often omitted from prototype BOMs:

- transport from warehouse/port;
- storage losses/theft/damage;
- cleaning/sanitizing vessels;
- rejected salvage;
- replacement seals/fittings;
- test consumables;
- training time;
- water lost during first flush;
- water lost during filter cleaning/backwash;
- downtime during repair;
- disposal of exhausted filters;
- failed prototypes.

---

# 15. Affordability metrics

Track at least:

```text
$ / household installed
$ / litre delivered
$ / 1,000 L delivered
$ / household-year
imported $ / household
imported kg / household
labor-hours / household install
maintenance-hours / household-month
```

For humanitarian logistics also track:

```text
packed volume / household
transport mass / household
number of specialized parts
```

---

# 16. Value of modularity

A modular design should permit staged affordability.

## Entry module

```text
1 collector
+ 1 raw barrel
+ bounded-use output
```

## Intermediate module

```text
4 collectors
+ raw barrel bank
+ pretreatment
```

## Full treatment module

```text
4 collectors
+ raw bank
+ controlled treatment
+ clean bank
+ verification kit
```

This allows cost to scale with need and available resources rather than requiring the entire system at once.

---

# 17. Cost-of-failure metric

A cheap system that silently fails can be more expensive in public-health terms than a higher-cost controlled system.

Therefore include a qualitative failure-cost rating:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Examples:

- broken pallet frame: MODERATE;
- torn collector liner: HIGH for drinking pathway;
- failed health-critical filter without warning: CRITICAL;
- missing status tag: HIGH because classification becomes uncertain.

---

# 18. Benchmark comparison

The integrated module should eventually be compared with:

- repaired municipal connection;
- delivered/trucked water;
- bottled water;
- standalone household filter;
- commercial rainwater kit;
- desalinated-water delivery;
- community-scale treatment node.

Comparison dimensions:

```text
capital cost
operating cost
litres delivered
reliability
water quality
labor burden
seasonality
repairability
logistics burden
```

---

# 19. Field cost worksheet

```text
SYSTEM ID: __________________
LOCATION: ___________________
DATE: _______________________

C1 LOCAL STRUCTURE           ______
C2 WATER-CONTACT MATERIALS   ______
C3 TREATMENT                 ______
C4 TEST / STATUS             ______
C5 INITIAL LABOR             ______
C6 TRANSPORT                 ______

INITIAL COST                 ______

ANNUAL CONSUMABLES           ______
ANNUAL TESTING               ______
ANNUAL MAINTENANCE LABOR     ______
ANNUAL REPLACEMENT           ______

MEASURED LITRES/YEAR         ______

FIRST-YEAR $/L               ______
MULTI-YEAR $/L               ______

IMPORTED MASS                ______ kg
LOCAL MASS                   ______ kg
BUILD LABOR                  ______ hr
MAINTENANCE                  ______ hr/month
```

---

# 20. Pre-bench BOM freeze

Before integrated bench assembly, freeze actual make/model/material for:

```text
1. collector liner
2. first-flush components
3. raw barrel(s)
4. clean barrel(s)
5. hose / plumbing materials
6. valves / unions
7. health-critical filter
8. disinfection method if used
9. sampling ports
10. status/lockout hardware
```

Structural salvage can remain site-dependent if it does not enter the controlled water-contact path.

---

# 21. Current affordability status

The architecture is **cost-structured but not yet cost-validated**.

Known advantages:

- most structural mass can be local;
- no grid-power requirement for the primary passive lane;
- modular scaling;
- low mechanical complexity;
- health-critical precision can be concentrated into a small imported component.

Unresolved affordability questions:

1. actual local cost/provenance of known-use barrels;
2. exact filter product cost and rated life;
3. controlled liner cost per square metre;
4. recurring microbial-test cost;
5. labor burden per household;
6. transport cost under contested logistics;
7. loss/replacement rates in field use.

---

# 22. Design decision

The cost model now freezes one economic doctrine:

```text
DO NOT OPTIMIZE FOR LOW PURCHASE PRICE ALONE.

OPTIMIZE FOR:
COST
+ VERIFIED LITRES
+ REPAIRABILITY
+ FAILURE VISIBILITY
+ LOW RECURRING DEPENDENCE
```

This better reflects WHO/UNICEF emergency WASH objectives than a simple BOM total.

---

# 23. Next pass

Proceed to the **durability-cycle protocol** for the integrated module.

The protocol should repeatedly exercise:

- collector setup/stow;
- simulated rainfall;
- first-flush reset;
- barrel fill/drain;
- manifold isolation;
- filter operation/maintenance;
- liner inspection/repair;
- status lockout/recommissioning;
- rubble-pad settlement checks.

The goal is to convert the current analytical durability score into measured evidence.
