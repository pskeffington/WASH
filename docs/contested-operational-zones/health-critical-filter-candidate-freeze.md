# Health-Critical Filter Candidate Freeze

## Purpose

This pass narrows the health-critical treatment lane from broad technology classes to exact candidate products with current independent/WHO evidence.

The selection remains conditional on exact product identity, procurement availability, and field confirmation. A product name or manufacturer family must not be treated as interchangeable with the exact model evaluated by WHO.

---

## 1. Selection criteria

Primary criteria:

```text
WHO / independent microbial evidence
passive or near-passive operation
household-scale throughput
low logistics footprint
low recurring consumables
field maintainability
fail-visible behavior
safe-storage compatibility
```

Secondary criteria:

- current availability;
- exact model traceability;
- procurement cost;
- replacement support;
- Gaza / contested-logistics suitability.

Chemical limitation remains upstream: these filters are not assumed to solve salinity, nitrate, fuel, solvents, or other dissolved-chemical hazards.

---

# 2. Primary technical benchmark — LifeStraw Family 2.0

## Exact WHO-listed identity

```text
LifeStraw Family 2.0
Manufacturer listed by WHO: LifeStraw SA / Vestergaard Group
Technology: membrane filtration
WHO HWT Scheme: Round I
Classification: Comprehensive protection ★★
```

WHO currently lists LifeStraw Family 2.0 as a two-star product providing comprehensive protection against bacteria, viruses, and protozoa.

WHO's product report states that the product met or exceeded three-star targets for bacteria and protozoa, while virus performance met the two-star threshold, resulting in an overall two-star classification.

---

## Why it fits the WASH architecture

LifeStraw Family 2.0 is a strong fit because it is:

- gravity-fed;
- household-scale;
- membrane-based;
- designed with integrated dirty-water and safe-water storage;
- independently evaluated;
- capable of virus reduction as well as bacteria/protozoa control.

Published field and technical literature describe the Family 2.0 as a gravity-fed hollow-fiber ultrafiltration system with household-scale safe storage and long rated capacity.

---

## Throughput fit

The repo's target drinking/cooking treatment throughput is approximately:

```text
12.5 L/day benchmark
20-30 L/day preferred prototype capacity
```

Published Family 2.0 specifications substantially exceed the minimum daily throughput target under normal operation.

Therefore throughput is not the limiting design variable for this candidate.

---

## Passive-operation fit

This candidate matches the preferred architecture:

```text
RAW STORAGE
→ GRAVITY MEMBRANE
→ SAFE STORAGE
```

No grid electricity or powered pump is required for normal filtration.

This is materially better aligned with the project's passive lane than a hand-pumped or electrically pressurized purifier.

---

## Maintenance / fail-visible considerations

The system includes membrane-cleaning/backwash functions.

The integrated WASH prototype should still add project-level controls:

- commissioning flow baseline;
- abnormal high-flow alert;
- membrane/housing status tag;
- post-maintenance GRAY status;
- clean-storage inspection;
- outlet lockout after failed verification.

Do not assume the product itself satisfies the repo's entire fail-visible architecture.

---

## Procurement caveat

The current LifeStraw retail site lists a product called `LifeStraw Family`, but current retail availability is shown as sold out in the emergency/gravity catalog at the time of this review.

The repo must **not** assume that the current retail `LifeStraw Family` SKU is identical to the WHO-tested `LifeStraw Family 2.0` without exact manufacturer/model confirmation.

Therefore the freeze is:

```text
PRIMARY TECHNICAL BENCHMARK:
LifeStraw Family 2.0

PROCUREMENT STATUS:
CONDITIONAL / EXACT MODEL VERIFICATION REQUIRED
```

---

# 3. Secondary comprehensive-protection candidate — Grifaid Family Filter

## Exact WHO-listed identity

```text
Grifaid Family Filter
Manufacturer: The Safe Water Trust Ltd
Technology: membrane filtration
WHO HWT Scheme: Round IV
Classification: Comprehensive protection ★★
```

WHO currently lists the Grifaid Family Filter as a two-star comprehensive-protection product.

---

## Strengths

Current manufacturer and humanitarian references describe:

- household/small-group use;
- compact form factor;
- high throughput;
- long rated membrane life;
- built-in cleaning/backwashing;
- humanitarian deployment history;
- current filter availability through the organization/distributor.

The manufacturer states approximately 2 L/min maximum flow and a rated membrane capacity up to 200,000 L, dependent on maintenance and feed-water quality.

---

## Main limitation for this program

The current Grifaid Family Filter uses a manual pump.

That means it does **not** satisfy the strict passive-gravity preference of the integrated household module.

However, it remains highly relevant as:

```text
LOW-ENERGY MANUAL FALLBACK
```

where gravity head is unavailable or where a verified comprehensive-protection product is required and hand pumping is acceptable.

---

## Candidate status

```text
SECONDARY / FALLBACK:
Grifaid Family Filter

ROLE:
manual low-energy comprehensive-protection option
```

---

# 4. Passive alternative requiring larger head — Sydney 905 Purifier

## Exact WHO-listed identity

```text
Sydney 905 Purifier
Manufacturer: Sydney 905 Filters (Pty) Ltd
Technology: membrane filtration
WHO HWT Scheme: Round III
Classification: Comprehensive protection ★★
```

The product is currently listed by WHO as a two-star comprehensive-protection product.

---

## Strengths

Current manufacturer information describes:

- 0.01 micron hollow-fiber ultrafiltration;
- gravity capability;
- no routine cartridge replacement claim;
- international shipping;
- low purchase price relative to many complete purifier systems.

