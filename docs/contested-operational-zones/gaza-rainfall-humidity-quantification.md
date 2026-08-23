# Gaza Rainfall and Humidity Quantification for Contested-Zone WASH

## Scope

This note quantifies the best available rainfall and humidity envelope for the Gaza Strip to support rainwater, dew, fog, and passive-condensation architecture. It uses Palestinian official statistics, Palestinian Water Authority-derived meteorological data, long-period peer-reviewed rainfall studies, and NASA/ERA5-style climatology as supporting context.

The strongest conclusion is that Gaza combines:

- a pronounced north-to-south rainfall gradient;
- a highly seasonal Mediterranean rainfall regime;
- moderate to high coastal relative humidity through much of the year;
- substantial interannual rainfall variability;
- summer humidity that can remain high even when rainfall approaches zero.

This makes rain harvesting a winter-season volume source and atmospheric condensation a separate warm-season resilience lane.

---

## 1. Long-term rainfall gradient

Peer-reviewed long-period analysis describes annual rainfall decreasing from roughly 450 mm in northern Gaza to about 200 mm in the south over only about 45 km. A Gaza-site average near 370 mm/year is reported for a 1973-2006 rainfall record.

A more recent 1974-2021 multi-station Gaza analysis similarly confirms a strong north-south rainfall gradient and substantial year-to-year variability.

A Palestinian Water Authority-based 2013 spatial analysis found:

- north: about 353 mm/year;
- south: about 193 mm/year;
- Gaza Strip mean: about 268 mm/year.

The design envelope should therefore not use one Gaza-wide annual rainfall value.

### Practical planning bands

```text
North Gaza:        ~350-450+ mm/year long-term planning range
Gaza City zone:    ~330-400 mm/year
Deir al-Balah:     ~280-330 mm/year
Khan Yunis:        ~230-280 mm/year
Rafah / far south: ~190-240 mm/year
```

These are planning bands, not annual guarantees.

---

## 2. Official station variability

Palestinian Central Bureau of Statistics data sourced from the Meteorological General Directorate show large interannual variation.

Selected annual rainfall totals (mm):

| Station | 2013 | 2015 | 2017 | 2019 | 2021 |
|---|---:|---:|---:|---:|---:|
| North Gaza | 544.0 | 594.5 | 256.4 | 398.5 | 266.4 |
| Gaza | 527.0 | 475.2 | 187.0 | 362.0 | 277.3 |
| Deir al-Balah | 353.5 | 514.0 | 240.2 | 217.5 | 210.5 |
| Khan Yunis | 367.0 | 485.0 | 165.0 | 129.2 | 142.5 |
| Rafah | 366.0 | 344.5 | 140.0 | 115.8 | 143.5 |

Simple five-observation means from those selected years are approximately:

```text
North Gaza       412 mm/year
Gaza             366 mm/year
Deir al-Balah    307 mm/year
Khan Yunis       258 mm/year
Rafah            222 mm/year
```

These are not formal climate normals because the years are non-consecutive and selectively reported. They are useful as a consistency check against the long-established north-south gradient.

---

## 3. Rainfall seasonality

The rainy season is concentrated from approximately October through March/April.

Historical Gaza-station data for 2000-2007 provide the following average monthly rainfall pattern:

| Month | Rainfall mm |
|---|---:|
| Jan | 94.3 |
| Feb | 78.9 |
| Mar | 35.7 |
| Apr | 10.6 |
| May | 0.1 |
| Jun | 0 |
| Jul | 0 |
| Aug | 0 |
| Sep | 13.2 |
| Oct | 42.6 |
| Nov | 68.5 |
| Dec | 114.4 |

Total of these monthly averages is approximately 458 mm/year for that limited station/time window.

The most important design implication is not the exact total but the shape:

```text
Dec-Jan-Feb = dominant collection season
Oct-Nov-Mar = secondary collection season
Apr = marginal
May-Aug = near-zero rainfall
Sep = highly variable shoulder month
```

A rainwater system in Gaza must therefore store winter event water if it is expected to bridge dry periods.

---

## 4. Relative humidity

Palestinian Water Authority-derived 2013 monthly meteorological data for Gaza show persistently moderate-to-high relative humidity:

| Month | Mean RH % |
|---|---:|
| Jan | 64.2 |
| Feb | 66.4 |
| Mar | 68.1 |
| Apr | 67.1 |
| May | 72.3 |
| Jun | 77.5 |
| Jul | 74.7 |
| Aug | 72.2 |
| Sep | 68.1 |
| Oct | 67.3 |
| Nov | 65.1 |
| Dec | 62.6 |

Simple annual mean:

```text
~68.8% RH
```

An older Palestine environmental assessment based on Meteorological Office data reported a Gaza annual mean relative humidity near 65%, with monthly values around 59-73%.

Modern model/reanalysis climatologies for central Gaza commonly place annual mean RH around roughly 65-71%, depending on location, period, and method.

### Operational envelope

A defensible planning range is therefore:

```text
Typical annual mean RH: ~65-70%
Common monthly means:   ~60-78%
Short-term conditions:  can fall near ~30% or rise toward ~90%
```

The coastal Mediterranean influence keeps summer humidity comparatively high even when rainfall is nearly absent.

---

## 5. Temperature and approximate dew-point envelope

Using the same PWA-derived 2013 mean monthly temperature and RH data, approximate mean-month dew points are:

| Month | Mean T °C | Mean RH % | Approx dew point °C |
|---|---:|---:|---:|
| Jan | 13.1 | 64.2 | 6.5 |
| Feb | 13.4 | 66.4 | 7.3 |
| Mar | 17.8 | 68.1 | 11.8 |
| Apr | 19.3 | 67.1 | 13.0 |
| May | 24.1 | 72.3 | 18.8 |
| Jun | 25.4 | 77.5 | 21.2 |
| Jul | 26.5 | 74.7 | 21.6 |
| Aug | 27.2 | 72.2 | 21.8 |
| Sep | 25.6 | 68.1 | 19.3 |
| Oct | 21.3 | 67.3 | 15.0 |
| Nov | 19.6 | 65.1 | 12.9 |
| Dec | 13.5 | 62.6 | 6.5 |

These dew points are calculated from monthly mean temperature/RH and should not be treated as hourly observations.

### Condensation implication

Summer is especially interesting:

```text
June-August mean dew point ~21-22 °C
```

Therefore a condenser surface maintained materially below about 21 °C during humid summer conditions could produce condensate even when rainfall is essentially zero.

This does not establish economic feasibility, because heat rejection, airflow, surface temperature, and recovery efficiency remain limiting factors.

---

## 6. Rain collection yield by zone

For a 4 ft x 4 ft pallet collector:

```text
area = 16 ft2
1 inch rainfall theoretical capture ≈ 10 gallons
at 80% recovery ≈ 8 gallons ≈ 30 litres
```

Using the selected-year station means above as illustrative rainfall depths, one pallet would collect approximately:

| Zone | Illustrative annual rainfall | Approx annual capture per pallet at 80% recovery |
|---|---:|---:|
| North Gaza | 412 mm | 129 gal / 490 L |
| Gaza | 366 mm | 115 gal / 435 L |
| Deir al-Balah | 307 mm | 96 gal / 365 L |
| Khan Yunis | 258 mm | 81 gal / 306 L |
| Rafah | 222 mm | 70 gal / 264 L |

These values assume all annual rainfall is intercepted by an unobstructed 16 ft2 surface and 80% of theoretical runoff is recovered. Real contested-zone yield may be lower because of wind, damaged collection surfaces, first-flush loss, overflow, contamination rejection, maintenance, and incomplete deployment during storms.

### Four-pallet module

A 64 ft2 four-pallet array would scale approximately to:

```text
North Gaza:       ~1,960 L/year
Gaza:             ~1,740 L/year
Deir al-Balah:    ~1,460 L/year
Khan Yunis:       ~1,220 L/year
Rafah:            ~1,060 L/year
```

This is seasonal production rather than smooth daily supply.

---

## 7. Survival-water interpretation

Rain capture should not be divided by 365 and treated as a dependable daily source because most production occurs during a few winter months.

The better contested-zone metric is:

```text
litres captured per storm
+ storage capacity
+ days of minimum-use demand buffered
```

Example:

One pallet receiving 25 mm (~1 inch) rainfall can yield about 30 L at 80% recovery.

A four-pallet array can yield about 120 L from the same event.

At a nominal emergency drinking/cooking allocation of 6 L/person/day, 120 L represents:

```text
20 person-days
```

