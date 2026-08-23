# Filtration Performance Next Pass

## Purpose

This pass narrows the collection-to-filtration literature review into performance rules for barrel-scale and household-scale systems. The emphasis is on what each stage can credibly do, where improvisation remains reasonable, and where controlled manufacturing or validated treatment becomes necessary.

## 1. Biosand / household slow-sand filtration

A 2022 critical review in *Water Research* identifies household slow-sand filtration as one of the more promising point-of-use treatment approaches for isolated communities while also noting remaining gaps for protozoa, cyanobacteria, and emerging pollutants.

WHO household-treatment literature reports that field/laboratory biosand performance can be variable; some evaluations achieved mean E. coli reductions below 2 log10. WHO therefore encourages supplemental disinfection where possible, especially because recontamination remains a concern after filtration.

### Design implication

Biosand should be treated as a strong **turbidity-reduction and microbial-risk-reduction barrier**, but not as a universal stand-alone potable-water guarantee.

The preferred research sequence is:

```text
settling
  -> roughing filtration
  -> biosand / slow-sand filtration
  -> validated disinfection
  -> safe storage
```

### Media-depth evidence

Published household slow-sand work shows substantial variation in sand-bed depth. CAWST's standard household design has used roughly 53 cm of filtration media, while literature studies span much smaller and larger depths. This means compact barrel designs are possible research targets, but performance cannot be assumed equivalent merely because the media is sand.

Variables that must be controlled include:

- effective sand size;
- uniformity coefficient;
- bed depth;
- hydraulic loading;
- pause period;
- diffuser design;
- maturation state;
- outlet elevation.

## 2. Ceramic filtration

WHO's household-treatment evaluation framework explicitly includes ceramic pot and ceramic filtration technologies and has separate microbiological testing protocols for ceramic pot filters.

### Key implication

Ceramic technology is attractive because it can be gravity driven, compact, and locally manufactured. However, performance depends heavily on:

- clay composition;
- pore-forming additive;
- firing temperature/time;
- wall thickness;
- cracks;
- seals;
- flow rate;
- post-firing handling.

WHO notes that locally manufactured ceramic and biosand products can vary widely depending on manufacturing quality.

Therefore:

```text
locally manufactured ceramic under QA/QC
```

is a valid technology lane, whereas:

```text
any fired clay container
```

is not.

## 3. Activated carbon / charcoal

WHO guidance is especially clear that conventional charcoal or activated carbon should **not** be relied upon for microbial reduction. Carbon can itself become colonized by bacteria and may shed microorganisms into treated water.

### Appropriate role

Activated carbon belongs primarily in a **chemical/taste/odor adsorption** role after particulate filtration.

```text
sand / ceramic / membrane
       -> activated carbon
       -> disinfection if required
```

### Improvised-charcoal boundary

Ordinary wood charcoal, coconut char, or other biomass char may be locally available, but should not be represented as equivalent to standardized activated carbon.

Improvised carbon research may examine:

- odor change;
- color change;
- selected measured organics;
- flow resistance;
- media life.

It should not claim reliable removal of pathogens, metals, pesticides, PFAS, or other chemicals without direct testing.

## 4. Membrane / hollow-fiber filtration

WHO evaluates membrane filtration as a separate household-treatment technology class. Commercial membrane products can provide strong microbial barriers, but product-specific performance varies.

The 2026 WHO Rounds III-IV report completes evaluation of 51 household water-treatment products across multiple technologies and reinforces that independent performance testing is necessary.

### Low-resource design implication

Gravity-fed hollow-fiber or ultrafiltration units can serve as an **advanced drop-in module** downstream of coarse pretreatment.

```text
raw collection
 -> settling
 -> roughing
 -> membrane element
 -> disinfection/safe storage as required
```

This preserves the low-cost improvised upstream architecture while using a controlled manufactured element for the health-critical barrier.

Reverse osmosis remains a poor first-choice barrel-scale design because it typically requires:

- pressure;
- pretreatment;
- higher maintenance;
- reject-water management;
- replacement membranes.

## 5. WHO performance framework

WHO household-treatment technologies are evaluated against microbial performance criteria for bacteria, viruses, and protozoa rather than by appearance or turbidity alone.

WHO's framework also explicitly supports **incremental improvement** in resource-scarce settings: a system need not solve every contaminant problem at once to be beneficial, but its actual protection level must be understood.

### Project implication

The WASH repo should adopt a similar evidence hierarchy:

```text
HYDRAULIC FUNCTION
    ↓
PARTICLE/TURBIDITY PERFORMANCE
    ↓
MICROBIAL PERFORMANCE
    ↓
CHEMICAL PERFORMANCE
    ↓
SAFE STORAGE / USER CONSISTENCY
```

