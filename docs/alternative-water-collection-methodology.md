# Alternative Water Collection Methodology

## Purpose

This document defines the active research methodology for low-cost alternative water collection systems developed in this repository. The emphasis is on prototypes that can be assembled from common, salvaged, reused, or locally obtainable materials and evaluated in rural, underserved, low-income, infrastructure-limited, or humanitarian settings.

All systems remain experimental unless independently validated. No design in this repository should be treated as a certified potable-water system, engineering plan, plumbing approval, or guarantee of safe water production.

## Default use boundary

Unless a prototype is built from known food-contact materials and its collected water is independently tested against applicable standards, all recovered water should be treated as experimental and non-potable.

Prototype evaluation should distinguish three separate questions:

1. Can the mechanism physically collect water?
2. Can the system do so at useful volume, cost, and labor burden?
3. Can the resulting water be made safe for its intended use?

A positive answer to the first question does not imply a positive answer to the second or third.

## Design philosophy

Alternative water collection in resource-constrained settings should prioritize:

- simple physical mechanisms;
- repairable construction;
- common hand tools;
- locally available components;
- low operating energy;
- gravity and passive flows where practical;
- explicit measurement of actual output;
- modular scaling;
- clear contamination boundaries;
- comparison against simpler established alternatives.

The project should avoid optimizing for technical novelty when a simpler collection method performs better.

## Prototype classes

### Rainwater capture

Rainwater systems are the primary benchmark for passive water collection because potential volume is often much larger than dew or atmospheric-condensation yield. Prototype variables include catchment area, first-flush separation, debris exclusion, storage, overflow, evaporation, contamination, and seasonal reliability.

### Radiative dew collection

Radiative condensers use nighttime long-wave radiation to cool a surface below atmospheric dew point. Key variables include emissivity, thermal mass, insulation, sky exposure, panel inclination, cloud cover, wind, drainage, and surface cleanliness.

### Ground-coupled atmospheric condensation

Ground-coupled systems use relatively cool soil as a thermal sink. The current prototype combines a buried or shaded air pre-cooler, a 55-gallon HDPE drum, a salvaged automotive radiator, a closed-loop PEX ground field, a condensate tray, and passive or solar-assisted exhaust draft.

The radiator is an experimental heat exchanger only. Used automotive components should not be considered potable-water-safe without material verification and appropriate testing.

### Stream- or spring-coupled atmospheric condensation

A cold stream or spring may serve as a thermal sink through an isolated closed-loop heat exchanger. Source water and condensate must remain separate. Site access, water rights, environmental rules, contamination, flood exposure, and mechanical anchoring all require separate review.

### Fog interception

Mesh and fibrous collectors can recover suspended droplets where fog frequency, wind, and droplet transport are favorable. These systems differ physically from dew condensers because they intercept liquid droplets rather than condensing vapor from air.

### Solar-assisted draft

Solar heating is used preferentially to increase exhaust buoyancy after condensation rather than to heat inlet air. Heating air without adding moisture generally lowers relative humidity but does not increase dew point; therefore inlet heating usually increases sensible cooling burden without increasing available atmospheric water.

## Core physics

### Dew-point condition

Condensation begins only when:

```text
T_surface < T_dewpoint
```

The difference:

```text
DeltaT_dew = T_dewpoint - T_surface
```

should be recorded as a primary performance variable.

### Humidity ratio

Water-production potential should be evaluated from moisture content rather than relative humidity alone:

```text
m_dot_water = m_dot_dry_air * (omega_in - omega_out)
```

where `omega` is humidity ratio.

### Sensible heat

```text
Q_sensible = m_dot_air * Cp_air * (T_in - T_out)
```

### Latent heat

```text
Q_latent = m_dot_water * h_fg
```

Condensing one kilogram of water releases approximately 2.4 MJ of latent heat near ordinary environmental temperatures. This makes heat rejection a central design constraint.

### Closed-loop ground heat transfer

```text
Q_ground = m_dot_coolant * Cp_coolant * (T_return - T_supply)
```

Ground-loop capacity must be measured during operation because nearby soil can warm and reduce performance over time.

## Current ground-coupled prototype

The present P2 concept uses:

- one 55-gallon HDPE drum;
- one approximately 20 x 18 in salvaged radiator core;
- an approximately 8 in smooth-wall humid-air intake;
- approximately 25-40 ft of buried or deeply shaded intake pipe for pre-cooling;
- three parallel 50 ft PEX ground loops, approximately 150 ft total;
- approximately 4-6 ft target burial depth where practical;
- approximately 24-36 in thermal spacing between loop runs where excavation allows;
- approximately 45-60 CFM nominal airflow;
- approximately 2-4 L/min total coolant flow;
- condensate drainage isolated from coolant;
- passive stack or solar-assisted exhaust.

Current water-production values remain design estimates. The apparatus should be scaled only after local measurements establish radiator temperature, dew-point margin, airflow, coolant flow, ground heat rejection, and actual collected volume.

## Prototype gates

### P0 - literature review

Establish prior art, physical mechanism, expected operating envelope, known limitations, and material risks.

### P1 - environmental survey

Measure the site's air temperature, RH, dew point, soil temperature by depth, stream temperature where relevant, rainfall, wind, fog, and seasonal conditions.

### P2 - small-scale mechanism test

Demonstrate measurable water production without assuming scalability.

### P3 - heat and mass balance

Measure the energy and moisture flows through the system. Compare theoretical water removal with actual collected water.

### P4 - resident buildability

Confirm that two or three residents can assemble, clean, repair, and operate the prototype using common tools and reasonable labor.

### P5 - water-quality review

Identify every wetted material, prior-use history, corrosion risk, contaminant pathway, storage condition, and treatment requirement. Testing is required before any potable claim.

### P6 - comparative utility

Compare the prototype with rainwater capture, repaired utility service, wells, hauled water, existing springs, approved treatment systems, or other established options.

## Salvaged-material controls

Salvage should be divided into three classes.

### Structural salvage

Examples include lumber, framing, brackets, stands, external insulation, and supports. These components may be reused when structurally sound and isolated from collected water.

### Thermal or mechanical salvage

Examples include radiator cores, fans, pumps, heat exchangers, coils, and metal panels. These may be suitable for non-potable experimental prototypes but require prior-use review and should not automatically contact finished water.

### Wetted potable-path components

These require the highest standard. Unknown drums, old automotive parts, lead-soldered assemblies, previously chemical-containing tanks, unidentified hoses, and questionable coatings should not be assumed safe merely because they have been cleaned.

## Minimum data record

Each run should document:

- prototype ID and configuration;
- date and runtime;
- environmental site class;
- ambient temperature and RH;
- calculated dew point;
- condenser temperature;
- inlet and outlet air conditions;
- airflow where measurable;
- coolant supply and return temperature;
- coolant flow where applicable;
- ground or stream sink temperature;
- rainfall, fog, cloud, or wind notes;
- water collected;
- collection rate in L/h;
- normalized yield if appropriate;
- material changes;
- leaks, fouling, icing, contamination, or maintenance observations.

## Reporting rules

- Label modeled yields as modeled.
- Label measured yields as measured.
- Do not extrapolate a single favorable test into an annual guarantee.
- Separate atmospheric condensate from rainfall or fog interception.
- Report zero-yield runs.
- Preserve failed prototypes and negative findings in the research record.
- Do not describe experimental condensate as potable without independent validation.

## Intended contribution

The intended contribution is an evidence-based library of low-cost alternative water collection methods that can be compared by physical mechanism, site requirements, construction burden, material risk, measured yield, maintainability, and potential usefulness in resource-constrained settings.
