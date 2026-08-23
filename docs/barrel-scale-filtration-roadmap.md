# Barrel-Scale Water Collection and Improvised Filtration Roadmap

## Purpose

This roadmap defines phased gates from low-cost rain collection through barrel-scale pretreatment, settling, improvised filtration, disinfection research, and safe-use validation.

The governing rule is simple:

> Clearer water is not automatically safer water.

Improvised filters can reduce debris, turbidity, odor, and some microorganisms, but they do not by themselves establish potable water. Any drinking-water use requires a validated treatment chain, appropriate testing, and compliance with applicable public-health requirements.

## Phase 0 — Source and material gate

### Objective

Control the contamination burden before water enters storage.

### Inputs

- pallet or other micro-catchment;
- known waterproof collection skin;
- screened gutter;
- first-flush diverter;
- known-use barrel or cistern.

### Gates

- catchment material provenance documented;
- no visibly contaminated or chemically treated water-contact surface;
- storage container prior use known;
- barrel has sealed lid and screened vent;
- overflow routed safely;
- system labeled non-potable during prototype testing.

### Failure condition

Unknown industrial/chemical drum history, lead-bearing contact material, automotive-fluid contamination, or other uncontrolled contact hazard.

---

## Phase 1 — Collection gate

### Objective

Demonstrate reliable water capture before adding treatment complexity.

### Architecture

```text
pallet catchment
   -> gutter
   -> screen
   -> first flush
   -> raw-water barrel
```

### Measurements

- rainfall depth;
- theoretical catch volume;
- first-flush volume;
- actual captured volume;
- leakage;
- overflow;
- visible debris.

### Acceptance gate

- repeatable gravity flow;
- no standing water in catchment/gutter;
- first-flush operates and resets;
- storage remains closed to insects and debris;
- measured collection efficiency characterized across multiple storms.

No filtration should be added until this gate is stable.

---

## Phase 2 — Coarse pretreatment gate

### Objective

Remove large debris and reduce solids entering the storage barrel.

### Candidate stages

```text
coarse leaf screen
   -> finer removable mesh
   -> first flush
```

Candidate materials:

- clean window/insect screen;
- washable synthetic mesh;
- perforated food-safe basket or strainer;
- clean cloth only as a temporary experimental pre-screen.

### Design requirement

All screens must be removable and washable. A finer screen that clogs and causes water to bypass the system is worse than a coarser screen that remains functional.

### Acceptance gate

- no hydraulic backup during design rainfall test;
- debris captured before storage;
- screen cleaned without specialized tools;
- no unintentional bypass path.

---

## Phase 3 — Settling / sedimentation barrel

### Objective

Use gravity to reduce suspended solids before fine filtration.

WHO household-water guidance recognizes simple sedimentation as a basic physical pretreatment step for reducing turbidity. citeturn538151search39

### Architecture

```text
raw-water barrel
       ↓
quiet settling period
       ↓
draw water from above sediment layer
```

Preferred barrel configuration:

- calm inlet near upper sidewall or diffuser;
- sediment zone at bottom;
- outlet located above the sediment zone;
- bottom drain or removable cleanout if practical;
- opaque, closed container.

### Research variables

- settling time: 1 h / 4 h / overnight;
- turbidity before and after settling;
- sediment depth;
- effect of storm intensity and first-flush size.

### Acceptance gate

Settling produces a repeatable reduction in visible suspended solids without creating stagnant, unmaintainable storage.

---

## Phase 4 — Roughing filter gate

### Objective

Protect finer filters from high solids loads.

WHO treatment guidance describes roughing filtration as a pretreatment method using coarse gravel or crushed stone, combining filtration with gravity settling and supporting treatment of relatively turbid water. citeturn538151search36turn538151search37

### Barrel-scale concept

A separate vertical barrel or bucket should be used rather than placing loose media directly in the main storage barrel.

```text
settled water
     ↓
coarse gravel
     ↓
medium gravel
     ↓
coarse sand
     ↓
next treatment stage
```

This is a **pretreatment filter**, not a drinking-water guarantee.

### Design principles

