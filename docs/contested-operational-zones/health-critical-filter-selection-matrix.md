# Health-Critical Filter Selection Matrix

## Purpose

This pass addresses the highest-priority gap identified in the UNICEF emergency HWTS scorecard: select low-energy treatment options that can serve as the **health-critical barrier** downstream of improvised collection, settling, and storage.

The guiding architecture is:

```text
LOCAL / IMPROVISED COLLECTION
        ↓
PASSIVE PRETREATMENT
        ↓
CONTROLLED HEALTH-CRITICAL FILTER
        ↓
VALIDATED DISINFECTION IF REQUIRED
        ↓
SAFE STORAGE
```

The goal is not to declare one universal filter. It is to define which technologies are credible for which hazards, what evidence tier they require, and where they fail.

---

## 1. External performance benchmark

WHO's International Scheme to Evaluate Household Water Treatment Technologies independently evaluates microbial performance of household treatment products.

WHO performance levels are based on log-reduction performance against bacteria, viruses, and protozoa. WHO's 2026 Rounds III-IV report expanded the Scheme to 51 evaluated products.

WHO also warns that technologies need to be used correctly and consistently; product-level performance does not by itself prove safe system-level performance.

The repo therefore uses this evidence hierarchy:

```text
T0 — improvised particulate control only
T1 — locally controlled filter with measured performance
T2 — standardized commercial product with independent evidence
T3 — WHO-evaluated or equivalent independently validated product
```

---

# 2. Candidate technologies

This pass compares:

1. biosand / slow sand;
2. locally produced ceramic;
3. standardized ceramic filter;
4. gravity hollow-fiber / ultrafiltration;
5. gravity-driven membrane (GDM / low-pressure UF family);
6. activated carbon as a secondary adsorptive stage;
7. multi-barrier hybrid train.

Activated carbon is included because it may be useful downstream, but it is **not** considered a primary pathogen barrier.

---

# 3. Decision matrix

Scoring:

```text
5 = strong fit
4 = good fit
3 = conditional
2 = weak
1 = poor
0 = unsuitable for that criterion
```

| Criterion | Biosand | Local ceramic | Standard ceramic | Gravity hollow-fiber/UF | Gravity-driven membrane | Activated carbon |
|---|---:|---:|---:|---:|---:|---:|
| No external power | 5 | 5 | 5 | 5 | 5 | 5 |
| Low consumables | 5 | 4 | 4 | 4 | 5 | 2 |
| Local build potential | 5 | 4 | 2 | 1 | 1 | 2-4 |
| Logistics footprint | 2 | 3 | 4 | 5 | 4 | 4 |
| Flow/throughput | 3 | 2-3 | 3 | 4 | 3-4 | 4 |
| Bacteria control potential | 3 | 3 | 4 | 5 | 5 | 1 |
| Protozoa control potential | 3 | 3 | 4 | 5 | 5 | 1 |
| Virus control potential | 1-2 | 1-2 | 1-3 | 2-5 product-dependent | 2-5 membrane-dependent | 0-1 |
| Turbidity tolerance | 3 | 2 | 2 | 2 | 2-3 | 2 |
| Maintenance simplicity | 4 | 4 | 4 | 3 | 4 potential | 4 |
| Fail-visible behavior | 2 | 2 | 2-3 | 3 | 3 | 1 |
| Local repairability | 5 | 4 | 2 | 2 | 1-2 | 3 |
| Salinity removal | 0 | 0 | 0 | 0 | 0 | 0 |
| Nitrate removal | 0 | 0 | 0 | 0 | 0 | 0-1 |
| Dissolved-metal removal | 0-1 | 0-1 | 0-1 | 0-1 | 0-1 | 1-4 compound-dependent |

No passive microfilter in this table should be assumed to solve Gaza's brackish/saline groundwater problem.

---

# 4. Biosand / slow sand

## Strengths

- no electricity;
- locally constructible;
- low recurring consumables;
- robust against supply-chain disruption;
- familiar gravity hydraulics;
- can reduce turbidity and microbial load.

