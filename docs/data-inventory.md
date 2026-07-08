# Public Data Inventory: Cochabamba-Sucre WASH Mapping

## Purpose

This inventory lists the public, non-sensitive datasets needed for a GIS-first WASH map of the Cochabamba-Sucre corridor. It is a planning document, not a final dataset catalog.

## Data ethics

- Do not publish household-level coordinates.
- Do not publish vulnerable community details without partner approval.
- Generalize sensitive points to settlement, municipal, or grid scale.
- Document source, license, date accessed, and processing steps.
- Separate observed field data from modeled or inferred data.

## Priority data categories

### Administrative boundaries

Needed layers:

- Bolivia national boundary.
- Department boundaries: Cochabamba, Chuquisaca, Potosi.
- Municipal boundaries for priority corridor municipalities.
- Locality or community names where public.

Potential sources to research:

- Bolivia national geospatial portals.
- Humanitarian Data Exchange.
- OpenStreetMap administrative data.
- GADM or other public boundary datasets, subject to license review.

### Roads and access

Needed layers:

- Primary roads.
- Secondary roads.
- Rural roads and tracks.
- Bridge and river crossing points where available.
- Road-surface or seasonal-access class where available.

Derived indicators:

- Distance to primary or secondary road.
- Estimated travel time to nearest town.
- Estimated travel time to nearest clinic.
- Estimated travel time to nearest school.

Potential sources to research:

- OpenStreetMap.
- Bolivia transport ministry or road authority data.
- Humanitarian Data Exchange.

### Hydrology and watershed layers

Needed layers:

- Rivers and streams.
- Watershed/catchment boundaries.
- Reservoirs, canals, and wetlands.
- Springs and public water points where available.

Derived indicators:

- Distance to nearest surface-water feature.
- Upstream/downstream relation to settlements.
- Watershed exposure class.
- Potential source-protection concern.

Potential sources to research:

- HydroSHEDS.
- OpenStreetMap.
- National watershed-management documents.
- Municipal or departmental water-planning sources.

### Climate and drought layers

Needed layers:

- Precipitation normals.
- Seasonal rainfall variation.
- Drought indicators.
- Soil moisture or vegetation-stress proxies.
- Flood or landslide susceptibility where public.

Derived indicators:

- Dry-season stress class.
- Drought exposure class.
- Flood/drainage exposure class.
- Rainfall reliability context.

Potential sources to research:

- CHIRPS precipitation.
- MODIS/VIIRS vegetation indices.
- SERVIR, NASA, or public climate portals.
- Bolivia climate-adaptation documents.

### Terrain

Needed layers:

- Digital elevation model.
- Slope.
- Terrain ruggedness.
- Valley/highland classification.

Derived indicators:

- Elevation band.
- Gravity-fed system feasibility context.
- Road-access difficulty.
- Flood/erosion exposure.

Potential sources to research:

- SRTM.
- Copernicus DEM.
- NASADEM.

### Population and settlement

Needed layers:

- Built-up settlement footprints.
- Population grids.
- Urban/peri-urban/rural classification.
- Community names where public.

Derived indicators:

- Population-weighted WASH risk.
- Peri-urban growth pressure.
- Settlement dispersion.
- Sparse-rural service challenge.

Potential sources to research:

- WorldPop.
- GHSL built-up areas.
- OpenStreetMap.
- Bolivia census sources.

### Schools and health facilities

Needed layers:

- Public schools.
- Health centers, clinics, and hospitals.
- Facility type and administrative authority where public.

Derived indicators:

- Distance from settlement to school.
- Distance from settlement to health facility.
- Priority public-facility WASH survey targets.

Potential sources to research:

- Ministry of Education directories.
- Ministry of Health directories.
- OpenStreetMap.
- Humanitarian Data Exchange.

### WASH infrastructure and service areas

Needed layers:

- Water utility/provider service areas where public.
- Wastewater treatment plants.
- Sewerage coverage where public.
- Public water points.
- Community water systems only where public or partner-approved.

Derived indicators:

- In-service-area vs out-of-service-area classification.
- Proximity to treatment or utility infrastructure.
- Settlement likely served by network vs community/self-supply.

Potential sources to research:

- Municipal provider reports.
- Cochabamba and Sucre municipal planning documents.
- Ministry of Environment and Water materials.
- Partner-confirmed field sources.

## Initial schema plan

Create tables for:

- `settlements` — generalized settlement-level WASH mapping units.
- `facilities` — schools, clinics, and public WASH nodes.
- `water_systems_public` — only publicly documented or partner-approved water-system information.
- `field_observations_private` — private field collection table, not published raw.
- `priority_index_public` — generalized and validated risk categories only.

## Immediate tasks

- Identify candidate public source URLs for each data category.
- Record licenses and date accessed.
- Build a municipal profile template.
- Create schema files before collecting any field data.
