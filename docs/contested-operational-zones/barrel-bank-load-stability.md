# Barrel-Bank Load and Stability Model for Rubble Foundations

## Purpose

This pass addresses roadmap item P8.3: estimate dead load, support pressure, stand geometry, tipping sensitivity, and load-spreader requirements for 1-4 approximately 200-L drums on screened rubble foundations.

This is a prototype engineering screen, not a certified structural design. Local ground conditions, barrel geometry, material condition, flood risk, seismic conditions, structural connections, and applicable engineering requirements remain controlling.

---

## 1. Reference barrel

Nominal vessel:

```text
55 US gal drum
≈ 208 L water capacity
```

Water mass at full volume:

```text
≈ 208 kg
```

Allow approximately 8-15 kg for the empty drum, lid, fittings, and small residual margin.

Reference filled mass used for design screening:

```text
220 kg per barrel
```

Equivalent weight:

```text
220 kg x 9.81 ≈ 2.16 kN
≈ 485 lbf
```

---

## 2. Total bank loads

| Barrels | Reference mass | Approx weight |
|---|---:|---:|
| 1 | 220 kg | 2.16 kN |
| 2 | 440 kg | 4.32 kN |
| 3 | 660 kg | 6.47 kN |
| 4 | 880 kg | 8.63 kN |

A four-drum bank therefore carries nearly 0.9 tonnes before adding stand, piping, ballast, or operators.

---

## 3. Reference geometry

Typical 55-gallon drum dimensions are approximately:

```text
diameter: ~0.58-0.60 m
height:   ~0.88-0.90 m
```

Reference footprint per drum:

```text
0.60 m x 0.60 m
= 0.36 m2 gross planning area
```

Circular true base area at 0.60 m diameter:

```text
A = pi r^2
≈ 0.283 m2
```

If the entire base were perfectly supported, bearing pressure from a 220-kg drum would be approximately:

```text
2.16 kN / 0.283 m2
≈ 7.6 kPa
```

This is modest for competent ground, but actual rubble contact is highly nonuniform unless a load-spreading cap is used.

---

## 4. Why direct barrel-on-rubble placement is poor practice

Direct placement creates:

- point loading on plastic or thin steel;
- puncture/abrasion risk;
- differential settlement;
- tilting;
- trapped water and corrosion zones;
- unstable outlet height;
- difficulty detecting leakage.

Preferred architecture:

```text
screened rubble sub-base
        ↓
leveled fine aggregate / flat masonry layer
        ↓
continuous load spreader
        ↓
barrel
```

---

## 5. Minimum load-spreader concept

For one drum, target a rigid support plate or plank deck at least slightly wider than the drum footprint.

Prototype target:

```text
0.70 m x 0.70 m
= 0.49 m2
```

Reference bearing pressure:

```text
2.16 kN / 0.49 m2
≈ 4.4 kPa
```

This lowers local bearing stress and, more importantly, bridges small voids in the rubble surface.

For four drums arranged 2 x 2, a continuous deck approximately:

```text
1.5 m x 1.5 m
= 2.25 m2
```

would give an average gross bearing pressure of:

```text
8.63 kN / 2.25 m2
≈ 3.8 kPa
```

before the stand/deck self-weight.

A continuous deck is preferable to four unrelated small pads because it reduces differential settlement between barrels.

---

## 6. Rubble pad geometry

Initial prototype pad for a four-drum bank:

```text
plan area: ~1.8 m x 1.8 m minimum
rubble depth: ~0.20-0.30 m
```

Recommended layering:

```text
stable native ground
    ↓
coarse screened rubble
    ↓
smaller graded rubble / crushed masonry
    ↓
flat cap layer
    ↓
rigid deck / load spreader
```

The pad should extend beyond the drum bank so edge settlement does not immediately destabilize the stand.

---

## 7. Stand height and gravity head

Raising the barrel increases useful gravity pressure but also raises the center of mass.

Hydrostatic pressure from water head is approximately:

```text
P = rho g h
```

Useful conversion:

```text
1 m water head ≈ 9.81 kPa ≈ 1.42 psi
```

If the barrel outlet is raised 0.30 m above the receiving point:

```text
available static head ≈ 2.9 kPa ≈ 0.43 psi
```

At 0.50 m:

```text
≈ 4.9 kPa ≈ 0.71 psi
```

These pressures are enough for simple gravity transfer through short, low-loss piping but not for high-pressure devices.

---

## 8. Recommended stand-height tiers

### BS-1 — low stand

```text
0.20-0.30 m elevation
```

Best default for:

- draw-off access;
- modest gravity transfer;
- lower tipping risk.

### BS-2 — moderate stand

```text
0.40-0.50 m elevation
```

Use where:

- more gravity head is useful;
- platform is broad and restrained;
- ground is competent.

### BS-3 — high stand

```text
>0.50 m
```

Requires stronger structural review because the raised center of mass increases overturning risk and consequences of failure.

For improvised rubble structures, the default should remain **low and broad**.

---

## 9. Center-of-mass screening

Assume a 0.90-m-high drum with roughly uniform water depth.

Approximate water center of mass when full:

```text
~0.45 m above drum base
```

If mounted on a 0.30-m stand:

```text
combined water COM ≈ 0.75 m above ground
```

If mounted on a 0.50-m stand:

```text
≈ 0.95 m above ground
```

Higher placement increases lateral-load overturning sensitivity.

---

## 10. Simple tipping screen

For a barrel on a 0.60-m-wide base, the geometric tipping angle from gravity alone is roughly:

```text
tan(theta) = half-width / COM height
```

### 0.30-m stand

```text
half-width = 0.30 m
COM ≈ 0.75 m

theta ≈ arctan(0.30/0.75)
≈ 22 degrees
```

