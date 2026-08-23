# Alternative Water Systems

Public research and prototype-development repository for **low-cost, passive, modular, and locally repairable alternative water systems** intended for resource-constrained, infrastructure-limited, humanitarian, disaster-recovery, and conflict-affected settings.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active research and prototype-validation program  
**Last documentation review:** 2026-08-23

## Current objective

The repository now centers on a family of alternative water architectures that can preserve or supplement water access when conventional service is unavailable, unreliable, damaged, delayed, or unaffordable.

The active program combines:

- rainwater capture;
- passive atmospheric collection;
- safe storage;
- gravity-driven pretreatment and filtration;
- controlled disinfection where required;
- rubble and locally available structural materials;
- field verification and sanitary inspection;
- WHO/UNICEF-aligned small-supply risk management;
- fail-visible operation and explicit use classification.

The objective is **not one universal purifier**. It is a modular family of systems that can be assembled, adapted, tested, repaired, and scaled while keeping the health-critical water-contact and treatment path controlled.

## Design doctrine

```text
USE LOCAL MASS UPSTREAM
        ↓
CONTROL THE WATER-CONTACT PATH
        ↓
USE EVIDENCE-BACKED TREATMENT
        ↓
STORE SAFELY
        ↓
MONITOR
        ↓
CORRECT / RECLASSIFY
```

Passive systems are prioritized where physics and source-water quality allow because they reduce dependence on grid power, fuel, pumps, moving parts, and specialized maintenance.

Powered systems remain necessary for functions such as desalination, deep pumping, some membrane processes, UV, and high-throughput distribution.

## Prototype and safety boundary

**All systems in this repository are prototypes unless explicitly documented otherwise.**

Designs, calculations, sketches, bills of materials, modeled yields, and performance estimates are research outputs. They are not certified engineering plans, potable-water approvals, public-health determinations, or guarantees of safe drinking water.

Unless a system uses known water-contact materials, appropriate treatment, independent testing, and validation against the intended-use requirements, collected water should be treated as:

> **experimental and non-potable by default.**

Clearer water is not automatically safer water. Modeled output is not measured output.

## Core system architecture

The current reference household architecture is:

```text
RAIN / CHARACTERIZED SOURCE
        ↓
PALLET / TARP / CONTROLLED CATCHMENT
        ↓
SCREEN
        ↓
FIRST FLUSH
        ↓
RAW STORAGE
        ↓
SETTLING / ROUGHING
        ↓
HEALTH-CRITICAL FILTER
        ↓
DISINFECTION IF REQUIRED
        ↓
CLEAN STORAGE
        ↓
CONTROLLED OUTLET
        ↓
MONITOR / CORRECT / RECLASSIFY
```

Supporting infrastructure may use screened rubble, pallets, scrap framing, locally available masonry, barrels of known prior use, and other low-resource structural materials. Rubble and unknown salvage should remain outside the controlled drinking-water contact path unless specifically characterized and isolated.

## WHO / UNICEF alignment

The alternative-water program is being aligned with current WHO and UNICEF principles for emergency household treatment and small water supplies.

The project now uses a risk-management sequence:

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
WU-9 resilience / service transition
```

The repository adapts WHO Water Safety Plan logic to alternative systems through an **Alternative Water Safety Plan (A-WSP)** and uses WHO-style sanitary inspection for rainwater systems.

UNICEF emergency HWTS criteria are used as an external design benchmark for:

- affordability;
- intuitive operation;
- fail-safe / fail-visible behavior;
- durability;
- low logistics footprint;
- safe storage;
- service life and throughput;
- reduced recurring consumables;
- bacteria, virus, and protozoa protection where drinking-water claims are intended.

No project document should imply WHO or UNICEF approval of a prototype.

## Current engineering priorities

### 1. Passive rain collection

The primary low-income architecture no longer assumes that the dwelling has an intact roof, affordable gutter replacement, or a structure suitable for modification.

Reference architecture:

```text
ELEVATED AGED / SALVAGED PALLET OR WOOD FRAME
        ↓
REPLACEABLE WATERPROOF SKIN
        ↓
LOW-EDGE GUTTER OR LINER TROUGH
        ↓
SCREEN
        ↓
FIRST FLUSH
        ↓
CONTINUOUS GRAVITY DROP
        ↓
EXISTING BARREL / CISTERN
        ↓
