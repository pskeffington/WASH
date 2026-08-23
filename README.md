# Alternative Water Collection Systems

Public research and prototype-development repository for **low-cost alternative water collection methods** intended for resource-constrained, rural, underserved, and infrastructure-limited settings.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active prototype, physics, WASH-methodology, and field-validation research scaffold  
**Last documentation review:** 2026-08-23

## Purpose

This repository investigates whether water can be collected, recovered, stored, or supplemented using inexpensive systems built from common, reused, salvaged, or locally obtainable materials.

The active research focus is not a single geography or one type of WASH infrastructure. It is the development of **alternative water collection systems that can be built, tested, repaired, and evaluated with limited resources**.

Candidate settings include:

- low-income rural communities;
- isolated households and settlements;
- communities with intermittent or unreliable water service;
- humanitarian or disaster-recovery settings;
- agricultural or non-potable water-support applications;
- locations where conventional infrastructure is difficult, delayed, or cost-prohibitive.

McDowell County, West Virginia and earlier Bolivia WASH work provide field context and case-study material, but the methods are intended to be evaluated as transferable prototypes rather than location-specific prescriptions.

## Prototype and safety boundary

**All systems in this repository are prototypes unless explicitly documented otherwise.**

Repository designs, calculations, sketches, bill-of-materials concepts, and performance estimates are research outputs. They are not certified water systems, engineering plans, plumbing approvals, public-health determinations, or guarantees of safe drinking water.

Unless a system has been built with known food-contact materials, appropriately treated, independently tested, and validated against applicable water-quality requirements, collected water should be treated as:

> **experimental and non-potable by default.**

Particular caution applies to salvaged components. Automotive radiators, used tanks, roofing materials, recycled tubing, metal fittings, drums, and other scrap may contain residual coolant, oils, metals, lead-bearing solder, corrosion products, plasticizers, biological contamination, or unknown prior-use residues. A component that is thermally useful is not automatically safe for drinking-water contact.

No prototype should replace an established safe water source merely because it produces measurable water.

## Research question

**How can basic thermodynamics, atmospheric moisture, precipitation, terrain, groundwater/soil temperature, solar energy, and locally available materials be combined into low-cost water-collection systems whose performance can be measured and reproduced?**

The repository emphasizes experimentally testable questions:

- How much water can a system actually collect per hour, day, month, and season?
- What environmental conditions control performance?
- Which components are the true thermal or hydraulic bottlenecks?
- Can recovered or inexpensive materials reduce construction cost without creating unacceptable contamination risk?
- Can two or three residents construct and maintain a useful prototype with ordinary tools?
- At what point is an alternative collector less useful than conventional rain capture, delivered water, repaired infrastructure, or another established option?

## Active methodology lanes

### 1. Rainwater capture

Rain remains the highest-volume passive atmospheric water source in many humid regions. Research includes roof and panel catchment, first-flush separation, storage, overflow management, debris exclusion, and comparison of liters captured per unit area and rainfall depth.

Rain collection provides an important baseline against which more experimental atmospheric systems should be judged.

### 2. Radiative dew collection

Thin, low-thermal-mass surfaces can cool through nighttime long-wave radiation. Condensation becomes possible when collector surface temperature falls below atmospheric dew point:

```text
T_surface < T_dewpoint
```

Prototype work examines surface material, emissivity, insulation, sky exposure, panel angle, drainage, wind, cloud cover, and liters collected per square meter.

### 3. Ground-coupled atmospheric condensation

Humid air can be cooled against a ground-derived thermal sink. The current prototype architecture uses:

```text
buried/shaded air intake
        -> 55-gallon HDPE drum
        -> salvaged automotive radiator heat exchanger
        -> condensate tray
        -> collection vessel
        -> passive or solar-assisted exhaust chimney
```

A separate closed-loop buried PEX field transfers heat from the radiator into cooler soil. The radiator functions as an experimental condenser rather than a potable-water-certified component.

Current P2 design basis:

