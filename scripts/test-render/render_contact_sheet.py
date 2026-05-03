#!/usr/bin/env python3
"""Render a contact sheet from real icon assets when they exist.

The script does not create test icons or placeholder art. With an empty skeleton
it reports that no source assets were found.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

SIZES = [16, 24, 32, 48, 64, 128, 256]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ensure_inside_repo(root: Path, path: Path) -> None:
    path.resolve().relative_to(root.resolve())


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a contact sheet from real PNG assets.")
    parser.add_argument("--apply", action="store_true", help="write the contact sheet")
    args = parser.parse_args()

    root = repo_root()
    sources = sorted((root / "source" / "png" / "256").glob("*.png"))
    if not sources:
        print("render_contact_sheet: no source assets found in source/png/256")
        return 0

    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("render_contact_sheet: Pillow is required when source assets exist", file=sys.stderr)
        return 2

    output = root / "source" / "master" / "contact-sheets" / "contact-sheet.png"
    if not args.apply:
        print(f"DRY-RUN would render {len(sources)} icon(s) into {output.relative_to(root)}")
        return 0

    cell = 160
    label_h = 24
    width = cell * len(SIZES)
    height = (cell + label_h) * len(sources)
    sheet = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(sheet)

    for row, source in enumerate(sources):
        ensure_inside_repo(root, source)
        with Image.open(source).convert("RGBA") as image:
            bbox = image.getbbox()
            if bbox:
                image = image.crop(bbox)
            for col, size in enumerate(SIZES):
                canvas = Image.new("RGBA", (cell, cell), (0, 0, 0, 0))
                rendered = image.copy()
                rendered.thumbnail((size, size), Image.LANCZOS)
                x = (cell - rendered.width) // 2
                y = (cell - rendered.height) // 2
                canvas.alpha_composite(rendered, (x, y))
                px = col * cell
                py = row * (cell + label_h)
                sheet.alpha_composite(canvas, (px, py))
                draw.text((px + 4, py + cell), f"{source.stem} {size}px", fill=(255, 255, 255, 255))

    output.parent.mkdir(parents=True, exist_ok=True)
    ensure_inside_repo(root, output)
    sheet.save(output)
    print(f"WROTE {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
