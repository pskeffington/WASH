# Contamination-Isolated Barrel Manifold

## Purpose

This pass addresses roadmap item P2.2: define a barrel-bank manifold that allows any one raw or clean storage vessel to be isolated, removed, cleaned, rejected, or replaced without hydraulically or mechanically compromising the rest of the bank.

The design is intended for low-resource, gravity-fed WASH systems using approximately 200-L barrels. It is a prototype architecture, not a plumbing certification.

---

## 1. Core design rule

```text
ONE BARREL FAILURE
MUST NOT FORCE
THE ENTIRE BANK TO FAIL
```

Each barrel should therefore have:

- its own isolation valve;
- a short flexible connection;
- a removable union/coupling;
- a clearly labeled ID;
- independent status classification;
- no structural dependence on rigid manifold piping.

---

## 2. Raw and clean banks remain separate

Never combine raw and treated barrels into one common manifold.

Preferred architecture:

```text
RAW BANK
[A] [B] [C] [D]
 |   |   |   |
 V   V   V   V
raw manifold
    ↓
pretreatment / filter

CLEAN BANK
[A] [B] [C] [D]
 |   |   |   |
 V   V   V   V
clean manifold
    ↓
controlled dispensing
```

Raw and clean fittings should be visually and, where practical, mechanically distinct.

---

## 3. Barrel branch architecture

Each barrel branch should follow:

```text
BARREL OUTLET
   ↓
LOCAL SHUTOFF VALVE
   ↓
SHORT FLEXIBLE HOSE
   ↓
REMOVABLE UNION / QUICK COUPLING
   ↓
COMMON MANIFOLD
```

The local valve should be mounted close enough to the barrel that the vessel can be isolated before disconnecting the flexible branch.

---

## 4. Why flexible branches matter

Rigid manifold connections can transmit:

- rubble-pad settlement;
- barrel tilt;
- thermal expansion;
- handling force;
- accidental impact.

into the barrel wall or fitting.

A short flexible branch reduces the chance that plumbing becomes structural bracing.

Recommended concept:

```text
150-500 mm flexible branch
```

where compatible tubing/hose is available.

Exact hose material must match intended use.

---

## 5. Individual branch isolation

Each barrel should be capable of the following state independently:

```text
OPEN
CLOSED
DISCONNECTED
QUARANTINED
```

Example:

```text
[A OPEN]
[B CLOSED]
[C QUARANTINED]
[D OPEN]
```

The manifold should still function with one or more branches removed.

---

## 6. No hidden crossflow assumption

If multiple barrels share a bottom manifold, water levels will tend to equalize whenever isolation valves are open.

This creates a contamination risk:

```text
ONE CONTAMINATED BARREL
+
OPEN COMMON MANIFOLD
=
POTENTIAL CONTAMINATION OF ALL CONNECTED BARRELS
```

Therefore:

- new/uncertain barrels enter CLOSED;
- barrels should not be joined to a clean bank until status is established;
- suspicious barrels are isolated immediately;
- cleaning one barrel requires disconnecting it from the bank.

---

## 7. Preferred clean-bank strategy

For treated water, prefer **draw-from-bank without uncontrolled refill between vessels** where practical.

Two operating modes are acceptable:

### Mode CB-1 — isolated vessels

```text
[A] [B] [C] [D]

no hydraulic cross-connection during storage
```

Each barrel is filled separately from the treatment outlet and dispensed independently.

Advantages:

- strongest contamination isolation;
- easiest traceback;
- one bad barrel does not contaminate others.

Disadvantages:

- more operator handling;
- less automatic level balancing.

### Mode CB-2 — valved common manifold

```text
[A]-V-\
[B]-V--+--> clean manifold
[C]-V--+
[D]-V-/
```

All branches remain individually valved.

Use only when operating discipline is strong enough that suspect vessels are isolated promptly.

For the current contested-zone prototype, **CB-1 is the preferred default for clean water**.

---

## 8. Preferred raw-bank strategy

Raw water can tolerate more hydraulic sharing than treated water, but source provenance still matters.

Preferred default:

```text
same-source barrels may share manifold
mixed-source barrels stay isolated
```

Do not mix:

- direct rainwater;
- trucked/desalinated water;
- groundwater;
- surface water;
- floodwater;

without an explicit treatment/source-management decision.

---

## 9. Manifold diameter

The manifold should not be smaller than individual branch plumbing without reason.

For low-head gravity transfer, excessive restriction causes poor balancing and low flow.

Prototype concept:

```text
branch: 1/2-3/4 in nominal
manifold: 3/4-1 in nominal
```

Exact sizing depends on:

- target flow;
- head;
- hose length;
- filter resistance;
- number of simultaneous barrels.

These are starting dimensions, not code requirements.

---

## 10. Gravity-head envelope

The current barrel-bank architecture provides low pressure.

Approximate static pressure:

```text
0.3 m head ≈ 2.9 kPa ≈ 0.43 psi
0.5 m head ≈ 4.9 kPa ≈ 0.71 psi
1.0 m head ≈ 9.8 kPa ≈ 1.42 psi
```

Therefore:

- short runs are preferred;
- elbows/restrictions should be minimized;
- filter selection must match low-head operation;
- check valves with high cracking pressure may be unsuitable.

---

## 11. Backflow control

The safest backflow strategy in a low-resource gravity system is often **layout and isolation**, not reliance on spring check valves.

Preferred controls:

1. one-way process flow by elevation;
2. separate raw and clean banks;
3. individual branch valves;
4. no shared fill/dispense hose;
5. physical disconnection during cleaning;
6. air gap where appropriate and practical.