Do not skip directly from "water looks clear" to "safe to drink."

## 6. Contaminant-to-treatment matrix

| Concern | Improvised pretreatment | Stronger treatment | Notes |
|---|---|---|---|
| Leaves/insects | screen/mesh | not needed | removable washable screen |
| Coarse sediment | settling + gravel | sand | protect finer stages |
| Fine turbidity | settling + roughing | slow sand / ceramic / membrane | turbidity affects disinfection |
| Bacteria | biosand may reduce | ceramic/membrane + validated disinfection | verify performance |
| Protozoa | filtration can help | ceramic/membrane/appropriate filter | product/media specific |
| Viruses | limited removal by many improvised filters | validated membrane/disinfection | key weakness of many gravity filters |
| Taste/odor | limited | activated carbon | carbon is not a microbial barrier |
| Dissolved metals | generally poor | contaminant-specific media / RO / ion exchange | testing required |
| Salinity | no practical improvised filter | RO/distillation | energy and reject-water burden |
| Hydrocarbons/solvents | unsafe to assume removal | specialized treatment | source rejection may be best |
| Pesticides/organics | uncertain | validated activated carbon / advanced treatment | compound-specific |

## 7. Barrel-scale architecture by confidence level

### Level A — improvised non-potable clarification

```text
catchment
 -> screen
 -> first flush
 -> settling barrel
 -> gravel/sand roughing filter
 -> non-potable storage
```

Purpose:

- irrigation;
- cleaning;
- process-water research;
- reduction of suspended solids.

### Level B — controlled household filtration research

```text
catchment
 -> screen
 -> first flush
 -> settling
 -> roughing
 -> controlled biosand OR validated ceramic
 -> clean storage
```

Purpose:

- measure microbial/turbidity improvement;
- not automatically potable.

### Level C — multi-barrier potable-research lane

```text
catchment
 -> exclusion / first flush
 -> settling
 -> roughing
 -> validated filter
 -> validated disinfection
 -> safe storage
 -> water-quality testing
```

This is the first architecture that should even be considered for potable research, and only after testing.

## 8. Material sourcing logic

### Abundant / salvaged

Best for low-risk structural or pretreatment roles:

- pallet wood;
- barrels with known prior use;
- buckets;
- PVC;
- hose;
- screens;
- clean cloth;
- gravel;
- sand;
- masonry blocks;
- simple valves/spigots.

### Locally processable but quality-sensitive

- graded filter sand;
- ceramic pots/candles;
- concrete filter bodies;
- biomass char;
- iron-coated media.

These require simple QA/QC protocols.

### Manufactured health-critical components

- hollow-fiber membranes;
- certified ceramic elements;
- granular activated carbon;
- chlorine products of known concentration;
- UV devices;
- contaminant-specific media.

These should not be replaced by visually similar improvised materials when the intended claim is health protection.

## 9. Measurement gates

Each barrel-stage prototype should record:

```text
flow rate
head loss
volume treated
turbidity in/out
maintenance interval
visible channeling or bypass
media loss
```

For any microbial-performance claim, add validated microbiological testing.

For any chemical-removal claim, add contaminant-specific chemistry.

## 10. Literature anchors

- World Health Organization, *International Scheme to Evaluate Household Water Treatment Technologies*, including filtration, ceramic, chemical, solar, UV, and membrane protocols.
- WHO, *Results of Rounds III and IV* (2026): total of 51 household-treatment products evaluated and continuing evidence that product/manufacturing quality materially affects performance.
- WHO, *Results of Round II* (2019): ceramic and membrane filtration among evaluated technologies; weak manufacturing quality identified among products failing performance criteria.
- WHO, *Evaluating household water treatment options* (2011): health-based targets and incremental-improvement framework for resource-scarce settings.
- *A critical overview of household slow sand filters for water treatment*, Water Research 208 (2022), 117870.
- WHO household-treatment guidance on activated carbon: conventional charcoal/activated carbon is not recommended as the primary microbial treatment barrier.

## Next research pass

1. Establish simple low-cost sieve/gradation testing for sand and gravel.
2. Compare biosand vs ceramic vs hollow-fiber modules on flow, maintenance, replacement burden, and microbial evidence.
3. Pull literature on low-cost turbidity measurement suitable for community operation.
4. Pull literature on ceramic manufacturing QA/QC and crack/failure detection.
5. Build a source-water classification matrix to decide when rain/dew/fog water should bypass or reject particular treatment paths.
6. Define water-quality sampling intervals after each treatment barrier.
