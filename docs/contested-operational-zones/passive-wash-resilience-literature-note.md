# Passive WASH Resilience in Contested Environments — Literature Note

## Scope

This note develops the literature basis for passive and low-energy water collection and treatment in conflict-affected or infrastructure-disrupted environments.

The emphasis is humanitarian and public-health focused:

- no or minimal dependence on grid power;
- reduced fuel dependence;
- fewer moving parts;
- lower maintenance burden;
- simple household/community-scale deployment;
- minimal consumables where possible;
- free-standing architectures that do not require intact buildings;
- repairability with locally available materials.

This note does **not** make claims about defeating surveillance systems or avoiding detection by military sensors. The relevant engineering argument is resilience: passive systems can continue functioning when powered infrastructure, fuel supply, pumps, and maintenance chains fail.

---

## 1. Why passive WASH matters in emergencies

WHO emergency WASH guidance explicitly recognizes household treatment as especially applicable after disasters where families lack facilities and resources. WHO identifies simple treatment methods such as solar disinfection and ceramic filtration as useful emergency options.

This supports a broader design principle:

```text
WHEN INFRASTRUCTURE FAILS,
HOUSEHOLD-SCALE PASSIVE OR LOW-ENERGY SYSTEMS
CAN PRESERVE PARTIAL WATER FUNCTION.
```

Passive collection and gravity treatment cannot replace intact municipal systems, but they can reduce dependence on damaged centralized assets.

---

## 2. Energy independence

The most immediate resilience advantage of passive systems is that they can operate without continuous electricity or fuel.

Examples include:

- rainwater harvesting;
- gravity settling;
- gravity roughing filtration;
- biosand filtration;
- ceramic filtration;
- some gravity-driven membrane systems;
- solar disinfection;
- gravity-fed distribution.

This matters in contested or disaster environments because water infrastructure often fails through the water-energy nexus:

```text
pump failure
+ grid loss
+ generator failure
+ fuel shortage
= water-access failure
```

A passive system removes some of those dependencies.

---

## 3. Fewer moving parts

Passive systems tend to rely on:

- gravity;
- head pressure;
- solar radiation;
- capillary/porous media;
- fixed collection geometry.

This reduces dependence on:

- motors;
- bearings;
- pumps;
- controllers;
- inverters;
- fuel systems;
- electrical repair capability.

The resulting benefit is not simply lower cost. It is **failure-mode reduction**.

A pallet catchment feeding a barrel can continue operating even if:

- the grid is unavailable;
- a generator cannot be fueled;
- electronics fail;
- a pump cannot be repaired.

---

## 4. Humanitarian design requirements align with passive architecture

UNICEF's emergency household-water-treatment work identifies desirable properties including:

- affordable;
- intuitive/simple;
- fail-safe;
- durable;
- compact logistical footprint;
- integrated safe storage;
- long service life;
- minimal or no recurring chemical provision.

These characteristics strongly overlap with passive WASH design.

UNICEF has also investigated gravity-driven membrane systems specifically because gravity operation can reduce backflushing and maintenance burdens compared with conventional membrane products.

The central lesson is:

> Reduced operational complexity is itself a humanitarian resilience feature.

---

## 5. Household-scale systems as distributed resilience

WHO's household water treatment programme evaluates technologies that are generally low-cost, free-standing, and capable of serving a household or small facility.

Distributed household-scale systems offer several resilience advantages:

- no single-point centralized failure;
- incremental deployment;
- easier repair;
- easier transport;
- local ownership;
- staged treatment upgrades;
- independent storage.

This aligns with the WASH repo's modular architecture:

```text
LOCAL COLLECTION
      ↓
RAW STORAGE
      ↓
PASSIVE PRETREATMENT
      ↓
CONTROLLED FILTER
      ↓
VALIDATED DISINFECTION
      ↓
SAFE STORAGE
```

---

## 6. Passive collection architectures

### Rainwater harvesting

Rainwater capture is the clearest passive collection method.

It can operate using only:

- collection surface;
- slope;
- gutter;
- first flush;
- gravity;
- storage.