CONTROLLED OVERFLOW
```

The working design principle is:

```text
storage may exist
+
wood may be abundant
+
roof work may be unaffordable
=
manufacture new catchment area independently of the house
```

The pallet collector must be elevated above the receiving barrel/cistern inlet so the complete transfer path remains gravity-descending. Future drawings should not depict the active pallet collector resting on the ground.

The current sketch contract also explicitly avoids recommending painting, staining, sealing, spraying, or coating the pallet as a routine waterproofing step. The design separates functions:

```text
WOOD = STRUCTURE
LINER = CONTROLLED WATER-CONTACT / WATERPROOF SURFACE
```

The reference pallet lane now uses measured pallet dimensions rather than assuming 4 x 4 ft. A common approximately 48 x 40 in pallet provides about 13.3 ft2 of surface area. At a shallow ~15 degree collector angle, horizontal projected area is about 12.9 ft2, corresponding to about 8.0 gallons theoretical per inch of rain and about 6.4 gallons per inch at an illustrative 80% recovery.

Current pallet research gates include:

- salvage acceptance / repairability;
- elevated structural stability;
- gravity-head relationship to storage;
- liner durability;
- hydraulic capacity;
- first-flush performance;
- actual collection efficiency;
- wind and ballast behavior;
- resident maintenance;
- new-material cost and salvage fraction;
- water-quality/use classification.

The goal is not to make aged pallet wood itself potable-safe. The wood is treated primarily as abundant structure, while the water-contact surface remains controlled and replaceable.

See:

- [Pallet Rain Collector Prototype](docs/pallet-rain-collector-prototype.md)
- [Pallet Rain Collector Sketch Specification](docs/pallet-rain-collector-sketch-specification.md)

### 2. Rubble-integrated support systems

Screened debris can serve as:

- ballast;
- foundations;
- barrel stands;
- erosion-control aprons;
- drainage sub-base;
- retaining structure;
- thermal/shading mass.

Core rule:

```text
RUBBLE / SCRAP STRUCTURE
        ↓
CONTROLLED LINER / BARRIER
        ↓
