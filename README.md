# WASH Bolivia: Cochabamba-Sucre Corridor

Public, civic-facing research repository for Water, Sanitation, and Hygiene (WASH) review, safe-base selection, and field-planning work along the Cochabamba-Sucre corridor in Bolivia.

## Research focus

This repository studies the central Bolivian corridor from Cochabamba through the inter-Andean valley and mountain corridor toward Sucre, with secondary attention to Potosi-linked highland water-quality and water-scarcity concerns.

The work is focused on:

- Safe living-zone selection before work-zone selection.
- Crime/safety exposure, medical access, internet reliability, and transport continuity for residential base planning.
- Drinking water access and reliability.
- Water quality and household water safety.
- Sanitation coverage, on-site sanitation, sewerage, wastewater, and drainage.
- Hygiene access in households, schools, clinics, and public facilities.
- Watershed protection, drought stress, and climate-resilient WASH.
- Community water systems, cooperatives, municipal providers, and local water governance.
- GIS-based spatial equity mapping using non-sensitive public-interest data.

## Corridor zones

1. **Cochabamba metropolitan and peri-urban edge** — municipal service reliability, peri-urban growth, water affordability, wastewater, and community systems.
2. **Valle Alto agricultural towns** — Punata, Cliza, and nearby rural/agricultural communities; irrigation overlap, runoff, sanitation, and rural water reliability.
3. **Inter-valley mountain corridor** — dispersed settlements, springs, gravity-fed systems, road access, dry-season stress, and system maintenance.
4. **Sucre municipal-rural transition** — urban service extension, peri-urban sanitation, public-facility WASH, and nearby Chuquisaca communities.
5. **Potosi-linked highland edge** — water scarcity, mining legacy, metal-contamination screening where relevant, and highland service reliability.

## Repository documents

- [Literature Review: Cochabamba-Sucre WASH Corridor](docs/literature-review.md)
- [Annotated Bibliography](docs/bibliography.md)
- [Public Data Inventory](docs/data-inventory.md)
- [Field Assessment Framework](docs/field-assessment-framework.md)
- [Safety and Living-Zone Mapping Framework](docs/safety-living-zones.md)
- [Municipal WASH Profile Template](docs/municipal-profile-template.md)
- [GIS Mapping System](gis/README.md)
- [GIS Layer Configuration](config/gis_layers.yaml)
- [WASH Site Observation Schema](schema/wash_site_schema.csv)
- [Living Zone GIS Schema](schema/living_zone_schema.csv)
- [Work Zone GIS Schema](schema/work_zone_schema.csv)

## GIS system

The GIS system ranks safe living zones first, then WASH work zones second. Residential base selection considers source-documented safety exposure, secure housing, internet/fiber access, medical services, daily services, transport reliability, and support networks. Work-zone selection then evaluates WASH priority, road access, daylight-return feasibility, communications, field safety, and partner status.

## Initial source base

- WHO/UNICEF Joint Monitoring Programme household WASH data and SDG 6 monitoring: https://washdata.org/data/household
- UNICEF Bolivia country office, reports, and child-priority framework: https://www.unicef.org/bolivia/en
- Bolivia water supply and sanitation sector overview: https://en.wikipedia.org/wiki/Water_supply_and_sanitation_in_Bolivia
- Cochabamba Water War governance background: https://en.wikipedia.org/wiki/Cochabamba_Water_War
- William Finnegan, "Leasing the Rain," The New Yorker, 2002: https://www.newyorker.com/magazine/2002/04/08/leasing-the-rain
- Bolivia water resources management overview: https://en.wikipedia.org/wiki/Water_resources_management_in_Bolivia
- Bolivia agriculture and runoff background: https://en.wikipedia.org/wiki/Agriculture_in_Bolivia
- Urban morphology and water scarcity method reference: https://arxiv.org/abs/2402.06676
- Public geospatial WASH mapping method reference: https://arxiv.org/abs/2111.04134

## Working hypothesis

The Cochabamba-Sucre corridor should be studied as a combined safe-base, WASH, watershed, and spatial-equity problem. The main field risk is not only whether a water source exists, but whether the researcher can safely live, communicate, travel, return to base, and work with local partners while assessing whether households, schools, clinics, and rural settlements have reliable, safe, affordable, and socially legitimate WASH access across dry-season and drought-stress conditions.

## Research standards

- Keep the repository public, civic-facing, scholarly, and non-operational.
- Do not publish household-level coordinates, personally identifiable information, or sensitive community-level vulnerability data without partner approval.
- Do not publish rumor-based crime labels or unverified neighborhood accusations.
- Distinguish evidence from hypothesis.
- Prefer official, peer-reviewed, municipal, NGO, and community-validated sources.
- Use Spanish-language sources where available.
- Treat local water governance as a social institution, not only an engineering problem.

## Near-term work plan

- Build current safety-source inventory for Cochabamba and Sucre.
- Create living-zone candidate polygons for Cochabamba and Sucre.
- Build municipal profile sheets for Cochabamba, Sacaba, Tiquipaya, Punata, Cliza, Sucre, Yotala, and selected inter-valley communities.
- Identify source URLs, licenses, and access dates for public GIS layers.
- Download and document JMP Bolivia WASH indicators.
- Add Spanish-language ministry, municipal, and university sources.
- Create a non-sensitive GIS workflow for corridor WASH priority mapping.
- Prepare a partner-facing concept note for municipal, NGO, parish, university, or public-health collaboration.