## Weaknesses

- bulky and difficult to transport;
- media grading matters;
- performance changes during maturation and after disturbance;
- virus reduction is generally the weakest microbial dimension;
- cleaning can alter performance;
- output varies among locally constructed systems.

## Best role

```text
PRETREATMENT / PRIMARY BIOLOGICAL FILTRATION
```

rather than sole health-critical barrier where comprehensive pathogen protection is required.

## Gaza fit

Strong where:

- sand can be graded and washed;
- units remain relatively stationary;
- water is not highly saline/chemically contaminated;
- a downstream disinfection or stronger barrier remains available.

Weak where repeated displacement requires frequent transport.

### Current recommendation

```text
KEEP AS T1/T2 SUPPORTING FILTER
DO NOT FREEZE AS SOLE FINAL BARRIER
```

---

# 5. Locally produced ceramic filters

## Strengths

- gravity-driven;
- potentially locally manufacturable;
- compact compared with biosand;
- relatively intuitive operation;
- low energy demand.

## Weaknesses

WHO evaluation work has documented substantial variability among household water-treatment products and manufacturing units. For locally produced ceramic systems, key concerns include:

- crack formation;
- firing variability;
- pore-size variability;
- flow inconsistency;
- possible leaching from clay/additives;
- uncertain virus performance;
- quality-control dependence.

## Best role

```text
CONTROLLED LOCAL FILTER
```

only when manufacturing QA is documented.

## Gaza fit

Potentially attractive if local ceramic production exists or can be supported, but the conflict environment makes production consistency and testing difficult.

### Current recommendation

```text
T1 RESEARCH LANE
NOT PRIMARY DEFAULT UNTIL QA IS DEMONSTRATED
```

---

# 6. Standardized ceramic filter

## Strengths

- gravity operation;
- compact;
- generally simple use;
- easier procurement/QA than improvised ceramic;
- low daily energy burden.

## Weaknesses

- imported replacement dependence;
- cracks may increase flow without obvious loss of user confidence;
- virus protection may be limited depending on the exact product;
- chemical contaminants remain untreated.

## Required controls

- exact product/manufacturer identified;
- independent microbial data;
- baseline flow documented;
- crack/impact inspection;
- abnormal high-flow trigger;
- post-storage protection.

### Current recommendation

```text
T2 CANDIDATE
```

for household systems where a validated product can be sourced.

---

# 7. Gravity hollow-fiber / ultrafiltration

## Strengths

UNICEF's filter product guide rates gravity membrane filters strongly on microbial protection compared with many other household filter classes.

Potential advantages:

- no electric pump when sufficient gravity head exists;
- compact imported component;
- high surface area;
- strong bacteria/protozoa removal potential;
- some products provide substantial virus reduction, depending on membrane rating and validation;
- can fit directly between raw and clean barrels.

## Weaknesses

- susceptible to clogging without pretreatment;
- backflush/cleaning may be required;
- membrane damage may not always be obvious;
- product-specific performance varies substantially;
- some membrane products evaluated by WHO have failed minimum performance criteria;
- dissolved chemicals and salinity pass through typical UF membranes.

WHO's product-evaluation history is important here: **membrane technology class alone is not evidence of safe performance**. Exact product validation is necessary.

## Gaza fit

This is a strong architecture for contested-zone deployment because it follows the project's core doctrine:

```text
IMPORT PRECISION
SOURCE MASS LOCALLY
```

Local rubble, pallets, barrels, sand, and settling can protect a compact standardized membrane element.

### Current recommendation

```text
PRIMARY T2/T3 CANDIDATE
```

provided exact product evidence is documented.

---

# 8. Gravity-driven membrane (GDM)

UNICEF has investigated gravity-driven membrane HWTS specifically because conventional ultrafiltration products often require backflushing. UNICEF describes a GDM concept in which biofilm formation can stabilize membrane operation and reduce or eliminate that maintenance burden.

## Strengths

