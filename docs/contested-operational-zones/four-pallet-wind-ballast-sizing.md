# Four-Pallet Collector Wind and Rubble-Ballast Sizing

## Purpose

This pass addresses roadmap item P8.2: estimate wind demand on the four-pallet Gaza collector and convert it into practical rubble-ballast and anchoring requirements.

This is a prototype engineering screen, not a certified structural design. Site wind climate, terrain exposure, panel geometry, anchoring, connection strength, temporary-structure rules, and local engineering judgment remain controlling.

## 1. Reference geometry

Four collector panels:

```text
4 panels x 4 ft x 4 ft
= 64 ft2 gross collection area
≈ 5.95 m2
```

Preferred operating slope:

```text
10-20 degrees above horizontal
```

Reference calculation slope:

```text
15 degrees
```

At 15 degrees, the vertical projected area is approximately:

```text
64 x sin(15°)
≈ 16.6 ft2
```

Keeping the collector low is therefore one of the strongest ways to reduce broadside wind demand.

## 2. Wind-pressure screening equation

For an initial screen, velocity pressure can be approximated from:

```text
q ≈ 0.00256 V^2  psf
```

where V is wind speed in mph.

This is the familiar sea-level dynamic-pressure relationship underlying code wind-load methods. Full ASCE 7 design requires additional exposure, topographic, directionality, gust, pressure-coefficient, and risk-category treatment.

For this prototype screen, an illustrative aerodynamic multiplier of 1.3 is applied to convert velocity pressure into a conservative panel-force estimate.

## 3. Wind scenarios

Three field-operational scenarios are used:

```text
40 mph  sheltered/moderate event
60 mph  strong wind event
80 mph  severe exposed event
```

These are scenario values, not Gaza code design speeds.

Approximate base velocity pressures:

| Wind speed | q |
|---|---:|
| 40 mph | 4.10 psf |
| 60 mph | 9.22 psf |
| 80 mph | 16.38 psf |

## 4. Low-profile 15-degree panel force

Using projected area ≈16.6 ft2 and multiplier 1.3:

```text
F = q x A_projected x 1.3
```

Approximate force:

| Wind | Force |
|---|---:|
| 40 mph | ~88 lbf |
| 60 mph | ~198 lbf |
| 80 mph | ~353 lbf |

If the resultant force acts approximately 1.5 ft above the base, overturning moments are roughly:

| Wind | Overturning moment |
|---|---:|
| 40 mph | ~132 ft-lb |
| 60 mph | ~297 ft-lb |
| 80 mph | ~530 ft-lb |

## 5. Ballast-only screening

Assume ballast resistance acts at an effective 3-ft lever arm from the overturning edge.

Required ballast weight before safety factor:

```text
W = overturning moment / 3 ft
```

Then apply a provisional 1.5 multiplier for prototype screening.

| Wind | Ballast after 1.5 factor |
|---|---:|
| 40 mph | ~66 lb / ~30 kg |
| 60 mph | ~149 lb / ~68 kg |
| 80 mph | ~265 lb / ~120 kg |

These values illustrate that a low-profile collector can plausibly use rubble ballast at moderate winds.

They do **not** capture every uplift/suction condition, connection failure, gust effect, or wind direction.

## 6. Broadside failure case

If the same 64-ft2 collector is accidentally or intentionally configured so most of the surface acts broadside to wind, demand increases sharply.

Using the full 64 ft2 area:

| Wind | Approx force |
|---|---:|
| 40 mph | ~341 lbf |
| 60 mph | ~767 lbf |
| 80 mph | ~1,363 lbf |

Using an illustrative 2.5-ft force height and 3-ft ballast lever arm with the same 1.5 screening factor gives ballast demand roughly:

| Wind | Approx ballast |
|---|---:|
| 40 mph | ~426 lb / ~193 kg |
| 60 mph | ~959 lb / ~435 kg |
| 80 mph | ~1,704 lb / ~773 kg |

This is the key engineering conclusion:

> Ballast-only stabilization becomes inefficient very quickly when a large sheet surface is exposed broadside to strong winds.

## 7. Design doctrine

The four-pallet system should therefore use:

```text
LOW PANEL ANGLE
+
MULTIPLE INDEPENDENT MODULES
+
RUBBLE BALLAST
+
GUYING / POSITIVE ANCHORAGE
+
STORM STOW / RELEASE LOGIC
```

rather than:

```text
LARGE CONTINUOUS SHEET
+
LOOSE BALLAST ONLY
```

## 8. Recommended prototype ballast tiers

For a 15-degree four-panel array, initial non-certified field-test ballast targets are:

### WB-1 — sheltered test

```text
minimum test ballast: ~50 kg total
```

Use only for controlled low-wind trials.

### WB-2 — moderate exposed prototype

```text
target rubble ballast: ~100-150 kg total
```

distributed between at least four anchor points.

### WB-3 — stronger-wind prototype

```text
target rubble ballast: ~200-300 kg total
+
positive guying / buried or structural anchors
```

