# WASH in Contested Operational Zones

## Scope

This sector addresses water, sanitation, and hygiene continuity where conflict, insecurity, infrastructure damage, displacement, access restrictions, or contested control disrupt normal water systems.

The sector is **actor-neutral and civilian-outcome focused**. It is intended for legitimate responders preserving civilian water and sanitation access under applicable law and humanitarian principles.

The boundary is defined by purpose: **civilian WASH survival, continuity, recovery, and resilient transition**.

## Current sector status

The contested-zone lane has moved beyond initial scoping into an integrated engineering and validation program.

Current work now includes:

- Gaza regional WASH evidence review;
- rainfall, humidity, yield, and storage modeling;
- pallet/rubble rain-collector architecture;
- rubble structural-use controls;
- wind/ballast sizing;
- barrel-bank load and stability analysis;
- passive WASH resilience literature;
- WHO/UNICEF-aligned small-supply management;
- sanitary inspection;
- Alternative Water Safety Plans;
- UNICEF HWTS prototype scoring;
- health-critical filter selection;
- fail-safe / fail-visible operation;
- pictorial SOP and usability testing.

The current program is documented in the [Phased Execution Roadmap](phased-execution-roadmap.md).

## Operating model

```text
SOURCE IDENTIFICATION
        ↓
COLLECTION
        ↓
SOURCE / MATERIAL SCREENING
        ↓
PRETREATMENT
        ↓
HEALTH-CRITICAL FILTRATION
        ↓
DISINFECTION AS REQUIRED
        ↓
SAFE STORAGE
        ↓
CONTROLLED DISTRIBUTION
        ↓
MONITOR / CORRECT / RECLASSIFY
```

The system should remain modular so a damaged or unavailable component can be isolated or replaced without collapsing the entire chain.

## Design doctrine

### Preserve existing safe supply first

Do not replace an intact safer source simply because an improvised source is available.

### Use abundant local materials upstream

Good structural roles include:

- screened rubble;
- pallets and scrap framing;
- barrels of known prior use;
- masonry;
- wire and brackets;
- local drainage material.

### Increase control toward the health-critical barrier

```text
LOCAL / IMPROVISED STRUCTURE
        ↓
CONTROLLED WATER-CONTACT PATH
        ↓
EVIDENCE-BACKED TREATMENT
        ↓
SAFE STORAGE
        ↓
VERIFICATION
```

### Separate raw and treated water

Raw and treated storage should remain physically and visually distinct.

### Design for partial failure

The system should degrade into a safer bounded-use state rather than silently remaining labeled as safe.

## WHO / UNICEF alignment

The sector now uses a compact management sequence:

```text
WU-0 context
WU-1 sanitary inspection
WU-2 system design
WU-3 operational monitoring
WU-4 treatment evidence
WU-5 safe storage
WU-6 corrective action
WU-7 verification
WU-8 use classification
WU-9 resilience transition
```

See:

- [WHO / UNICEF Alternative Water Systems Alignment](who-unicef-alternative-water-systems-alignment.md)
- [WHO-Style Sanitary Inspection](who-style-sanitary-inspection-pallet-rubble-rain-collector.md)
- [Alternative Water Safety Plan](alternative-water-safety-plan-template.md)
- [UNICEF HWTS Prototype Scorecard](unicef-hwts-prototype-scorecard.md)

## Current reference household architecture

```text
PALLET / SCRAP FRAME
        ↓
KNOWN LINER / BARRIER
        ↓
GUTTER / SCREEN
        ↓
FIRST FLUSH
        ↓
RAW BARREL BANK
        ↓
SETTLING / ROUGHING
        ↓
STANDARDIZED HEALTH-CRITICAL FILTER
        ↓
DISINFECTION IF REQUIRED
        ↓
CLEAN STORAGE
        ↓
STATUS-CONTROLLED OUTLET
```

The strongest current near-term treatment lane is passive pretreatment followed by a standardized gravity UF/membrane element and safe storage. Biosand/controlled ceramic remain fallback or supporting lanes; gravity-driven membrane remains a priority research lane.

See [Health-Critical Filter Selection Matrix](health-critical-filter-selection-matrix.md).

## Passive-system doctrine

Passive systems are attractive in disrupted environments because they reduce dependence on:

- grid electricity;
- fuel supply;
- pumps;
- moving parts;
- specialized maintenance.

This is a resilience argument, not a claim of invisibility or guaranteed protection from surveillance or attack.