- gravity driven;
- potentially very low maintenance;
- no powered backflush requirement in the intended concept;
- compact health-critical barrier;
- strong fit with safe-storage integration;
- aligns directly with UNICEF emergency design objectives.

## Weaknesses

- less field-standardized than mature commercial gravity filters;
- exact membrane and operating conditions matter;
- startup/maturation may affect flux;
- source turbidity and temperature can affect performance;
- procurement may be specialized;
- salinity/nitrate are not removed.

## Gaza fit

Conceptually excellent for:

```text
settling barrel
→ roughing filter
→ GDM module
→ clean barrel
```

because the system can stay passive while using local structures upstream.

### Current recommendation

```text
PRIORITY RESEARCH CANDIDATE
```

but not yet the default field technology without a specific validated implementation.

---

# 9. Activated carbon

## Strengths

- passive gravity use;
- taste/odor improvement;
- useful for selected organic contaminants when standardized media is appropriate;
- compact.

## Weaknesses

- not a reliable standalone microbial barrier;
- performance is compound-specific;
- ordinary charcoal is not equivalent to activated carbon;
- exhausted media may continue to pass water without obvious warning;
- replacement media are recurring consumables;
- carbon beds can support microbial growth if poorly managed.

### Current recommendation

```text
SECONDARY / CONTAMINANT-SPECIFIC STAGE ONLY
```

never the sole pathogen barrier.

---

# 10. Hybrid multi-barrier option

The strongest fit for the WASH architecture is not one filter, but a staged system:

```text
RAIN / CHARACTERIZED SOURCE
        ↓
SCREEN + FIRST FLUSH
        ↓
RAW STORAGE / SETTLING
        ↓
ROUGHING FILTER
        ↓
OPTIONAL BIOSAND / SAND
        ↓
STANDARDIZED GRAVITY MEMBRANE OR CERAMIC
        ↓
VALIDATED DISINFECTION IF REQUIRED
        ↓
CLEAN STORAGE
```

This allows cheap/local stages to remove solids while preserving the imported precision component for the health-critical barrier.

---

# 11. Gaza source-water constraint matrix

| Source | Main concern | Passive microfilter useful? | Additional requirement |
|---|---|---|---|
| Direct rainwater | microbes, dust, roof/material chemistry | yes | first flush + source/material QA + disinfection as required |
| Trucked/desalinated water | recontamination during transport/storage | yes | safe storage + verification |
| Protected freshwater well | microbes + local chemistry | yes conditionally | chemistry screen |
| Brackish/saline well | salinity, nitrate, microbes | only for microbes | desalination/specific treatment required |
| Floodwater | extreme microbial/chemical contamination | poor default source | avoid/reject unless rigorous treatment available |
| Surface water | turbidity + pathogens + chemistry | yes after pretreatment | strong multi-barrier treatment |
| Atmospheric condensate | surface contamination, storage contamination | yes conditionally | material QA + disinfection/storage verification |

---

# 12. Throughput requirement

UNICEF's emergency HWTS design target cites approximately:

```text
family of 5
x 2.5 L/person/day
≈ 12.5 L/day
≈ 4.5 m3/year
```

The health-critical element should therefore be screened for at least:

```text
>= 15 L/day nominal household drinking/cooking throughput
```

with margin for cleaning, aging, and treatment losses.

Preferred prototype target:

```text
20-30 L/day sustained clean-water output
```

for one household module.

This is a treatment target, not a rainwater collection target.

---

# 13. Head requirement

A passive gravity filter must be compatible with the barrel-bank architecture.

Target design envelope:

```text
0.3-1.0 m available water head
```

If an exact product requires substantially more pressure, it is a poor fit for the passive household lane unless a hand pump or other non-grid mechanism is explicitly accepted.

---

# 14. Fail-visible selection criterion

The selected health-critical filter should score well on failure visibility.

Preferred characteristics:

- flow decreases as clogging develops;
- integrity checks are possible;
- abnormal high flow can be detected;
- element can be visually inspected;
- seals are accessible;
- raw/clean fittings cannot be easily reversed;
- maintenance state can be recorded;
- end-of-life criterion exists.

