#!/usr/bin/env python3
"""Normalize real source PNGs into size-specific source/png directories.

The script does not generate placeholder art. It writes output only when --apply is
passed and real source PNGs exist inside source/master/raster.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

SIZES = [1024, 512, 256, 128, 64, 48, 32, 24, 16]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ensure_inside_repo(root: Path, path: Path) -> None:
    path.resolve().relative_to(root.resolve())


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize real PNG source assets.")
    parser.add_argument("--apply", action="store_true", help="write generated PNG outputs")
    args = parser.parse_args()

    root = repo_root()
    source_dir = root / "source" / "master" / "raster"
    sources = sorted(source_dir.glob("*.png"))
    if not sources:
        print("normalize_pngs: no source assets found in source/master/raster")
        return 0

    try:
        from PIL import Image
    except ImportError:
        print("normalize_pngs: Pillow is required when source assets exist", file=sys.stderr)
        return 2

    print(f"normalize_pngs: found {len(sources)} source PNG(s)")
    if not args.apply:
        for source in sources:
            print(f"DRY-RUN would normalize {source.relative_to(root)} into source/png/<size>/")
        return 0

    for source in sources:
        ensure_inside_repo(root, source)
        with Image.open(source).convert("RGBA") as image:
            bbox = image.getbbox()
            if bbox:
                image = image.crop(bbox)
            for size in SIZES:
                output_dir = root / "source" / "png" / str(size)
                output_dir.mkdir(parents=True, exist_ok=True)
                output = output_dir / source.name
                canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
                safe = max(1, int(size * 0.86))
                scale = safe / max(image.width, image.height)
                target = (max(1, int(round(image.width * scale))), max(1, int(round(image.height * scale))))
                resized = image.resize(target, Image.LANCZOS)
                x = (size - resized.width) // 2
                y = (size - resized.height) // 2
                canvas.alpha_composite(resized, (x, y))
                ensure_inside_repo(root, output)
                canvas.save(output)
                print(f"WROTE {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
