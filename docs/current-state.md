<!-- codex-memory-scaffold:current-state -->
# Current State

## Project Purpose
- Sauriil Dark Archive is a non-destructive cross-platform icon-theme asset project for Windows 11 and Arch Linux/KDE Plasma.

## Apparent Stack
- Python scripts for asset conversion, contact sheet generation, and validation.
- PowerShell scripts for Windows dry-run, apply, and rollback workflows.
- Bash scripts for Linux dry-run, user-scope install, and rollback workflows.
- No standard package manifest, Makefile, or CI workflow was discovered in the inspected repo root.

## Key Folders
- docs
- DOCUMENTATION
- handoffs
- linux
- mappings
- proof
- reports
- scripts
- source
- VERSIONS
- windows

## Manifest And Config Files
- No standard package manifest or CI config was discovered.
- [.gitignore](../.gitignore) ignores the local Obsidian settings directory.
- Key theme config: [linux/Sauriil-Dark-Archive/index.theme](../linux/Sauriil-Dark-Archive/index.theme)

## Key Mapping Files
- [mappings/icon-assets.csv](../mappings/icon-assets.csv)
- [mappings/windows-shortcuts.csv](../mappings/windows-shortcuts.csv)
- [mappings/windows-filetypes.csv](../mappings/windows-filetypes.csv)
- [mappings/windows-drives.csv](../mappings/windows-drives.csv)
- [mappings/linux-desktop-icons.csv](../mappings/linux-desktop-icons.csv)
- [mappings/linux-mimetypes.csv](../mappings/linux-mimetypes.csv)
- [mappings/linux-standard-names.csv](../mappings/linux-standard-names.csv)

## Important Docs And Reports
- [AGENTS.md](../AGENTS.md)
- [README.md](../README.md)
- [docs/architecture.md](architecture.md)
- [docs/asset-guidelines.md](asset-guidelines.md)
- [docs/commands.md](commands.md)
- [docs/current-state.md](current-state.md)
- [docs/decisions.md](decisions.md)
- [docs/icon-name-mapping.md](icon-name-mapping.md)
- [docs/linux-plan.md](linux-plan.md)
- [docs/project-overview.md](project-overview.md)
- [docs/proof-checklist.md](proof-checklist.md)
- [docs/rollback.md](rollback.md)
- [docs/security-model.md](security-model.md)
- [docs/testing.md](testing.md)
- [docs/third-party-risk.md](third-party-risk.md)
- [docs/v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- [docs/windows-plan.md](windows-plan.md)
- [proof/v0.0.2-source-asset-inventory.md](../proof/v0.0.2-source-asset-inventory.md)
- [proof/v0.0.2-generated-assets.md](../proof/v0.0.2-generated-assets.md)
- [proof/v0.0.2-contact-sheet-report.md](../proof/v0.0.2-contact-sheet-report.md)
- [proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)
- [proof/validation-report.md](../proof/validation-report.md)
- [proof/dry-run-report.md](../proof/dry-run-report.md)
- [proof/known-gaps.md](../proof/known-gaps.md)
- [reports/2026-07-07-memory-workflow-validation.md](../reports/2026-07-07-memory-workflow-validation.md)
- [DOCUMENTATION/001 Dark Archive theme WinRAR build.md](<../DOCUMENTATION/001 Dark Archive theme WinRAR build.md>)
- [DOCUMENTATION/002 Dark Archive cross-platform ic.md](<../DOCUMENTATION/002 Dark Archive cross-platform ic.md>)
- [DOCUMENTATION/003 v0.0.1 skeleton creation.md](<../DOCUMENTATION/003 v0.0.1 skeleton creation.md>)

## Important Commands Found
- python scripts/convert/normalize_pngs.py --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_windows_ico.py --context apps --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_windows_ico.py --context filetypes --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_windows_ico.py --context folders --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_linux_png_fallbacks.py --context apps --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_linux_png_fallbacks.py --context mimetypes --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/convert/export_linux_png_fallbacks.py --context places --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/test-render/render_contact_sheet.py --apply - explicit README command, source: README.md; detail: README documented command
- python scripts/validate/validate_structure.py - explicit README command, source: README.md; detail: README documented command
- python scripts/validate/validate_mappings.py - explicit README command, source: README.md; detail: README documented command
- python scripts/validate/validate_index_theme.py - explicit README command, source: README.md; detail: README documented command
- python scripts/validate/generate_dry_run_report.py - explicit README command, source: README.md; detail: README documented command
- powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1 - explicit README/proof-checklist dry-run command
- bash scripts/dry-run/linux_plan_install.sh - explicit README/proof-checklist dry-run command
- powershell -ExecutionPolicy Bypass -File scripts/apply/windows_apply_icons.ps1 -Apply - apply-capable Windows command; do not run without explicit user request
- bash scripts/apply/linux_install_user_theme.sh --apply - apply-capable Linux command; do not run without explicit user request
- powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1 [-Apply] - rollback command; dry-run by default
- bash scripts/rollback/linux_rollback_user_theme.sh [--apply] - rollback command; dry-run by default

## Current Release State
- Current documented version is v0.0.2.
- v0.0.2 contains 12 accepted raster source icons and generated Windows ICO/Linux PNG fallback assets.
- Existing proof reports record passing structure, mapping, index.theme, contact sheet, and dry-run safety checks.
- The package still does not install or apply icons to the live OS by default.
- `VERSIONS/` contains release ZIP archives; do not edit or regenerate them unless explicitly requested.

## Open Unknowns
- No existing handoff files were present under handoffs/ during the 2026-07-07 memory validation.
- Runtime apply behavior was not executed during the 2026-07-07 memory validation.
- Validation/proof scripts append to or rewrite proof files, so treat them as mutating checks.
- Some older planning text may still use skeleton-era wording; prefer README.md, docs/v0.0.2-asset-batch.md, and proof/v0.0.2-validation-report.md for current release facts.
