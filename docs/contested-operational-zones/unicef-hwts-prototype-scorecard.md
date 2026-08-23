# UNICEF Emergency HWTS Prototype Scorecard

## Purpose

This scorecard evaluates the current WASH repo architecture against UNICEF emergency Household Water Treatment and Safe Storage (HWTS) design criteria.

UNICEF's emergency HWTS innovation work identifies the following target characteristics for household systems:

- affordable;
- easy/intuitive to use;
- fail-safe;
- durable;
- packable / low logistics footprint;
- safe storage and dispensing;
- approximately one-year service life for a family of five at 2.5 L/person/day;
- no continuing chemical consumable requirement during the service period;
- protection against bacteria, viruses, and protozoa.

This scorecard does not claim UNICEF approval or certification. It uses those criteria as an external design benchmark.

---

## 1. Systems scored

### PRC — pallet/rubble rain collector

```text
screened rubble foundation
+ pallet/scrap structural frame
+ known liner/barrier
+ gutter
+ screen
+ first flush
+ raw storage
```

### BBS — barrel-bank storage system

```text
2-4 isolated ~200-L drums
+ rubble pad
+ continuous load spreader
+ independent valves
+ overflow management
```

### PTF — passive treatment family

```text
settling
+ roughing filtration
+ controlled sand/biosand or ceramic/membrane
+ validated disinfection where required
+ safe storage
```

### IHM — integrated household module

```text
PRC + BBS + PTF
```

---

## 2. Scoring scale

```text
0 = not addressed
1 = concept only
2 = partially engineered
3 = analytically scaffolded / evidence supported
4 = bench/field validated
5 = deployment-ready with verified performance
```

Current scores are intentionally conservative.

---

# 3. UNICEF criterion: affordability

UNICEF benchmark:

```text
affordable household-level emergency treatment
```

UNICEF's innovation page historically cites a target below $20/family for the treatment product itself. The current WASH architecture is broader than a single filter product, so direct comparison requires separating locally salvaged structure from controlled treatment components.

## PRC score: 3/5

Strengths:

- rubble, pallets, scrap timber, wire, and locally available storage can reduce imported-material costs;
- collector scales incrementally;
- no pump/generator required;
- repairable with common materials.

Gap:

- actual build cost has not been measured;
- safe liner, fittings, and first-flush components may dominate cost;
- humanitarian labor/logistics costs are unquantified.

## BBS score: 3/5

Strengths:

- uses common barrels and local structural mass;
- modular expansion avoids large custom tanks.

Gap:

- known-use/food-compatible barrels may be scarce or expensive;
- cost per stored litre not documented.

## PTF score: 2/5

Strengths:

- settling and roughing filtration can be locally constructed;
- biosand can have low recurring energy burden.

Gap:

- validated ceramic/membrane/disinfection components may raise cost substantially;
- no total cost/litre model exists.

## IHM score: 2/5

The integrated system has not yet demonstrated a household all-in cost compatible with UNICEF's aggressive emergency-product target.

### Required pass

Create:

```text
cost per module
cost per litre/year
imported cost
local-material cost
labor-hours
replacement cost
```

---

# 4. UNICEF criterion: easy / intuitive use

## PRC score: 3/5

Strengths:

- passive rain collection is conceptually simple;
- few daily operator actions;
- visible flow path.

Gap:

- first-flush operation may confuse users;
- storm-stow and inspection procedures need simplified instructions.

## BBS score: 3/5

Strengths:

- ordinary barrel storage is familiar;
- independent valves are easy to understand if labeled.

Gap:

- raw versus treated vessel management requires clear visual coding;
- multiple valves can introduce operator error.

## PTF score: 2/5

Gap:

- filter maintenance and disinfection add complexity;
- biosand maturity, ceramic integrity, membrane cleaning, and disinfection procedures require training.

## IHM score: 2/5

### Required pass

Create one-page pictorial operating cards for:

- rain collection;
- first flush;
- raw barrel;
- treatment;
- clean storage;
- stop-use conditions.

Field-test whether an unfamiliar operator can run the system correctly after brief instruction.

---

# 5. UNICEF criterion: fail-safe behavior

UNICEF describes a desired end-of-life mechanism that prevents a treatment product from continuing to provide water when it can no longer provide clean water.

This is currently the weakest major criterion.

## PRC score: 1/5

The collector can continue producing water even when:

- liner material becomes contaminated;
- first flush fails;
- storage becomes unsafe.

The sanitary-inspection and classification system can identify failures, but there is no physical fail-safe.

## BBS score: 2/5

Independent valves allow manual isolation, which is valuable, but the system does not automatically prevent use after contamination.

## PTF score: 1/5

Potential dangerous failure modes include:

