# WASH Bolivia — Cochabamba–Sucre Corridor

Public, civic-facing research repository for Water, Sanitation, and Hygiene (WASH), watershed stress, service reliability, and spatial equity along the Cochabamba–Sucre corridor in Bolivia.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active WASH systems and spatial-analysis research scaffold.  
**Last documentation review:** 2026-08-12

## Public-interest research boundary

This repository is maintained for public-health scholarship, environmental-health research, open-data methods, GIS analysis, and reproducible documentation.

It does not provide travel-security guidance, residential site selection, surveillance or observation planning, operational field tasking, household-level vulnerability findings, infrastructure targeting, clinical determinations, or policy mandates. Public geospatial outputs should remain appropriately generalized and should not expose sensitive household, facility, or infrastructure details.

## Research focus

This repository studies WASH conditions and environmental-health systems across the central Bolivian corridor from Cochabamba through inter-Andean communities toward Sucre, with contextual attention to highland water scarcity and water-quality concerns where supported by evidence.

Primary domains include:

- drinking-water access, continuity, affordability, and reliability;
- water quality and household water safety at appropriate aggregation levels;
- sanitation coverage, sewerage, onsite sanitation, wastewater, and drainage;
- hygiene access in households, schools, clinics, and public facilities;
- watershed protection, drought stress, and climate-resilient WASH;
- community water systems, cooperatives, municipal providers, and local water governance;
- rural and peri-urban service disparities;
- GIS-based spatial equity analysis using non-sensitive public-interest data;
- source provenance, uncertainty, and reproducibility.

## Core research question

How do water access, sanitation, hygiene, watershed stress, service governance, and geographic isolation vary across the Cochabamba–Sucre corridor, and how can those differences be documented reproducibly using public and community-validated evidence?

## Study zones

1. **Cochabamba metropolitan and peri-urban edge** — service reliability, peri-urban growth, affordability, wastewater, and community systems.
2. **Valle Alto agricultural towns** — rural water reliability, sanitation, irrigation overlap, runoff, and seasonal stress.
3. **Inter-valley communities** — dispersed settlement patterns, springs, gravity-fed systems, road accessibility, dry-season stress, and system maintenance.
4. **Sucre municipal-rural transition** — service extension, peri-urban sanitation, public-facility WASH, and nearby Chuquisaca communities.
5. **Highland contextual layer** — water scarcity and water-quality concerns where supported by authoritative or peer-reviewed sources.

## Repository documents

- [Literature Review: Cochabamba-Sucre WASH Corridor](docs/literature-review.md)
- [Annotated Bibliography](docs/bibliography.md)
- [Public Data Inventory](docs/data-inventory.md)
- [Field Assessment Framework](docs/field-assessment-framework.md)
- [GIS Build Plan](docs/gis-build-plan.md)
- [Municipal WASH Profile Template](docs/municipal-profile-template.md)
- [Cochabamba Geography Layer Manifest](gis/metadata/cochabamba_geography_manifest.md)
- [GIS Mapping System](gis/README.md)
- [GIS Layer Configuration](config/gis_layers.yaml)
- [WASH Site Observation Schema](schema/wash_site_schema.csv)

Legacy planning documents that are unrelated to WASH research should be treated as historical artifacts and excluded from the current research surface.

## GIS research system

The GIS layer should support descriptive mapping of WASH access, service reliability, environmental context, and spatial inequity. It should prioritize public, appropriately licensed, non-sensitive data and preserve source metadata for every layer.

Appropriate analyses include municipal or regional comparisons, service-area context, watershed relationships, drought exposure, travel-time accessibility at generalized resolution, and public-facility WASH context.

Avoid publishing precise household coordinates, sensitive infrastructure locations, restricted facilities, or geospatial outputs that could create security or privacy risks.

## Initial source hierarchy

Priority sources should be verified and logged before research use. Prefer:

1. official Bolivian national, departmental, and municipal sources;
2. WHO/UNICEF Joint Monitoring Programme and other UN sources;
3. peer-reviewed literature;
4. university, NGO, utility, cooperative, and community-validated sources with documented provenance;
5. reputable secondary sources for historical context only.

General-reference sources such as Wikipedia may be useful for orientation but should not serve as manuscript-weight evidence when authoritative or peer-reviewed sources are available.

## Data and documentation standards

- Record source URL, publisher, publication/update date, access date, geography, license, and verification status.
- Distinguish observed data, modeled estimates, historical context, and research hypotheses.
- Use Spanish-language and local sources where available.
- Preserve administrative-boundary versions and geospatial processing steps.
- Document missingness, temporal mismatch, and uncertainty before comparing municipalities or communities.
- Treat local water governance as a social and institutional system, not solely an engineering variable.
- Do not commit personally identifying information, restricted partner data, household-level vulnerability coordinates, or sensitive infrastructure details.

## Reproducible geography workflow

A public geography downloader is available for reproducible staging of source layers:

```bash
python scripts/download_cochabamba_geography.py
```

Downloaded sources should remain subject to their original licenses and redistribution terms. Processed layers should retain source metadata and transformation notes.

## Near-term research plan

1. Refresh the public data inventory and bibliography with authoritative Bolivian, JMP, peer-reviewed, and Spanish-language sources.
2. Remove or archive legacy non-WASH planning objects from the active research surface.
3. Download and document current JMP Bolivia WASH indicators.
4. Build municipal profile sheets for selected Cochabamba, Valle Alto, inter-valley, and Sucre-area communities.
5. Establish a reproducible GIS workflow for WASH access, watershed stress, and spatial equity.
6. Add explicit uncertainty and temporal-harmonization rules for cross-source comparisons.
7. Develop a partner-facing research concept note for municipal, university, NGO, public-health, or community-water-system collaboration.
8. Connect validated outputs to the broader public-health portfolio evidence ledger.

## Supported contribution

A reproducible WASH systems and spatial-equity research framework for studying service reliability, sanitation, hygiene, watershed stress, governance, and geographic disparities in the Cochabamba–Sucre corridor.

## Unsupported contribution

No travel-security recommendation, residential-base recommendation, surveillance or observation guidance, operational field prioritization, household-level risk determination, infrastructure targeting, or policy mandate is made.