See [Passive WASH Resilience Literature Note](passive-wash-resilience-literature-note.md).

## Rubble integration

Conflict debris can be useful structural material when screened and kept outside the health-critical water-contact path.

Preferred roles:

- ballast;
- foundations;
- barrel stands;
- drainage aprons;
- retaining structures;
- erosion control;
- protective mass.

Core rule:

```text
RUBBLE / SCRAP STRUCTURE
        ↓
CONTROLLED LINER / BARRIER
        ↓
CONTROLLED WATER PATH
```

See:

- [Rubble as WASH Construction Material](rubble-as-wash-construction-material.md)
- [Rubble-Integrated WASH Prototype](rubble-integrated-wash-prototype.md)
- [Four-Pallet Wind / Ballast Sizing](four-pallet-wind-ballast-sizing.md)
- [Barrel-Bank Load / Stability](barrel-bank-load-stability.md)

## Gaza case study

Gaza remains the primary current contested-zone case study because it combines:

- damaged centralized infrastructure;
- displacement;
- storage constraints;
- groundwater salinity/nitrate concerns;
- winter rainfall;
- high summer humidity;
- fuel/power constraints;
- abundant rubble and salvaged structural material.

The working seasonal architecture is:

```text
WINTER
rain capture
→ raw storage
→ passive pretreatment
→ controlled filtration
→ disinfection if required
→ clean storage

SUMMER
protected/delivered/desalinated sources
+
atmospheric-water research where productive
```

See:

- [Gaza Regional WASH Literature Review](gaza-regional-wash-literature-review.md)
- [Gaza Rainfall and Humidity](gaza-rainfall-humidity-quantification.md)
- [Gaza Monthly Yield and Storage Sizing](gaza-monthly-yield-and-storage-sizing.md)

## Phase gates

The original COZ gates remain the authoritative sector sequence:

```text
COZ-0 context and access
COZ-1 immediate survival water
COZ-2 collection expansion
COZ-3 pretreatment
COZ-4 household/barrel filtration
COZ-5 disinfection
COZ-6 safe storage/distribution
COZ-7 field verification
COZ-8 continuity/redundancy
```

The detailed engineering passes are tracked in the phased roadmap.

## Use classification

Every water stream should be explicitly classified:

```text
REJECT
NON-POTABLE / BOUNDED USE
TREATMENT REQUIRED
TREATMENT RESEARCH ONLY
VALIDATED FOR INTENDED USE
```

No water should be upgraded based on appearance alone.

## Fail-visible operation

Every treated-water outlet should display one of four states:

```text
GREEN  = validated for stated use
AMBER  = restricted / treatment required
RED    = do not use
GRAY   = status unknown
```

Unknown does not default to safe.

Current freeze rules include:

- no status card = not GREEN;
- maintenance automatically produces GRAY;
- positive final microbial result = RED;
- unknown source or barrel history = not GREEN;
- raw and clean outlets must remain distinct;
- drinking outlet must support physical lockout;
- return to GREEN requires documented recommissioning.

See [Fail-Safe and Fail-Visible Design](fail-safe-and-fail-visible-design.md).

## Usability

The system is being designed for unfamiliar responders using low-text pictorial SOPs.

Current internal target:

```text
>=18/20 usability score
AND
zero critical errors
```

See [Pictorial SOP and Usability-Test Protocol](pictorial-sop-and-usability-test-protocol.md).

## Immediate execution queue

1. Freeze FF-M1 and FF-F1 first-flush hydraulic designs.
2. Build contamination-isolated barrel manifold details.
3. Build actual BOM and lifecycle-cost model.
4. Create durability-cycle protocol.
5. Freeze a specific health-critical filter candidate from product-level evidence.
6. Build integrated household bench architecture.
7. Continue hourly Gaza summer atmospheric-water modeling.
8. Normalize older references and remove stale citation artifacts.

## Safety and legal boundary

This sector supports WASH protection, continuity, and recovery for civilians and other protected populations.

It does not provide guidance for:

- denying water access;
- poisoning or contaminating water;
- targeting water infrastructure;
- disguising military capability as humanitarian infrastructure;
- unrelated tactical movement, evasion, or force-protection operations.

Work should comply with applicable public-health requirements, humanitarian principles, environmental rules, and international humanitarian law.

## Sector objective

The objective is a **validated family of low-resource alternative water architectures that legitimate responders can assemble, adapt, test, repair, and scale to preserve civilian water access when normal infrastructure no longer functions reliably.**
