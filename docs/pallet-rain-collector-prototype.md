# Pallet Rain Collector Prototype

## Purpose

This prototype converts a wooden shipping pallet or equivalent salvaged timber frame into a small freestanding rainwater catchment system for low-resource settings where barrels or cisterns may be available but roof repair, gutter replacement, or structural modification is unaffordable.

The design assumption is deliberately conservative:

```text
storage may already exist
wood and repair materials may be locally abundant
housing stock may be old
roof access may be unsafe or unaffordable
specialized fittings may be scarce
```

The system is modular, resident-buildable, gravity-fed, and intended to make the **catchment structure inexpensive and replaceable** while preserving a controlled water-contact layer.

Collected water is **experimental and non-potable by default** unless the entire contact path, treatment train, and resulting water quality are independently validated for the intended use.

## Core architecture

```text
ELEVATED SALVAGED PALLET / WOOD FRAME
        ↓
REPLACEABLE WATERPROOF SKIN
        ↓
LOW-EDGE GUTTER ABOVE STORAGE INLET
        ↓
REMOVABLE DEBRIS SCREEN
        ↓
FIRST-FLUSH DIVERTER
        ↓
GRAVITY DROP
        ↓
EXISTING BARREL / CISTERN
        ↓
CONTROLLED OVERFLOW
```

The pallet is primarily **structure**. The liner or other characterized surface is the primary rainwater-contact layer.

## Sketch and deployment geometry requirement

All future sketches, diagrams, field drawings, and prototype layouts for the pallet collector must show the catchment **elevated above the receiving barrel or cistern inlet**. A pallet resting flat on the ground is not the reference architecture.

The purpose of the elevation is hydraulic, not decorative: the entire pathway from collector to storage must operate by gravity without requiring a pump.

Reference vertical relationship:

```text
          UPPER PALLET EDGE
                /--------/
               / LINER  /
              /--------/
                  ↓
             LOW-EDGE GUTTER
                  ↓
              SCREEN / TEE
                  ↓
          FIRST-FLUSH DIVERTER
                  ↓
             GRAVITY DROP
                  ↓
          BARREL / CISTERN INLET
            ┌─────────────┐
            │             │
            │   STORAGE   │
            │             │
            └─────────────┘
```

### Mandatory sketch cues

Every concept sketch should visibly communicate:

- pallet collector supported on legs, braces, blocks, a second pallet, or another stable frame;
- low collector edge and gutter **higher than the barrel/cistern inlet**;
- continuously descending pipe or channel from gutter to storage;
- first-flush diverter positioned without creating an uphill return path;
- barrel/cistern on stable ground or a low broad base;
- overflow leaving the storage vessel independently of the collector;
- no requirement to lift collected water into storage.

The minimum useful elevation is the amount needed to preserve positive hydraulic fall through the gutter, screen, first-flush hardware, connecting pipe, and storage inlet. Final dimensions should be derived from the actual barrel/cistern and fittings rather than from one universal height.

### Reference prototype height logic

For a typical 55-gallon drum, the inlet is near the top of a vessel roughly 34-36 in high. A practical sketch should therefore begin with the pallet's low collection edge approximately **42-48 in above grade**, then confirm that the actual plumbing configuration preserves downward slope to the inlet.

This is a starting geometry, not a fixed requirement. A lower cistern inlet can permit a lower collector; a taller barrel or large first-flush assembly may require greater elevation.

The preferred rule is:

```text
LOW EDGE OF CATCHMENT
        >
GUTTER OUTLET
        >
TRANSFER / TEE ELEVATION
        >
STORAGE INLET
```

with sufficient vertical separation to prevent standing water, reverse slope, or backup during heavy rainfall.

The structure should not be raised higher than necessary. Excessive elevation increases overturning risk and structural demand. The design objective is **minimum stable elevation that reliably gravity-feeds the chosen storage vessel**.

## Reference pallet geometry

Do not assume all pallets are 4 ft x 4 ft.

A useful reference module is the common approximately **48 x 40 in** pallet:

```text
surface area ≈ 13.3 ft2
```

Some locally available pallets may be approximately 48 x 48 in:

```text
surface area = 16 ft2
```

The actual pallet must be measured before estimating yield or cutting a liner.

### Operating slope