Avoid systems where performance can silently disappear while flow remains normal.

---

# 15. Chemical-treatment boundary

None of the main candidates in this matrix should be assumed to remove:

- seawater salinity;
- high chloride;
- nitrate;
- many dissolved metals;
- PFAS;
- solvents;
- fuel contamination.

Therefore the source-risk gate remains upstream of filter selection.

For Gaza this is critical because groundwater salinity and nitrate are established regional problems.

The correct rule is:

```text
MICROBIAL FILTER SELECTION
DOES NOT OVERRIDE
SOURCE CHEMISTRY REJECTION
```

---

# 16. Recommended prototype lanes

## HC-A — lowest-import lane

```text
settling
→ biosand
→ validated disinfection
→ safe storage
```

Use where imported membranes are unavailable and local media quality can be controlled.

Classification:

```text
T1/T2 depending validation
```

## HC-B — compact humanitarian lane

```text
settling / roughing
→ standardized gravity ceramic or UF element
→ validated disinfection if product evidence/source risk requires
→ safe storage
```

Classification:

```text
preferred near-term T2/T3 candidate
```

## HC-C — UNICEF-aligned research lane

```text
settling / roughing
→ gravity-driven membrane
→ safe storage
```

with disinfection added if system/product evidence does not support the required protection level.

Classification:

```text
priority research lane
```

---

# 17. Selection gate

Before a filter is frozen into the integrated bench prototype, document:

```text
manufacturer / build method
exact model
technology class
independent microbial evidence
WHO evaluation status if any
bacteria performance
virus performance
protozoa performance
nominal flow
minimum head
cleaning method
replacement interval
consumables
failure indicator
safe-storage interface
chemical limitations
cost
local availability
```

No product should be selected solely because its marketing description says "membrane," "ceramic," or "purifier."

---

# 18. Current engineering decision

For the WASH contested-zone household prototype:

### First-choice architecture

```text
PASSIVE PRETREATMENT
+
STANDARDIZED GRAVITY UF / MEMBRANE HEALTH-CRITICAL ELEMENT
+
SAFE STORAGE
```

### Parallel fallback lane

```text
BIOSAND / CONTROLLED CERAMIC
+
VALIDATED DISINFECTION
+
SAFE STORAGE
```

### Research lane

```text
GRAVITY-DRIVEN MEMBRANE (GDM)
```

The exact commercial or locally produced product remains **unfrozen** until product-level evidence, availability, and cost are reviewed.

---

# 19. Evidence anchors

- WHO, *International Scheme to Evaluate Household Water Treatment Technologies: Results of Rounds III and IV* (2026): 21 products evaluated in Rounds III-IV; 51 total products evaluated under the Scheme.
- WHO, evaluated-product database: WHO performance levels are based on bacterial, viral, and protozoan log-reduction criteria; some membrane and ceramic products have failed or had undetermined performance, demonstrating the need for exact-product evaluation.
- WHO Round II: documented substantial unit-to-unit performance variability among some household treatment products.
- UNICEF, *Household Water Treatment Filters Product Guide* (2020): compares ceramic, gravity membrane, pumping membrane, biosand, solar, and multi-step systems across protection, flow, transportability, lifetime, setup, O&M, price, and safe storage.
- UNICEF Office of Innovation, *HWTS in Emergency Settings*: identifies gravity-driven membrane filtration as a research direction intended to reduce clogging/backflush burden while preserving gravity operation.

---

# 20. Next pass

Proceed to **Priority 2 — fail-safe / fail-visible design**.

Develop a field architecture where:

```text
FILTER FAILURE
OR UNKNOWN STATUS
        ↓
VISIBLE / PHYSICAL WARNING
        ↓
OUTLET DOWNGRADE OR LOCKOUT
        ↓
REINSPECTION / RETEST
```

The goal is to approach UNICEF's fail-safe requirement even when using simple humanitarian hardware.