- media washed before use;
- graded layers kept physically separated where practical;
- drainage underlayer prevents outlet blockage;
- water distribution across the top minimizes channeling;
- filter can be drained and media removed for cleaning;
- avoid unknown crushed material that could leach contaminants.

### Acceptance gate

- measurable turbidity reduction;
- stable flow without major channeling;
- no media carried into downstream water;
- resident-maintainable cleaning procedure.

---

## Phase 5 — Slow-sand / biosand research gate

### Objective

Evaluate a more effective biological/physical filtration stage using a dedicated barrel-scale filter.

WHO describes slow sand filters as using approximately 0.15-0.3 mm effective-size sand, commonly 0.5-1.5 m deep, with low filtration rates. A biologically active surface layer contributes to microorganism removal. citeturn538151search36

WHO household-treatment material also documents biosand filters as an intermittent household-scale adaptation of slow-sand filtration. citeturn538151search38

### Conceptual barrel architecture

```text
inlet diffuser
      ↓
standing water layer
      ↓
fine sand bed
      ↓
coarse sand
      ↓
gravel support
      ↓
underdrain
      ↓
raised outlet
```

The raised outlet maintains water above the sand bed in a biosand-style configuration.

### Critical distinction

This filter should **not** be treated as a bag of mixed sand and gravel poured into a barrel.

Performance depends on:

- correct sand grading;
- bed depth;
- hydraulic loading rate;
- diffuser design;
- avoidance of short-circuiting;
- biological maturation;
- maintenance method;
- source-water quality.

### Development gates

#### G5A — hydraulic gate

- stable flow;
- no visible preferential channels;
- no sand loss;
- predictable residence behavior.

#### G5B — maturation gate

Allow appropriate biological maturation before evaluating full performance. WHO material notes biological-layer development over a period of weeks in slow-sand systems. citeturn538151search38

#### G5C — performance gate

Compare:

```text
turbidity in/out
flow rate
odor/color observations
microbial test results where available
```

Do not infer microbial safety from turbidity alone.

---

## Phase 6 — Adsorptive media research gate

### Objective

Evaluate whether a replaceable activated-carbon stage improves taste, odor, or selected chemical contaminants after particulate filtration.

WHO household-water guidance notes that activated carbon works through adsorption and has a finite capacity that is exhausted as adsorption sites become occupied. citeturn538151search39

### Architecture

```text
roughing / sand filtration
        ↓
activated-carbon cartridge or controlled bed
        ↓
post-filter storage
```

### Important boundary

Charcoal made from unknown scrap material is not equivalent to standardized activated carbon.

Improvised charcoal should not be represented as a reliable chemical-removal stage without testing.

### Acceptance gate

Only claim improvements that are directly measured. Do not claim removal of metals, pesticides, PFAS, solvents, or other chemicals without contaminant-specific evidence.

---

## Phase 7 — Disinfection gate

### Objective

Separate **filtration** from **pathogen inactivation**.

WHO identifies household disinfection methods including chlorine, solar disinfection, UV, and boiling. citeturn538151search39

WHO also maintains technology-specific protocols for evaluating filtration and disinfection systems because household treatment performance varies substantially by design and manufacturing quality. citeturn538151search0turn538151search5

### Architecture

```text
collection
   ↓
pretreatment
   ↓
filtration
   ↓
DISINFECTION
   ↓
safe-storage research vessel
```

The disinfection stage must occur **after turbidity has been reduced sufficiently for the chosen method to work effectively**.

### Prototype rule

Do not invent chlorine doses, UV doses, or contact times from generic assumptions. Use an applicable validated protocol/product instruction and verify water conditions.

### Acceptance gate

A disinfection process may only be credited when its operating parameters and microbiological performance are known or independently tested.

---

## Phase 8 — Safe storage gate

### Objective

Prevent filtered/disinfected water from being recontaminated.

### Storage requirements

- dedicated clean vessel;
- covered and opaque;
- screened vent where needed;
- narrow or controlled dispensing outlet;
- no dipping cups or hands into the vessel;
- cleanable interior;
- raw-water plumbing physically separated from treated-water plumbing.

### Architecture

```text
RAW BARREL
    ↓
filter train
    ↓
disinfection
    ↓
CLEAN-WATER BARREL
    ↓
controlled outlet
```

