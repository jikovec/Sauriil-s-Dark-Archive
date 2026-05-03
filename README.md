# Sauriil Dark Archive Icons Skeleton

This repository is the first non-destructive skeleton package for the Sauriil Dark Archive cross-platform icon customization project.

It is not a completed icon theme. It contains directory layout, mapping CSVs, dry-run tooling, rollback skeletons, conversion planning scripts, validation scripts, and proof outputs. It intentionally contains no PNG, SVG, ICO, CUR, or sample icon art.

## Purpose

The project prepares a safe asset pipeline for a dark fantasy archive-machine icon identity across:

- Windows 11 native shortcut, folder, desktop icon, selected file type, drive, and tooling workflows.
- Arch Linux with KDE Plasma as the primary Linux target through a per-user XDG icon theme.
- Secondary Linux compatibility notes for GNOME and XFCE.

The visual direction to preserve in future real assets is black forged steel, ash parchment, blood-red ritual seals, subtle cyan system glow, restrained pale-gold filigree, occult circular geometry, strong silhouettes, and readable small-size icons.

## Skeleton status

This package is intentionally incomplete. It does not include real icons, placeholder images, generated sample art, registry exports, system files, installed desktop overrides, or caches.

The Linux theme directory is valid as a skeleton. It declares the intended XDG directories and inherits `breeze,hicolor`, but it has no real icon files yet.

## Safety model

All live-changing scripts are dry-run gated.

- Windows apply script refuses to run without `-Apply`.
- Linux install script refuses to run without `--apply`.
- Registry-related workflows print backup/export plans before any future apply path.
- Linux scripts target only `$HOME/.local/share/icons/Sauriil-Dark-Archive` and `$HOME/.local/share/applications`.
- No script may write to `/usr/share/icons` or `/usr/share/applications`.
- Missing mapped icons are reported as expected gaps unless a row is explicitly marked `required`.

## Intentionally not implemented yet

- No icon art.
- No sample dark-fantasy icons.
- No live system customization.
- No Windows registry edits.
- No Linux system-wide install.
- No 7TSP or Windows system-resource patching.
- No claim that the theme is installed or visually complete.

## Validation

Run from the repository root:

```bash
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
```

Optional dry-run checks:

```powershell
pwsh ./scripts/dry-run/windows_plan_changes.ps1
```

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Proof files are written under `proof/`.

## Adding real icon assets later

1. Add master raster art to `source/master/raster/` or vector art to `source/master/vector/`.
2. Export normalized PNG sizes into `source/png/<size>/` or SVGs into `source/svg/full-color/` and `source/svg/symbolic/`.
3. Generate Windows `.ico` files into `windows/ico/<context>/` using `scripts/convert/export_windows_ico.py --apply`.
4. Generate Linux PNG fallbacks into `linux/Sauriil-Dark-Archive/<size>/<context>/` using `scripts/convert/export_linux_png_fallbacks.py --apply`.
5. Update mapping CSV rows from `example` to `required` only after the referenced real asset exists.
6. Re-run all validation scripts and inspect `proof/known-gaps.md`.
