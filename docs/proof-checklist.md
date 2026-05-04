# Proof Checklist

## v0.0.2 validation

Run:

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

Expected result: generated assets exist, mappings point only to existing required assets, `index.theme` is structurally valid, and no system install/apply action occurs.

## Script dry-run proof

Run where available:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

Run:

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Expected result: commands print planned changes only. No registry write, no `/usr/share` write, and no install occurs.

## Package contents proof

Check:

```bash
python scripts/validate/generate_dry_run_report.py
```

Expected result: `proof/package-manifest.txt` and `proof/known-gaps.md` are regenerated and required mapping gaps are zero.

## Windows no-live-registry-modification proof

Only dry-run scripts are executed during validation. The apply script refuses without `-Apply`, and no `.reg` export from the live machine is bundled.

## Linux no-system-directory-modification proof

Only dry-run scripts are executed during validation. The Linux install script refuses without `--apply` and contains explicit `/usr/share` refusal checks.

## Contact sheet proof

Confirm these files exist:

```txt
source/master/contact-sheets/v0.0.2-contact-sheet-16.png
source/master/contact-sheets/v0.0.2-contact-sheet-24.png
source/master/contact-sheets/v0.0.2-contact-sheet-32.png
source/master/contact-sheets/v0.0.2-contact-sheet-48.png
source/master/contact-sheets/v0.0.2-contact-sheet-256.png
```

The 48px sheet is the visual identity proof sheet.

## Known gap proof

`proof/known-gaps.md` must state that v0.0.2 is not installed/applied to the live OS and that no SVG scalable icons exist yet.
