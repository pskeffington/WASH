# Cochabamba Geography Layer Manifest

## Purpose

This manifest defines the first geography layers to pull for the Cochabamba GIS build. The target is a QGIS-ready base map for safe living-zone, topographic viewshed, and WASH work-zone planning.

## Primary geography pulls

### Administrative boundaries

- Bolivia department boundary.
- Cochabamba Department boundary.
- Cochabamba municipality / Cercado boundary.
- Metropolitan municipalities: Cochabamba, Sacaba, Tiquipaya, Quillacollo, Colcapirhua, Sipe Sipe, Vinto.
- Valle Alto municipalities for later corridor expansion: Punata, Cliza, Tolata, Tarata, Arani.

Preferred source:

- geoBoundaries open administrative boundaries API for Bolivia ADM1 and ADM2.

### Roads and transport

- Primary roads.
- Secondary roads.
- Local streets.
- Rural tracks.
- Bus terminals and transport nodes where available.

Preferred source:

- Geofabrik Bolivia OpenStreetMap shapefile extract.

### Hydrology and terrain context

- Rivers.
- Streams.
- Canals and water bodies where present in OSM.
- DEM-derived elevation, slope, hillshade, aspect, and terrain ruggedness.

Preferred sources:

- Geofabrik Bolivia OSM extract for waterways and water features.
- Copernicus DEM, NASADEM, or SRTM for terrain.

### Settlements and built environment

- Place points.
- Built-up areas.
- Landuse.
- Public facilities where available.

Preferred sources:

- Geofabrik Bolivia OSM extract.
- OpenStreetMap-derived POI and place layers.

## Local output targets

Raw layers:

- `gis/layers/raw/cochabamba/`

Processed layers:

- `gis/layers/processed/cochabamba/cochabamba_department.geojson`
- `gis/layers/processed/cochabamba/cochabamba_metropolitan_municipalities.geojson`
- `gis/layers/processed/cochabamba/cochabamba_roads.geojson`
- `gis/layers/processed/cochabamba/cochabamba_waterways.geojson`
- `gis/layers/processed/cochabamba/cochabamba_places.geojson`
- `gis/layers/processed/cochabamba/cochabamba_public_facilities.geojson`
- `gis/layers/processed/cochabamba/cochabamba_dem_clip.tif`
- `gis/layers/processed/cochabamba/cochabamba_hillshade.tif`
- `gis/layers/processed/cochabamba/cochabamba_slope.tif`

## Downloader

Run locally:

```bash
python scripts/download_cochabamba_geography.py
```

Then inspect and clip/filter in QGIS.

## Review rules

- Confirm source license before committing any derived layer.
- Keep large raw downloads out of git unless clearly permitted and useful.
- Commit generalized and processed layers only after review.
- Do not publish private residential coordinates, exact vulnerable community locations, airport-perimeter observation points, or rumor-based safety/crime layers.

## Next processing step

After downloading, the QGIS pass should clip the Bolivia-wide source layers to Cochabamba Department and the metropolitan safe-base study area. The first analytical output should be a base map containing administrative boundaries, roads, places, waterways, terrain, and candidate safe living zones.
