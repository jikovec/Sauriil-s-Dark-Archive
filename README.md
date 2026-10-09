# Sauriil Dark Archive Icons

Sauriil Dark Archive is a non-destructive cross-platform icon-theme asset project for Windows 11 and Arch Linux/KDE Plasma.

Current version: `v0.0.2`.

## Status

v0.0.2 contains the first real asset batch:

```txt
apps:       sauriil-terminal, sauriil-browser, sauriil-code-editor, sauriil-file-manager
places:     folder, folder-documents, folder-downloads, user-home
mimetypes:  application-zip, application-x-rar, text-x-script, text-x-python
```

Generated outputs include:

- master raster PNGs under `source/master/raster/`
- normalized PNGs under `source/png/<size>/`
- Windows multi-size `.ico` files under `windows/ico/apps/`, `windows/ico/filetypes/`, and `windows/ico/folders/`
- Linux PNG fallbacks under `linux/Sauriil-Dark-Archive/<size>/<context>/`
- v0.0.2 contact sheets under `source/master/contact-sheets/`
- proof reports under `proof/`

The package still does not install or apply icons to the live OS.

## Visual identity

The icon direction is dark fantasy archive-machine utility design: black forged steel, ash parchment, blood-red ritual seals, subtle cyan magical/system glow, restrained pale-gold filigree, occult circular geometry, strong silhouettes, and small-size readability.

The project avoids copied Elder Scrolls, Dark Brotherhood, Aldmeri, Microsoft, KDE, GNOME, Arch, WinRAR, Python, browser, file-manager, editor, and other protected official symbols.

## Safety model

All live-changing scripts are dry-run gated.

- Windows apply script refuses to run without `-Apply`.
- Linux install script refuses to run without `--apply`.
- Registry-related workflows print backup/export plans before any future apply path.
- Linux scripts target only `$HOME/.local/share/icons/Sauriil-Dark-Archive` and `$HOME/.local/share/applications`.
- No script may write to `/usr/share/icons` or `/usr/share/applications`.
- Missing mapped required icons fail validation.

## Validation

Run from the repository root:

```bash
python scripts/convert/normalize_pngs.py --apply
python scripts/convert/export_windows_ico.py --context apps --apply
python scripts/convert/export_windows_ico.py --context filetypes --apply
python scripts/convert/export_windows_ico.py --context folders --apply
python scripts/convert/export_linux_png_fallbacks.py --context apps --apply
python scripts/convert/export_linux_png_fallbacks.py --context mimetypes --apply
python scripts/convert/export_linux_png_fallbacks.py --context places --apply
python scripts/test-render/render_contact_sheet.py --apply
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
```

Optional dry-run checks:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Proof files are written under `proof/`.

## Documentation

Start with:

- `00_Index.md`
- `docs/INDEX.md`
- `docs/agent-index.md`
- `docs/source-map.md`
- `docs/connections.md`
- `docs/v0.0.2-asset-batch.md`
- `proof/v0.0.2-source-asset-inventory.md`
- `proof/v0.0.2-generated-assets.md`
- `proof/v0.0.2-contact-sheet-report.md`
- `proof/v0.0.2-validation-report.md`
- `proof/known-gaps.md`


## Planned NightTab integration

NightTab is a researched new integration surface, separate from v0.0.2 and the candidate v0.0.3 icon batch. See the [integration guide](integrations/nighttab/README.md). No theme has been implemented or live-applied; personal browser state stays private outside Git.
