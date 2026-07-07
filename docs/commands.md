<!-- codex-memory-scaffold:commands -->
# Commands

## Discovered Commands
Run commands from the repository root.

### Asset conversion and proof generation

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

These commands are not no-op tests. Conversion/contact-sheet commands write generated assets when passed `--apply`. Validation and dry-run proof commands append to or rewrite files under proof/.

### Dry-run planners

- powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1 - writes proof/windows-dry-run.md; does not modify live Windows registry or shortcuts
- bash scripts/dry-run/linux_plan_install.sh - writes proof/linux-dry-run.md; does not install the theme

### Apply-capable commands

- powershell -ExecutionPolicy Bypass -File scripts/apply/windows_apply_icons.ps1 -Apply - gated Windows registry apply path; do not run without explicit user request
- bash scripts/apply/linux_install_user_theme.sh --apply - gated user-scope Linux install path; do not run without explicit user request

### Rollback commands

- powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1 - Windows rollback dry-run
- powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1 -Apply - imports rollback registry backups; do not run without explicit user request
- bash scripts/rollback/linux_rollback_user_theme.sh - Linux rollback dry-run
- bash scripts/rollback/linux_rollback_user_theme.sh --apply - removes the user-scope theme and mapped desktop overrides; do not run without explicit user request

## Command Sources Inspected
- README.md
- docs/proof-checklist.md
- docs/rollback.md
- scripts/convert/
- scripts/test-render/
- scripts/validate/
- scripts/dry-run/
- scripts/apply/
- scripts/rollback/
- No standard package manifest, Makefile, or CI workflow was found.

## Notes
- explicit means the command came from README.md, project docs, or a script interface.
- inferred means the repository shape suggests the command, but it was not directly declared as a script.
- .env and other secret-bearing files were not read.
- Prefer dry-run planners before any future apply-capable workflow.
- Treat `VERSIONS/` as release archives and avoid regenerating or editing it unless explicitly requested.