Check valves may be added only when their low-pressure behavior is characterized.

---

## 12. Air-gap preference

Where treated water is transferred into clean storage, an air gap is preferable to submerged hose ends or back-siphon-prone connections.

Concept:

```text
TREATMENT OUTLET
      ↓
    AIR GAP
      ↓
CLEAN STORAGE INLET
```

This helps prevent storage water from migrating backward into the treatment path.

---

## 13. Fill topology

### Raw bank

Preferred:

```text
collector / source
→ labeled inlet
→ selected raw barrel(s)
```

### Clean bank

Preferred:

```text
treatment outlet
→ air-gap fill
→ one selected clean barrel at a time
```

This strengthens batch traceability.

---

## 14. Batch identity

Each vessel should carry:

```text
BARREL ID
SOURCE
DATE FILLED
TREATMENT STATUS
LAST CLEANING
CURRENT CLASSIFICATION
```

If batch identity is unknown:

```text
STATUS = GRAY
```

until reassessed.

---

## 15. Contamination-response sequence

If a barrel is suspected contaminated:

1. close branch valve;
2. mark vessel RED or GRAY;
3. disconnect branch if feasible;
4. cap both manifold port and barrel outlet;
5. record whether common manifold was open at time of detection;
6. if clean bank was interconnected, treat connected barrels as potentially exposed;
7. inspect/clean/retest before reopening.

---

## 16. Dead-leg control

Unused manifold branches can trap stagnant water.

Therefore removed branches should be:

- capped at the manifold;
- drained when possible;
- kept short;
- included in cleaning/inspection.

Avoid long blind-ended hose sections.

---

## 17. Drain / cleanout

The lowest point of a common manifold should include a drain/cleanout where practical.

Concept:

```text
BARREL BRANCHES
      ↓
COMMON HEADER
      ↓
LOW-POINT DRAIN
```

The drain allows:

- flushing sediment;
- emptying stagnant water;
- cleaning after contamination;
- winterization where relevant.

---

## 18. Structural independence

The manifold should be independently supported.

Do not hang the manifold from barrel fittings.

Preferred:

```text
barrels on load-spreader deck
manifold clipped to separate frame / rail
flex branches between them
```

This preserves the barrel-bank settlement strategy defined in P8.3.

---

## 19. Overflow isolation

Each barrel should have its own overflow or a controlled shared overflow header that cannot backflow into another vessel.

Best low-risk concept:

```text
individual overflow
→ open discharge / air break
→ common drainage apron
```

rather than submerged interconnected overflows.

---

## 20. Cleaning state

Any barrel undergoing cleaning should be:

```text
VALVE CLOSED
BRANCH DISCONNECTED
OUTLET CAPPED
STATUS GRAY / RED
```

It should not remain hydraulically connected to a clean bank during cleaning.

---

## 21. Minimum prototype hardware per barrel

For each branch:

- 1 barrel outlet fitting;
- 1 full-port isolation valve where available;
- 1 short flexible hose;
- 1 removable coupling/union;
- 1 barrel ID/status tag;
- 1 cap/plug for disconnected state.

For common manifold:

- header pipe/hose;
- supported mounting rail;
- capped spare ports if used;
- low-point drain;
- clearly marked RAW or CLEAN identity.

---

## 22. Bench test sequence

### M1 — leak test

Fill one barrel and inspect branch/manifold joints.

### M2 — one-barrel isolation

Operate with A/B/C open, D closed.

Confirm D remains hydraulically isolated.

### M3 — branch removal

Close B, disconnect it, cap manifold port.

Confirm remaining branches continue operating.

### M4 — settlement simulation

Introduce small controlled height difference under one barrel.

Confirm flexible branch absorbs motion without loading fitting/manifold.

### M5 — contamination simulation

Use harmless tracer/dye in one raw test barrel.

With valve closed, verify no tracer enters adjacent isolated barrels.

Do not use hazardous chemicals for this test.

### M6 — manifold cleaning

Drain, flush, and reopen system using defined procedure.

### M7 — clean-bank batch test

Fill clean barrels one at a time and verify batch labels remain traceable.

---

## 23. Acceptance gates

P2.2 bench gate passes when:

```text
[ ] each barrel isolates independently
[ ] one branch can be removed without draining the whole bank
[ ] manifold is independently supported
[ ] flexible branches absorb minor settlement
[ ] raw and clean components are visually distinct
[ ] clean bank can operate in isolated-vessel mode
[ ] disconnected ports can be capped
[ ] low-point drain works
[ ] no long stagnant dead legs remain
[ ] batch identity is preserved
```

---

## 24. Design freeze

For the current prototype, freeze:

```text
1. RAW and CLEAN use separate manifolds.
2. CLEAN defaults to isolated-vessel batch storage.
3. Every barrel gets its own valve + flexible branch + removable coupling.
4. The manifold is structurally independent of barrel fittings.
5. New/unknown barrels enter CLOSED / GRAY.
6. Removed branches are capped at both ends.
7. Low-point manifold drainage is required.
8. Treated-water filling prefers an air gap.
9. Mixed source waters are not automatically manifolded together.
10. One barrel can be removed without disabling the remaining bank.
```

---

## 25. Next pass

Proceed to the **actual BOM and lifecycle-cost model** for the integrated household module, separating:

```text
local/salvaged mass
controlled imported materials
health-critical treatment component
consumables
labor
replacement intervals
cost per litre/year
```

This will close the next major UNICEF scorecard gap: measured affordability rather than assumed affordability.
