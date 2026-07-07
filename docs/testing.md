<!-- codex-memory-scaffold:testing -->
# Testing

## Explicit Or Discovered Test And Check Commands
- python scripts/convert/normalize_pngs.py --apply
- python scripts/convert/export_windows_ico.py --context apps --apply
- python scripts/convert/export_windows_ico.py --context filetypes --apply
- python scripts/convert/export_windows_ico.py --context folders --apply
- python scripts/convert/export_linux_png_fallbacks.py --context apps --apply
- python scripts/convert/export_linux_png_fallbacks.py --context mimetypes --apply
- python scripts/convert/export_linux_png_fallbacks.py --context places --apply
- python scripts/test-render/render_contact_sheet.py --apply
- python scripts/validate/validate_structure.py
- python scripts/validate/validate_mappings.py
- python scripts/validate/validate_index_theme.py
- python scripts/validate/generate_dry_run_report.py

Expected result: generated assets exist, mapping rows point only to existing required assets, linux/Sauriil-Dark-Archive/index.theme is structurally valid, and no live OS install/apply action occurs.

## Dry-Run Proof Commands
- powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
- bash scripts/dry-run/linux_plan_install.sh

Expected result: commands print or write planned changes only. No registry write, no `/usr/share` write, and no install occurs.

## Inferred Commands
- No inferred test commands were added.

## Verification Notes
- Commands listed above were discovered in README.md, docs/proof-checklist.md, and the scripts directory.
- There is no separate unit-test framework or package manifest in the inspected repo root.
- Validation/proof commands mutate files under proof/; use them when proof regeneration is acceptable.
- During the 2026-07-07 memory validation, these commands were statically verified but not run because the task was documentation-memory validation only.
