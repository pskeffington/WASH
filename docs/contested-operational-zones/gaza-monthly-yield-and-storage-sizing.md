# Gaza Monthly Rain Yield and Storage Sizing

## Purpose

This note converts the Gaza rainfall envelope into operational sizing for modular rainwater collection. It estimates monthly yield for a four-pallet array, storage needs for representative storm depths, and person-day equivalents for emergency water planning.

The model is intentionally conservative in interpretation: rainfall is highly variable, monthly values are scenario-based, and collected water is not assumed potable without treatment and validation.

## 1. Model assumptions

### Collector geometry

One pallet module:

```text
4 ft x 4 ft = 16 ft2 = ~1.49 m2
```

Four-pallet array:

```text
64 ft2 = ~5.95 m2
```

### Recovery efficiency

Illustrative recovery efficiency:

```text
80%
```

This accounts broadly for first-flush loss, splash, incomplete drainage, and other collection losses. Field efficiency must be measured.

### Rainfall-to-volume equation

```text
V(L) = rainfall(mm) x area(m2) x recovery efficiency
```

For one pallet:

```text
~1.19 L per mm rainfall
```

For four pallets:

```text
~4.76 L per mm rainfall
```

## 2. Representative annual rainfall used

The following values are scenario anchors derived from the Gaza rainfall quantification pass and are consistent with the established north-south gradient:

| Zone | Representative annual rainfall |
|---|---:|
| North Gaza | 412 mm |
| Gaza City | 366 mm |
| Deir al-Balah | 307 mm |
| Khan Yunis | 258 mm |
| Rafah | 222 mm |

These are not formal climate normals and should not be interpreted as annual guarantees.

## 3. Monthly distribution model

Because complete long-term monthly station tables for every Gaza location are not consistently available in a single harmonized source, this pass uses the historical Gaza City seasonal rainfall shape as a **distribution template** and scales it to each representative annual total.

Template monthly rainfall pattern:

```text
Jan  20.6%
Feb  17.2%
Mar   7.8%
Apr   2.3%
May  ~0%
Jun   0%
Jul   0%
Aug   0%
Sep   2.9%
Oct   9.3%
Nov  14.9%
Dec  25.0%
```

This is a modeled seasonal allocation, not a claim that every governorate receives those exact fractions.

## 4. Four-pallet modeled monthly yield

Approximate litres collected per month at 80% recovery:

| Month | North Gaza | Gaza City | Deir al-Balah | Khan Yunis | Rafah |
|---|---:|---:|---:|---:|---:|
| Jan | 403 | 358 | 300 | 253 | 217 |
| Feb | 337 | 300 | 251 | 211 | 182 |
| Mar | 153 | 136 | 114 | 96 | 82 |
| Apr | 45 | 40 | 34 | 28 | 24 |
| May | ~0 | ~0 | ~0 | ~0 | ~0 |
| Jun | 0 | 0 | 0 | 0 | 0 |
| Jul | 0 | 0 | 0 | 0 | 0 |
| Aug | 0 | 0 | 0 | 0 | 0 |
| Sep | 56 | 50 | 42 | 35 | 30 |
| Oct | 182 | 162 | 136 | 114 | 98 |
| Nov | 293 | 260 | 218 | 183 | 158 |
| Dec | 489 | 435 | 365 | 306 | 264 |
| **Annual** | **~1,960** | **~1,741** | **~1,460** | **~1,227** | **~1,056** |

The major operational feature is obvious: most useful production is concentrated in December through February.

## 5. Storm-event storage sizing

Storage should be designed around storm depth rather than average monthly rainfall.

### One pallet

At 80% recovery:

| Storm depth | Approx capture |
|---|---:|
| 10 mm | 11.9 L |
| 25 mm | 29.7 L |
| 50 mm | 59.5 L |
| 100 mm | 118.9 L |

### Four pallets

| Storm depth | Approx capture |
|---|---:|
| 10 mm | 47.6 L |
| 25 mm | 118.9 L |
| 50 mm | 237.8 L |
| 100 mm | 475.7 L |

This leads to practical storage tiers:

```text
~120 L vessel  -> captures about 25 mm from four pallets
~240 L vessel  -> captures about 50 mm
~500 L vessel  -> captures about 100 mm
```

A 55-gallon drum (~208 L) can therefore capture most of a roughly 40-45 mm event from a four-pallet array before overflow, assuming the barrel starts empty and actual recovery is near 80%.

## 6. Person-day equivalents

WHO emergency guidance distinguishes immediate survival quantities from more adequate emergency service levels. WHO notes that around 7.5 L/person/day can meet basic survival drinking/cooking requirements under many conditions, while 15 L/person/day should be provided as soon as possible for broader emergency needs. These values are planning benchmarks, not rigid individual physiological prescriptions. 

### Four-pallet storm yield

| Storm | Captured volume | Person-days at 7.5 L/day | Person-days at 15 L/day |
|---|---:|---:|---:|
| 25 mm | 119 L | 15.9 | 7.9 |
| 50 mm | 238 L | 31.7 | 15.9 |
| 100 mm | 476 L | 63.4 | 31.7 |

Example for a household of five:

```text
25 mm storm -> ~119 L
```

At 7.5 L/person/day:

```text
5-person household demand = 37.5 L/day
119 L / 37.5 ≈ 3.2 household-days
```

At 15 L/person/day:

```text
5-person household demand = 75 L/day
119 L / 75 ≈ 1.6 household-days
```

These calculations assume all collected water is suitable for the intended use after treatment and do not subtract treatment losses.

## 7. Annual person-day equivalents

The annual totals are useful only as an upper-level productivity measure because production is seasonal.

For a four-pallet array:

| Zone | Annual modeled capture | Person-days at 7.5 L | Person-days at 15 L |
|---|---:|---:|---:|
| North Gaza | 1,960 L | 261 | 131 |
| Gaza City | 1,741 L | 232 | 116 |
| Deir al-Balah | 1,460 L | 195 | 97 |
| Khan Yunis | 1,227 L | 164 | 82 |
| Rafah | 1,056 L | 141 | 70 |

Again, these values do not imply continuous daily availability.

## 8. Recommended storage architectures

### P1 — minimal household module

```text
1-2 pallets
+ 55-gal / ~200-L barrel
```

Purpose:

- proof of collection;
- small household reserve;
- hygiene/non-potable use initially;
- treatment research.

### P2 — four-pallet household module

```text
4 pallets
+ 250-500 L storage
```

Purpose:

- capture common moderate-to-heavy winter events without immediate overflow;
- support multiple days of household emergency water after treatment.

### P3 — distributed community module

```text
8-16 pallets
+ 1,000-2,000 L storage bank
```

Purpose:

- shared collection node;
- modular repair;
- multiple barrels/cisterns rather than one single-point-failure tank.

## 9. Why multiple containers are preferable

In contested environments, four 200-L barrels can be more resilient than one 800-L vessel because:

- one contaminated vessel can be isolated;
- one damaged vessel does not eliminate all storage;
- containers can be moved independently;
- different source waters can remain segregated;
- repairs are simpler;
- distribution can be decentralized.

Preferred architecture:

```text
COLLECTOR ARRAY
     ↓
first flush
     ↓
source manifold
     ↓
BARREL A
BARREL B
BARREL C
BARREL D
```

with controlled overflow sequencing where materials allow.

## 10. Overflow sequencing

A simple gravity cascade can preserve storage when multiple barrels are available:

```text
collector
   ↓
barrel 1
   ↓ overflow
barrel 2
   ↓ overflow
barrel 3
   ↓ overflow
safe drainage
```

However, barrels should not be hydraulically joined in a way that prevents isolation if contamination is detected.

Valved or removable interconnections are preferable to permanent common-bottom connections in research/deployment settings.

## 11. First-flush impact on storage sizing

First-flush diversion slightly reduces captured volume but can materially improve raw-water quality.

For four pallets (~64 ft2), even a relatively generous 1-2 gallons of first-flush diversion represents only approximately 4-8 L per storm.

For a 25 mm event producing roughly 119 L gross recovered water, an 8-L first flush would leave approximately:

```text
~111 L
```

before other losses.

The first flush therefore remains worthwhile where contamination risk is significant.

## 12. Deployment implications by zone

### North Gaza / Gaza City

Recommended emphasis:

```text
larger winter storage per unit catchment
```

because rainfall yield is strongest.

### Deir al-Balah

Balanced architecture:

```text
moderate rain-storage capacity
+ summer humidity research
```

### Khan Yunis / Rafah

Because annual rainfall is lower:

```text
maximize capture efficiency
avoid unnecessary overflow
pair rain systems with alternative dry-season sources
```

Storage remains useful because storm events can still be intense even where annual totals are lower.

## 13. Design thresholds for the next prototype

For a four-pallet Gaza deployment, initial design targets should be:

```text
Catchment area:       ~5.95 m2
Recovery assumption:  0.8 for modeling only
Storage P1:           ~200-250 L
Storage P2:           ~500 L
First flush:          adjustable and measured
Overflow:             >= inlet hydraulic capacity
Sampling:             raw + post-treatment + post-storage
```

A 500-L storage target is particularly useful because it is large enough to retain approximately a 100-mm event from four pallets without major overflow under the model.

## 14. Evidence basis

Long-term peer-reviewed Gaza rainfall analysis reports annual rainfall declining from roughly 450 mm in the north to about 200 mm in the south, with most rain falling from mid-October through March. citeturn942587search3

A 1974-2021 eight-station study confirms the strong Gaza rainfall gradient and high month-to-month/year-to-year variability. citeturn942587search1

Official Palestinian meteorological statistics likewise show large annual variability and lower rainfall toward Khan Yunis and Rafah. citeturn942587search8

WHO emergency guidance states that approximately 7.5 L/person/day can meet immediate survival water requirements under many conditions, while a minimum of about 15 L/person/day should be provided as soon as possible in emergencies. citeturn942587search0turn942587search32

## 15. Next pass

1. Model summer atmospheric-condensation yield using Gaza temperature/RH/dew-point data.
2. Compare 1-, 4-, 8-, and 16-pallet systems against household and community demand.
3. Add storm-frequency/intensity data to improve overflow and gutter sizing.
4. Develop a barrel-bank manifold that preserves contamination isolation.
5. Build seasonal operating logic: winter rain capture versus summer condensation.