- cracked ceramic with increased flow;
- filter bypass;
- exhausted adsorbent;
- failed disinfection;
- storage recontamination.

These may not stop flow automatically.

## IHM score: 1/5

### Highest-priority design gap

Develop a **fail-safe / fail-visible architecture** rather than requiring true automatic shutdown in every improvised component.

Candidate design principles:

```text
FLOW CHANGE = visible warning

BROKEN SEAL = obvious

FILTER ELEMENT = removable / inspectable

RAW / CLEAN = physically incompatible connections where possible

FAILED TEST = red-tag outlet

UNKNOWN STATUS = outlet mechanically locked or capped
```

For commercial health-critical elements, prefer products with evidence-backed end-of-life or integrity indicators where available.

---

# 6. UNICEF criterion: durability

## PRC score: 3/5

Strengths:

- rubble ballast;
- low panel angles;
- modular four-panel architecture;
- storm-stow concept;
- replaceable liner.

Gap:

- no field durability cycles yet;
- UV, abrasion, dust, repeated storm setup, and structural fatigue untested.

## BBS score: 3/5

Strengths:

- low/broad stand architecture;
- staged loading model;
- continuous support deck;
- isolated drums.

Gap:

- rubble settlement and barrel aging not field validated.

## PTF score: 2/5

Durability depends heavily on selected filter technology.

## IHM score: 2/5

### Required durability trial

Test:

- repeated wet/dry cycles;
- 10+ simulated storm cycles;
- liner removal/repair;
- barrel fill/empty cycles;
- filter maintenance cycles;
- transport/disassembly/reassembly.

---

# 7. UNICEF criterion: packable / minimal logistics footprint

## PRC score: 4/5

This is one of the architecture's strongest categories because most structural mass is sourced at the deployment site:

```text
rubble
pallets
scrap framing
```

Imported kit can be concentrated into:

- liner;
- screen;
- fittings;
- first-flush hardware;
- sample/test supplies.

## BBS score: 3/5

Barrels are bulky, but where they already exist locally they do not require international transport.

## PTF score: 3/5

A compact ceramic/hollow-fiber/membrane health-critical element can have a favorable logistics footprint compared with complete powered treatment systems.

## IHM score: 4/5 conceptually

### Core logistics doctrine

```text
IMPORT PRECISION
SOURCE MASS LOCALLY
```

Import or centrally procure only components where material quality or treatment performance is health-critical.

---

# 8. UNICEF criterion: safe storage and dispensing

## PRC score: 2/5

Collection ends in raw storage, so safe drinking storage is downstream.

## BBS score: 4/5 analytically

Strengths:

- covered vessels;
- screened vents;
- controlled spigots;
- independent isolation;
- raw/clean separation;
- no hand dipping;
- sanitation inspection.

Gap:

- field verification required.

## PTF score: 3/5

Architecture requires a clean-storage endpoint.

## IHM score: 3/5

The design direction aligns strongly with UNICEF's treatment-plus-safe-storage principle, but integrated field validation is not complete.

---

# 9. UNICEF criterion: one-year service life / household volume

UNICEF's cited target is approximately:

```text
family of 5
x 2.5 L/person/day
x 365 days
≈ 4,560 L/year
```

The current four-pallet Gaza rain model produces approximately:

```text
~1,050-1,960 L/year
```

across the modeled south-to-north rainfall gradient at 80% modeled recovery.

Therefore:

> a four-pallet rain collector cannot independently meet the UNICEF treatment-product annual-volume target in Gaza.

This is expected because collection and treatment are different functions.

## PRC score: 1/5 as sole annual source

## PRC score: 3/5 as supplemental seasonal source

## BBS score: 3/5

Storage can cycle repeatedly and is not constrained to one fill/year.

## PTF score: 2/5

No treatment element has yet been selected and validated for >=4.5 m3 annual household throughput.

## IHM score: 2/5

### Required design shift

The integrated household module must be explicitly **multi-source**:

```text
RAIN
+
PROTECTED / DELIVERED / OTHER CHARACTERIZED SOURCE
      ↓
SHARED TREATMENT / SAFE STORAGE ARCHITECTURE
```

Rain provides seasonal offset and redundancy, not complete annual supply in Gaza.

---

# 10. UNICEF criterion: no recurring chemical provision

## PRC score: 5/5

Collection itself requires no chemical consumables.

## BBS score: 5/5

Storage itself requires no routine treatment chemical, although cleaning/disinfection may periodically be necessary.

## PTF score: variable

### Biosand / ceramic / gravity membrane

Potential score:

```text
3-5/5
```

depending on actual product and source water.

### Chlorination-dependent system

Score:

```text
1-2/5
```

against the no-consumable target because chlorine supply must be replenished.

However, public-health safety takes priority over meeting the no-consumable design target.

## IHM score: 3/5 conceptually