No powered component is intrinsically required.

For Gaza-like environments, this creates a useful winter-season resilience layer when rainfall is available.

### Dew and radiative collection

Passive dew collection relies on a surface cooling below atmospheric dew point, often through nocturnal radiative heat loss.

Advantages:

- no pump required in the simplest form;
- few moving parts;
- can operate during dry periods when humidity remains high.

Limitations:

- typically low yield per unit area;
- strongly weather dependent;
- surface material and sky exposure matter;
- water quality still requires validation.

### Fog interception

Fog nets are also passive but require a suitable meteorological environment and wind-driven fog droplets.

They are highly site dependent and should not be assumed useful everywhere.

---

## 7. Passive treatment architectures

### Settling

Sedimentation requires only time and gravity.

Useful for:

- suspended solids;
- protecting downstream filters.

It does not provide complete microbial protection.

### Roughing filtration

Gravity-fed gravel systems can reduce turbidity and protect finer filters.

They are attractive in disrupted settings because media can sometimes be locally sourced, though water-contact media must be screened and washed.

### Biosand / slow sand

Slow sand and biosand systems can operate without electricity and have long histories in household treatment.

Their benefits include:

- simple hydraulics;
- locally available media;
- low recurring energy burden.

However, performance depends on media grading, maturity, flow rate, maintenance, and microbial validation.

### Ceramic filtration

WHO recognizes ceramic filtration as a household-treatment technology class.

Ceramic elements can operate under gravity and therefore fit passive architectures well, but manufacturing quality and crack integrity are critical.

### Gravity-driven membrane filtration

UNICEF has investigated gravity-driven membrane household treatment as a way to combine stronger filtration performance with reduced maintenance and no pressurized pump requirement.

This is especially relevant for a hybrid architecture where improvised upstream collection and settling feed a standardized health-critical filter.

---

## 8. Passive disinfection

Solar disinfection is an emergency household-water-treatment method recognized by WHO.

It offers:

- no fuel requirement;
- no electrical requirement;
- minimal equipment.

Constraints include:

- relatively clear water required;
- limited batch volume;
- adequate sunlight;
- sufficient exposure time;
- suitable containers.

Passive disinfection is therefore best treated as one tool within a multi-barrier system, not a universal solution.

---

## 9. Low thermal and acoustic burden as a secondary consequence

Passive systems generally generate little active mechanical heat and little or no machinery noise because they lack motors, generators, and pumps.

From a humanitarian engineering perspective, this has practical benefits:

- less fuel storage;
- less generator exhaust;
- less mechanical maintenance;
- less nuisance noise near shelters;
- fewer hot mechanical components;
- simpler deployment near households and medical areas.

These should be framed as **operational and environmental benefits**, not as claims of invisibility or guaranteed protection from surveillance or attack.

---

## 10. Form factor and integration into civilian environments

Simple passive WASH systems can often be built from familiar civilian objects:

- barrels;
- cisterns;
- tarps;
- pallets;
- gutters;
- masonry;
- rubble supports;
- gravity-fed filter vessels.

This matters because emergency systems need to fit within damaged neighborhoods, shelters, camps, courtyards, and household plots without requiring specialized infrastructure.

The design benefit is **compatibility with ordinary civilian environments and materials**.

---

## 11. Passive versus powered system comparison

| Attribute | Passive / gravity system | Powered system |
|---|---|---|
| Grid dependence | none/low | often moderate-high |
| Fuel dependence | none/low | may be substantial |
| Moving parts | few | often many |
| Maintenance | typically lower | typically higher |
| Peak treatment capacity | usually lower | often higher |
| Pressure capability | low | high |
| Desalination suitability | poor | generally required |
| Repairability | often high | component dependent |
| Logistics burden | generally lower | often higher |
| Scale potential | modular/distributed | often centralized/high-output |

The correct design is not always passive. Salinity, nitrate, industrial contaminants, high throughput, deep groundwater, or municipal-scale distribution may require powered treatment.

The resilience strategy is therefore:

```text
USE PASSIVE SYSTEMS WHERE PHYSICS ALLOWS
+
RESERVE POWERED SYSTEMS FOR TASKS THAT REQUIRE THEM
```

---

## 12. Gaza case-study implications

Gaza is particularly relevant because the environment combines:

- long-term groundwater-quality problems;
- damaged centralized infrastructure;
- electricity/fuel constraints;
- heavy dependence on storage and distribution;
- seasonal winter rainfall;
- high summer humidity;
- abundant rubble and salvaged structural material.

This suggests a seasonal passive architecture:

```text
WINTER
rain collection
→ gravity first flush
→ raw storage
→ settling / passive filtration
→ validated disinfection
→ safe storage

SUMMER
humidity/dew research
+
protected existing sources
+
stored/desalinated water
```

Passive rain collection will not solve Gaza's salinity problem and cannot replace municipal desalination, but it can supplement supply during productive weather periods.

---

## 13. Design priorities for the WASH repo

The passive-system lane should prioritize:

### PA-1 — no-power collection

- pallet rain collectors;
- tarp collectors;
- freestanding sheet collectors;
- passive dew surfaces.

### PA-2 — gravity conveyance

- standardized gutter/downpipe interfaces;
- first flush;
- gravity barrel banks;
- overflow management.

### PA-3 — passive pretreatment

- screens;
- settling;
- roughing filtration.

### PA-4 — passive controlled filtration

- biosand;
- ceramic;
- gravity membrane.

### PA-5 — passive/low-input disinfection

- validated solar disinfection where appropriate;
- other health-critical barriers selected according to source risk.

### PA-6 — safe storage

- closed vessels;
- controlled dispensing;
- independent raw/treated banks.

---

## 14. Research gaps

Further literature work should quantify:

1. failure rates and maintenance burdens of passive versus pumped household systems;
2. lifetime cost per litre;
3. imported mass per litre delivered;
4. local labor burden;
5. solar-disinfection practicality under Gaza seasonal cloud cover;
6. gravity membrane performance at low head;
7. passive dew yields under hourly Gaza climate conditions;
8. effects of dust/debris environments on passive collector maintenance;
9. durability of liners/coatings under conflict-zone exposure;
10. multi-source passive treatment trains.

---

## 15. Evidence anchors

- WHO, *Water, Sanitation and Health in Humanitarian Emergencies*: household water treatment is simple, inexpensive, and relevant where affected populations lack resources; WHO discusses solar disinfection and ceramic filters as emergency options.
- WHO, *International Scheme to Evaluate Household Water Treatment Technologies*: provides independent performance evaluation across solar, filtration, chemical, ceramic, membrane, and UV technologies.
- WHO, *Results of Rounds III and IV* (2026): extends the evidence base to 51 evaluated household treatment products.
- UNICEF Office of Innovation, *Household Water Treatment and Safe Storage in Emergency Settings*: identifies affordability, intuitive operation, durability, small logistics footprint, safe storage, and low consumable burden as key emergency-design properties and describes gravity-driven membrane research.
- UNICEF, *WASH in Emergencies*: emphasizes resilient WASH service provision during armed conflict and other fragile contexts.
- ICRC, *Humanitarian Engineering: Protecting Lives Through Essential Services* (2026): frames water, sanitation, energy, and infrastructure continuity as core protection functions in armed conflict.

---

## 16. Working conclusion

Passive WASH systems are attractive in contested environments because they can preserve partial water access when the dependencies of centralized and powered infrastructure fail.

Their strongest advantages are:

```text
NO/LOW POWER
+
NO/LOW FUEL
+
FEW MOVING PARTS
+
LOW MAINTENANCE
+
SMALL LOGISTICS FOOTPRINT
+
MODULAR DEPLOYMENT
+
LOCAL REPAIRABILITY
```

These properties make passive collection and gravity treatment a strong resilience layer for civilian WASH systems in modern conflict and disaster environments.

They should be evaluated on measured water yield, treatment performance, maintenance burden, material safety, and public-health outcomes—not on assumptions about invisibility to surveillance systems.