Initial prototype range:

```text
10-20 degrees from horizontal
nominal starting point: ~15 degrees
```

This is intentionally much shallower than a steep A-frame. The objective is to provide reliable drainage while retaining most of the horizontal rainfall interception area and keeping wind loading manageable.

The frame must still be adjusted if local wind, debris, drainage, snow, or terrain conditions require a different angle.

## Rainfall-yield correction: use horizontal projected area

Rainfall depth is normally referenced to a horizontal surface. Therefore the rainfall-volume model for a tilted collector should use its **horizontal projected area**:

```text
A_projected = A_surface × cos(theta)
```

and:

```text
V_theoretical = 0.623 × A_projected × rainfall_inches
```

where volume is in US gallons when area is in ft2.

### Example: 48 x 40 in pallet at 15 degrees

```text
A_surface = 13.33 ft2
A_projected = 13.33 × cos(15 deg)
            ≈ 12.88 ft2
```

For one inch of rainfall:

```text
V_theoretical ≈ 0.623 × 12.88
              ≈ 8.0 gal/in
```

At an illustrative 80% recovery efficiency:

```text
V_recovered ≈ 6.4 gal/in
```

Four such modules would therefore produce approximately:

```text
~25.6 gal per inch of rain
```

at the same assumed efficiency.

### Example: 48 x 48 in pallet at 15 degrees

```text
A_surface = 16 ft2
A_projected ≈ 15.45 ft2
V_theoretical ≈ 9.6 gal/in
V_recovered at 80% ≈ 7.7 gal/in
```

These are modeled yields. Field measurements should replace assumed recovery efficiency as soon as prototype data exist.

## Salvaged-pallet acceptance gate

The research objective is not to require new lumber. It is to identify when aged wood remains useful as **structure** and when it should be rejected.

### Accept for structural prototype use

Candidate pallet is generally acceptable for further inspection when:

- deck boards and stringers are substantially intact;
- joints can be tightened with screws, bolts, straps, or battens;
- wood is dry enough to inspect;
- no major rot is present at load-bearing joints;
- no strong chemical or petroleum odor is present;
- no visible chemical residue, heavy oil contamination, or unknown powder is present;
- the frame can be braced without relying on badly split members.

### Repair before use

Repairable conditions may include:

- one or more missing deck boards;
- loose nails;
- minor checking or end splits;
- localized surface weathering;
- damaged non-critical slats;
- uneven deck surface that can be bridged by battens or a backing sheet.

The liner should not depend on rough aged pallet boards for a smooth hydraulic surface. A thin backing layer, battens, or tensioned membrane can bridge gaps.

### Reject from collector structure

Reject pallets with:

- advanced rot in stringers or major joints;
- structural crushing;
- widespread insect damage that materially reduces section strength;
- obvious chemical spills or persistent unknown contamination;
- strong petroleum, pesticide, solvent, or other chemical odor;
- fire damage that has materially weakened the frame;
- instability that cannot be corrected with simple local reinforcement.

Rejected wood may still have non-water-contact uses if locally appropriate, but should not be represented as a verified collector component.

## Pallet markings and provenance

Where markings are present, record them photographically rather than assuming age or appearance identifies treatment history.

Unknown provenance does **not** automatically make the pallet unusable as an external structural frame. It does mean the project should prevent the wood itself from being treated as a validated drinking-water contact surface.

Core rule:

```text
UNKNOWN / AGED WOOD
        ↓
STRUCTURE ONLY
        ↓
CONTROLLED LINER
        ↓
CONTROLLED WATER PATH
```

## Catchment skin

Candidate prototype surfaces include:

- intact EPDM or pond-liner membrane;
- heavy polyethylene sheet;
- characterized roofing membrane;
- other intact waterproof liner appropriate to the intended research use.

Unknown paints, aged coatings, treated wood, old roofing residues, or chemically contaminated sheet material should not be assumed suitable for drinking-water contact.

The liner should:

- extend beyond the wood edge;
- be secured with washers, battens, rope, clips, or other broad-load fasteners rather than relying only on staples;
- drain continuously toward the gutter;
- avoid deep wrinkles or pockets;
- be removable without destroying the pallet frame;
- be replaceable independently of the structural wood.

This creates a repair hierarchy:

```text
wood frame lasts as long as structurally useful
liner is replaced when damaged or unsuitable
gutter is independently repairable
storage remains independent
```

## Freestanding support architecture

The collector should not require attachment to an aging roof or exterior wall.

Reference side geometry:

```text
               upper edge
                  _________
                 /        /
                / liner  /
               /________/
                   ↓
                 gutter
                   ↓
             gravity plumbing
                   ↓
          top/side inlet of barrel
              ┌─────────┐
              │ storage │
              └─────────┘

 elevated legs / rear brace
 +
 low broad footing
 +
 ballast or anchors as required
```

Possible structural inputs include:

- second pallet used as a rear brace/base;
- scrap dimensional lumber;
- short poles;
- masonry blocks;
- screened rubble used outside the water-contact path;
- earth anchors or stakes where appropriate.

The collector must be high enough for gravity transfer to the storage inlet while remaining as low and broad as practical for stability.

## Gutter and hydraulic path

The hydraulic path should preserve gravity flow and avoid unnecessary traps or undersized transitions.

```text
CATCHMENT
   ↓
GUTTER
   ↓
COARSE SCREEN
   ↓
VERTICAL DROP / TEE
   ├── FIRST-FLUSH STANDPIPE
   └── LATER FLOW TO STORAGE
                ↓
          BARREL / CISTERN
                ↓
             OVERFLOW
```

### Gutter

For one pallet:

- length approximately equal to the measured low edge;
- split PVC, bent sheet metal, folded liner channel, or conventional gutter section;
- minimum slope around 1/8 in per ft toward outlet as a starting point;
- avoid flat sections that retain sediment or water.

A 2-3 in nominal gutter is a useful prototype starting range for one small collector, but actual capacity must be checked under locally relevant rainfall intensity.

### Low-material gutter option

Where conventional gutter is unavailable, the catchment liner itself may extend past the lower deck and fold into a supported trough.

```text
liner surface
      ↓
liner fold / trough
      ↓
small outlet fitting
```

This reduces the number of distinct manufactured parts, but the fold must not trap water or tear under accumulated load.

### Downpipe

A 2 in nominal downpipe is a useful low-cost starting point because it provides greater debris tolerance than small hose.

The path from gutter to diverter should remain:

```text
short
smooth
continuously descending
accessible for cleaning
```

## First-flush logic

A simple first-flush diverter can use a vertical capped standpipe below a tee.

```text
                 to storage
                    →
              ┌─────┴─────┐
collector  →  │     T     │
              └─────┬─────┘
                    │
                    │ first-flush standpipe
                    │
                    ● slow drain / cleanout
```

Initial prototype test volumes for a single pallet module:

```text
0.25 gal
0.5 gal
1.0 gal
```

Do not freeze one universal value. Compare first-flush volume against rainfall interval, visible contamination, turbidity, and other available water-quality observations.

Approximate cylindrical-pipe capacities:

- 2 in pipe: ~0.16 gal/ft;
- 3 in pipe: ~0.37 gal/ft;
- 4 in pipe: ~0.65 gal/ft.

Actual inside diameter must be used for final dimensions.

## Storage interface

The architecture assumes barrels or cisterns may already be locally available.

Preferred interface characteristics:

- closed or closable lid;
- screened inlet;
- protected vent;
- overflow near maximum intended water level;
- low-point drain or service outlet where practical;
- stable broad footing;
- known previous contents when water quality matters.

Unknown prior container contents should not be treated as drinking-water safe merely because the container appears clean.

## Overflow

Overflow is a required part of the architecture.

Recommended characteristics:

- capacity comparable to the inlet path;
- discharge away from foundations, footpaths, latrines, and unstable slopes;
- erosion-resistant termination;
- visible flow so blockages or full-storage events are apparent.

Possible destinations include a stable rock apron, vegetated swale, rain garden, infiltration area, or another locally appropriate drainage feature.

## Modular scaling

The smallest reference architecture is:

```text
1 elevated pallet collector
→ 1 existing barrel
```

Expansion can occur without changing the basic module:

```text
2 elevated pallets → 1 barrel / cistern
4 elevated pallets → barrel bank / cistern
```

or as independent units:

```text
1 pallet → 1 barrel
1 pallet → 1 barrel
1 pallet → 1 barrel
```

