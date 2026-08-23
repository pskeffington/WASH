# Phased Execution Roadmap — WASH in Contested Operational Zones

## Purpose

This roadmap converts the contested-operational-zone sector into a sequence of bounded research, engineering, validation, and deployment passes.

The existing sector gates remain authoritative:

```text
COZ-0 context/access
COZ-1 immediate survival water
COZ-2 collection expansion
COZ-3 pretreatment
COZ-4 household/barrel filtration
COZ-5 disinfection
COZ-6 safe storage/distribution
COZ-7 field verification
COZ-8 continuity/redundancy
```

This document defines the work needed to mature those gates into tested prototype families.

The primary case-study environment is Gaza and surrounding regional conflict-affected zones, with transfer checks against Syria, Lebanon, Yemen, Ukraine, and other infrastructure-disrupted settings.

The sector remains actor-neutral and civilian-outcome focused.

---

# Phase 0 — Evidence baseline and operating envelope

## Objective

Establish the physical, climatic, public-health, materials, and infrastructure conditions that constrain design.

## Current status

Substantially underway.

Existing work includes:

- Gaza-centered contested-zone WASH literature review;
- rainfall/humidity quantification;
- monthly yield/storage sizing;
- rubble reuse framework;
- collection-to-filtration literature review;
- filtration-performance review;
- microbial/chemical-risk review;
- field QA framework.

## Passes

### P0.1 — Gaza infrastructure baseline

Map or tabulate:

- wells;
- desalination capacity;
- major reservoirs;
- pumping stations;
- distribution dependence;
- wastewater-treatment assets;
- sewage pumping;
- trucking/filling-point dependence;
- known infrastructure-damage reports.

Deliverable:

`gaza-wash-infrastructure-baseline.md`

### P0.2 — source-risk matrix

Define source classes:

- municipal/desalinated;
- protected well;
- brackish well;
- rainwater;
- surface water;
- floodwater;
- atmospheric condensate;
- trucked water;
- stored unknown-source water.

Map each to:

- microbial risk;
- salinity;
- nitrate;
- metals;
- hydrocarbons/industrial contamination;
- required testing;
- likely treatment burden.

Deliverable:

`gaza-source-risk-matrix.md`

### P0.3 — material availability index

Classify locally likely materials:

- rubble;
- pallet/scrap wood;
- sheet metal;
- wire/fencing;
- tarps/liners;
- barrels;
- IBCs;
- PVC/hose;
- sand;
- gravel;
- ceramic capacity;
- activated carbon;
- membrane elements;
- chlorine/disinfectants;
- solar panels/batteries/pumps.

For each:

```text
abundance
water-contact suitability
structural suitability
contamination risk
repairability
import dependence
```

Gate to advance:

A credible evidence-backed design envelope exists for at least one northern, central, and southern Gaza operating condition.

---

# Phase 1 — Rapid collection architecture

## Objective

Produce low-import, rapidly repairable collection systems that remain useful when roofs, gutters, power, and municipal pressure are unavailable.

## Prototype family

```text
RC-P0  tarp micro-catchment
RC-P1  single pallet collector
RC-P2  four-pallet household array
RC-P3  8-16 panel community array
RC-R1  rubble-integrated collector
```

## Passes

### P1.1 — standard collector interfaces

Freeze common interfaces for:

- catchment-to-gutter;
- gutter-to-screen;
- screen-to-first-flush;
- first-flush-to-storage;
- overflow;
- sampling point.

Goal:

Any collector surface can feed the same downstream hardware.

### P1.2 — first-flush hydraulic correction

Finalize two explicitly different designs:

#### FF-M1 — manual/simple

- low parts count;
- positive manual dump/reset;
- no claim of automatic isolation.

#### FF-F1 — float shutoff

- chamber fills;
- float seals contaminated branch;
- later runoff goes to storage;
- more moving parts and QA burden.

Gate:

No documentation implies that a plain open tee automatically isolates contaminated first-flush water.

### P1.3 — rubble anchoring and ballast

Quantify:

- expected panel wind force;
- overturning moment;
- ballast mass;
- anchor spacing;
- gabion/rubble crate options.

Output:

one conservative prototype anchoring schedule for sheltered, moderate, and exposed conditions.

### P1.4 — coating/liner lane

Compare:

- tarp/PE sheet;
- EPDM/pond liner;
- known food-contact membrane;
- P151-type rainwater catchment coatings where available;
- generic coatings as non-potable experimental controls only.

Measure:

- runoff efficiency;
- abrasion;
- UV durability;
- cracking;
- leaching indicators;
- repair method.

Gate to advance:

At least one collector design has repeatable hydraulic performance, stable anchoring, safe overflow, inspectable wetted materials, and measured collection efficiency.

---

# Phase 2 — Storage and hydraulic resilience

## Objective