Do not infer that 300 kg makes the collector code-compliant in severe wind.

The ballast range exceeds the simple static estimate deliberately because actual field load paths and debris foundations are uncertain.

## 9. Distributed ballast layout

Preferred layout:

```text
ANCHOR A -------- PANEL ARRAY -------- ANCHOR B
   |                                      |
   |                                      |
ANCHOR C ----------------------------- ANCHOR D
```

Each anchor should have its own rubble crate/gabion/pocket.

Advantages:

- load sharing;
- easier repair;
- one failed anchor does not release all ballast;
- geometry can be widened to increase resisting lever arm.

A wider base is often more efficient than simply adding more rubble vertically.

## 10. Rubble anchor modules

Candidate anchor:

```text
wire/fencing crate
~0.3-0.5 m3 gross volume
filled only as needed with screened masonry rubble
```

Actual required fill should be determined by measured rubble bulk density and target anchor mass.

For example, if field-measured bulk density were approximately 1,500 kg/m3:

```text
100 kg ballast ≈ 0.067 m3 rubble
200 kg ballast ≈ 0.133 m3 rubble
300 kg ballast ≈ 0.200 m3 rubble
```

Do not assume 1,500 kg/m3 without weighing a local sample.

## 11. Guying strategy

Rubble ballast should act as the deadweight anchor for guy lines rather than relying on friction under pallet feet alone.

Preferred:

- two windward guys;
- two leeward guys where practical;
- attachment to structural frame, not liner;
- low guy angle where space permits;
- abrasion protection at wire/rope contacts;
- independent knots/clamps or fasteners.

Guy lines should not cross pedestrian routes where they create a trip hazard.

## 12. Storm-stow architecture

The most material-efficient wind design may be a collector that can rapidly reduce projected area.

Possible strategies:

- fold panels flat;
- disconnect and stack panels;
- roll/furl tarp surface;
- release one edge of flexible membrane;
- hinge frame down onto rubble pad.

This can dramatically lower required ballast compared with designing a lightweight collector to remain deployed through every severe wind event.

## 13. Panel segmentation

Four independent 4x4-ft panels are preferred over one monolithic 8x8-ft sheet.

Reasons:

- smaller aerodynamic load per unit;
- easier stowage;
- easier replacement;
- independent anchoring;
- local damage does not disable all collection.

The hydraulic header can remain common while structural modules remain separate.

## 14. Connection gates

Wind resistance is controlled by the weakest element.

Inspect:

```text
liner-to-frame attachment
frame joints
frame-to-guy attachment
guy line
guy-to-rubble anchor
rubble-anchor containment
foundation settlement
```

A 200-kg ballast pile is irrelevant if a light screw or rotten pallet slat fails first.

## 15. Field pull test

Before storm deployment, each anchor should undergo a simple documented pull test where feasible.

Record:

- anchor mass;
- guy geometry;
- applied test force if measurable;
- movement/slip;
- frame deformation;
- connection damage.

The test should remain below any load that would create uncontrolled structural failure near personnel.

## 16. Wind operational states

Use three operating states:

### GREEN

Low/moderate wind.

```text
collector deployed
normal inspection
```

### AMBER

Strong winds expected or frame movement observed.

```text
increase ballast if safe
inspect guys
reduce panel angle
prepare stow
```

### RED

Severe wind, unstable debris foundation, damaged anchor, or frame movement.

```text
stow / flatten / remove collector surface
```

The system should prioritize preventing injury and preserving reusable components over collecting rain during the most severe wind conditions.

## 17. Temporary-structure context

Modern temporary-structure codes explicitly require wind-load consideration. The 2024 IBC contains dedicated wind provisions for public-occupancy temporary structures, reinforcing that temporary status does not eliminate wind risk. Full field deployment should use applicable local engineering requirements rather than this simplified screening model. 

The prototype calculations use the standard dynamic-pressure relationship q proportional to V^2, consistent with ASCE wind methodology. Because pressure rises with the square of speed, increasing wind from 40 to 80 mph produces approximately four times the dynamic pressure. 

## 18. Gate P8.2 status

P8.2 can be considered **analytically scaffolded but not validated**.

Completed:

- projected-area calculation;
- 40/60/80-mph force scenarios;
- overturning screen;
- ballast-only estimates;
- broadside failure demonstration;
- recommended ballast tiers;
- guying/stow doctrine.

Still required before closure:

1. obtain a Gaza/coastal regional wind climatology and gust envelope;
2. choose exact panel frame geometry;
3. test rubble bulk density;
4. define actual guy anchor spacing;
5. field-test frame and connection strength;
6. review a final configuration against applicable structural requirements.

## 19. Next pass

Proceed to P8.3:

**barrel-bank load and stability model for 1-4 approximately 200-L drums on screened rubble foundations.**

That pass should quantify:

- total dead load;
- support pressure;
- minimum load-spreader area;
- tipping sensitivity;
- rubble settlement;
- stand height versus gravity head;
- safe separation between barrels.
