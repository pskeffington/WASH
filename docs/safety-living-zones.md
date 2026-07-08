# Safety and Living-Zone Mapping Framework

## Purpose

This framework adds a safety-first residential siting layer to the WASH corridor project. The goal is to identify the safest practical living bases first, then define WASH work zones and field circuits that can be reached from those bases with reasonable safety, communications, and logistics support.

## Core rule

Living zones are selected before work zones.

A WASH field program should not be based from the most technically interesting site if the daily living environment, internet access, transport, medical access, or personal-security context is weak. The residential base should provide stability, communications, recovery capacity, and trusted local support.

## Residential safety indicators

### Crime and public-safety exposure

Collect only public, non-sensitive, and source-documented indicators:

- Reported theft, robbery, assault, or vehicle-break-in concentration areas.
- Market, bus terminal, nightlife, and high-congestion zones with higher pickpocket or petty-theft exposure.
- Demonstration, roadblock, or protest-prone corridors.
- Poorly lit streets, isolated pedestrian routes, and weak night transport areas.
- Known taxi or transport-risk areas.
- Police-station proximity and response-access context.

Do not publish informal accusations, rumor-based labels, or neighborhood claims without sourcing and review.

### Practical living safety

- Secure apartment availability.
- Controlled building access.
- Walkability in daytime.
- Avoidance of long isolated walks at night.
- Reliable taxi or app-based transport availability.
- Proximity to clinics, pharmacies, grocery, banks, and cafés.
- Stable internet/fiber availability.
- Local contacts, parish/community support, university, NGO, or professional networks.

### Health and continuity

- Distance to private clinic or hospital.
- Pharmacy access.
- Food and water availability.
- Backup power/internet options.
- Altitude tolerance and air-quality concerns.
- Airport or intercity transport access.

## Preliminary candidate living zones

These are planning candidates only, pending local verification and current crime/safety review.

### Cochabamba priority base areas

1. Recoleta
   - Strong candidate for expat-style residential base.
   - Good access to restaurants, cafés, services, and central activity.
   - Requires review for nightlife-adjacent petty theft and night-walking exposure.

2. Cala Cala
   - Strong residential candidate.
   - Likely better for quieter secure housing and longer-term stability.
   - Requires building-level internet and security verification.

3. Queru Queru
   - Residential candidate with calmer profile.
   - Useful if close to services and reliable transport.

4. Tupuraya
   - Practical residential candidate near universities and clinics.
   - Requires street-by-street review for traffic, noise, and night-walking conditions.

5. Tiquipaya
   - Semi-rural/green edge candidate.
   - Useful for watershed and rural WASH proximity.
   - Requires careful review of transport reliability, night travel, internet, and emergency access.

### Sucre secondary base areas

1. Centro Historico
   - Good short-term landing zone due to walkability, services, and lodging.
   - Requires petty-theft, night-walking, and tourist-zone exposure review.

2. La Recoleta
   - Residential/scenic candidate.
   - Requires slope, transport, and night-access review.

3. Avenida de las Americas / Zona Norte side
   - Longer-stay candidate if secure housing and internet are verified.
   - Useful for avoiding some tourist-center congestion.

4. Yotala and nearby outskirts
   - Field-adjacent candidate, not a first landing base.
   - Only viable with trusted local contacts, secure housing, and reliable transport.

## Living-zone scoring model

Use a 0-3 score where higher means better suitability.

### Safety score

- 0: Avoid as base; high or poorly understood safety risk.
- 1: Usable only with strong local support and limited movement.
- 2: Generally suitable with routine precautions and verified housing.
- 3: Preferred base; lower exposure, reliable transport, services, and secure housing options.

### Internet and work-continuity score

- 0: unreliable or unknown.
- 1: usable only with backup cellular/hotspot.
- 2: stable enough if apartment fiber is verified.
- 3: strong fiber/coworking/café redundancy.

### Medical and services score

- 0: weak access.
- 1: basic access.
- 2: good access to clinic, pharmacy, grocery, and transport.
- 3: strong access plus redundant options.

### Field-access score

- 0: weak staging point for WASH corridor work.
- 1: usable for occasional field trips.
- 2: good staging point for defined day circuits.
- 3: strong base for repeated fieldwork and return-to-base routing.

### Support-network score

- 0: no known local support.
- 1: limited contacts.
- 2: likely institutional/community support nearby.
- 3: verified NGO, parish, university, professional, or community contacts.

## Priority classification

Total score: 0-15

- 0-5: not recommended as a base.
- 6-9: possible short-term base with caution.
- 10-12: suitable base after verification.
- 13-15: preferred base.

## Field-safety rule for work zones

Work zones should be built as day circuits from a safe base whenever possible.

Each work zone should have:

- Known departure and return route.
- Daylight-only field plan where appropriate.
- Communications check.
- Nearest clinic/hospital noted.
- Nearest police/municipal contact if relevant.
- Weather, roadblock, and road-condition check.
- Local partner or community contact before arrival.

## Mapping outputs

- `living_zones` layer: candidate residential zones, generalized polygons.
- `safety_indicators_public` layer: aggregated and source-documented public safety indicators.
- `avoid_or_limit_zones` layer: generalized areas requiring caution; no rumor-based labeling.
- `field_circuits` layer: day-trip work circuits from safe bases.
- `work_zones` layer: WASH assessment zones, scored separately from living zones.

## Verification needs

Before ranking final residential zones, collect:

- Current local safety guidance from residents, NGOs, hotels, parishes, universities, and expat groups.
- Public travel advisories and embassy guidance.
- Current local news on demonstrations, roadblocks, and transport risk.
- Building-level security checks.
- Internet speed tests before signing housing.
- Day and night route checks with local guidance.
