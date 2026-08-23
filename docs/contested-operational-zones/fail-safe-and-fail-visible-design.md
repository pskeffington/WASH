# Fail-Safe and Fail-Visible Design for Alternative Water Systems

## Purpose

This pass addresses the weakest UNICEF-aligned design criterion in the current contested-zone WASH architecture: **the system must not silently continue to present water as safe when critical treatment status is unknown or failed**.

The practical objective is not to make every improvised component automatically self-disabling. Instead, the system should combine:

```text
FAIL-VISIBLE DESIGN
+
SIMPLE PHYSICAL ISOLATION
+
STATUS LABELING
+
OUTLET LOCKOUT / CAPPING
+
DEFINED REINSPECTION AND RETEST GATES
```

The default rule is:

> unknown or failed status cannot remain visually equivalent to validated status.

This document applies to legitimate civilian WASH delivery and public-health protection.

---

## 1. Core state model

Every treated-water outlet should be in one of four visible states:

```text
GREEN  = validated for intended use
AMBER  = treatment required / restricted use
RED    = reject / do not dispense
GRAY   = status unknown / inspection overdue
```

Color alone is not sufficient. Each state should also have:

- plain-text wording;
- symbol or shape;
- date/status card;
- physical outlet condition where practical.

Recommended text:

```text
GREEN: APPROVED FOR STATED USE
AMBER: TREATMENT / RESTRICTION REQUIRED
RED: DO NOT USE
GRAY: STATUS UNKNOWN - DO NOT ASSUME SAFE
```

---

## 2. Physical state should match information state

A central design principle is:

```text
SAFE STATUS   -> outlet can operate
UNKNOWN       -> outlet capped / tagged / restricted
FAILED        -> outlet closed / isolated
```

Do not rely on a written log alone if the dispensing point still looks normal.

Preferred low-resource mechanisms:

- removable outlet cap;
- valve lock wire / tamper tie;
- red mechanical tag through valve handle;
- removable spigot handle;
- separate non-potable outlet;
- physical disconnection of clean-storage outlet;
- distinct raw and treated fittings.

---

## 3. Raw / treated incompatibility

Where feasible, raw and clean connections should not be easily interchangeable.

Examples:

- different hose diameters;
- different connector types;
- male/female orientation chosen to prevent accidental reversal;
- distinct valve handles;
- clearly separated fill ports;
- physical distance between raw and clean banks.

Design objective:

```text
RAW WATER CANNOT BE ACCIDENTALLY CONNECTED
TO THE CLEAN-WATER DISPENSING PATH
WITHOUT AN OBVIOUS ADAPTER OR DELIBERATE CHANGE.
```

---

## 4. Filter failure indicators

### 4.1 Sudden high flow

A cracked ceramic, broken seal, or membrane bypass can produce **more** flow rather than less.

Therefore abnormal high flow should be treated as a possible failure.

Record a commissioning baseline:

```text
Q_baseline = measured clean-water flow
```

Then define a field alert band.

Prototype research trigger:

```text
>25-50% unexpected increase from established baseline
```

should trigger inspection before drinking-water use continues.

This is not a universal product specification; exact thresholds should ultimately follow manufacturer or validation data.

### 4.2 Sudden low flow

Low flow more commonly indicates:

- clogging;
- fouling;
- blocked pretreatment;
- exhausted head.

This is operationally inconvenient but may be safer than silent bypass.

### 4.3 No baseline = unknown status

If no baseline exists after installation or maintenance:

```text
STATUS = GRAY
```

until recommissioned.

---

## 5. Filter integrity tag

Each health-critical element should carry a compact status tag:

```text
FILTER ID:
TYPE / MODEL:
INSTALL DATE:
BASELINE FLOW:
LAST CLEANING:
LAST INTEGRITY CHECK:
NEXT REVIEW:
STATUS:
```

If tag is missing or illegible:

```text
STATUS = UNKNOWN
```

until re-established.

---