### 0.50-m stand

```text
COM ≈ 0.95 m

theta ≈ arctan(0.30/0.95)
≈ 18 degrees
```

This illustrates why a narrow elevated barrel is vulnerable to uneven settlement or lateral impact.

A shared wide deck and barrel restraints materially improve stability.

---

## 11. Bank arrangement

Preferred four-drum arrangement:

```text
[A] [B]
[C] [D]
```

rather than a tall vertical stack or long narrow row.

Advantages:

- broad footprint;
- lower overturning sensitivity;
- shorter manifold runs;
- shared load spreader;
- easier cross-bracing.

Approximate bank footprint including spacing:

```text
1.4-1.6 m square
```

before access clearance.

---

## 12. Barrel separation

Leave enough clearance to:

- inspect sidewalls;
- access valves;
- detect leaks;
- remove one barrel without disturbing all others.

Prototype target:

```text
75-150 mm between drums
```

where site area permits.

Do not pack barrels so tightly that valves or sidewalls become inaccessible.

---

## 13. Restraint system

A filled drum is heavy but can still shift during impact, flooding, stand settlement, or seismic motion.

Preferred restraint:

- perimeter frame around lower third of barrels;
- upper strap or cross-brace where feasible;
- straps attached to structural stand, not plumbing;
- removable restraints for barrel replacement.

The restraint should prevent lateral walking without crushing the vessel.

---

## 14. Flood and scour risk

A raised bank in a contested zone must not be placed in a drainage path.

Floodwater can:

- erode rubble support;
- undercut one corner;
- float partially empty barrels;
- contaminate outlets;
- carry sewage or debris into the storage area.

Therefore:

```text
barrel bank
must be upslope / outside dirty runoff path
```

and protected by drainage/berm logic developed elsewhere in the sector.

---

## 15. Differential settlement gate

Differential settlement is likely a bigger risk than average soil bearing pressure.

Field check:

Measure deck elevation at all four corners during installation, then again after:

- first filling;
- 24 hours;
- first major rain event;
- first empty/refill cycle.

Prototype alert threshold:

```text
>10 mm corner-to-corner change
```

should trigger inspection and re-leveling.

This is a conservative operational trigger, not a formal geotechnical criterion.

---

## 16. Settlement indicators

Investigate if:

- one barrel leans;
- manifold alignment changes;
- valves bind;
- water levels appear unequal when they should not;
- deck gaps open;
- rubble migrates from edge;
- overflow path changes;
- straps become loose or overly tight.

---

## 17. Plumbing load isolation

Do not let rigid plumbing become a structural brace between settling barrels.

Preferred:

- short flexible couplings where compatible;
- independently supported manifolds;
- valves near each barrel;
- removable unions.

If one drum settles, piping should not be forced to carry the vessel load.

---

## 18. Raw versus treated storage

Raw and treated barrels should not share a common stand manifold unless hydraulically isolated.

Preferred:

```text
RAW BANK
separate from
CLEAN BANK
```

Even if both sit on the same rubble pad, use distinct labels, valves, and plumbing.

---

## 19. Structural material strategy

### Rubble roles

- sub-base;
- ballast;
- erosion control;
- outer retaining geometry.

### Controlled structural cap

Use one of:

- sound timber deck;
- flat stone slabs;
- known steel plate/frame;
- intact concrete slab fragments after screening.

### Water-contact path

Rubble should not touch stored treated water.

---

## 20. Prototype loading summary

### One barrel

```text
reference mass: 220 kg
minimum preferred load spreader: ~0.70 x 0.70 m
stand: 0.20-0.30 m default
```

### Two barrels

```text
reference mass: 440 kg
preferred shared deck: ~0.8 x 1.5 m or larger
```

### Four barrels

```text
reference mass: 880 kg
preferred shared deck: ~1.5 x 1.5 m or larger
rubble pad: ~1.8 x 1.8 m or larger
```

The exact dimensions must be adjusted to actual drum diameter and access requirements.

---

## 21. Commissioning load test

Before relying on the bank:

1. inspect rubble screening and pad drainage;
2. level the load spreader;
3. place empty drums;
4. fill to ~25%;
5. inspect settlement;
6. fill to ~50%;
7. inspect again;
8. fill to 100%;
9. inspect deck, restraints, plumbing, and corner elevations;
10. re-check after 24 hours.

Stop if:

- deck cracks or bows visibly;
- one corner settles rapidly;
- barrel wall distorts;
- restraint tears vessel surface;
- plumbing becomes load-bearing;
- rubble pad begins to shear or migrate.

---

## 22. P8.3 gate status

P8.3 is now **analytically scaffolded but not field-validated**.

Completed:

- full-mass estimates for 1-4 barrels;
- bearing-pressure screen;
- shared-deck concept;
- stand-height/head tradeoff;
- center-of-mass and tipping screen;
- differential-settlement logic;
- restraint and plumbing-isolation guidance;
- commissioning load-test sequence.

Remaining before closure:

1. weigh actual barrels and fittings;
2. measure actual rubble bulk density;
3. test local pad settlement under staged filling;
4. select exact load-spreader material and thickness;
5. confirm restraint geometry;
6. verify local flood/drainage exposure;
7. obtain structural review for larger communal tanks.

---

## 23. Next roadmap item

Proceed to **P1.2 — first-flush hydraulic correction and freeze**.

That pass should formalize:

- FF-M1 manual/simple diverter;
- FF-F1 floating-ball shutoff;
- reset logic;
- drain/cleanout;
- sizing by catchment area;
- explicit failure modes;
- no assumption that an open standpipe branch automatically isolates after filling.