Independent modules may be preferable where repair capacity is limited because one failure does not disable the entire system.

## Barrel-fill intuition

For a nominal 48 x 40 in collector at 15 degrees and an illustrative 80% recovery:

```text
~6.4 gal collected per inch of rain
```

Therefore a 55-gallon barrel would require roughly:

```text
55 / 6.4 ≈ 8.6 inches of cumulative rainfall
```

from one module if the barrel starts empty and there are no withdrawals or overflow losses.

Four modules feeding the same storage could theoretically collect roughly 25-26 gallons per inch under the same assumptions, meaning a 55-gallon barrel could fill during a little over two inches of cumulative rainfall.

This illustrates why the architecture should scale by **adding inexpensive collector area to storage that already exists**.

## Wind and stability gate

A freestanding elevated collector introduces wind load that a roof-mounted rain barrel does not.

Before field use, verify:

- frame cannot rack easily by hand;
- rear brace cannot fold under normal handling;
- feet cannot slide on the local surface;
- liner attachment cannot peel progressively from one corner;
- collector elevation remains stable under asymmetric loading;
- the structure remains stable with storage both empty and full;
- ballast or anchors do not create trip hazards or interfere with drainage.

A high-angle or unnecessarily tall collector may increase wind exposure and overturning moment. For the first pallet prototype, use the lowest practical angle and minimum elevation that still provide reliable drainage and gravity transfer into storage.

## Field measurements

Each prototype should record:

```text
actual pallet dimensions
collector angle
low-edge height above grade
storage-inlet height above grade
vertical head between gutter outlet and storage inlet
horizontal projected area
rainfall depth
first-flush volume
storage volume before storm
storage volume after storm
overflow occurrence
visible debris / turbidity
leakage
liner condition
frame movement or damage
maintenance performed
```

Calculate:

```text
collection efficiency = measured captured volume / theoretical rainfall volume
```

with:

```text
V_theoretical = 0.623 × A_projected × rainfall_inches
```

for gallons and ft2.

## Prototype gates

### P0 - salvage acceptance

Document pallet dimensions, condition, provenance/markings where visible, contamination concerns, and required repairs. Reject unsafe structural stock.

### P1 - elevated structural geometry

Collector is independently supported above grade, remains stable under handling and locally relevant wind exposure, and maintains the required gravity-feed relationship to the storage inlet.

### P2 - hydraulic

Gutter, screen, diverter, storage inlet, and overflow pass a simulated heavy-rain test without uncontrolled backup. The complete path from catchment to storage remains continuously gravity-descending.

### P3 - first flush

First runoff is measurably separated and the diverter reliably resets between events.

### P4 - collection efficiency

Measure actual versus theoretical captured rainfall over multiple storms using projected area.

### P5 - durability

Track liner puncture, UV/weather exposure, wood movement, fastener loosening, gutter distortion, support settlement, and repair frequency.

### P6 - resident maintenance

A resident can inspect the frame, clean the screen, repair or replace the liner, service the diverter, and manage overflow with ordinary tools and locally obtainable parts.

### P7 - cost and salvage fraction

Record:

```text
new-material cost
salvaged-material fraction
labor time
replacement consumables
maintenance time
```

Useful comparison metrics include:

```text
$/ft2 catchment
$/gallon storage connected
liters collected / dollar of new material
liters collected / labor-hour
```

### P8 - water-quality/use boundary

Collected water remains experimental/non-potable unless a separate validated water-contact, treatment, testing, and use-classification pathway is established.

## Design principle

The pallet system is not primarily a rain barrel accessory. It is a method for manufacturing **new elevated catchment area from locally abundant structural waste without touching an unsafe or unaffordable roof**.

```text
ABUNDANT AGED WOOD
        +
SIMPLE REPAIR / BRACING
        +
ELEVATED GRAVITY-FEED GEOMETRY
        +
REPLACEABLE WATERPROOF SKIN
        +
EXISTING STORAGE
        =
LOW-COST MODULAR MICRO-CATCHMENT
```

The research question is therefore not simply whether a pallet can collect rain. It is whether a pallet-based module can deliver useful water volume per unit cost, labor, and maintenance while remaining structurally understandable, repairable, gravity-fed, and honest about water quality.