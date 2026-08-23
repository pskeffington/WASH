# Hillside Placement Logic for Alternative Water Collection Systems

## Purpose

This note translates mountain-airflow and complex-terrain literature into placement logic for prototype water collectors on hillsides, valleys, ridges, and saddles.

The objective is not to identify a universally optimal elevation. Different collection mechanisms benefit from different terrain-driven flows. Placement should therefore be based on the physical mechanism being harvested: liquid fog droplets, atmospheric water vapor, radiative cooling, or a ground/water thermal sink.

All systems remain experimental and non-potable by default unless independently validated.

## 1. Core terrain airflow mechanisms

### Daytime anabatic flow

Sunlit slopes heat the adjacent air column. The warmer air becomes buoyant and develops an upslope pressure-gradient flow.

Typical fair-weather anabatic flow:

```text
DAY

       ridge
        /\
       /  \      ↑ upslope flow
      /    \    ↑
     /      \  ↑
valley ______\
```

Mountain-meteorology literature commonly reports daytime anabatic flow on the order of roughly 1-5 m/s depending on slope, heating, vegetation, and background wind.

### Nighttime katabatic flow

After sunset, the slope loses heat by long-wave radiation. Air next to the surface becomes colder and denser and drains downslope.

```text
NIGHT

       ridge
        /\
       /  \  ↓
      /    \  ↓ downslope cold air
     /      \  ↓
valley ______\____ cold-air pool
```

Drainage flow can feed a valley inversion or cold-air pool. Under moist conditions, this can bring air temperature toward dew point and promote valley fog.

### Background or synoptic wind

Terrain-driven slope winds are strongest when larger-scale winds are weak. Strong background winds can overwhelm or distort the local anabatic/katabatic circulation.

Therefore every prototype site should distinguish:

```text
terrain-driven flow
from
regional/background wind
```

rather than assuming one fixed daily wind direction.

## 2. Flow over hills and ridges

Boundary-layer flow over a gentle hill generally accelerates toward and across the crest.

```text
prevailing wind --->

                faster
                 --->
              ___/\___
             /        \
      --->  /          \   turbulent / sheltered lee
           /            \    ~~~~~~~
```

The windward slope and crest can therefore offer higher mean airflow.

On sufficiently steep lee slopes, however, flow can separate from the surface. The resulting wake has lower mean velocity, increased turbulence, recirculation, and unpredictable direction.

For passive collectors that depend on stable through-flow, the immediate lee of a steep ridge is generally a poor placement zone.

## 3. Fog-collector placement

Fog harvesting is an interception process. The goal is to expose mesh to the largest flux of suspended liquid droplets.

Preferred terrain locations are therefore:

```text
fog-bearing wind --->

             COLLECTOR
                 |
                 |
           ______|___ ridge
         /            \
        /              \
 windward             leeward
 preferred             avoid
```

Placement rules supported by fog-harvesting guidance:

- favor windward slopes and ridge/crest positions;
- orient collector face approximately perpendicular to the fog-bearing wind;
- avoid major upwind obstructions;
- avoid locations immediately behind ridges where flow is descending, sheltered, or separated;
- use passes or saddles cautiously because they can funnel wind and increase structural loading;
- verify fog occurrence with a small 1 m2 collector before scaling.

High relative humidity alone does not justify a fog collector. Suspended liquid droplets must actually be present.

## 4. Ground-cooled atmospheric condenser placement

A ground-cooled condenser has a different objective. Water production is approximately governed by:

```text
m_dot_water = m_dot_dry_air * (omega_in - omega_out)
```

The hillside site therefore needs both:

```text
high moisture availability
AND
adequate airflow
```

while maintaining:

```text
T_condenser < T_dewpoint
```

A stagnant valley bottom may have very high RH but very little air exchange. A windy ridge may have excellent airflow but lower dew-point margin or excessive thermal load.

The best location is likely an intermediate hydraulic/meteorological position rather than either extreme.

### Candidate lower/mid-slope location

For a humid Appalachian-style site, a strong candidate is the lower or middle portion of a slope where nighttime drainage air remains moving but has already cooled substantially.

```text
                 ridge
                  /\
                 /  \
                /    \
               /      \
              / [A]    \
             /           \
            / [B]         \
valley ____/[C]____________\
```

Where:

- **A: upper slope/crest** — strong airflow, potentially higher turbulence and wind exposure;
- **B: lower/mid slope** — candidate balance of drainage airflow, humidity, access, and ground coupling;
- **C: valley bottom** — coldest/highest-RH conditions possible, but susceptible to stagnant cold pools and low ventilation.

For the drum/radiator prototype, **B should be the first candidate test zone**, not a fixed design rule.

## 5. Valley-bottom logic

Cold air commonly pools in topographic depressions under clear, weak-wind nighttime conditions. This produces inversions and can generate fog.

Advantages:

- lower air temperature;
- high nighttime RH;
- frequent approach to saturation;
- potentially favorable radiative-dew conditions.

Disadvantages:

- airflow may collapse as the cold pool deepens;
- locally colder air does not automatically contain more absolute moisture;
- drainage currents may flow over the top of an established cold pool rather than ventilating its center;
- flooding and drainage hazards may be greater;
- buried thermal systems may encounter groundwater or saturated-soil construction issues.

Therefore valley-bottom placement should be evaluated from **dew point plus airflow**, not RH alone.

## 6. Windward vs leeward logic for condensers

For a prevailing background wind:

### Windward side

Potential advantages:

- cleaner and more predictable inflow;
- terrain-induced acceleration;
- better passive ventilation.

Potential disadvantages:

- high airflow can exceed ground-loop cooling capacity;
- convective heat load on radiative collectors rises with wind;
- structural loads increase.

