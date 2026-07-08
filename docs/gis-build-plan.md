# GIS Build Plan: Safe Base, Topography, and WASH Work Zones

## Purpose

This build plan turns the repository into an operational GIS workspace for public, civic-facing planning. The first map objective is to identify safe living zones with strong internet, medical access, transport reliability, and topographic overlook potential. WASH work zones are ranked only after safe bases are selected.

## Build order

### Phase 1: Base layers

1. Administrative boundaries: Bolivia, departments, municipalities.
2. Roads and transport nodes.
3. Settlements and built-up areas.
4. Hydrology: rivers, streams, reservoirs, watersheds.
5. DEM, slope, hillshade, and terrain ruggedness.
6. Public facilities: clinics, hospitals, schools, markets, municipal offices, parishes, universities.
7. Airports as generalized context polygons only, with restricted/perimeter areas excluded from public viewpoint planning.

### Phase 2: Living-zone candidates

Load `data/seed/living_zones_seed.csv` and create generalized candidate polygons for:

- Cochabamba: Recoleta, Cala Cala, Queru Queru, Tupuraya, Tiquipaya.
- Sucre: Centro Historico, La Recoleta, Zona Norte / Avenida de las Americas, Yotala/outskirts.

Each zone should be scored for:

- Safety and crime exposure.
- Secure housing potential.
- Internet/fiber potential.
- Medical and daily services.
- Transport reliability.
- Support-network potential.

### Phase 3: Topographic viewpoints

Load `data/seed/topographic_viewpoints_seed.csv` and use the DEM to calculate:

- Elevation.
- Elevation advantage over nearby valley floor.
- Slope.
- Aspect.
- Hillshade context.
- Viewshed toward generalized valley and airport-basin areas.

Exclude any location that is restricted, airport-perimeter-adjacent, isolated, or not suitable for lawful public/residential access.

### Phase 4: Safety overlay

Add public and source-documented safety indicators only:

- Petty-theft exposure clusters.
- Night-mobility risk zones.
- Protest or roadblock-prone corridors.
- Transport-risk areas.
- Clinic/emergency access.

Do not add rumor-based labels. Do not publish sensitive or defamatory neighborhood claims.

### Phase 5: WASH work zones

Create generalized work-zone polygons for:

- Cochabamba peri-urban edge.
- Valle Alto agricultural towns.
- Inter-valley mountain corridor.
- Sucre municipal-rural transition.
- Potosi-linked highland edge.

Rank only after safe base, route, and communications feasibility are understood.

## QGIS processing workflow

### DEM workflow

1. Load DEM raster.
2. Reproject to appropriate local CRS for analysis.
3. Clip to Cochabamba-Sucre corridor bounding area.
4. Generate hillshade.
5. Generate slope and aspect rasters.
6. Sample elevation values to candidate living-zone and viewpoint points.
7. Generate viewsheds from generalized viewpoint candidates.
8. Join topographic scores back to living-zone candidate table.

### Safety workflow

1. Load living-zone polygons.
2. Load source-documented safety indicators.
3. Join or summarize safety indicators by living-zone polygon.
4. Add manual verification fields.
5. Calculate living-zone suitability score.
6. Flag zones requiring local review.

### WASH work-zone workflow

1. Load work-zone polygons.
2. Overlay roads, clinics, schools, hydrology, settlement, and elevation.
3. Add WASH risk attributes from literature and field planning.
4. Calculate work-zone priority.
5. Link each work zone to nearest safe base and daylight return route.

## Initial scoring formula

### Living-zone total score

Positive suitability components:

- Safety score.
- Secure housing score.
- Internet score.
- Medical services score.
- Daily services score.
- Transport score.
- Support-network score.
- Topographic safe-overlook score.

Risk deductions:

- Petty theft exposure.
- Violent crime exposure.
- Night mobility risk.
- Protest/roadblock exposure.
- Transport risk.
- Airport security sensitivity risk.

Use the result only as a draft ranking until locally reviewed.

### Work-zone priority

A work zone should not be prioritized if it cannot be reached and exited safely.

Priority factors:

- WASH severity.
- Public-facility relevance.
- Climate and reliability risk.
- Local partner status.
- Road access.
- Communications.
- Daylight return feasibility.
- Nearest safe base.

## Public map outputs

- Safe Living Zones: Cochabamba.
- Safe Living Zones: Sucre.
- Topographic Overlook Suitability: Cochabamba.
- Topographic Overlook Suitability: Sucre / Alcantari corridor.
- WASH Work Zones: Cochabamba-Sucre corridor.
- Daylight Field Circuits from Safe Bases.

## Repository next tasks

- Add placeholder GeoJSONs for living zones and topographic viewpoints.
- Add QGIS style files for living-zone suitability and WASH work-zone priority.
- Add source metadata template.
- Add Spanish-language public-source inventory.
- Add first municipal profiles for Cochabamba and Sucre.