before treatment loss and assuming the water is suitable for that use.

This illustrates why small catchments can have survival value even though they cannot meet total WASH demand year-round.

---

## 8. Humidity versus rainfall architecture

Gaza has an unusual resilience opportunity because the seasonal signals are partly complementary:

```text
WINTER:
high rainfall
moderate-high humidity
→ prioritize rain capture and storage

SUMMER:
near-zero rainfall
high humidity
high dew point
→ investigate dew/condensation systems
```

This suggests a hybrid seasonal architecture:

```text
RAIN MODULE
      +
CONDENSATION / DEW MODULE
      ↓
SEPARATE MEASUREMENT
      ↓
CONTROLLED STORAGE
```

Rain should remain the expected high-volume source when storms occur. Condensation should be investigated as a dry-season supplemental source.

---

## 9. Spatial deployment implications

### North Gaza / Gaza City

- strongest rainfall opportunity;
- dense urban contamination risk likely high;
- winter catchment plus large storage has the strongest volume case.

### Deir al-Balah

- intermediate rainfall;
- rain still meaningful;
- humidity remains favorable for atmospheric-collection research.

### Khan Yunis / Rafah

- lower annual rainfall;
- storage per unit catchment area remains useful but produces less annually;
- atmospheric humidity may become relatively more important as a supplemental research lane.

---

## 10. Data-quality hierarchy

### Highest-confidence sources used

1. Palestinian Central Bureau of Statistics, with rainfall data sourced from the Meteorological General Directorate.
2. Palestinian Water Authority-derived meteorological station datasets used in published Gaza water-balance research.
3. Peer-reviewed long-period rainfall studies using Gaza meteorological stations.

### Secondary support

- NASA POWER / reanalysis-based humidity climatology;
- ERA5-derived long-term climate summaries;
- broader Palestinian environmental assessments.

### Main uncertainty

The current conflict has disrupted observation infrastructure and station continuity. Therefore the strongest design approach is to combine historical climatology with portable local sensors before deployment.

---

## 11. Field-data recommendation

Every contested-zone pilot should carry its own microclimate record:

```text
rain gauge
air temperature
relative humidity
dew point
wind speed/direction
collector surface temperature
```

Log at 5-15 minute intervals where possible.

A local sensor package can determine whether a site follows the regional climatology or is materially altered by coastal exposure, urban heat, shelter, dust, smoke, or damaged built environment.

---

## 12. Design conclusions

1. Annual rainfall declines roughly by half from northern Gaza to Rafah.
2. Rainfall is extremely seasonal, with the practical dry season extending through much of May-September.
3. Relative humidity remains moderate to high year-round and can peak during the dry summer season.
4. Summer mean dew points around 21-22 °C make passive/ground-cooled condensation scientifically plausible if a sufficiently cold surface can be maintained.
5. Rain collection should be sized for storm events and storage, not averaged into a fictitious steady daily supply.
6. A 4x4-ft pallet can plausibly collect roughly 260-490 L/year across the Gaza north-south gradient under an illustrative 80% recovery assumption.
7. Four-pallet arrays can reach roughly 1.1-2.0 m3/year depending on location and year, concentrated in winter storms.
8. Local sensing is essential because rainfall variability and contested-zone microclimates can be substantial.

## Sources

- Palestinian Central Bureau of Statistics. *Palestine in Figures 2024* (published 2025), annual rainfall by station, source: Meteorological General Directorate.
- Palestinian Water Authority meteorological data as reported in *Estimation of Water Balance Components in the Gaza Strip with GIS Based WetSpass Model*.
- Mhanna et al., *Stochastic single-site generation of daily and monthly rainfall in the Middle East*, Meteorological Applications (2012).
- Long-period 1974-2021 multi-station rainfall analysis for the Gaza region.
- Palestinian environmental assessment data on relative humidity.
- NASA POWER climatology documentation and derived supporting climate summaries.

## Next pass

1. Build monthly pallet-array collection tables for North Gaza, Gaza City, Deir al-Balah, Khan Yunis, and Rafah.
2. Quantify storage required to capture 25 mm, 50 mm, and 100 mm storm events.
3. Model dew/condensate potential from summer humidity and dew-point conditions.
4. Compare rain-capture yield against emergency litres-per-person-per-day requirements.
5. Develop seasonal hybrid collection architecture for Gaza deployment.