### Leeward side

Potential advantages:

- shelter can reduce excessive wind and convective heating.

Potential disadvantages:

- steep hills can create separation and recirculation;
- airflow may become turbulent, intermittent, or reversed;
- fog can dissipate after crossing a ridge;
- passive chimney performance becomes less predictable.

A mild sheltered position may be useful for radiative dew panels, but the immediate wake of a steep crest should generally be avoided for forced-through-flow condenser systems.

## 7. Placement logic for the current drum prototype

For the current architecture:

```text
buried/shaded intake
    -> radiator in 55-gal drum
    -> solar/passive chimney
```

### Daytime summer operation

Daytime solar heating commonly produces upslope anabatic wind.

A hillside installation could exploit this by placing:

```text
VALLEY SIDE                     HILL SIDE

humid air ---> buried intake ---> DRUM ---> chimney ---> uphill
```

The intake mouth would face the valley/downhill direction and the exhaust would discharge toward the uphill side.

This aligns the apparatus with natural daytime upslope flow while the solar chimney adds buoyancy in the same direction.

### Nighttime operation

At night, natural slope flow commonly reverses:

```text
HILL SIDE ---> downslope ---> VALLEY
```

A fixed one-direction system may therefore work against the natural slope circulation for part of the day.

This suggests testing either:

1. a primarily daytime ground-cooled/solar-chimney operating window;
2. dual intake ports with manually selectable direction;
3. passive low-resistance flap valves if a later prototype warrants added complexity;
4. a fan-assisted mode when natural terrain flow reverses.

The first prototype should favor **measurement over mechanical complexity**.

## 8. A placement metric for condensation systems

A useful theoretical site metric is the available condensate flux:

```text
W_site = rho_air * Q_air * max(omega_air - omega_sat(T_condenser), 0)
```

where:

- `rho_air` = air density;
- `Q_air` = volumetric flow through the device;
- `omega_air` = ambient humidity ratio;
- `omega_sat(T_condenser)` = saturated humidity ratio at condenser temperature.

This captures the main reason RH alone is inadequate.

Two sites might have:

```text
Site 1: very high RH + weak airflow
Site 2: slightly lower RH + strong airflow
```

Site 2 can produce more water if the higher vapor mass flux outweighs the smaller humidity-ratio difference.

A field-placement study should therefore measure simultaneously:

```text
dew point
air temperature
RH
wind speed
wind direction
soil temperature
```

at multiple slope positions.

## 9. Recommended hillside survey

Before permanent excavation, place inexpensive sensors at three or four elevations for at least several representative days.

Suggested positions:

```text
S1 - near crest / upper windward slope
S2 - middle slope
S3 - lower slope
S4 - valley floor where safe and accessible
```

Log at 5-15 minute intervals:

```text
air temperature
RH
dew point
wind speed
wind direction
soil temperature at shallow reference depth
```

If feasible, add a small identical passive intake/airflow tube or anemometer at each station.

## 10. Decision criteria by collector type

| Collector type | Preferred terrain tendency | Avoid |
|---|---|---|
| Fog mesh | windward upper slope / ridge | lee wake, sheltered hollow |
| Radiative dew panel | open sky, low/moderate wind; often lower slope can be favorable | heavy canopy, excessive wind, warm massive structures |
| Ground-cooled condenser | site maximizing dew-point margin x useful airflow | stagnant cold pocket or turbulent lee wake |
| Solar-chimney hybrid | slope orientation that supports daytime natural flow | layout where terrain flow directly opposes exhaust |
| Stream-coupled condenser | location driven by thermal sink and safe/legal access, with intake in clean humid airflow | flood-prone placement, direct condensate-stream contact |

## 11. Appalachian prototype hypothesis

For a humid, forested Appalachian valley, the first placement hypothesis should be:

> **Lower-to-mid slope, on the side exposed to the dominant daytime/seasonal humid-air approach, above the deepest stagnant valley cold pool but below the most turbulent ridge zone.**

This location potentially combines:

- cool/moist air;
- useful slope-driven ventilation;
- stable soil temperatures;
- reduced ridge turbulence;
- easier excavation and structural access than a steep crest;
- less flood exposure than the valley bottom.

This remains a hypothesis until a vertical sensor transect is run.

## 12. Literature anchors

- Royal Meteorological Society guidance on anabatic and katabatic mountain winds: daytime upslope and nighttime downslope thermal circulations.
- Farina et al., *Understanding Thermally Driven Slope Winds: Recent Advances and Open Questions*, Boundary-Layer Meteorology: slope-flow structure, drainage jets, canopy effects, valley cold pools, and background-wind interaction.
- American Meteorological Society mountain-meteorology literature: speed-up approaching hill crests and potential lee-side separation.
- Belcher & Hunt, *Turbulent Flow Over Hills and Waves*, Annual Review of Fluid Mechanics: terrain pressure gradients, acceleration, separation, and wakes.
- Ishihara et al., wind-tunnel steep-hill experiments: flow speed-up at hilltop and side slope with separation behind the crest.
- OAS fog-harvesting guidance: windward ridge/crest placement, obstacle avoidance, and avoidance of lee-side downslope flow.
- National Weather Service mountain/valley fog guidance: cold-air drainage, valley accumulation, saturation, and fog formation.
- FAO frost-protection guidance: valley bottoms are frequently colder than slopes and can be identified through terrain and nighttime temperature observations.

## Research boundary

Terrain placement should not be inferred from a map alone. Forest canopy, buildings, roads, cuts, ridges, valley shape, seasonal leaf cover, and regional winds can all alter local circulation.

The repository should therefore treat terrain models as **candidate placement logic**, followed by local measurement before excavation or deployment.
