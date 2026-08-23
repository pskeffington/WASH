# Field Assessment Framework: Alternative Water Collection Prototypes

## Purpose

This document defines the field-assessment framework for experimental alternative water collection systems developed in this repository. It supports research design, prototype comparison, partner review, and reproducible documentation in rural, low-income, underserved, infrastructure-limited, and humanitarian settings.

It is not a deployment authorization, engineering certification, potable-water approval, inspection authority, emergency-response protocol, or substitute for local ethical, institutional, environmental, utility, or regulatory requirements.

## Core principles

- Treat every apparatus as a prototype unless independently validated.
- Treat collected water as non-potable by default unless known materials, treatment, and independent testing support another classification.
- Separate modeled performance from measured performance.
- Measure the physical mechanism directly rather than inferring success from water volume alone.
- Preserve failed runs and zero-yield results.
- Do not use salvage indiscriminately; prior-use history and water-contact pathways matter.
- Compare experimental systems against simpler established options.
- Require local permission and appropriate utility-location, excavation, stream-access, electrical, and structural precautions before field construction.

## Prototype classes

Field assessment may be applied to:

- rainwater catchment;
- radiative dew collectors;
- ground-coupled atmospheric condensers;
- stream- or spring-coupled condensers;
- fog-interception systems;
- solar-assisted passive-draft systems;
- hybrid systems combining more than one mechanism.

## Site characterization

Before building, establish the environmental variables that control the proposed mechanism.

### Atmospheric variables

Record as applicable:

- ambient air temperature;
- relative humidity;
- calculated dew point;
- wind speed or qualitative wind condition;
- cloud cover;
- fog presence;
- precipitation;
- solar exposure;
- nighttime sky exposure.

### Ground variables

For ground-coupled prototypes, measure temperature at multiple depths where practical, for example:

- near surface;
- approximately 1 ft;
- approximately 3 ft;
- approximately 5 ft or proposed loop depth.

Record soil moisture qualitatively or quantitatively where possible because thermal performance is strongly dependent on soil contact and moisture.

### Stream or spring variables

For closed-loop stream-coupled systems, record:

- source-water temperature;
- flow condition;
- seasonal variation;
- flood exposure;
- access and property constraints;
- environmental or regulatory restrictions.

Source water and collected condensate should remain physically separate.

## Prototype record

Each apparatus should have a unique identifier and configuration record containing:

- prototype class;
- dimensions;
- materials;
- source or prior-use history of salvaged components;
- estimated build cost;
- number of builders;
- construction time;
- tools required;
- plumbing or airflow layout;
- collector or condenser area;
- intake and exhaust dimensions;
- coolant-loop length and depth where relevant;
- intended operating mode;
- known contamination or safety concerns.

## Ground-coupled condenser assessment

The current reference prototype consists of a buried or shaded smooth-wall air intake, a 55-gallon HDPE drum, a salvaged automotive radiator used as an experimental condenser, a closed-loop PEX ground field, a condensate tray, and passive or solar-assisted exhaust draft.

The radiator is not assumed potable-water-safe. Condensate from prototypes using used automotive heat exchangers remains experimental/non-potable unless the entire water-contact pathway is independently characterized and validated.

### Required measurements

At minimum measure:

- `T_air_in`;
- `RH_air_in`;
- calculated `T_dewpoint`;
- `T_radiator` or condenser surface temperature;
- `T_air_out` and preferably outlet RH;
- coolant supply temperature;
- coolant return temperature;
- coolant flow where measurable;
- airflow where measurable;
- ground temperature away from and near the loop;
- runtime;
- collected water volume.

### Key derived variables

Condensation margin:

```text
DeltaT_dew = T_dewpoint - T_condenser
```

Positive values indicate thermodynamic condensation potential.

Ground-side heat transfer:

```text
Q_ground = m_dot_coolant * Cp_coolant * (T_return - T_supply)
```

Atmospheric moisture removal:

```text
m_dot_water_theoretical = m_dot_dry_air * (omega_in - omega_out)
```

Collection efficiency:

```text
eta_collection = measured_water / theoretical_water_removed
```

## Rainwater assessment

For rain systems record:

