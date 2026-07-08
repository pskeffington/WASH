#!/usr/bin/env python3
"""Download and prepare public geography layers for Cochabamba.

This script is designed for local/QGIS preparation. It downloads public source
layers, writes metadata, and prepares a project folder structure. Large raw
layers should not be committed unless their license permits it.

Primary outputs:
- gis/layers/raw/cochabamba/
- gis/layers/processed/cochabamba/
- gis/metadata/cochabamba_geography_sources.md

Notes:
- Exact public-source URLs may change. Review logs before relying on outputs.
- Administrative layers should be clipped/filtered to Cochabamba Department and
  corridor municipalities before public map export.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "gis" / "layers" / "raw" / "cochabamba"
PROCESSED_DIR = ROOT / "gis" / "layers" / "processed" / "cochabamba"
METADATA_DIR = ROOT / "gis" / "metadata"


@dataclass(frozen=True)
class SourceLayer:
    layer_id: str
    label: str
    url: str
    output_name: str
    notes: str


SOURCES = [
    SourceLayer(
        layer_id="geoboundaries_bol_adm1",
        label="geoBoundaries Bolivia ADM1 departments",
        url="https://www.geoboundaries.org/api/current/gbOpen/BOL/ADM1/",
        output_name="geoboundaries_bol_adm1_api.json",
        notes="API endpoint. Resolve downloadURL from JSON, then filter for Cochabamba Department.",
    ),
    SourceLayer(
        layer_id="geoboundaries_bol_adm2",
        label="geoBoundaries Bolivia ADM2 provinces/municipal admin level",
        url="https://www.geoboundaries.org/api/current/gbOpen/BOL/ADM2/",
        output_name="geoboundaries_bol_adm2_api.json",
        notes="API endpoint. Resolve downloadURL from JSON and filter to Cochabamba-related units.",
    ),
    SourceLayer(
        layer_id="geofabrik_bolivia_shp",
        label="Geofabrik Bolivia OpenStreetMap Shapefile Extract",
        url="https://download.geofabrik.de/south-america/bolivia-latest-free.shp.zip",
        output_name="bolivia-latest-free.shp.zip",
        notes="Contains OSM roads, waterways, places, POIs, landuse, and other feature classes. Clip to Cochabamba corridor.",
    ),
]


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)


def download(url: str, output_path: Path) -> None:
    print(f"Downloading {url} -> {output_path}")
    req = urllib.request.Request(url, headers={"User-Agent": "WASH-GIS-Research/0.1"})
    with urllib.request.urlopen(req, timeout=120) as response:
        output_path.write_bytes(response.read())


def resolve_geoboundaries_download(api_json_path: Path) -> str | None:
    try:
        payload = json.loads(api_json_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"Could not parse {api_json_path}: {exc}")
        return None
    return payload.get("gjDownloadURL") or payload.get("simplifiedGeometryGeoJSON") or payload.get("downloadURL")


def write_metadata() -> None:
    metadata = METADATA_DIR / "cochabamba_geography_sources.md"
    lines = [
        "# Cochabamba Geography Source Metadata",
        "",
        "## Purpose",
        "",
        "This file records the first public geography layers for the Cochabamba WASH GIS build.",
        "Raw downloads should be reviewed for license, CRS, coverage, and sensitivity before being committed or published.",
        "",
        "## Sources",
        "",
    ]
    for source in SOURCES:
        lines.extend(
            [
                f"### {source.label}",
                "",
                f"- Layer ID: `{source.layer_id}`",
                f"- Source URL: {source.url}",
                f"- Local raw output: `gis/layers/raw/cochabamba/{source.output_name}`",
                f"- Notes: {source.notes}",
                "- Public release status: source/license review required before committing derived data.",
                "",
            ]
        )
    lines.extend(
        [
            "## Processing targets",
            "",
            "- Cochabamba Department boundary.",
            "- Cochabamba municipality / Cercado boundary.",
            "- Metropolitan municipalities: Cochabamba, Sacaba, Tiquipaya, Quillacollo, Colcapirhua, Sipe Sipe, Vinto.",
            "- Candidate living-zone context: Recoleta, Cala Cala, Queru Queru, Tupuraya, Tiquipaya.",
            "- Roads, waterways, public facilities, landuse, and settlement features clipped to the Cochabamba study area.",
            "",
            "## Data protection",
            "",
            "Do not publish private household coordinates, sensitive community locations, airport-perimeter observation points, or rumor-based safety/crime layers.",
            "",
        ]
    )
    metadata.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {metadata}")


def main() -> int:
    ensure_dirs()
    write_metadata()

    for source in SOURCES:
        output_path = RAW_DIR / source.output_name
        if output_path.exists():
            print(f"Skipping existing file: {output_path}")
            continue
        try:
            download(source.url, output_path)
        except Exception as exc:  # noqa: BLE001
            print(f"FAILED {source.layer_id}: {exc}", file=sys.stderr)
            continue

        if source.layer_id.startswith("geoboundaries"):
            gj_url = resolve_geoboundaries_download(output_path)
            if gj_url:
                gj_path = RAW_DIR / source.output_name.replace("_api.json", ".geojson")
                try:
                    download(gj_url, gj_path)
                except Exception as exc:  # noqa: BLE001
                    print(f"FAILED resolved GeoJSON for {source.layer_id}: {exc}", file=sys.stderr)

    print("Download pass complete. Next: inspect layers in QGIS and clip/filter to Cochabamba.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
