#!/usr/bin/env python3
"""Export Linux PNG fallback sizes from real PNG source assets.

The exporter is asset-manifest aware for v0.0.2. When
mappings/icon-assets.csv exists, only assets assigned to the requested
linux_context are exported. This keeps apps, places, and MIME icons in their
correct XDG theme directories.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

SIZES = [16, 24, 32, 48, 64, 128, 256]
VALID_CONTEXTS = {"apps", "mimetypes", "places", "devices", "status", "actions"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ensure_inside_repo(root: Path, path: Path) -> None:
    path.resolve().relative_to(root.resolve())


def manifest_sources(root: Path, context: str) -> list[Path]:
    manifest = root / "mappings" / "icon-assets.csv"
    if not manifest.is_file():
        return []

    sources: list[Path] = []
    with manifest.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            contexts = [item.strip() for item in row.get("linux_context", "").split(";") if item.strip()]
            if context not in contexts:
                continue
            source_value = row.get("source_master_path", "").strip()
            if not source_value:
                continue
            source = root / source_value
            if source.is_file():
                sources.append(source)
    return sorted(set(sources))


def fallback_sources(root: Path) -> list[Path]:
    source_dirs = [root / "source" / "png" / "256", root / "source" / "master" / "raster"]
    return sorted({path for directory in source_dirs for path in directory.glob("*.png")})


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Linux PNG fallback assets.")
    parser.add_argument("--context", default="apps", choices=sorted(VALID_CONTEXTS), help="icon theme context")
    parser.add_argument("--apply", action="store_true", help="write PNG fallback outputs")
    args = parser.parse_args()

    root = repo_root()
    sources = manifest_sources(root, args.context) or fallback_sources(root)
    svg_sources = sorted((root / "source" / "svg" / "full-color").glob("*.svg"))

    if svg_sources:
        print("export_linux_png_fallbacks: SVG sources found; convert SVGs with Inkscape/CairoSVG in a later toolchain step")
    if not sources:
        print("export_linux_png_fallbacks: no PNG source assets found for requested context")
        return 0

    try:
        from PIL import Image
    except ImportError:
        print("export_linux_png_fallbacks: Pillow is required when PNG source assets exist", file=sys.stderr)
        return 2

    print(f"export_linux_png_fallbacks: found {len(sources)} source PNG(s) for {args.context}")
    for source in sources:
        ensure_inside_repo(root, source)
        with Image.open(source).convert("RGBA") as image:
            bbox = image.getbbox()
            if bbox:
                image = image.crop(bbox)
            for size in SIZES:
                output_dir = root / "linux" / "Sauriil-Dark-Archive" / f"{size}x{size}" / args.context
                output = output_dir / source.name
                if not args.apply:
                    print(f"DRY-RUN would export {source.relative_to(root)} -> {output.relative_to(root)}")
                    continue
                output_dir.mkdir(parents=True, exist_ok=True)
                canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
                resized = image.copy()
                safe = max(1, int(size * 0.86))
                resized.thumbnail((safe, safe), Image.LANCZOS)
                canvas.alpha_composite(resized, ((size - resized.width) // 2, (size - resized.height) // 2))
                ensure_inside_repo(root, output)
                canvas.save(output)
                print(f"WROTE {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
