#!/usr/bin/env python3
"""Render v0.0.2 contact sheets from generated PNG icon assets."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

SIZES = [16, 24, 32, 48, 256]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ensure_inside_repo(root: Path, path: Path) -> None:
    path.resolve().relative_to(root.resolve())


def draw_checker(draw, x0: int, y0: int, w: int, h: int, block: int = 8) -> None:
    colors = [(35, 31, 35, 255), (18, 15, 18, 255)]
    for y in range(y0, y0 + h, block):
        for x in range(x0, x0 + w, block):
            color = colors[((x - x0) // block + (y - y0) // block) % 2]
            draw.rectangle([x, y, min(x + block - 1, x0 + w - 1), min(y + block - 1, y0 + h - 1)], fill=color)


def render_sheet(root: Path, size: int, sources: list[Path], apply: bool) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    output = root / "source" / "master" / "contact-sheets" / f"v0.0.2-contact-sheet-{size}.png"
    if not apply:
        print(f"DRY-RUN would render {len(sources)} icon(s) into {output.relative_to(root)}")
        return output

    cols = 4
    rows = (len(sources) + cols - 1) // cols
    cell = max(96, size + 48) if size < 128 else 320
    label_h = 34
    margin = 16
    width = margin * 2 + cols * cell
    height = margin * 2 + rows * (cell + label_h)
    sheet = Image.new("RGBA", (width, height), (8, 7, 9, 255))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 11)
        header_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 12)
    except Exception:
        font = ImageFont.load_default()
        header_font = font

    draw.text((margin, 2), f"Sauriil Dark Archive v0.0.2 — {size}px contact sheet", fill=(220, 202, 156, 255), font=header_font)

    for index, source in enumerate(sources):
        ensure_inside_repo(root, source)
        row = index // cols
        col = index % cols
        px = margin + col * cell
        py = margin + row * (cell + label_h)
        draw.rounded_rectangle([px, py, px + cell - 8, py + cell - 8], radius=10, fill=(14, 11, 14, 255), outline=(65, 35, 38, 255), width=1)
        draw_checker(draw, px + 8, py + 8, cell - 24, cell - 24, block=8)
        with Image.open(source).convert("RGBA") as image:
            x = px + (cell - image.width) // 2 - 4
            y = py + (cell - image.height) // 2 - 4
            sheet.alpha_composite(image, (x, y))
        label = source.stem
        draw.text((px + 8, py + cell - 4), label[:28], fill=(230, 220, 202, 255), font=font)

    output.parent.mkdir(parents=True, exist_ok=True)
    ensure_inside_repo(root, output)
    sheet.save(output)
    print(f"WROTE {output.relative_to(root)}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Render v0.0.2 contact sheets from real PNG assets.")
    parser.add_argument("--apply", action="store_true", help="write contact sheets")
    args = parser.parse_args()

    root = repo_root()
    any_sources = False
    for size in SIZES:
        source_dir = root / "source" / "png" / str(size)
        sources = sorted(source_dir.glob("*.png"))
        if not sources:
            print(f"render_contact_sheet: no source assets found in source/png/{size}")
            continue
        any_sources = True
        try:
            render_sheet(root, size, sources, args.apply)
        except ImportError:
            print("render_contact_sheet: Pillow is required when source assets exist", file=sys.stderr)
            return 2
    return 0 if any_sources else 0


if __name__ == "__main__":
    sys.exit(main())