## 6. Seal and tamper evidence

Critical joints should be inspectable.

Low-resource options:

- numbered cable tie;
- paint witness mark;
- breakable paper/plastic seal;
- wire seal;
- alignment mark across housing and cap.

If the witness mark is broken or alignment changes unexpectedly:

```text
DO NOT ASSUME FILTER INTEGRITY
```

Reinspect and recommission.

---

## 7. Outlet lockout states

### FL-0 — normal

```text
GREEN status card
outlet openable
current inspection date
```

### FL-1 — restricted

```text
AMBER tag
outlet available only for defined bounded use
```

### FL-2 — failed

```text
RED tag
valve closed
cap installed or handle removed
```

### FL-3 — unknown / overdue

```text
GRAY tag
same physical restriction as RED for drinking use
```

Unknown should never default to green.

---

## 8. First-flush failure logic

The rain collector should not silently feed raw storage if the first-flush system is known to be malfunctioning.

### FF-OK

- device reset;
- chamber clean;
- known flow path;
- storage inlet open.

### FF-FAIL

If:

- diverter jammed;
- float absent;
- chamber overflowing incorrectly;
- unknown valve state;
- first-flush branch blocked;

then:

```text
DIVERT COLLECTOR AWAY FROM POTABLE-RESEARCH STORAGE
```

until corrected.

This can be implemented with a manual swing hose or removable inlet coupling.

---

## 9. Storage fail-visible design

Treated storage should have visible integrity checks.

Record:

- lid sealed/closed;
- vent screen intact;
- spigot clean;
- no flood contact;
- no raw cross-connection;
- last cleaning date.

If any critical condition is unknown:

```text
CLEAN STORAGE STATUS -> GRAY
```

A treated-water filter does not preserve safe status if downstream storage is compromised.

---

## 10. Sampling-triggered lockout

The A-WSP should link field results to outlet status.

Examples:

### Positive microbial indicator after final treatment

```text
GREEN -> RED
```

Action:

- close/cap drinking outlet;
- identify whether failure occurred in treatment or storage;
- apply validated corrective action;
- retest before returning to green.

### Unexpected conductivity/TDS rise

```text
GREEN -> AMBER or RED depending source/use
```

because salinity or chemical source mixing may have occurred.

### Sudden turbidity increase

```text
GREEN -> AMBER
```

until source/filter/bypass is inspected.

---

## 11. Maintenance-induced downgrade

Any invasive maintenance should automatically downgrade status.

Examples:

- opening membrane housing;
- replacing ceramic element;
- disturbing biosand media;
- replacing outlet plumbing;
- cleaning clean-storage vessel;
- repairing liner near clean pathway.

Immediately after maintenance:

```text
STATUS = GRAY
```

Then complete recommissioning checks before upgrade.

---

## 12. Recommissioning sequence

After a RED or GRAY state:

1. identify failure/unknown condition;
2. correct it;
3. inspect system flow path;
4. flush where applicable;
5. measure flow against baseline;
6. verify turbidity/operational parameters;
7. complete microbial or chemistry verification as required by the A-WSP;
8. sign/date status card;
9. reopen drinking outlet only when evidence supports it.

---

## 13. Pictorial status system

For low-literacy or multilingual contexts, use both text and shape.

Suggested scheme:

```text
GREEN  = circle + check
AMBER  = triangle + exclamation
RED    = octagon / stop symbol
GRAY   = square + question mark
```

Avoid relying exclusively on English wording.

The exact symbols should be field-tested for comprehension.

---

## 14. Fail-visible architecture by component

| Component | Silent-failure risk | Fail-visible control |
|---|---|---|
| Collector liner | tear / contamination | visual inspection + status downgrade |
| First flush | bypass | manual diversion + visible valve position |
| Raw barrel | unknown source | source/date label + separate outlet |
| Settling/roughing | channeling | turbidity/flow trend |
| Ceramic | crack | baseline flow + visual inspection + seal mark |
| UF/membrane | bypass/damage | flow baseline + integrity method + sealed housing |
| Disinfection | dose/process failure | residual/device check + status gate |
| Clean storage | recontamination | lid/vent/outlet inspection + post-storage test |
| Barrel stand | settlement | level marks + visual lean check |