- one 55-gallon HDPE drum;
- approximately 20 x 18 in automotive radiator core;
- 8 in smooth-wall buried/shaded air intake;
- approximately 25-40 ft intake pre-cooler;
- approximately 3 x 50 ft parallel 3/4 in PEX ground loops;
- 4-6 ft target hydronic burial depth where site conditions allow;
- 45-60 CFM design airflow;
- approximately 2-4 L/min closed-loop coolant flow;
- radiator target approximately 55-58 F under favorable summer conditions;
- experimental summer collection target approximately 1-2.5 L/day, with higher short-duration output possible under favorable dew-point conditions.

These values are design hypotheses until verified by field measurements.

### 4. Stream- or spring-coupled condensation

Where a naturally cold stream or spring is available and lawful access is established, moving water may serve as a heat sink for a **closed-loop** condenser.

Stream water and collected condensate should remain physically separated. The research question is whether the local water body can remove enough heat to keep a condensation surface below atmospheric dew point without contaminating the collected water.

### 5. Solar-assisted passive airflow

Solar heat is most useful on the **exhaust side**, where it can strengthen stack effect and increase airflow across a cold condenser.

Heating humid inlet air alone does not raise its dew point unless additional moisture is added; it usually increases sensible cooling demand. Current designs therefore investigate dark solar chimneys and passive reflectors after the condenser instead of heating the incoming air before cooling it.

### 6. Fog and high-humidity interception

Mesh, screen, fibrous surfaces, and terrain-assisted fog interception remain a separate collection lane. These systems should be evaluated by local fog frequency, wind, droplet size, collection geometry, fouling, and water-quality characteristics.

## Physics foundation

### Dew point

Condensation requires:

```text
T_condenser < T_dewpoint
```

Relative humidity alone is insufficient for design. Heating moist air lowers relative humidity but, absent moisture addition or removal, leaves dew point approximately unchanged.

### Moisture balance

The theoretical condensate rate is determined from the change in humidity ratio:

```text
m_dot_water = m_dot_dry_air * (omega_in - omega_out)
```

where `omega` is kilograms of water vapor per kilogram of dry air.

### Thermal balance

The cold sink must absorb both sensible heat from cooling the air and latent heat released during condensation:

```text
Q_total = Q_sensible + Q_latent + environmental gains
```

with:

```text
Q_sensible = m_dot_air * Cp_air * DeltaT
Q_latent   = m_dot_water * h_fg
```

Near ordinary environmental temperatures, condensing one kilogram of water releases roughly 2.4 MJ of latent heat. Therefore meaningful atmospheric water production requires meaningful heat rejection; a collector is fundamentally a heat exchanger.

### Ground-loop balance

For a closed water-based coolant loop:

```text
Q_ground = m_dot_coolant * Cp_water * (T_return - T_supply)
```

This quantity should be measured rather than assumed.

## Prototype development gates

Every prototype should advance through explicit gates.

### G0 - literature and mechanism

Document the physical mechanism, comparable systems, known limits, and plausible failure modes.

### G1 - environmental feasibility

Measure the local variables that govern the mechanism. Depending on system type, these may include air temperature, relative humidity, dew point, soil temperature, stream temperature, rainfall, cloud cover, wind, or fog frequency.

### G2 - bench prototype

Demonstrate the mechanism with the smallest practical system. Do not scale on theoretical yield alone.

### G3 - thermal and mass balance

Measure input and output temperatures, humidity, airflow, coolant flow where applicable, and actual collected water. Compare predicted condensate with recovered condensate.

### G4 - resident-buildable prototype

Determine whether two or three people using common tools and locally obtainable materials can build, operate, clean, and repair the system.

### G5 - water-quality gate

Characterize material-contact risks and test collected water before proposing any use beyond clearly bounded experimental or non-potable applications.

### G6 - comparative utility

Compare cost, labor, liters produced, reliability, maintenance, seasonal availability, and water-quality burden against established alternatives such as rain capture, repaired service, wells, hauled water, or other approved sources.

## Scrap and locally available materials