Convert episodic collection into usable reserve while preventing storage from becoming a single point of failure.

## Prototype family

```text
ST-P1  single 200-L barrel
ST-P2  isolated 2-4 barrel bank
ST-P3  500-L household reserve
ST-P4  1,000-2,000-L community modular bank
```

## Passes

### P2.1 — rubble barrel-bank stand

Calculate for 1-4 drums:

- full mass;
- bearing load;
- load-spreader area;
- overturning/tipping resistance;
- stand settlement;
- safe gravity-draw height.

### P2.2 — contamination-isolated manifold

Develop plumbing that allows:

- independent fill isolation;
- independent draw-off;
- independent draining/cleaning;
- overflow sequencing;
- no unavoidable common-bottom cross-contamination.

### P2.3 — storm storage sizing

Existing 25/50/100-mm capture models become design checks.

Add:

- storage utilization fraction;
- overflow frequency;
- first-flush loss;
- treatment loss;
- household reserve days.

### P2.4 — storage hygiene

Freeze minimum storage requirements:

- covered vessel;
- screened vent;
- controlled outlet;
- no hand-dipping;
- cleaning access;
- raw/treated labeling;
- source/date tagging.

Gate to advance:

Storage survives a modeled storm event, remains stable on rubble support, can isolate a failed vessel, and preserves source identity.

---

# Phase 3 — Pretreatment and sediment control

## Objective

Protect health-critical filters by removing debris and suspended solids using locally maintainable stages.

## Prototype family

```text
PT-P1  mesh/screen
PT-P2  settling barrel
PT-P3  rubble-protected settling bay with controlled liner
PT-P4  gravel roughing filter
```

## Passes

### P3.1 — screen hierarchy

Compare:

- coarse mesh;
- window screen;
- clean cloth;
- perforated basket;
- multilayer removable screen.

Measure:

- clogging rate;
- cleaning burden;
- head loss;
- debris capture.

### P3.2 — settling barrel hydraulics

Test:

- calm inlet;
- diffused inlet;
- outlet elevation;
- sediment depth;
- 1 h / 4 h / overnight settling.

Measure turbidity at inlet/outlet.

### P3.3 — roughing filter media

Use only known/washed gravel for treatment research.

Do not substitute unknown demolition rubble as potable-path filter media.

Measure:

- turbidity reduction;
- head loss;
- clogging;
- cleaning recovery;
- media carryover.

Gate to advance:

Pretreatment measurably lowers suspended-solids burden without becoming hydraulically unstable or unmaintainable.

---

# Phase 4 — Controlled filtration family

## Objective

Compare low-resource filtration options by performance, maintenance, local material demand, and supply-chain dependence.

## Prototype family

```text
F-P1  controlled sand/biosand
F-P2  validated ceramic element
F-P3  controlled activated-carbon stage
F-P4  commercial hollow-fiber/membrane drop-in
F-P5  hybrid filter train
```

## Passes

### P4.1 — sand grading protocol

Freeze low-cost media QA:

```text
D10
D60
UC = D60/D10
washing protocol
bed-depth record
flow record
```

### P4.2 — biosand hydraulic trials

Measure:

- initial flow;
- mature flow;
- pause period;
- turbidity;
- microbial indicators;
- cleaning burden;
- performance after disturbance.

### P4.3 — ceramic QA lane

Track:

- source/manufacturer;
- flow rate;
- visual crack inspection;
- acoustic/tap screening where appropriate;
- suspected high-flow failure;
- initial chemical leaching where locally manufactured.

### P4.4 — membrane drop-in lane

Compare commercial gravity/hollow-fiber units for:

- flow;
- cleaning/backflush burden;
- replacement life;
- imported mass;
- microbial evidence;
- compatibility with local pretreatment.

### P4.5 — carbon adsorption lane

Separate:

```text
ordinary char = experimental material
```

from:

```text
standardized activated carbon = controlled adsorbent
```

No universal contaminant-removal claim without testing.

Gate to advance:

At least one filtration chain has stable hydraulics, measurable particulate performance, documented maintenance, and an evidence-backed microbial-risk-reduction path.

---

# Phase 5 — Disinfection and health-critical barrier

## Objective

Ensure that filtration is not mistaken for complete pathogen control.

## Passes

### P5.1 — chlorine lane

Use only validated product-specific/public-health dosing protocols.

Record:

- source water turbidity;
- product concentration;
- dose protocol source;
- contact conditions;
- residual where applicable.

### P5.2 — boiling lane

Evaluate:

- fuel burden;
- batch size;
- cooling/storage contamination risk;
- practicality under scarcity.

### P5.3 — solar disinfection lane

Evaluate applicability based on:

- container availability;
- turbidity;
- solar exposure;
- batch volume;
- seasonal conditions.

### P5.4 — UV lane

Evaluate only with controlled device/dose parameters and sufficiently clear water.