- catchment area;
- rainfall depth;
- first-flush volume;
- gross captured volume;
- measured stored volume;
- overflow;
- visible debris;
- storage condition;
- estimated collection efficiency.

A useful theoretical comparison is:

```text
V_theoretical = rainfall_depth * catchment_area
```

Rainwater should be used as a benchmark because it may provide much larger volumes than dew or atmospheric-condensation systems in humid climates.

## Dew and fog assessment

For radiative dew collectors record:

- collector area;
- surface material;
- surface temperature;
- dew point;
- cloud cover;
- wind;
- night-sky exposure;
- panel angle;
- water collected;
- normalized yield in L/m2/night.

For fog collectors additionally record mesh type, projected area, wind direction, wind speed where available, fog duration, and collected water.

## Solar-draft assessment

When a solar chimney or reflector is used, measure:

- ambient temperature;
- chimney temperature;
- condenser temperature;
- airflow;
- water-production rate.

Solar heating should generally be evaluated on the exhaust side because heating moist inlet air without adding water vapor does not increase dew point and increases sensible cooling load.

## Scrap-material assessment

Document salvaged components in three categories.

### Structural salvage

Examples: framing, brackets, stands, external insulation, supports. Record condition and structural suitability.

### Thermal/mechanical salvage

Examples: automotive radiators, fans, pumps, coils, sheet metal, heat exchangers. Record prior use, cleaning method, corrosion, and whether the component contacts collected water.

### Wetted-path components

Any surface touching collected water requires particular scrutiny. Unknown drums, chemical containers, automotive cooling components, lead-soldered assemblies, unidentified hoses, and questionable coatings must not be assumed potable-safe.

## Resident-buildability assessment

A core research objective is determining whether a useful prototype can be built and maintained by two or three residents with common tools.

Record:

- total person-hours;
- number of builders;
- specialist skills required;
- excavation burden;
- lifting burden;
- power-tool requirements;
- replacement-part availability;
- cleaning access;
- seasonal maintenance;
- failure modes;
- estimated recurring cost.

A physically successful apparatus may still fail this gate if construction or maintenance is impractical for the intended setting.

## Performance classes

Do not classify a prototype from theoretical calculations alone. After sufficient measured runs, describe performance using transparent bands such as:

- mechanism not demonstrated;
- intermittent/measurable collection;
- repeatable low-volume collection;
- repeatable useful supplemental collection;
- candidate for larger controlled field study.

Avoid terms such as `safe`, `self-sufficient`, `potable`, or `reliable supply` unless independently supported.

## Water-quality boundary

Water quantity and water safety are separate evidence lanes.

Before any potable claim, characterize as appropriate:

- every wetted material;
- prior-use contamination;
- microbiological risk;
- metals;
- chemical contaminants;
- particulate contamination;
- storage conditions;
- treatment process;
- applicable local standards;
- independent laboratory results.

A prototype should not be presented as a drinking-water solution solely because condensation or precipitation initially appears visually clean.

## Comparative utility gate

Each mature prototype should be compared with plausible alternatives available to the setting, such as:

- conventional rainwater collection;
- repaired or extended utility service;
- approved wells;
- existing springs;
- delivered/hauled water;
- centralized community storage;
- approved filtration or treatment systems.

Compare:

- liters/day and liters/year;
- capital cost;
- recurring energy;
- labor;
- seasonal reliability;
- water-quality burden;
- maintenance;
- lifespan;
- local repairability.

The alternative collector should advance only where its measured utility justifies the added complexity.

## Research-governance requirements

Before any real-world build or data collection, document as applicable:

- landowner or site permission;
- utility-location requirements before excavation;
- stream or environmental permissions;
- electrical and structural safety controls;
- research or program purpose;
- partner authorization;
- source and data-rights constraints;
- privacy rules;
- quality-control procedures;
- water-use restrictions;
- reporting and community-review process.

The repository itself confers no authority to excavate, divert water, modify utilities, enter private property, distribute collected water, or make public-health determinations.

## Minimum field output

Every prototype field report should provide enough information for another researcher or community partner to understand:

1. what was built;
2. why the mechanism should work;
3. what environmental conditions were present;
4. what was actually measured;
5. how much water was actually collected;
6. what the dominant limitations were;
7. what material and safety concerns remain;
8. whether further scaling is justified.