The project intentionally evaluates materials that may already exist in resource-constrained settings, including:

- food-grade HDPE drums;
- smooth PVC or HDPE pipe;
- PEX tubing;
- salvaged lumber and structural framing;
- gutters and drainage fittings;
- screens and filters;
- used automotive heat exchangers for **non-potable experimental prototypes only**;
- recovered sheet metal or roofing where material history is known;
- common insulation;
- gravity-fed plumbing components;
- low-power pumps or fans where passive operation is insufficient.

The objective is not to use scrap indiscriminately. The objective is to distinguish between components that can be safely reused structurally or thermally and components whose prior use makes them unsuitable for water contact.

## Measurement standards

Prototype reports should record, as applicable:

- date and site class;
- ambient air temperature;
- relative humidity;
- calculated dew point;
- condenser surface temperature;
- inlet and outlet air temperature/RH;
- airflow;
- coolant supply and return temperature;
- coolant flow;
- soil or water-sink temperature;
- rainfall/fog/cloud conditions;
- runtime;
- collected volume;
- collection rate in L/h;
- normalized yield where applicable in L/m2/day;
- known material-contact risks;
- maintenance or fouling observations.

Do not report modeled output as measured output.

## Current development priority

The current engineering prototype is a **ground-coupled atmospheric condenser** designed around components that are widely obtainable:

1. shaded or buried smooth-wall air intake for sensible pre-cooling;
2. 55-gallon blue HDPE drum as an enclosure/plenum;
3. cleaned scrap automotive radiator as the experimental condenser;
4. sloped condensate pan and isolated collection vessel;
5. closed-loop PEX ground heat exchanger;
6. passive stack or solar-assisted exhaust draft;
7. temperature, humidity, coolant-flow, airflow, and water-volume instrumentation.

The development objective is to verify whether the apparatus can hold the radiator several degrees below dew point while processing enough humid air to produce useful water without exhausting the ground thermal sink.

## Geographic case studies

Earlier repository work on Bolivia, including the Cochabamba-Sucre corridor, remains useful as WASH context and as a source of questions about service reliability, drought, spatial inequity, and community water systems. Those materials should now be interpreted as **case-study and legacy research lanes**, not as the primary repository identity.

McDowell County, West Virginia is being used as a current humid Appalachian reference environment for alternative collection calculations and prototype planning. Site-specific claims remain provisional until measured locally.

## Public-interest research boundary

This repository supports public-health research, environmental-health research, physics and engineering prototyping, open methods, and reproducible documentation.

It does not provide:

- certified engineering designs;
- guaranteed water production;
- potable-water certification;
- regulatory approval;
- household-specific safety determinations;
- instructions to bypass public-health advisories;
- authority to divert streams, excavate property, modify utilities, or construct regulated water systems;
- a substitute for reliable municipal, utility, well, or other approved drinking-water service.

Field deployments must consider property permission, excavation hazards, buried utilities, stream and environmental rules, electrical safety, structural stability, freezing, sanitation, local codes, and applicable public-health requirements.

## Repository documentation

Active methodology documents should center on alternative collection mechanisms, prototype design, measurement, and validation. Existing Bolivia and corridor documents are retained as historical/case-study research unless explicitly superseded.

Current core files include:

- [Alternative Water Collection Methodology](docs/alternative-water-collection-methodology.md)
- [Field Assessment Framework](docs/field-assessment-framework.md)
- [Literature Review](docs/literature-review.md)
- [Annotated Bibliography](docs/bibliography.md)
- [Public Data Inventory](docs/data-inventory.md)
- [GIS Build Plan](docs/gis-build-plan.md)

## Supported contribution

A reproducible, physics-based research framework for evaluating inexpensive and locally buildable water-collection prototypes, with explicit attention to measured performance, material safety, field maintainability, environmental suitability, and uncertainty.

## Unsupported contribution

No repository prototype should be represented as a proven drinking-water system, certified engineering solution, emergency-water guarantee, regulatory finding, or substitute for independently validated safe-water infrastructure.