Raw and treated storage should not be the same barrel during testing.

---

## Phase 9 — Water-quality validation gate

### Objective

Determine what uses, if any, the treated water can support.

WHO's drinking-water framework is based on health-based targets, risk management from catchment to consumer, and independent surveillance rather than visual appearance alone. citeturn538151search2turn538151search1

### Minimum research categories

Depending on intended use and local risks:

- turbidity;
- indicator bacteria / E. coli;
- pH;
- selected metals where collection materials or local atmospheric sources create concern;
- other locally relevant chemicals;
- residual disinfectant where applicable.

### Gate outputs

```text
NON-POTABLE ACCEPTABLE FOR BOUNDED USE
or
FURTHER TREATMENT REQUIRED
or
REJECT WATER / SYSTEM
```

No drinking-water claim is made solely because water has passed through sand, gravel, carbon, cloth, ceramic, or another improvised medium.

---

# Barrel-scale prototype families

## P1 — Two-barrel basic system

```text
PALLET COLLECTOR
      ↓
first flush
      ↓
BARREL 1
settling/raw storage
      ↓
coarse filtration
      ↓
BARREL 2
non-potable clarified storage
```

Use case: irrigation, cleaning, system research, depending on source/material risks.

## P2 — Three-stage research system

```text
PALLET
  ↓
RAW BARREL
  ↓
ROUGHING FILTER BARREL
  ↓
SAND/BIO-SAND FILTER
  ↓
CLEAN RESEARCH BARREL
```

This system enables each treatment step to be sampled independently.

## P3 — Full research train

```text
CATCHMENT
   ↓
SCREEN + FIRST FLUSH
   ↓
SETTLING BARREL
   ↓
ROUGHING FILTER
   ↓
SLOW-SAND / BIOSAND FILTER
   ↓
OPTIONAL CONTROLLED CARBON STAGE
   ↓
VALIDATED DISINFECTION
   ↓
SAFE STORAGE
   ↓
LAB / FIELD TESTING GATE
```

This is the preferred scientific architecture because treatment stages remain separable and independently measurable.

---

# Measurement matrix

At each stage record:

| Stage | Volume | Turbidity | Flow | Microbiology* | Maintenance |
|---|---:|---:|---:|---:|---|
| rainfall/catchment | yes | optional | event | optional | surface condition |
| first flush | yes | yes | event | research | sediment/debris |
| raw barrel | yes | yes | outlet | research | sediment |
| roughing filter | yes | yes | L/h | research | clogging |
| sand/biosand | yes | yes | L/h | important | maturation/cleaning |
| carbon | yes | yes | L/h | not sufficient alone | replacement |
| disinfected water | yes | yes | batch/flow | required for potable claims | dose/process |

`*` Microbial testing should use appropriate validated methods.

---

# Development priorities

### Phase A — immediately buildable

1. pallet collector;
2. first-flush diverter;
3. screened raw barrel;
4. settling outlet above sludge layer;
5. overflow management.

### Phase B — improvised filtration research

1. separate gravel roughing barrel;
2. sand grading and hydraulic trials;
3. barrel-scale slow-sand/biosand prototype;
4. turbidity and flow logging.

### Phase C — treatment validation

1. microbiological testing;
2. controlled disinfection protocol;
3. safe-storage barrel;
4. material/contact testing;
5. comparison with WHO household-treatment performance framework.

### Phase D — deployment package

Only after previous gates:

- standardized build drawings;
- locally adaptable bill of materials;
- maintenance card;
- failure indicators;
- water-use classification;
- resident training protocol;
- cost per gallon and maintenance burden.

## Final design rule

The project should optimize the treatment chain in this order:

```text
KEEP CONTAMINATION OUT
        ↓
REMOVE LARGE SOLIDS
        ↓
SETTLE FINE SOLIDS
        ↓
FILTER
        ↓
DISINFECT WHEN REQUIRED
        ↓
PREVENT RECONTAMINATION
        ↓
TEST BEFORE CLAIMING SAFETY
```

The least expensive contaminant to remove is the contaminant that never enters the barrel.
