# First-Flush Hydraulic Design Freeze

## Purpose

This pass closes roadmap item P1.2 by freezing two first-flush variants for the pallet/rubble rain-collector family:

```text
FF-M1 — manual/simple diverter
FF-F1 — floating-ball positive-closure diverter
```

A plain open tee with a vertical standpipe is **not** treated as an automatic self-isolating first-flush device. After the standpipe fills, water can continue interacting with that branch unless a deliberate hydraulic or mechanical closure exists.

The first-flush stage reduces initial debris and contamination loading. It does not by itself make collected water potable.

---

## 1. System location

Reference sequence:

```text
COLLECTOR
  ↓
GUTTER
  ↓
SCREEN
  ↓
FIRST FLUSH
  ↓
RAW STORAGE
```

The first-flush device belongs upstream of raw storage and must never discharge directly into clean storage.

---

## 2. Reference collector areas

Current prototype sizes:

```text
single 4 x 4 ft panel  = 16 ft2
single 4 x 8 ft panel  = 32 ft2
four 4 x 4 ft panels   = 64 ft2
four 4 x 8 ft panels   = 128 ft2
```

First-flush sizing should be documented as a function of catchment area and site contamination burden rather than treated as one universal volume.

A practical research starting band drawn from common rainwater-harvesting practice is approximately:

```text
1-2 gal first flush per 100 ft2 catchment
```

This is a provisional design band for comparison and field testing, not a universal public-health requirement.

Corresponding starting volumes:

| Catchment | 1 gal/100 ft2 | 2 gal/100 ft2 |
|---|---:|---:|
| 16 ft2 | 0.16 gal | 0.32 gal |
| 32 ft2 | 0.32 gal | 0.64 gal |
| 64 ft2 | 0.64 gal | 1.28 gal |
| 128 ft2 | 1.28 gal | 2.56 gal |

Dust, ash, bird activity, demolition debris, long dry periods, industrial fallout, or visible contamination may justify larger diversion or complete rejection of an event.

---

## 3. Standpipe volume reference

Approximate water volume per foot of vertical pipe:

| Nominal pipe | Approx gal/ft |
|---|---:|
| 2 in | ~0.16 |
| 3 in | ~0.37 |
| 4 in | ~0.65 |

Therefore approximate straight-pipe lengths for 1 gallon are:

```text
2 in pipe -> ~6.25 ft
3 in pipe -> ~2.7 ft
4 in pipe -> ~1.5 ft
```

These are conceptual volumes; fittings and actual internal diameter alter capacity.

---

# 4. FF-M1 — manual/simple diverter

## Architecture

```text
GUTTER / DOWNPIPE
      ↓
SCREEN
      ↓
MANUAL DIVERTER
   ↙       ↘
FIRST       RAW
FLUSH       STORAGE
```

The operator deliberately routes initial runoff to waste/first-flush storage, then switches flow to raw storage after the target volume or event condition is met.

## Preferred mechanisms

- swing hose;
- two-position valve;
- removable elbow;
- Y fitting with one branch capped/opened manually;
- simple diverter flap.

The operator should be able to see which path is active.

## Advantages

- lowest complexity;
- minimal specialized hardware;
- easily repaired;
- failure state is visible;
- works with improvised plumbing.

## Weaknesses

- requires operator presence;
- can be forgotten during sudden rain;
- incorrect valve position can send dirty runoff to raw storage;
- training and pictorial SOP required.

---

## 5. FF-M1 operating states

### RESET

```text
collector clean enough for event
screen installed
first-flush path OPEN
raw-storage path CLOSED
```

### DIVERT

Initial runoff goes to first-flush/waste path.

### SWITCH

Once required diversion volume/condition is met:

```text
first-flush path CLOSED
raw-storage path OPEN
```

### POST-EVENT

- close raw inlet;
- drain first-flush chamber;
- clean screen;
- inspect for debris/ash/oil/fecal material;
- return system to RESET.

---

# 6. FF-F1 — floating-ball positive closure

## Architecture

```text
GUTTER / DOWNPIPE
      ↓
SCREEN
      ↓
TEE
   ↙     ↘
VERTICAL   RAW STORAGE
FIRST-FLUSH
CHAMBER
   ↓
FLOAT BALL
   ↓
SEAT / CLOSURE
```

Initial water preferentially fills the first-flush chamber. As the water level rises, a buoyant ball is driven into a seat, creating a **positive closure** of the first-flush branch. Subsequent flow then proceeds to raw storage.

The closure mechanism must be physically verified; the presence of a ball alone is not proof of sealing.

---

## 7. FF-F1 design requirements

### Ball

Must be:

- buoyant in water;
- chemically compatible with expected water contact;
- too large to pass through the seat;
- smooth enough to seal consistently;
- accessible for inspection.

### Seat

Must:

- center the ball;
- produce repeatable closure;
- avoid sharp edges;
- remain inspectable and cleanable.

### Chamber

Must:

- hold the design diversion volume;
- drain/reset after the event;
- permit sediment removal;
- remain structurally supported.

### Reset drain

Preferred:

```text
small controlled drain / valve
```

The chamber must reset before the next rainfall event.

---

# 8. FF-F1 failure modes

