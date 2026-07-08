# GIS Mapping System

## Purpose

This directory defines the GIS system for building a public, civic-facing WASH and safety map for the Cochabamba-Sucre corridor.

The map is intended to support:

- Safe living-zone selection for a U.S.-based WASH professional.
- Work-zone selection for WASH field assessment.
- Public-interest mapping of water access, sanitation, hygiene, watershed, public-facility, and transport-access conditions.
- Non-sensitive risk mapping that avoids exposing household-level or vulnerable community-level data.

## Map products

### 1. Living-zone suitability map

Ranks candidate residential zones based on:

- Safety and crime exposure, using public and locally verified indicators.
- Distance from high-theft locations such as bus terminals, dense market congestion, nightlife clusters, and known demonstration corridors.
- Access to clinics, pharmacies, grocery, trusted transport, and secure housing.
- Internet/fiber availability.
- Proximity to airports, universities, NGOs, parishes, municipal offices, and trusted local contacts.

### 2. WASH work-zone map

Ranks field zones based on:

- Water access and reliability risk.
- Sanitation and wastewater risk.
- School and clinic WASH relevance.
- Drought, watershed, and seasonal access constraints.
- Road access, cell coverage, and safe day-trip feasibility.
- Partner presence and local verification status.

### 3. Corridor operations map

Supports planning without publishing sensitive data:

- Base locations and staging zones.
- Day-trip field circuits.
- Return-to-base routes.
- Clinic and emergency service proximity.
- Roadblock-prone and weather-sensitive corridors where public and verified.

## Directory structure

```text
gis/
  README.md
  qgis-project/
    WASH_Cochabamba_Sucre.qgz.placeholder
  layers/
    raw/              # downloaded public source layers; not committed unless license permits
    processed/        # generalized public-ready layers
    private/          # local-only sensitive field layers; never commit raw private data
  styles/             # QGIS .qml styles
  exports/            # public map exports
  metadata/           # source metadata and processing notes
```

## Data-protection rules

- Do not commit private household coordinates.
- Do not commit exact vulnerable-site locations unless already public and partner-approved.
- Keep raw field observations local or encrypted outside the public repository.
- Public maps should generalize to settlement, municipal, corridor-zone, or grid-cell level.
- All safety/crime indicators must be sourced, dated, and confidence-scored.

## Recommended platform

Use QGIS as the main desktop GIS platform.

Suggested CRS:

- Storage/interchange: EPSG:4326, WGS 84.
- Local measurement/analysis: choose the appropriate Bolivia UTM zone after source-layer review.

## Initial workflow

1. Create base map from administrative boundaries, roads, settlements, rivers, elevation, and public facilities.
2. Add living-zone candidate polygons for Cochabamba and Sucre.
3. Add safety/crime exposure indicators from public, current, and locally verified sources.
4. Add WASH work-zone polygons for corridor field assessment.
5. Add scoring fields from `schema/living_zone_schema.csv` and `schema/work_zone_schema.csv`.
6. Export only generalized, non-sensitive public maps.