CONTROLLED WATER PATH
```

Unscreened demolition debris is not assumed safe as potable-path filter media or storage material.

### 3. Barrel-bank storage

The current reference bank uses 1-4 approximately 200-L drums on a broad screened-rubble pad with a continuous load spreader, independent valves, raw/clean separation, and controlled overflow.

A full four-drum bank approaches 0.9 tonnes, so low, broad support and settlement control are prioritized over elevated towers.

### 4. Health-critical filtration

Current preferred architecture:

```text
PASSIVE PRETREATMENT
+
STANDARDIZED GRAVITY UF / MEMBRANE ELEMENT
+
SAFE STORAGE
```

Parallel fallback/research lanes include controlled ceramic, biosand, and gravity-driven membrane systems.

Technology class alone is not accepted as evidence of pathogen protection. Exact product or system performance must be documented.

### 5. Fail-visible operation

Every treated-water outlet should have an explicit state:

```text
GREEN  = validated for stated use
AMBER  = restricted / treatment required
RED    = do not use
GRAY   = status unknown
```

Unknown does not default to safe. Critical failures should produce visible downgrade and, where practical, physical outlet lockout.

### 6. Usability

The integrated prototype is being designed so an unfamiliar responder can operate it after brief instruction using pictorial SOPs.

Current internal usability target:

```text
>= 18/20 task score
AND
zero critical errors
```

## Passive atmospheric collection lanes

Atmospheric collection remains an active secondary research area.

### Radiative dew

```text
T_surface < T_dewpoint
```

Research focuses on surface temperature, emissivity, sky exposure, humidity, wind, fouling, and yield per area.

### Ground-coupled condensation

The earlier P2 ground-condenser architecture remains an experimental lane using a buried/shaded intake, closed-loop ground heat sink, radiator heat exchanger, and passive/solar-assisted exhaust.

It remains **non-potable experimental hardware** unless the water-contact path is independently validated.

### Fog / high-humidity interception

Fog and mesh-based collection remain site-dependent research lanes requiring local meteorological evidence.

## Contested operational zones

A dedicated research sector addresses WASH continuity where conflict, infrastructure damage, displacement, access restrictions, or supply-chain failure disrupt normal water systems.

The sector is **actor-neutral and civilian-outcome focused**. It is intended for legitimate responders preserving civilian water and sanitation access under applicable law and humanitarian principles.

It does not provide guidance for:

- denying water access;
- poisoning or contaminating water;
- targeting water infrastructure;
- disguising military capability as humanitarian infrastructure;
- unrelated tactical movement, evasion, or force-protection operations.

The primary current case study is Gaza, with regional transfer checks planned for other conflict- and disaster-affected environments.

See:

- [Contested Operational Zones](docs/contested-operational-zones/README.md)
- [Phased Execution Roadmap](docs/contested-operational-zones/phased-execution-roadmap.md)
- [WHO / UNICEF Alternative Water Systems Alignment](docs/contested-operational-zones/who-unicef-alternative-water-systems-alignment.md)
- [Alternative Water Safety Plan Template](docs/contested-operational-zones/alternative-water-safety-plan-template.md)

## Current validation stack

The repository now separates engineering maturity from water-use claims.

### Engineering

```text
G0 literature / mechanism
G1 environmental feasibility
G2 bench prototype
G3 mass / energy / hydraulic balance
G4 resident-buildable prototype
G5 water-quality gate
G6 comparative utility
```

### Water-use classification

```text
REJECT
NON-POTABLE / BOUNDED USE
TREATMENT REQUIRED
TREATMENT RESEARCH ONLY
VALIDATED FOR INTENDED USE
```

### WHO/UNICEF-aligned management

```text
SANITARY INSPECTION
+
A-WSP
+
OPERATIONAL MONITORING
+
CORRECTIVE ACTION
+
VERIFICATION
```

## Current documentation

### Core methodology

- [Alternative Water Collection Methodology](docs/alternative-water-collection-methodology.md)
- [Field Assessment Framework](docs/field-assessment-framework.md)
- [Literature Review](docs/literature-review.md)
- [Annotated Bibliography](docs/bibliography.md)
- [Pallet Rain Collector Prototype](docs/pallet-rain-collector-prototype.md)
- [Pallet Rain Collector Sketch Specification](docs/pallet-rain-collector-sketch-specification.md)
- [Barrel-Scale Filtration Roadmap](docs/barrel-scale-filtration-roadmap.md)
- [Field Validation and Filter QA](docs/field-validation-and-filter-qa.md)
- [Microbial Field Testing and Rainwater Chemical Risk](docs/microbial-field-testing-and-rainwater-chemical-risk.md)

### Contested-zone / alternative-system program

- [Sector Overview](docs/contested-operational-zones/README.md)
- [Phased Execution Roadmap](docs/contested-operational-zones/phased-execution-roadmap.md)
- [Gaza WASH Literature Review](docs/contested-operational-zones/gaza-regional-wash-literature-review.md)
- [Gaza Rainfall and Humidity](docs/contested-operational-zones/gaza-rainfall-humidity-quantification.md)
- [Gaza Yield and Storage Sizing](docs/contested-operational-zones/gaza-monthly-yield-and-storage-sizing.md)
- [Rubble as WASH Construction Material](docs/contested-operational-zones/rubble-as-wash-construction-material.md)
- [Rubble-Integrated WASH Prototype](docs/contested-operational-zones/rubble-integrated-wash-prototype.md)
- [Four-Pallet Wind / Ballast Sizing](docs/contested-operational-zones/four-pallet-wind-ballast-sizing.md)
- [Barrel-Bank Load / Stability](docs/contested-operational-zones/barrel-bank-load-stability.md)
- [Passive WASH Resilience Literature Note](docs/contested-operational-zones/passive-wash-resilience-literature-note.md)
- [WHO / UNICEF Alignment](docs/contested-operational-zones/who-unicef-alternative-water-systems-alignment.md)
- [WHO-Style Sanitary Inspection](docs/contested-operational-zones/who-style-sanitary-inspection-pallet-rubble-rain-collector.md)
- [Alternative Water Safety Plan](docs/contested-operational-zones/alternative-water-safety-plan-template.md)
- [UNICEF HWTS Prototype Scorecard](docs/contested-operational-zones/unicef-hwts-prototype-scorecard.md)
- [Health-Critical Filter Selection Matrix](docs/contested-operational-zones/health-critical-filter-selection-matrix.md)
- [Fail-Safe and Fail-Visible Design](docs/contested-operational-zones/fail-safe-and-fail-visible-design.md)
- [Pictorial SOP and Usability-Test Protocol](docs/contested-operational-zones/pictorial-sop-and-usability-test-protocol.md)

## Immediate next passes

1. Freeze pallet P0 salvage acceptance sheet and repair classes.
2. Freeze FF-M1 manual and FF-F1 floating-ball first-flush designs for pallet-scale catchments.
3. Build a low-material liner-fold gutter variant and compare it with split-PVC guttering.
4. Build contamination-isolated barrel manifold details.
5. Complete actual BOM / lifecycle cost model for one-, two-, and four-pallet systems.
6. Run durability-cycle protocol for aged wood, liner, fasteners, and gutter attachments.
7. Freeze a specific health-critical filter candidate from product-level evidence.
8. Build integrated household bench architecture.
9. Continue Gaza hourly climate / atmospheric-water analysis.
10. Clean and normalize older case-study documentation and references.

## Public-interest research boundary

This repository supports public-health research, environmental-health research, WASH engineering, physics, open methods, and reproducible prototype development.

Field deployments must consider property permission, structural stability, flood/drainage hazards, excavation and utilities, environmental rules, sanitation, treatment requirements, local codes, and public-health oversight.

No prototype should replace an established safer source merely because it produces measurable water.