| Failure | Consequence | Required response |
|---|---|---|
| Ball missing | no positive closure | divert manually / stop potable-research collection |
| Ball jammed low | first-flush branch remains open | inspect/clean/reset |
| Ball jammed high | first flush bypassed | reject initial runoff event / reset |
| Seat fouled | leakage after supposed closure | clean and retest |
| Chamber not drained | little/no diversion next event | drain/reset |
| Drain left open | continuous water loss | close/reset |
| Chamber cracked | uncontrolled bypass/leak | repair/replace |
| Incorrect chamber volume | inadequate/excessive diversion | resize/document |

---

# 9. Manual versus floating-ball selection

Use FF-M1 when:

- operator presence is reliable;
- hardware availability is minimal;
- maintainability is more important than automation;
- transparent operation is desired.

Use FF-F1 when:

- rain may begin without operator presence;
- hardware quality is sufficient;
- ball/seat assembly can be inspected and maintained;
- automatic positive closure adds practical value.

Neither system should be selected solely because it appears more sophisticated.

---

# 10. Standardized interfaces

To keep the collector modular, freeze a standard first-flush interface concept:

```text
UPSTREAM: screened downpipe connection
DOWNSTREAM: raw-storage inlet connection
WASTE: visible drain / chamber
```

Preferred prototype plumbing size:

```text
1.5-2 in main conveyance
```

for household-scale pallet collectors, subject to actual rainfall intensity and gutter geometry.

The first-flush module should be removable without rebuilding the catchment frame.

---

# 11. Hydraulic principles

The module should avoid unnecessary restriction in the main flow path.

Key checks:

- gutter/downpipe capacity exceeds expected event flow;
- screen does not create excessive ponding;
- first-flush branch actually receives initial flow;
- downstream raw-storage inlet does not backflood the diverter;
- chamber drain does not siphon or continuously steal flow during collection;
- overflow has a safe path.

For a collector area A and rainfall intensity i:

```text
Q = C * i * A
```

where C is a runoff coefficient appropriate to the catchment surface.

Use measured event behavior where possible rather than relying only on design rainfall assumptions.

---

# 12. First-flush commissioning test

Before field use:

1. set system to RESET;
2. apply clean test water at representative low flow;
3. observe first-flush fill path;
4. verify target chamber volume;
5. verify switch/closure;
6. increase flow to a higher test rate;
7. check for bypass, backup, leakage, or overflow;
8. confirm raw-storage path activates only after intended diversion;
9. drain/reset;
10. repeat at least three cycles.

For FF-F1, verify the ball seats reliably each cycle.

---

# 13. Fail-visible requirements

Each first-flush module must expose its operating state.

FF-M1:

```text
valve/diverter position visible
```

FF-F1:

```text
float/chamber state visible directly
or through inspection window / indicator
```

If closure state cannot be determined:

```text
STATUS = GRAY
```

for drinking-water research use until inspected.

---

# 14. Dust / conflict-debris event logic

In high-dust or demolition environments, first flush should be treated as an adaptive control.

After:

- nearby demolition;
- major dust storm;
- fire/smoke deposition;
- visible ash;
- bird/animal fouling;
- long dry interval;

operator should:

1. inspect catchment;
2. clean if practical;
3. increase diversion or reject event if contamination is severe;
4. document the decision.

First flush is not an adequate control for unknown chemical deposition or heavily contaminated surfaces.

---

# 15. First-flush classification boundary

First flush can reduce:

- loose debris;
- dust;
- some surface microbial loading;
- initial accumulated contamination.

It does **not** reliably remove:

- dissolved metals;
- salinity;
- nitrate;
- persistent chemical leaching;
- contamination continuously released from the catchment material.

Therefore:

```text
FIRST FLUSH != POTABILITY
```

---

# 16. Design freeze

The project now freezes the following principles:

```text
1. PLAIN OPEN TEE/STANDPIPE IS NOT AN AUTOMATIC FIRST-FLUSH SHUTOFF.
2. FF-M1 IS THE DEFAULT LOW-COMPLEXITY VARIANT.
3. FF-F1 REQUIRES A VERIFIED BALL-AND-SEAT POSITIVE CLOSURE.
4. FIRST-FLUSH STATE MUST BE VISIBLE.
5. MODULE MUST RESET BETWEEN EVENTS.
6. DIRTY INITIAL RUNOFF MUST NOT ENTER CLEAN STORAGE.
7. FIRST-FLUSH VOLUME MUST BE DOCUMENTED BY CATCHMENT AREA.
8. HEAVY DUST/CHEMICAL EVENTS MAY REQUIRE EVENT REJECTION, NOT JUST LARGER FIRST FLUSH.
9. FIRST FLUSH DOES NOT SUBSTITUTE FOR TREATMENT OR WATER-QUALITY VERIFICATION.
```

---

# 17. Bench specification for four-pallet reference system

Reference catchment:

```text
4 x 4 ft x 4 panels
= 64 ft2
```

Starting first-flush research band:

```text
~0.6-1.3 gal
(~2.3-4.9 L)
```

Suggested prototype comparison:

```text
FF-M1-A = 2.5 L manual diversion
FF-M1-B = 5.0 L manual diversion
FF-F1-A = 2.5 L float chamber
FF-F1-B = 5.0 L float chamber
```

Compare:

- turbidity of first-flush vs post-flush water;
- E. coli/indicator results where appropriate;
- conductivity/pH changes;
- debris load;
- reset reliability;
- operator error;
- lost water fraction.

No volume should be promoted as universal until field data support it.

---

## Next pass

Proceed to **P2.2 contamination-isolated barrel manifold**.

The next design should allow any one raw or clean barrel to be isolated, removed, cleaned, or rejected without contaminating the rest of the bank.
