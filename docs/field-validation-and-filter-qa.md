# Field Validation and Filter QA for Low-Resource Water Systems

## Purpose

This document defines field-operational quality checks for low-resource water collection and filtration systems. The objective is to detect failure early using inexpensive measurements rather than relying on visual appearance alone.

The central rule is:

> A filter is only useful if its hydraulic behavior, media condition, and water-quality performance remain within known bounds.

All systems remain experimental and non-potable by default unless independently validated for the intended use.

## 1. Turbidity as an operational control

Turbidity is one of the most useful low-cost measurements because it responds quickly to source changes, filter breakthrough, channeling, sediment disturbance, and treatment failure.

WHO guidance uses nephelometric turbidity units (NTU). For low-resource supplies, keeping turbidity below about 5 NTU is an important operational target; where disinfection is used, turbidity should ideally be below about 1 NTU because particles can shield microorganisms and reduce disinfection effectiveness.

### Monitoring logic

Measure turbidity at:

```text
raw source
post-settling
post-roughing filter
post-sand/biosand filter
post-final filtration
```

### Frequency

For an active prototype:

- each new rain event during early testing;
- before and after each filtration stage during commissioning;
- daily during continuous treatment trials;
- immediately after filter cleaning or media disturbance;
- more frequently after heavy rainfall or an unexpected turbidity increase.

### Failure triggers

Investigate when:

- filtered turbidity rises unexpectedly;
- outlet turbidity approaches inlet turbidity;
- a previously stable filter produces cloudy water;
- flow increases suddenly without a deliberate hydraulic change;
- media has been disturbed.

A sudden increase in flow plus worsening turbidity can indicate channeling or structural bypass.

## 2. Low-cost turbidity measurement ladder

### Tier A — visual comparator

Lowest-cost field screening can compare water against standardized visual references or simple clear-tube methods.

Use only for trend detection, not a potable-water claim.

### Tier B — turbidity tube

A transparent calibrated tube provides a low-cost way to estimate turbidity by viewing a target through a known water depth.

Advantages:

- no electricity;
- minimal maintenance;
- suitable for rough field comparison.

Limitations:

- poor precision at low NTU values;
- operator dependent;
- not sufficient for validating a sub-1-NTU disinfection target.

### Tier C — portable turbidity meter

A portable nephelometric meter is the preferred field instrument once the system enters treatment-performance research.

Use the same instrument and calibration protocol across stages so relative changes remain meaningful.

## 3. Sand grading as a QA gate

Slow-sand and biosand performance depends strongly on particle-size distribution.

The key parameters are:

```text
D10 = particle size for which 10% of the sample is finer
D60 = particle size for which 60% of the sample is finer
UC  = D60 / D10
```

Typical slow-sand literature places effective size around approximately 0.15-0.35 mm, with tighter ranges often used for household biosand designs. A uniformity coefficient below roughly 2 is generally preferred, although published designs vary.

### Practical field method — sieve analysis

Preferred equipment:

- nested sieves;
- sample container;
- scale or graduated-volume method;
- graph/table for cumulative percent passing.

Procedure concept:

```text
dry representative sand sample
        ↓
sieve into size fractions
        ↓
measure fraction mass or volume
        ↓
calculate cumulative percent passing
        ↓
derive D10 and D60
        ↓
calculate UC
```

A 2025 comparison of laboratory and field biosand-sand methods found that field versus laboratory protocol differences could change calculated effective size and uniformity coefficient by up to about 24%. Field methods are useful, but the protocol used must therefore be documented and kept consistent.

### Field fallback — settling jar

Where sieves are unavailable, a transparent jar can provide an approximate grain-size distribution through sedimentation and visual stratification.

This is a screening tool rather than an exact replacement for sieve analysis.

### Washing gate

Filter sand should be washed until excessive fine material, clay, and organic debris are removed. Very fine material can plug pores and cause poor hydraulic behavior or cloudy filtrate.

## 4. Flow rate as a filter-health indicator

Flow is not simply a convenience measurement. It is an operational diagnostic.

Measure:

```text
volume collected / elapsed time
```

and record it after every significant maintenance event.

### Biosand behavior

Published biosand experiments show flow commonly declines with maturation and accumulated solids. A gradual decline can be expected; a sudden change is more concerning.

### Failure signatures

**Flow too high:**

- media channeling;
- bypass around filter bed;
- cracked ceramic element;
- poorly graded or overly coarse sand;
- failed seals.

**Flow too low:**

- excessive fine material;
- surface clogging;
- accumulated sediment;
- biofilm overgrowth;
- blocked outlet/underdrain.

## 5. Ceramic-filter quality assurance

Locally manufactured ceramic filters can be valuable, but evidence strongly supports treating production as a controlled manufacturing process rather than a casual artisan improvisation.

Potters for Peace/Good Foundations guidance describes ceramic pot filters as requiring standardized production, proper pressing and firing, flow-rate testing, and quality control.

### Manufacturing variables that matter

- clay source and composition;
- combustible pore-forming material;
- particle-size distribution of clay and additive;
- material ratio;
- water content;
- forming pressure;
- drying conditions;
- firing temperature profile;
- firing duration;
- cooling rate;
- post-firing handling.

### Visual and structural inspection

Reject elements with:

- through-wall cracks;
- major chips at sealing surfaces;
- distorted seating surfaces;
- obvious firing defects;
- unstable or friable ceramic.

### Acoustic inspection

Some ceramic-production protocols use a simple tap or ring test as a screening method for major cracking. A dull or abnormal sound can trigger rejection or further testing.

This should be treated as a screening step, not a microbiological validation.

