# Annotated Bibliography: Alternative Water Collection Systems

## Purpose

This bibliography supports the active physics-first WASH research lane on low-cost alternative water collection. Priority is given to peer-reviewed field experiments, reviews, and standard methods that can inform prototypes made from common or salvaged materials.

All prototype implications remain non-potable by default until material safety and water quality are independently validated.

## 1. Passive radiative dew collection

### Khalil et al. (2016) — review of passive and active dew collection

**Citation:** Khalil, B., Adamowski, J., Shabbir, A., Jang, C., Rojas, M., Reilly, K., & Ozga-Zielinski, B. *A review: dew water collection from radiative passive collectors to recent developments of active collectors.* Sustainable Water Resources Management, 2, 71-86. DOI: 10.1007/s40899-015-0038-z.

**Key findings:**

- Dew forms when collector surface temperature falls below atmospheric dew point.
- Radiative passive collectors require no external energy input.
- Typical reported maximum yields for 1 m2 passive condensers in favorable arid/semi-arid environments are about 0.3-0.6 L/day.
- The review cites an approximate radiative upper limit near 0.8 L/m2/day.
- Favorable conditions include high humidity, high sky visibility, low cloud cover, and low but non-zero wind.
- Ground-coupled cooling is identified as one pathway for reducing the energy burden of active condensation.

**Repository implication:**

Use 0.3-0.6 L/m2/day as a favorable-condition benchmark, not a McDowell guarantee. Treat radiative panels as the zero-energy control against which cooled prototypes are compared.

### Muselli et al. (2002) — 30 m2 Ajaccio radiative dew collector

**Citation:** Muselli, M., Beysens, D., Marcillat, J., Milimouk, I., Nilsson, T., & Louche, A. *Dew water collector for potable water in Ajaccio (Corsica Island, France).* Atmospheric Research, 64, 297-312. DOI: 10.1016/S0169-8095(02)00100-X.

**Key findings:**

- Tested a 10 x 3 m radiative condenser inclined 30 degrees from horizontal.
- Condensing surface used polyethylene containing TiO2 and BaSO4 microspheres.
- Over 478 days, the large condenser produced dew on 214 days, about 45% of the observation period.
- Total reported collection was approximately 767 L, averaging about 3.6 L per dew day.
- Maximum reported daily yield was 11.4 L.
- Yield correlated with temperature, humidity, wind velocity, and cloud cover.
- Chemical analysis found some chloride and sulfate contribution from local sea spray and combustion sources.

**Repository implication:**

Large-area radiative systems can accumulate meaningful seasonal volume, but the average yield per square meter remains modest. The study also demonstrates why local airborne contamination sources must be considered even when the collector material itself is relatively clean. citeturn373531search0

### Lin & Wu (2025) — material thermal properties and radiative dew performance

**Citation:** Lin, J.-J., & Wu, M.-C. *Experimental investigation on material thermal properties in radiative cooling for dew condensation.* Applied Thermal Engineering, 280, 127989 (2025).

**Key findings:**

- Field-tested five materials in a portable 30-degree radiative condenser geometry.
- Compared PMMA, glass, iron, stainless steel, and aluminum.
- Found a strong relationship between material thermal properties and daily dew yield.
- Surface state also mattered; rusted surfaces deviated from simple bulk-property expectations.

**Repository implication:**

Low thermal mass remains important, but surface condition and drainage cannot be inferred from nominal material alone. Scrap materials should therefore be tested empirically rather than ranked only by conductivity or heat capacity. citeturn944116search6

## 2. Ground-coupled cooling and condensation

### Wei et al. (2020) — full-scale hot/humid earth-to-air heat exchanger field experiment

**Citation:** *Field experiments on the cooling capability of earth-to-air heat exchangers in hot and humid climate.* Applied Energy, 276, 115493. DOI: 10.1016/j.apenergy.2020.115493.

**Key findings:**

- Full-scale testing used multiple buried PVC pipes with different diameters and depths.
- Inlet air temperature varied from approximately 21.5 to 41.2 C.
- Inlet moisture content varied from approximately 11.2 to 20.52 g/kg.
- Maximum measured air-temperature reduction was approximately 22.13 C.
- Maximum measured moisture-content reduction was approximately 7.41 g/kg.
- Deeper burial and smaller diameter generally improved outlet temperature and moisture reduction.
- Sensible cooling represented about 60.5-82.82% of total cooling capacity.
- Latent cooling represented about 17.18-39.5% of total cooling capacity.
- Maximum total cooling capacity in the tested configurations approached 2.99 kW.
- Soil thermal recovery was slower than soil thermal response during operation.

**Repository implication:**

This is the strongest current field precedent for the ground-coupled condenser lane. Our prototype target of roughly 0.15-0.30 L/h requires much less moisture removal than the experiment's maximum 7.41 g/kg reduction, but our shallow, short, low-cost ground field will have much less thermal capacity. Soil recovery must therefore be measured explicitly.

