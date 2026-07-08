# Cochabamba Processed GIS Layers

This directory is for reviewed, clipped, generalized geography layers for the Cochabamba GIS build.

## Target layers

- `cochabamba_department.geojson`
- `cochabamba_metropolitan_municipalities.geojson`
- `cochabamba_roads.geojson`
- `cochabamba_waterways.geojson`
- `cochabamba_places.geojson`
- `cochabamba_public_facilities.geojson`
- `cochabamba_dem_clip.tif`
- `cochabamba_hillshade.tif`
- `cochabamba_slope.tif`
- `cochabamba_viewshed_candidates.tif`

## Public release requirements

Before committing processed layers:

- Confirm source license.
- Confirm CRS.
- Confirm clipping extent.
- Remove sensitive or private features.
- Generalize safety and viewpoint layers.
- Attach a metadata record under `gis/metadata/`.

## First analytical objective

Build a safe-base topographic map for Cochabamba that overlays:

- candidate living zones,
- roads and services,
- clinic/emergency access,
- elevation/slope/hillshade,
- safe public/residential viewpoint candidates,
- WASH work-zone access corridors.