### Flow-rate testing

Each ceramic element should be filled and its initial flow measured.

Potters for Peace production systems historically targeted approximately 1.5-2.5 L/h for their specific filter design, while literature shows that acceptable production limits need to be established against actual microbiological performance for the local manufacturing process.

The important rule is:

> Flow rate is a manufacturing consistency metric, not proof of pathogen removal by itself.

### Bubble-point / crack testing

Published ceramic-filter work has proposed bubble-point testing as an additional QC method for unusually high-flow elements, especially when a large pore or crack is suspected.

The project should therefore treat high flow as a trigger for crack investigation rather than assuming higher throughput is automatically better.

## 6. Ceramic-material leaching gate

Ceramic materials themselves can introduce contaminants.

Published work on locally produced ceramic filters has detected initial leaching of metals such as arsenic, manganese, and silver in some systems. Concentrations may decline after flushing, but the result is highly material-specific.

Therefore every new local clay/additive recipe intended for drinking-water research should include:

```text
initial flush water chemistry
repeat chemistry after defined flush volume
selected metals based on clay/mineral source
```

Do not assume fired clay is chemically inert.

## 7. Barrel-scale sampling points

A full research train should use physically distinct sampling locations:

```text
S0 = collected raw water
S1 = after first flush / raw barrel
S2 = after settling
S3 = after roughing filter
S4 = after sand/biosand
S5 = after ceramic/membrane/carbon stage
S6 = after disinfection
S7 = after safe storage interval
```

Sampling after storage is important because recontamination can occur even if treatment initially performs well.

## 8. Sampling cadence

### Commissioning

Sample every stage during initial build validation.

### Early operation

Sample each major stage repeatedly over multiple rainfall events or source batches.

### Stable operation

Reduce frequency only after hydraulic and water-quality behavior has demonstrated stability.

### Triggered sampling

Return to high-frequency testing after:

- heavy rainfall;
- catchment contamination event;
- filter cleaning;
- sand disturbance;
- ceramic replacement;
- unexpected flow change;
- odor/color change;
- storage contamination concern.

## 9. Minimum prototype QA sheet

For each treatment stage record:

| Variable | Why it matters |
|---|---|
| Date/time | traceability |
| Source/event | compare rainfall/source conditions |
| Volume processed | media loading |
| Flow rate | clogging/channeling indicator |
| Turbidity in/out | treatment performance |
| Head/water level | hydraulic condition |
| Visible bypass | structural failure |
| Media condition | maintenance state |
| Last cleaning | lifecycle tracking |
| Microbiology | required for microbial claims |
| Chemistry | required for chemical-removal claims |

## 10. Gate logic

### QA-0 — material provenance

All water-contact materials documented or explicitly classified experimental.

### QA-1 — hydraulic integrity

No leaks, bypass, uncontrolled overflow, or unstable flow path.

### QA-2 — media qualification

Sand/gravel size and washing procedure documented.

### QA-3 — baseline flow

Initial flow recorded for every filter element.

### QA-4 — turbidity performance

Each treatment stage demonstrates measurable and repeatable turbidity behavior.

### QA-5 — failure detection

Operator can identify channeling, clogging, cracking, or bypass from simple observations and measurements.

### QA-6 — microbial validation

Any microbial protection claim requires validated microbiological testing.

### QA-7 — chemical validation

Any chemical-removal or potable-use claim requires contaminant-specific testing.

## 11. Recommended field kit

### Minimum improvised research kit

- clear sample bottles;
- graduated container;
- stopwatch;
- ruler/tape;
- thermometer;
- pH strips or meter;
- turbidity tube;
- notebook/data sheet;
- basic sieves where available.

### Preferred enhanced kit

- portable turbidity meter;
- conductivity/TDS meter;
- digital pH meter;
- chlorine residual test kit where chlorination is used;
- calibrated flow meter or graduated flow vessel;
- standardized sieve set;
- microbiological field test or laboratory access.

## 12. Literature anchors

- WHO, *Water Quality and Health — Review of Turbidity: Information for Regulators and Water Suppliers*: operational turbidity monitoring, with increased frequency where filtration/disinfection performance or rapidly changing source conditions demand it.
- WHO, *Compendium of Drinking-water Systems and Technologies from Source to Consumer* (2025): aim for turbidity below 5 NTU in lower-resource systems and ideally below 1 NTU for effective disinfection.
- *Comparison of Laboratory and Field Methods for Biosand Filter Sand Characterization*, Water 17(18), 2706 (2025): field/lab determination of effective size and uniformity coefficient can differ materially; protocol consistency matters.
- Ahammed & Davra, *Performance evaluation of biosand filter modified with iron oxide-coated sand*, Desalination 276 (2011): documents sieved/washed media and changing flow with filter maturation.
- Potters for Peace / Good Foundations ceramic water filter production resources: standardized production and filter-specific flow testing are central to reliable local manufacture.
- *Best Practice Recommendations for Local Manufacturing of Ceramic Pot Filters for Household Water Treatment* (2011): manufacturing and quality-control framework.
- Matthies et al., *Morphology, composition and performance of a ceramic filter for household water treatment in Indonesia* (2015): demonstrates both strong bacterial reduction and the need to evaluate virus performance and material leaching.

## Next pass

1. Develop a low-cost turbidity tube calibration protocol against a portable meter.
2. Define an inexpensive sieve stack using commonly obtainable mesh sizes.
3. Build a standard filter commissioning sheet for barrel-scale deployments.
4. Review microbial field-test options suitable for low-resource monitoring.
5. Review treatment methods for rainwater-specific chemical risks from catchment surfaces and atmospheric deposition.