### Agrawal et al. — soil moisture effect on buried heat-exchanger performance

**Source:** *Effect of soil moisture contents on thermal performance of earth-air-pipe heat exchanger for winter heating in arid climate: In situ measurement.* Geothermics.

**Key findings:**

- Experimental systems were buried approximately 3.7 m deep.
- Dry-soil knee point occurred around 40 m of pipe after 12 h operation.
- With added soil moisture, knee points fell to about 28 m, 27 m, and 26 m at 5%, 10%, and 15% moisture respectively.
- At 15% soil moisture, average heat-transfer rate and COP increased by roughly 26% relative to dry soil at the tested length.

**Repository implication:**

Soil moisture is a major design variable, not a minor site descriptor. The PEX field should record moisture state and avoid assuming that a dry hillside and a moist valley soil provide equivalent thermal capacity. citeturn373531search2turn373531search5

### Summer EAHE with active soil-moisture control

**Citation:** *Experimental investigation on the cooling performance of an Earth to Air Heat Exchanger (EAHE) equipped with an irrigation system to adjust soil moisture.* Energy and Buildings, 196, 280-292 (2019). DOI: 10.1016/j.enbuild.2019.05.007.

**Key findings:**

- Summer field tests showed an average air-temperature reduction of approximately 14.6 C.
- Reported average total cooling capacity was approximately 8.79 kW for the tested system.
- Soil-moisture adjustment materially affected cooling performance.

**Repository implication:**

Moisture-controlled soil enhancement is physically credible, but deliberate soil irrigation should not be assumed appropriate for low-resource deployment because it consumes water and changes maintenance burden. For our prototype, naturally moist soil is preferable to deliberately spending harvested water to improve the sink. citeturn373531search3

## 3. Condensation behavior on heat exchangers

### Humid-air condensation on plate/fin heat exchangers

**Source:** *Characteristics of primary air condensation in indirect evaporative cooler: Theoretical analysis and visualized validation.* Building and Environment, 174, 106783 (2020).

**Key findings:**

- Dropwise and filmwise condensation can coexist on heat-exchanger surfaces.
- Relative humidity materially changes condensation coverage and heat flux.
- Condensate behavior affects air-side heat-transfer performance.
- Surface geometry and wettability influence drainage and effective heat transfer.

**Repository implication:**

The scrap automotive radiator should be evaluated not only by temperature but by drainage behavior. Water retained in fins can increase thermal resistance, re-evaporate, or remain trapped. The prototype should therefore measure condensate recovered at the tray versus psychrometrically predicted moisture removal.

## 4. Solar chimneys and passive airflow

### Experimental solar chimney, full-scale natural ventilation

**Citation:** *Experimental study for natural ventilation on a solar chimney.* Renewable Energy, 34(12), 2928-2934 (2009). DOI: 10.1016/j.renene.2009.04.026.

**Key findings:**

- Full-scale testing under real meteorological conditions.
- Maximum reported solar irradiance about 604 W/m2 produced an air-temperature rise of roughly 7 C in the chimney.
- Measured airflow ranged from about 50 to 374 m3/h during the test day.
- Mean 24 h airflow was about 177 m3/h.
- Experimental discharge coefficient was approximately 0.52.

**Repository implication:**

The airflow range is well above the current P2 target of roughly 45-60 CFM (about 76-102 m3/h), indicating that passive solar draft is physically capable of supplying prototype-scale airflow if duct losses and geometry are controlled. Use discharge coefficients around 0.5 as an initial engineering prior, then measure actual flow. citeturn435586search2

### Roof solar chimney empirical synthesis

**Citation:** *Developing an empirical model for roof solar chimney based on experimental data from various test rigs.* Building and Environment, 110, 115-128 (2016). DOI: 10.1016/j.buildenv.2016.10.002.

**Key findings:**

- Synthesized experimental data from multiple test rigs.
- Equal inlet and outlet areas improved chimney performance.
- Outlet sizing was especially important when inlet and outlet areas differed.

**Repository implication:**

The prototype should avoid a narrow outlet bottleneck. Matching the 8 in intake with a comparable effective exhaust area remains a defensible starting geometry. citeturn435586search4

### Solar chimney coupled with earth-air heat exchanger

**Citation:** *Experimental investigation of natural ventilation characteristics of a solar chimney coupled with earth-air heat exchanger (SCEAHE) system in summer and winter.* Renewable Energy, 193, 1001-1018 (2022). DOI: 10.1016/j.renene.2022.05.076.

**Key findings:**

- Demonstrated a purely passive coupled solar-chimney/earth-air system experimentally.
- Verified stable natural ventilation behavior in both summer and winter.
- Reported average thermal efficiencies of approximately 0.61 in summer and 0.86 in winter.

**Repository implication:**

This directly supports the architecture now proposed in WASH: buried/earth cooling on the intake or condenser side with solar buoyancy on the exhaust side. Our use is different because the goal is condensation rather than room conditioning, but the coupled passive-flow mechanism is established. citeturn435586search10