---

## Limitation

The manufacturer states the purifier has low flow under gravity and is ideally used with a relatively large head or pressurized system.

The current barrel architecture provides only about:

```text
0.3-1.0 m water head
```

Therefore the Sydney 905 Purifier is not frozen as the primary household candidate until low-head flow is directly measured.

Candidate status:

```text
PASSIVE ALTERNATE
LOW-HEAD VALIDATION REQUIRED
```

---

# 5. LifeStraw Family / Mission lineage — do not conflate products

LifeStraw currently markets gravity-fed `Family` and `Mission` products with virus-removal claims and approximately 18,000 L rated membrane capacity.

However:

```text
CURRENT COMMERCIAL PRODUCT NAME
≠ AUTOMATICALLY
WHO-TESTED FAMILY 2.0 IDENTITY
```

The WHO candidate freeze must remain tied to the exact evaluated model.

If a current product is proposed as a substitute, record:

- exact SKU/model;
- membrane part number;
- manufacturer declaration of equivalence;
- independent test basis;
- WHO listing if applicable.

---

# 6. Product comparison

| Criterion | LifeStraw Family 2.0 | Grifaid Family Filter | Sydney 905 Purifier |
|---|---|---|---|
| WHO comprehensive protection | ★★ | ★★ | ★★ |
| Gravity-only normal operation | Yes | No | Possible |
| Manual pumping | No | Yes | No if sufficient head |
| Household scale | Yes | Yes | Yes |
| Virus protection evidence | Yes | Yes | Yes |
| Low imported mass | Moderate | Strong | Strong |
| Integrated safe storage | Yes | No | No |
| Low-head fit | Strong conceptually | Not relevant | Unverified / likely limiting |
| Current exact procurement clarity | Uncertain | Better | Available internationally |
| Fit with passive design doctrine | Highest | Medium | Conditional |

---

# 7. Selection decision

## Primary candidate

```text
HC-P1
LifeStraw Family 2.0
```

Reason:

- exact WHO-evaluated household product;
- comprehensive two-star microbial protection;
- gravity-fed;
- integrated household form factor;
- strong fit with passive WASH architecture.

Status:

```text
TECHNICALLY FROZEN
PROCUREMENT NOT YET FROZEN
```

---

## Secondary candidate

```text
HC-P2
Grifaid Family Filter
```

Reason:

- current WHO two-star comprehensive protection;
- strong humanitarian use case;
- high throughput;
- current organizational procurement path.

Limitation:

```text
manual pumping required
```

---

## Passive alternative

```text
HC-P3
Sydney 905 Purifier
```

Reason:

- WHO two-star comprehensive protection;
- hollow-fiber UF;
- gravity-capable.

Limitation:

```text
low-head flow not yet demonstrated in the repo's 0.3-1.0 m head envelope
```

---

# 8. Bench integration for HC-P1

If an exact LifeStraw Family 2.0 is obtained, initial integration should preserve the manufacturer's treatment path rather than modifying the membrane housing.

Test interfaces around it:

```text
repo raw source / pretreatment
        ↓
manufacturer feed reservoir / inlet
        ↓
LifeStraw Family 2.0
        ↓
manufacturer safe-storage outlet
        ↓
repo sampling / status verification
```

Do not cut open, re-plumb, or alter the evaluated purifier before baseline testing.

---

# 9. Bench acceptance tests

For any candidate product:

```text
[ ] exact model identity confirmed
[ ] WHO / independent evidence captured
[ ] feed-water limits documented
[ ] baseline flow measured
[ ] 20-30 L/day target demonstrated
[ ] maintenance procedure completed
[ ] abnormal-flow detection tested
[ ] clean-storage pathway verified
[ ] post-maintenance GRAY logic tested
[ ] lifecycle cost recorded
[ ] source chemistry limitations documented
```

---

# 10. Chemical boundary

The candidate products are selected for microbial treatment performance.

They are **not assumed to remove**:

- seawater salinity;
- high chloride;
- nitrate;
- fuel;
- solvents;
- many dissolved metals;
- other source-specific chemical hazards.

For Gaza or other chemically compromised sources:

```text
SOURCE CHEMISTRY GATE
PRECEDES
MICROBIAL FILTER USE
```

---

# 11. Evidence summary

WHO's current evaluated-products list identifies LifeStraw Family 2.0, Grifaid Family Filter, and Sydney 905 Purifier as membrane products achieving two-star comprehensive protection under the WHO HWT Scheme.

UNICEF's household-filter guide notes that gravity membrane filters can provide strong microbial protection with low external-energy requirements, but also emphasizes product-specific evaluation, maintenance, leakage risk, safe-storage limitations, and lack of universal fail-safe mechanisms.

Current manufacturer information supports continued availability or support for some candidate lineages, but procurement status must be checked at the exact-model level before field planning.

---

# 12. Design freeze

The project now freezes:

```text
PRIMARY TECHNICAL BENCHMARK:
LifeStraw Family 2.0

SECONDARY MANUAL FALLBACK:
Grifaid Family Filter

PASSIVE LOW-HEAD RESEARCH ALTERNATE:
Sydney 905 Purifier
```

No substitution is allowed solely on brand similarity.

---

# 13. Next pass

Proceed to the **integrated household bench architecture** using HC-P1 as the reference health-critical treatment block while keeping the membrane device itself unmodified.

The bench should integrate:

- four-panel catchment;
- FF-M1 or FF-F1;
- isolated raw storage;
- passive pretreatment;
- HC-P1 treatment block;
- clean storage/status control;
- sampling ports;
- durability and usability instrumentation.