Gate to advance:

The selected treatment chain has a defined, validated pathogen-control barrier appropriate to the source water and intended use.

---

# Phase 6 — Field verification and use classification

## Objective

Create a system that can detect its own failure conditions with realistic field tools.

## Passes

### P6.1 — minimum field kit

Standardize:

- clear sample bottles;
- volume vessel;
- stopwatch;
- thermometer;
- pH;
- conductivity/TDS;
- turbidity tube or meter;
- chlorine residual kit where relevant;
- microbial field test where available.

### P6.2 — sampling ports

Freeze sample points:

```text
S0 source
S1 post-first-flush
S2 post-settling
S3 post-roughing
S4 post-primary filter
S5 post-secondary filter
S6 post-disinfection
S7 post-storage
```

### P6.3 — microbial testing comparison

Compare practical field options for E. coli/coliform screening and quantify limitations versus laboratory methods.

### P6.4 — chemical escalation

Build trigger-specific chemistry panels for:

- galvanized/copper catchments;
- burned areas;
- industrial sites;
- unknown barrels;
- saline wells;
- rubble-contact incidents.

### P6.5 — use classification

Every output must resolve to:

```text
REJECT
NON-POTABLE / BOUNDED USE
TREATMENT REQUIRED
TREATMENT RESEARCH ONLY
VALIDATED FOR INTENDED USE
```

Gate to advance:

Field operators can detect major hydraulic, particulate, microbial, material, and storage failures without relying on water appearance.

---

# Phase 7 — Summer humidity and atmospheric-water lane

## Objective

Investigate whether Gaza's high summer humidity can supplement water supply during the near-zero-rainfall season.

## Existing evidence

Summer mean RH is commonly high, and modeled monthly mean dew points are roughly 21-22 C during June-August.

## Prototype family

```text
AW-P0  radiative dew surface
AW-P1  shaded/buried air pre-cooler
AW-P2  ground-coupled radiator condenser
AW-P3  solar-draft assisted condenser
AW-R1  rubble-shaded thermal-mass enclosure
```

## Passes

### P7.1 — hourly climate model

Move beyond monthly means using hourly/reanalysis climate data where available.

Compute:

- dew-point hours;
- hours condenser surface would be below dew point;
- seasonal humidity ratio;
- theoretical condensable water per air volume.

### P7.2 — rubble thermal-mass test

Measure:

- surface rubble temperature;
- rubble-core temperature;
- shaded soil temperature;
- diurnal lag;
- nighttime recovery.

Purpose:

Determine whether rubble is only structural mass or provides useful thermal buffering.

### P7.3 — passive condenser model

Model:

```text
PRECOOL -> CONDENSE -> SOLAR DRAFT
```

rather than heating incoming moist air before condensation.

### P7.4 — field prototype

Measure:

- airflow;
- radiator/surface temperature;
- dew-point margin;
- condensate L/h;
- energy use;
- water chemistry/microbiology.

Gate to advance:

Measured atmospheric-water production exists under Gaza-like summer conditions and exceeds a minimum useful L/day threshold defined against material, energy, and maintenance burden.

---

# Phase 8 — Rubble-integrated structural engineering

## Objective

Turn abundant screened debris into predictable WASH-support infrastructure.

## Passes

### P8.1 — debris screening intake

Create a one-page classification sheet:

```text
RR-0 reject
RR-1 structural only
RR-2 crush/reuse
RR-3 encapsulated use
```

### P8.2 — wind/ballast calculations

For pallet collectors calculate:

- projected area;
- wind pressure scenarios;
- uplift/overturning;
- rubble mass;
- anchor geometry;
- safety factor.

### P8.3 — barrel stand loading

Calculate:

- one full 200-L barrel;
- 2-barrel bank;
- 4-barrel bank;
- load spreader dimensions;
- rubble settlement sensitivity.

### P8.4 — overflow apron hydraulics

Evaluate:

- discharge rate;
- erosion risk;
- apron dimensions;
- splash contamination;
- drainage path.

### P8.5 — lined rubble filter structure

Prototype a rubble outer shell with controlled liner for:

- settling;
- roughing;
- slow sand.

Gate to advance:

Rubble structures are stable, inspectable, repairable, and physically isolated from controlled water-contact paths.

---

# Phase 9 — Integrated household module

## Objective

Assemble the first complete end-to-end system.

## Reference architecture

```text
4-PANEL COLLECTOR
        ↓
SCREEN
        ↓
FIRST FLUSH
        ↓
RAW BARREL BANK
        ↓
SETTLING
        ↓
ROUGHING
        ↓
CONTROLLED FILTER
        ↓
DISINFECTION
        ↓
CLEAN STORAGE
        ↓
CONTROLLED OUTLET
```

Support infrastructure:

```text
screened rubble pad
rubble ballast/gabion anchors
rubble overflow apron
controlled liners at all wetted interfaces
```

## Passes

### P9.1 — bench integration

Dry/hydraulic test without drinking-water claims.

### P9.2 — clean-water hydraulic commissioning

Check:

- leaks;
- bypass;
- flow;
- first-flush operation;
- barrel isolation;
- overflow.

### P9.3 — challenged-water testing

Controlled non-potable test water used to compare stages.

### P9.4 — field environmental trial

Measure multiple rain events and storage cycles.

### P9.5 — maintenance-cycle trial

Track performance through:

- clogging;
- cleaning;
- media disturbance;
- vessel isolation;
- component replacement.

Gate to advance:

The integrated system produces reproducible measured performance and failures are detectable/isolatable.

---

# Phase 10 — Community node scaling

## Objective

Scale household modules without creating a new centralized single point of failure.

## Prototype family

```text
CN-P1  8-panel node
CN-P2  16-panel node
CN-P3  multi-source storage node
CN-P4  shared treatment node
```

## Passes

### P10.1 — source manifold

Accept multiple inputs while preserving source identity.

### P10.2 — modular storage bank

Prefer multiple isolatable tanks over one undivided reservoir where practical.

### P10.3 — treatment parallelization

Parallel filter trains allow maintenance without complete shutdown.

### P10.4 — distribution control

Design for:

- measured dispensing;
- clean outlet;
- queue/use hygiene;
- source/use labeling.

### P10.5 — operating burden

Measure:

- labor-hours/day;
- cleaning time;
- replacement parts;
- consumables;
- energy;
- litres/person/day delivered.

Gate to advance:

Scale improves served population without proportionally increasing failure fragility or imported-material dependence.

---

# Phase 11 — Contested-zone deployment package

## Objective

Translate research prototypes into a controlled field package for legitimate WASH responders.

## Deliverables

### Technical

- drawings;
- BOMs;
- alternative-material matrix;
- hydraulic diagrams;
- storage tables;
- filter commissioning sheets;
- maintenance cards;
- sampling forms;
- failure indicators;
- use-classification labels.

### Operational

- site-selection sheet;
- rubble-screening intake;
- source-risk matrix;
- treatment-selection matrix;
- seasonal operating guidance;
- contamination-response procedure;
- winter rain / summer humidity strategy.

### Evidence

- literature review;
- model assumptions;
- bench results;
- field results;
- unresolved uncertainties;
- explicit non-confirmatory boundaries.

Gate to advance:

A third party can reproduce the system without relying on undocumented assumptions.

---

# Phase 12 — Regional transfer and universality check

## Objective

Separate Gaza-specific assumptions from universal contested-zone design principles.

Compare against:

- Syria;
- Lebanon;
- Yemen;
- Ukraine;
- other conflict/disaster environments with different rainfall, temperature, source water, and material availability.

## Questions

1. Which modules remain useful everywhere?
2. Which are Gaza-climate dependent?
3. Which rely on coastal humidity?
4. Which fail under freezing conditions?
5. Which require locally unavailable media?
6. Which depend excessively on imported consumables?
7. Which are robust to displacement and repeated setup/teardown?

Final outcome:

```text
UNIVERSAL CORE
+
CLIMATE MODULES
+
SOURCE-WATER MODULES
+
LOCAL-MATERIAL MODULES
```

---

# Immediate next-pass queue

Recommended execution order from the current repository state:

1. **P8.2 — wind/ballast calculation for the four-pallet rubble collector.**
2. **P8.3 — barrel-bank load/stability model for 1-4 drums.**
3. **P1.2 — correct/freeze first-flush hydraulic variants.**
4. **P2.2 — contamination-isolated barrel manifold.**
5. **P7.1 — hourly Gaza summer dew/condensation model.**
6. **P3.2 — settling-barrel hydraulic specification.**
7. **P4.1 — field sand-grading protocol.**
8. **P6.1/P6.2 — minimum field kit and standardized sampling ports.**
9. **P9.1 — integrated four-panel bench architecture.**
10. **P10.1 — community-node scaling model.**

This sequence prioritizes unresolved physical engineering before adding more treatment complexity.

---

# Program-level success criteria

The contested-zone sector is mature when it can demonstrate all of the following:

```text
LOCAL MATERIAL USE
        +
LOW IMPORT BURDEN
        +
MEASURED WATER PRODUCTION
        +
MEASURED TREATMENT PERFORMANCE
        +
FAILURE DETECTION
        +
SOURCE / STORAGE ISOLATION
        +
REPAIRABILITY
        +
SEASONAL RESILIENCE
        +
EXPLICIT WATER-USE CLASSIFICATION
```

The target is not a single universal purifier. The target is a modular family of WASH systems that can preserve civilian water access when normal infrastructure is damaged, inaccessible, or unreliable.