## 5. Fog collection

### Schemenauer and Cereceda standard fog collector

**Citation:** Schemenauer, R. S., & Cereceda, P. (1994). *A proposed standard fog collector for use in high-elevation regions.* Journal of Applied Meteorology, 33, 1313-1322.

**Key findings:**

- Established a standardized 1 m2 fog-collector geometry for site comparison.
- Uses a vertical polypropylene mesh collector oriented to fog-bearing wind.
- The method is designed primarily for evaluating site potential before scaling.

**Repository implication:**

Any fog lane should begin with a 1 m2 standard or near-standard collector rather than a large community mesh. This gives a defensible local L/m2/day baseline.

### Peru/Chile fog-site evaluation work

**Source:** Conference work by Cereceda, Villegas, Osses, Schemenauer and collaborators using standardized fog collectors.

**Key findings:**

- Used 1 m2 Standard Fog Collectors for systematic site evaluation.
- Site-selection variables included altitude, relief/topography, valley/slope orientation, distance to sea, available collector area, access, land use, and ownership.

**Repository implication:**

Fog collection needs a site-screening protocol rather than simple deployment wherever RH is high. High humidity without suspended liquid droplets is not sufficient. citeturn373531search36

## 6. Water quality of condensate and dew

### Heavy metals and microbial assessment of AC condensate

**Citation:** *Heavy metals and microbial assessment of air conditioning condensate water in Jeddah city-Saudi Arabia: concept of sustainable water resources.* Sustainable Water Resources Management (2024).

**Key findings:**

- Condensate collection materials were sterilized before use.
- Samples were tested for microbial, chemical, and heavy-metal parameters including As, Cd, Cr, Cu, Mn, Ni, Pb, Fe, Zn, and Hg.
- Study design demonstrates that condensate intended for reuse requires direct water-quality characterization rather than assumptions based on apparent clarity.

**Repository implication:**

Any future potable lane requires a defined sampling panel and sanitary collection chain. The scrap-radiator prototype should remain outside that lane. citeturn944116search0

### Metals deposited in dew — Changchun, China

**Citation:** *Fluxes and sources of metals deposited in dew in Changchun, China.* Atmospheric Pollution Research, 14(5), 101729 (2023). DOI: 10.1016/j.apr.2023.101729.

**Key findings:**

- Measured 12 metals in dew over six months.
- Dew contained both natural-source and anthropogenic-source metals.
- Identified contributions from crustal dust, biomass burning, vehicle exhaust, and coal combustion.
- Metal concentrations in dew were generally higher than those measured in rain in the study.

**Repository implication:**

Dew is not chemically equivalent to distilled water. Atmospheric deposition can concentrate contaminants on condensing surfaces, especially in traffic, industrial, combustion, or mining-influenced environments. citeturn944116search1turn944116search2

### Urban dew chemistry and bacteriology — Bordeaux

**Citation:** *Chemical and biological characteristics of dew and rain water in an urban coastal area (Bordeaux, France).* Atmospheric Environment.

**Key findings:**

- Dew chemistry varies substantially by local atmospheric environment.
- Prior studies found dew ranging from corrosive/high-ion to acidic or weakly mineralized depending on location.
- The Bordeaux work explicitly investigated both chemical and bacteriological characteristics rather than chemistry alone.

**Repository implication:**

Even where one prior dew collector met selected chemical limits, that result cannot be generalized to another geography or collector. Microbial testing must be separate from chemistry testing. citeturn373531search1

## 7. Physics equations to carry into prototype work

### Condensation threshold

```text
T_surface < T_dewpoint
```

### Moisture mass balance

```text
m_dot_water = m_dot_dry_air * (omega_in - omega_out)
```

### Sensible load

```text
Q_sensible = m_dot_air * Cp_air * (T_in - T_out)
```

### Latent load

```text
Q_latent = m_dot_water * h_fg
```

### Ground-loop heat rejection

```text
Q_ground = m_dot_coolant * Cp_water * (T_return - T_supply)
```

### Stack-driven airflow starting point

```text
Q_air ~ Cd * A * sqrt(2 * DeltaP / rho)
```

with `Cd` initially treated around 0.5 as a field-derived engineering prior rather than a fixed constant.

## 8. Evidence gaps for the next pull

- Stream/spring or lake-water-coupled condensation studies applicable to a closed secondary loop.
- Appalachian or West Virginia soil thermal-property datasets by depth and moisture state.
- Freeze protection and seasonal shutdown behavior for shallow PEX and buried-air systems.
- Comparative pressure-drop data for 6 in versus 8 in smooth-wall passive intake ducts at 30-100 CFM.
- Condensate treatment trains appropriate for low-resource settings after material-safe collection is established.
- Long-duration fouling and biofilm behavior inside passive buried air intakes.

## Evidence boundary

Yield values from other climates are comparison points only. They should not be transferred directly into McDowell or another deployment location without local measurements of dew point, soil/water temperature, airflow, collector temperature, and actual recovered volume.