### Design objective

Prefer a health-critical barrier that minimizes consumables, but retain validated disinfection where source risk requires it.

---

# 11. UNICEF criterion: bacteria, virus, and protozoa protection

This is the other major unresolved criterion.

## PRC score: 0/5

Collection is not treatment.

## BBS score: 0/5

Storage is not pathogen treatment.

## PTF score: 1/5 current architecture

Potential treatment technologies exist, but the repo has not frozen a specific independently validated health-critical barrier.

Biosand and generic ceramic systems should not automatically be assumed to provide full bacteria-virus-protozoa protection.

## IHM score: 1/5

### Highest-priority treatment gap

Freeze one or more controlled treatment options using an evidence hierarchy:

```text
T0 improvised sediment control only
T1 controlled locally produced filter with measured performance
T2 standardized commercial filter with independent evidence
T3 WHO-evaluated / equivalent health-critical product where accessible
```

Then separately address chemical contamination such as salinity, nitrate, metals, or hydrocarbons, because microbial protection alone is insufficient.

---

# 12. Additional UNICEF-aligned criterion: local procurement

UNICEF emergency supply practice encourages local procurement where appropriate, particularly in recurring crises.

## Current architecture score: 4/5 conceptually

Strong candidates for local sourcing:

- screened rubble;
- pallets;
- lumber;
- wire;
- barrels where provenance is known;
- sand/gravel where characterized;
- basic plumbing.

Controlled/imported procurement should focus on:

- liners where local material quality is uncertain;
- validated filter elements;
- test kits;
- disinfectant where required;
- specialized valves/fittings.

---

# 13. Overall current scorecard

| Criterion | PRC | BBS | PTF | Integrated module |
|---|---:|---:|---:|---:|
| Affordability | 3 | 3 | 2 | 2 |
| Intuitive use | 3 | 3 | 2 | 2 |
| Fail-safe | 1 | 2 | 1 | 1 |
| Durability | 3 | 3 | 2 | 2 |
| Logistics footprint | 4 | 3 | 3 | 4 |
| Safe storage | 2 | 4 | 3 | 3 |
| Annual household throughput | 1 supplemental / 3 seasonal | 3 | 2 | 2 |
| Low consumables | 5 | 5 | 1-5 | 3 |
| Bacteria-virus-protozoa protection | 0 | 0 | 1 | 1 |
| Local procurement | 4 | 4 | 2-4 | 4 |

These are internal maturity scores, not UNICEF ratings.

---

# 14. Highest-value design gaps

## Priority 1 — health-critical filter selection

Select at least one treatment element with independent evidence for microbial performance.

Deliverable:

`health-critical-filter-selection-matrix.md`

## Priority 2 — fail-visible / fail-safe system behavior

Build explicit failure indicators and outlet-lockout/red-tag logic.

Deliverable:

`fail-safe-and-fail-visible-design.md`

## Priority 3 — annual throughput

Test selected filter and storage architecture against:

```text
>=4.5 m3/year household treatment throughput
```

where that UNICEF benchmark is being used.

## Priority 4 — intuitive operation

Create pictorial SOP cards and conduct usability trials.

## Priority 5 — durability

Run repeated setup, storm, filtration, cleaning, and transport cycles.

## Priority 6 — actual affordability

Produce measured BOM and lifecycle cost.

---

# 15. Pre-bench gate

Do not proceed to an integrated potable-water claim merely because collection/storage engineering is mature.

Before integrated bench assembly intended for drinking-water research, freeze:

1. the water-contact liner/material set;
2. first-flush design;
3. raw/clean barrel configuration;
4. treatment element;
5. disinfection strategy;
6. sampling ports;
7. stop-use indicators;
8. use-classification labels.

The initial bench system can remain **TREATMENT RESEARCH ONLY** until verification supports a stronger classification.

---

## Evidence anchors

UNICEF's emergency HWTS innovation criteria identify affordability, intuitive operation, fail-safe behavior, durability, minimal logistics footprint, safe storage, long service life, reduced consumable dependence, and bacteria/virus/protozoa protection as desirable characteristics for emergency household treatment systems. UNICEF has investigated gravity-driven membrane filtration partly because it can operate without pressurized pumping and reduce maintenance requirements.

UNICEF's household-filter product guide also emphasizes that no single filter technology is universally appropriate and compares options across protection, flow, lifetime, setup, operation and maintenance, transportability, price, and safe storage.

## Next pass

Proceed with **Priority 1: health-critical filter selection matrix**, comparing ceramic, biosand, gravity hollow-fiber/ultrafiltration, gravity-driven membrane, and other appropriate low-energy options against WHO/UNICEF evidence, Gaza source-water constraints, consumables, throughput, field repair, and chemical-contaminant limitations.