---

## 15. Preferred humanitarian hardware

The fail-visible system should minimize specialized parts.

Potential kit:

- colored reusable status tags;
- weatherproof marker;
- numbered cable ties;
- outlet caps;
- spare valve handles;
- simple flow-measure vessel;
- stopwatch;
- turbidity tube;
- status card sleeve;
- laminated pictorial SOP.

This kit is intentionally much smaller and lighter than the water system itself.

---

## 16. Field status card

```text
SYSTEM ID: __________
DATE: _______________

STATUS:
[ ] GREEN - approved for stated use
[ ] AMBER - restricted / treatment required
[ ] RED - do not use
[ ] GRAY - status unknown

LAST INSPECTION: __________
LAST FILTER CHECK: ________
LAST MICROBIAL CHECK: _____
LAST CHEMISTRY CHECK: _____

AUTHORIZED BY: ____________

NEXT REVIEW: ______________
```

The card should be attached physically at the dispensing point.

---

## 17. Fail-safe hierarchy

Where possible, preference order is:

### Level 1 — physical automatic fail-safe

Example:

- element stops producing water at end of life;
- device automatically closes on loss of treatment integrity.

Best but not always available.

### Level 2 — mechanical interlock

Example:

- outlet remains capped until verification tag is applied;
- removable handle controlled by operator.

### Level 3 — fail-visible status

Example:

- conspicuous RED/GRAY state with defined restriction.

### Level 4 — documentation only

Logs without visible outlet control.

This is the weakest and should not be the sole protection.

---

## 18. UNICEF alignment

UNICEF's emergency HWTS design target emphasizes fail-safe behavior, including systems that do not continue dispensing apparently safe water after treatment capability is exhausted.

The WASH repo cannot assume every passive humanitarian component can achieve a fully automatic end-of-life shutoff.

Therefore the project adopts a layered approximation:

```text
AUTOMATIC FAIL-SAFE WHERE AVAILABLE
+
MECHANICAL LOCKOUT WHERE PRACTICAL
+
FAIL-VISIBLE STATUS EVERYWHERE
+
RECOMMISSIONING BEFORE UPGRADE
```

---

## 19. Bench-test requirements

Before integrated household-module trials, test the fail-visible architecture deliberately.

Simulate:

1. cracked/bypassed filter;
2. abnormally high flow;
3. clogged filter;
4. missing status tag;
5. failed first flush;
6. raw/clean connection attempt;
7. contaminated clean-storage outlet;
8. overdue inspection;
9. post-maintenance unknown state.

Success criterion:

> an unfamiliar operator following the field card should not continue to dispense the system as validated drinking water after a simulated critical failure.

---

## 20. Current design freeze

For the integrated prototype, freeze the following principles now:

```text
1. NO STATUS CARD = NOT GREEN
2. FILTER MAINTENANCE = AUTOMATIC GRAY
3. POSITIVE FINAL MICROBIAL TEST = RED
4. CRITICAL STRUCTURAL/WATER-CONTACT FAILURE = RED
5. UNKNOWN SOURCE OR BARREL HISTORY = NOT GREEN
6. RAW AND CLEAN OUTLETS PHYSICALLY DISTINCT
7. DRINKING OUTLET MUST BE CAPABLE OF PHYSICAL LOCKOUT
8. RETURN TO GREEN REQUIRES DOCUMENTED RECOMMISSIONING
```

---

## 21. Next pass

Proceed to **first-flush hydraulic correction and freeze** or, if keeping the UNICEF priority sequence, create the **pictorial/intuitive operating SOP and usability-test protocol**.

The latter directly addresses the next major UNICEF scorecard gap: intuitive operation under emergency conditions.
