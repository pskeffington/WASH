# Microbial Field Testing and Rainwater Chemical-Risk Pass

## Purpose

This pass extends the low-resource filtration roadmap into two areas that determine whether a system is merely clarifying water or actually reducing health risk:

1. low-cost microbial field testing;
2. rainwater-specific chemical risk from catchment, plumbing, and storage materials.

The operating principle is:

> First flush and filtration can reduce contamination load, but they cannot compensate for a chemically unsafe source or prove microbiological safety by appearance alone.

## 1. Microbial verification for rainwater systems

WHO drinking-water guidance recommends that rainwater systems be verified for microbial quality using **E. coli or thermotolerant coliforms**. WHO also recommends occasional measurement of lead, zinc, or other metals when rainwater contacts metallic collection or storage surfaces.

Rainwater contamination is commonly highest during the first part of a rainfall event. WHO notes that E. coli and a range of other pathogens have been detected in collected rainwater, while first-flush diversion can reduce the initial microbial load.

### Project implication

The WASH repo should treat the first flush as a **load-reduction barrier**, not a microbial safety guarantee.

The minimum verification chain becomes:

```text
raw rainwater
  ↓
post-first-flush sample
  ↓
post-filter sample
  ↓
post-disinfection sample
  ↓
post-storage sample
```

## 2. Field microbiology ladder

### Tier 0 — no microbial test available

Allowed claims:

- hydraulic function;
- debris removal;
- turbidity reduction;
- sediment reduction.

Not allowed:

- bacterial safety;
- pathogen removal;
- potable-water claim.

### Tier 1 — presence/absence screening

Potential low-resource options include commercially standardized presence/absence tests for coliforms or E. coli.

Published biosand research comparing candidate field indicators found that a Colilert presence/absence method correlated better with an EPA reference method than several simpler indicators, although the evidence base was not sufficient to treat it as a complete replacement for quantitative testing.

Use case:

```text
screen for obvious failure
```

not:

```text
certify treatment performance
```

### Tier 2 — quantitative field or incubated tests

Where resources allow, use a validated method that estimates or counts E. coli / thermotolerant coliforms.

Possible operational forms include:

- membrane filtration kits;
- compartment-bag or MPN-style field systems;
- validated enzyme-substrate methods;
- laboratory culture.

The exact test method should be documented and kept consistent across the prototype series.

### Tier 3 — laboratory validation

Needed when the project intends to make stronger microbial-performance claims or compare against WHO household water-treatment performance criteria.

WHO's International Scheme evaluates household water treatment technologies through designated laboratories using standardized protocols for bacteria, viruses, and protozoa.

The project should not claim WHO-equivalent protection based on E. coli testing alone.

## 3. Microbial sampling points

Recommended sample locations:

```text
M0 = direct rainfall / source control sample where practical
M1 = catchment runoff before first flush
M2 = post-first-flush raw water
M3 = post-settling
M4 = post-roughing filter
M5 = post-biosand / ceramic / membrane
M6 = post-disinfection
M7 = after 24-48 h safe-storage interval
```

The M7 sample is particularly important because storage can reverse gains through recontamination.

## 4. Microbial failure logic

Trigger investigation if:

- E. coli is detected after a stage expected to provide microbial protection;
- microbial counts increase after filtration;
- storage sample is worse than post-treatment sample;
- flow increases unexpectedly through a ceramic or membrane element;
- turbidity rises after a treatment stage;
- filter media or seals are disturbed.

A filter that reduces turbidity but allows microbial breakthrough remains a failed health barrier.

## 5. Rainwater chemical-risk model

Rainwater chemistry should be considered as the sum of several contamination pathways:

```text
atmospheric deposition
+ catchment material
+ fasteners / gutters
+ plumbing
+ storage vessel
+ treatment media
```

Peer-reviewed runoff studies show that metals and organic compounds can be released from both metallic and non-metallic roofing materials. Recent systematic review evidence indicates that roof material, roof condition, rainfall characteristics, air quality, gutters, and fixings can all influence metal concentrations.

### Important distinction

Many metals released from copper, zinc, or galvanized surfaces may occur in dissolved form.

This means:

```text
first flush + settling + sand filtration
```

may remove some particle-bound contamination while leaving a significant dissolved-metal fraction.

## 6. Material-specific risk categories

### Lower concern for structural reuse only

- untreated sound wood used behind a separate liner;
- clean pallet framing that does not contact collected water;
- masonry or blocks used as supports;
- external steel bracing isolated from water.

### Controlled water-contact materials

Preferred when provenance is known:

- known potable-water-rated plastic;
- known clean HDPE barrels;
- food-contact liners;
- new or known compatible PVC plumbing;
- validated ceramic elements.

### Higher-risk / test-before-use materials

- galvanized metal;
- copper sheet or copper plumbing;
- lead-soldered joints;
- unknown painted metal;
- aged roofing materials;
- unknown PVC or flexible plastic formulations;
- treated or painted wood;
- previously used industrial barrels;
- bituminous roofing products;
- unknown adhesives and sealants.

### Reject from potable research pathway unless specifically characterized

- containers previously holding fuel, pesticide, solvent, coolant, oil, or unknown industrial chemicals;
- visibly contaminated catchment surfaces;
- lead-containing components in direct water contact;
- automotive cooling-system parts in a drinking-water pathway.

## 7. First-flush limitations

First-flush control is strongly justified for reducing initial pollutant mass and microbial contamination. However, it is not a universal chemical-treatment step.

