# Topographic Viewpoint Analysis: Safe Living Zones and Airport Overlook Criteria

## Purpose

This document adds a topographic viewshed layer to the WASH Bolivia GIS system. The goal is to identify legal, safe, public-facing residential or observation areas with broad valley visibility, including places where aircraft can be seen from a distance during ordinary airport arrivals and departures.

This is not an aviation operations document. It should not be used for interference with airports, restricted areas, military facilities, flight operations, or airport perimeter activity.

## Core principle

Use terrain and lawful public access to select safe overlooks. Do not select airport-adjacent, restricted, isolated, or security-sensitive locations.

Preferred locations are elevated residential or public-view areas that also score well for safe living, secure housing, internet, medical access, and transport.

## Airport context for the corridor

### Cochabamba: Jorge Wilstermann International Airport

- Airport: Jorge Wilstermann International Airport.
- City served: Cochabamba.
- Airport elevation is approximately 8,360 ft.
- Publicly reported runway orientations include 14/32 and 04/22.
- GIS implication: because the airport sits within the Cochabamba basin, residential hill-edge or slope-zone views may provide broad views over the urban valley. Viewpoint selection should prioritize safe residential districts and avoid airport-perimeter proximity.

### Sucre: Alcantari International Airport

- Airport: Alcantari International Airport.
- City served: Sucre.
- Location: Yamparaez municipality, southeast of Sucre.
- Airport elevation is approximately 3,104 m / 10,184 ft.
- Publicly reported runway orientation is 18/36.
- GIS implication: Sucre viewing candidates should be assessed from elevated public/residential areas with long-distance visibility toward the airport plateau, while recognizing that Alcantari is outside Sucre proper and may require separate field verification.

## Topographic analysis method

### 1. Build base elevation model

Use a public DEM such as SRTM, NASADEM, or Copernicus DEM.

Required derived rasters:

- Elevation.
- Slope.
- Aspect.
- Terrain ruggedness.
- Hillshade.
- Viewshed raster from candidate observation points.

### 2. Define candidate viewpoint zones

A viewpoint candidate should be a generalized polygon or point cluster, not a private address.

Candidate types:

- Residential hill-edge zones.
- Public miradors or parks.
- University or institutional hilltop areas where publicly accessible.
- Secure apartment zones with valley views.
- Café/hotel terrace zones only where lawful and public.

Avoid:

- Airport perimeter roads.
- Restricted airport or military areas.
- Isolated night-access roads.
- Informal trespass routes.
- Locations requiring unsafe transport or unverified local access.

### 3. Viewshed criteria

For each candidate viewpoint, calculate:

- Elevation advantage over nearby valley floor.
- Line of sight toward airport area, generalized.
- Visible valley area.
- Slope and terrain accessibility.
- Road access and return-to-base feasibility.
- Daytime and nighttime safety context.
- Internet and living-zone suitability if residential.

### 4. Safety-first filtering

A topographic viewpoint should be discarded if it fails living-zone safety criteria.

Discard conditions:

- High or unverified crime exposure.
- Poor night transport or isolated access.
- No nearby clinic/pharmacy/service access.
- Weak communications or no verified internet.
- Unclear legal/public access.
- Any airport-security concern.

## Candidate analysis logic

### Cochabamba

Priority should be given to safe residential zones with valley visibility:

- Recoleta: potential café/residential overlook value; verify exact slope, night safety, and petty-theft exposure.
- Cala Cala: likely stronger long-term residential base; identify buildings or public streets with valley views.
- Queru Queru: assess quiet residential overlooks and secure housing.
- Tupuraya: evaluate university/clinic proximity plus slope visibility.
- Tiquipaya: possible semi-rural views and watershed access, but transport and nighttime return must be verified.

### Sucre

Priority should be given to safe residential and public viewpoint areas:

- La Recoleta: potential scenic overlook candidate; verify safety, slope, transport, and actual line of sight toward airport approaches.
- Centro Historico upper edges: possible short-term base with visibility, but tourist/petty-theft exposure must be reviewed.
- Zona Norte / Avenida de las Americas side: evaluate longer-stay residential suitability and sightlines.
- Yotala/outskirts: do not use as first base unless local support, transport, internet, and safety are verified.

## Scoring model

Use a 0-3 score where higher is better unless marked as risk.

### Elevation and view score

- 0: no useful line of sight or blocked by terrain/buildings.
- 1: partial valley visibility.
- 2: good generalized airport-valley visibility.
- 3: strong broad valley visibility from safe public/residential area.

### Access safety score

- 0: unsafe, restricted, isolated, or unverified.
- 1: usable only with local support.
- 2: generally usable during daytime.
- 3: safe public/residential access with reliable transport.

### Living suitability score

- 0: not suitable as living base.
- 1: short-term only.
- 2: suitable after housing/internet verification.
- 3: preferred residential base candidate.

### Airport-security sensitivity risk

- 0: no concern; distant generalized public view.
- 1: minor concern; requires local verification.
- 2: near sensitive facility or perimeter; avoid publishing details.
- 3: restricted/perimeter/security-sensitive; exclude.

## Output layers

- `topographic_viewpoints_public`: generalized safe public/residential viewpoints.
- `viewshed_airport_generalized`: broad, non-sensitive visibility zones.
- `excluded_sensitive_airport_areas`: generalized exclusion layer for airport perimeter and restricted/security-sensitive areas.
- `living_zones_with_view_score`: safe living zones joined to topographic visibility score.

## Data-protection and safety rules

- Do not publish exact private residential viewpoints.
- Do not publish precise airport-perimeter observation points.
- Do not publish operational flight timing, surveillance, tracking, or restricted-area details.
- Use only public, legal, civic-facing observation context.
- Keep airport observation subordinate to residential safety and WASH field planning.

## Immediate GIS tasks

1. Add DEM source to `docs/data-inventory.md`.
2. Create `schema/topographic_viewpoint_schema.csv`.
3. Add candidate viewpoint zones for Cochabamba and Sucre.
4. Run viewshed analysis using QGIS from generalized public/residential candidate points.
5. Join viewpoint score to `living_zones`.
6. Rank zones by combined safety, internet, medical access, living suitability, and topographic view.
