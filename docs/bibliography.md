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

### Sharan — Kutch passive condenser experiments

**Source:** Indian Institute of Management Ahmedabad working paper, *Dew yield from passive Condensers in a coastal arid Area - Kutch*.

**Key findings:**

- Compared six inexpensive condenser materials, including aluminum, galvanized iron, polyethylene, coated polyethylene, and fiber-reinforced plastics.
- Test panels were 1 x 1 m and insulated with approximately 25 mm styrene foam.
- Panels were inclined approximately 30 degrees from horizontal.
- Condensate drained by gravity to a collection vessel.
- Meteorological conditions were logged continuously.

**Repository implication:**

This is a strong precedent for a resident-buildable 1 m2 control panel. The 1 m2 geometry also makes yield comparison simple in L/m2/night.

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

## 3. Condensation behavior on heat exchangers

### Humid-air condensation on plate/fin heat exchangers

**Source:** *Characteristics of primary air condensation in indirect evaporative cooler: Theoretical analysis and visualized validation.* Building and Environment, 174, 106783 (2020).

**Key findings:**

- Dropwise and filmwise condensation can coexist on heat-exchanger surfaces.
- Relative humidity materially changes condensation coverage and heat flux.
- Condensate behavior affects air-side heat-transfer performance.
- Published heat-exchanger work shows that surface geometry and wettability influence drainage and effective heat transfer.

**Repository implication:**

The scrap automotive radiator should be evaluated not only by temperature but by drainage behavior. Water retained in fins can increase thermal resistance, re-evaporate, or remain trapped. The prototype should therefore measure condensate recovered at the tray versus psychrometrically predicted moisture removal.

## 4. Fog collection

### Schemenauer and Cereceda standard fog collector

**Citation:** Schemenauer, R. S., & Cereceda, P. (1994). *A proposed standard fog collector for use in high-elevation regions.* Journal of Applied Meteorology, 33, 1313-1322.

**Key findings:**

- Established a standardized 1 m2 fog-collector geometry for site comparison.
- Uses a vertical polypropylene mesh collector oriented to fog-bearing wind.
- The method is designed primarily for evaluating site potential before scaling.

**Repository implication:**

Any fog lane should begin with a 1 m2 standard or near-standard collector rather than a large community mesh. This gives a defensible local L/m2/day baseline.

### Structural design review of fog collectors

**Source:** *Structural design of efficient fog collectors: A review.*

**Key findings:**

- Standard Fog Collectors use approximately 1 x 1 m collection area.
- Large Fog Collectors are commonly around 4 m high by 10 m wide.
- Raschel mesh remains widely used because it is inexpensive and field proven.
- Double-layered mesh is common in many field systems.
- Mesh geometry and wettability materially affect yield and drainage.

**Repository implication:**

Fog collection is fundamentally an aerodynamic droplet-interception problem, not a condensation problem. It belongs in a separate prototype family with wind and liquid-water-content measurements.

## 5. Physics equations to carry into prototype work

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

These equations allow every prototype to be checked against conservation of energy and mass rather than relying only on bucket volume.

## 6. Evidence gaps for the next pull

- Field data on low-cost radiator-style air-to-water condensers using non-refrigerated cold sinks.
- Stream/spring or seawater-coupled condensation experiments that can inform a closed-loop water-side heat sink.
- Solar-chimney pressure and airflow studies applicable to approximately 8 in passive ductwork.
- Soil thermal conductivity and thermal diffusivity ranges for Appalachian soils by moisture state.
- Water-quality studies of dew/fog condensate and contamination introduced by collector materials.
- Freezing and seasonal shutdown considerations for shallow ground loops in Appalachian climates.

## Evidence boundary

Yield values from other climates are comparison points only. They should not be transferred directly into McDowell or another deployment location without local measurements of dew point, soil/water temperature, airflow, collector temperature, and actual recovered volume.