If a contaminant is continuously leached from the catchment material, every part of the storm can remain contaminated.

Therefore:

```text
first flush reduces deposited contamination
```

but:

```text
first flush does not neutralize an intrinsically unsuitable catchment material
```

## 8. Rainwater chemistry screening matrix

| Material / context | Main concern | Initial response |
|---|---|---|
| Galvanized metal | zinc | test Zn; avoid potable assumptions |
| Copper metal | copper | test Cu; avoid potable assumptions |
| Lead-soldered parts | lead | reject or replace |
| Old painted surface | metals/organics unknown | characterize or exclude |
| PVC / flexible plastic | additives / organics | use known material for potable pathway |
| Bitumen / roofing felt | organics | non-potable unless characterized |
| Treated wood | preservatives | do not use as water-contact surface |
| Unknown barrel | residual chemicals | reject if prior use unknown |
| Known food-grade HDPE | lower material risk | still clean and verify |
| Ceramic filter | metal leaching possible | initial flush chemistry + periodic check |

## 9. Minimum chemical test set for experimental rainwater

The exact panel should be source-specific, but a baseline research set can include:

- pH;
- conductivity/TDS;
- turbidity;
- lead;
- zinc;
- copper;
- iron;
- manganese;
- any locally relevant contaminant linked to catchment material or air pollution.

Additional tests may be needed for:

- arsenic;
- pesticides;
- hydrocarbons;
- solvents;
- PFAS;
- salinity;
- other locally identified contaminants.

The correct response to a suspected toxic chemical source may be **source rejection**, not attempting to improvise a downstream filter.

## 10. Treatment-selection logic for chemical risk

### Particle-bound contamination

Useful barriers may include:

```text
first flush
settling
roughing filtration
sand filtration
```

### Dissolved metals

Sand and gravel generally should not be assumed sufficient.

Potential controlled options include:

- ion exchange;
- contaminant-specific adsorbents;
- validated activated-carbon media for compounds it is known to remove;
- reverse osmosis;
- precipitation/coagulation systems where appropriate.

Treatment selection must follow actual contaminant identification.

### Organic chemicals

Potential options depend on compound and can include:

- validated granular activated carbon;
- advanced oxidation;
- membranes;
- source rejection.

Ordinary charcoal should not be treated as equivalent to a validated GAC system.

## 11. Combined field gate

A barrel-scale system should not advance toward potable research unless it passes all of the following:

### CR-0 — source gate

Catchment and storage materials have known provenance or are specifically characterized.

### CR-1 — hydraulic gate

System collects and conveys water without uncontrolled bypass or stagnation.

### CR-2 — particulate gate

Turbidity reduction is stable and measurable.

### CR-3 — microbial gate

Validated microbial testing demonstrates the performance expected from the treatment stage.

### CR-4 — chemical gate

Material-specific chemical risks have been evaluated.

### CR-5 — disinfection gate

Where microbial risk remains, a validated disinfection step is present.

### CR-6 — storage gate

Post-storage microbial quality does not deteriorate beyond the defined threshold.

### CR-7 — use-classification gate

Water is explicitly classified as:

```text
REJECT
NON-POTABLE / BOUNDED USE
TREATMENT RESEARCH ONLY
or
VALIDATED FOR INTENDED USE
```

## 12. Research implications for the pallet collector

The pallet design is strengthened by keeping the pallet itself structurally useful but outside the water-contact layer.

Preferred sequence:

```text
pallet frame
  ↓
known waterproof liner
  ↓
known gutter material
  ↓
first flush
  ↓
known-use barrel
```

This separates abundant salvaged structural material from the more tightly controlled water-contact pathway.

## 13. Literature anchors

- World Health Organization, *Guidelines for drinking-water quality: fourth edition incorporating the first, second and third addenda* (2026): risk management from catchment to consumer, microbial verification of rainwater, and material-related chemical monitoring.
- WHO, *International Scheme to Evaluate Household Water Treatment Technologies*: standardized independent performance evaluation for household treatment products.
- WHO Round II and Rounds III-IV household treatment evaluations: manufacturing quality and product-specific testing materially affect performance.
- WHO, *Evaluating household water treatment options* (2011): health-based targets and incremental improvement in resource-scarce settings.
- Stauber et al. (2006), biosand filter characterization: mean E. coli reductions around 94% in laboratory studies, improving with maturation but not implying universal complete pathogen removal.
- O'Connell et al. (2017), biosand filter review: field-effectiveness measurement remains challenging in low-resource environments.
- Murphy et al. (2010), critical evaluation of biosand and ceramic filters: emphasizes evaluation of both microbial and chemical water quality.
- *Heavy metal pollutant contributions from roofing materials: A systematic review* (2025): roof materials, condition, rainfall, atmosphere, gutters, and fixings influence metal runoff.
- *Assessment of overall chemical hazard of runoff from eight roofing materials* (2026): substantial Cu/Zn release from some metal roofs and additional organic/biological-effect concerns in runoff.
- *Rooftop runoff as a source of contamination: A review* (2009): both chemical and microbiological contamination can require treatment/disinfection depending on intended use.

## Next pass

1. Build a rainwater-specific source/material acceptance checklist.
2. Define a low-cost E. coli field-testing comparison protocol.
3. Review commercially available low-cost membrane filtration and ceramic elements as controlled drop-in barriers.
4. Develop a contaminant-specific escalation matrix for metals, microbial risk, hydrocarbons, and salinity.
5. Link the microbial/chemical gates into the barrel-scale roadmap and README status summary.
