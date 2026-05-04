#!/usr/bin/env python3
"""Export multi-size Windows ICO files from real PNG assets.

The exporter is asset-manifest aware for v0.0.2. When
mappings/icon-assets.csv exists, only assets assigned to the requested
windows_context are exported. This prevents app, folder, and filetype icons from
being blindly copied into unrelated Windows output directories.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

ICO_SIZES = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
VALID_CONTEXTS = {"apps", "filetypes", "folders", "drives", "shell"}


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
            contexts = [item.strip() for item in row.get("windows_context", "").split(";") if item.strip()]
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
    parser = argparse.ArgumentParser(description="Export Windows ICO files from real PNG assets.")
    parser.add_argument("--context", default="apps", choices=sorted(VALID_CONTEXTS), help="windows/ico context")
    parser.add_argument("--apply", action="store_true", help="write ICO outputs")
    args = parser.parse_args()

    root = repo_root()
    sources = manifest_sources(root, args.context) or fallback_sources(root)
    if not sources:
        print("export_windows_ico: no source assets found for requested context")
        return 0

    try:
        from PIL import Image
    except ImportError:
        print("export_windows_ico: Pillow is required when source assets exist", file=sys.stderr)
        return 2

    output_dir = root / "windows" / "ico" / args.context
    print(f"export_windows_ico: found {len(sources)} source PNG(s) for {args.context}")
    for source in sources:
        ensure_inside_repo(root, source)
        output = output_dir / f"{source.stem}.ico"
        if not args.apply:
            print(f"DRY-RUN would export {source.relative_to(root)} -> {output.relative_to(root)}")
            continue
        output_dir.mkdir(parents=True, exist_ok=True)
        with Image.open(source).convert("RGBA") as image:
            bbox = image.getbbox()
            if bbox:
                image = image.crop(bbox)
            canvas = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
            resized = image.copy()
            resized.thumbnail((220, 220), Image.LANCZOS)
            canvas.alpha_composite(resized, ((256 - resized.width) // 2, (256 - resized.height) // 2))
            ensure_inside_repo(root, output)
            canvas.save(output, format="ICO", sizes=ICO_SIZES)
            print(f"WROTE {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
