<!-- codex-memory-scaffold:commands -->
# Commands

#repo/development #repo/testing #sauriil/proof

Run commands from the repository root. There is no package manifest, Makefile, or CI workflow.

## Docs-Safe Checks

These are appropriate for documentation-only work:

```powershell
git status --short
git diff --check
python -m json.tool docs/agent-index.json
```

Use a Markdown link scan after editing docs. The implementation report in [../reports/2026-07-09-docs-indexing-implementation.md](../reports/2026-07-09-docs-indexing-implementation.md) records the local scan shape used for this docs pass.

## Asset Conversion And Proof Generation

These commands are documented by [README.md](../README.md) and [proof-checklist.md](proof-checklist.md). They can write generated assets or proof files.

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

Expected scope: project files only. Conversion/contact-sheet commands write generated assets when `--apply` is present. Validation and dry-run proof commands can append to or rewrite files under `proof/`.

## Dry-Run Planners

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Expected scope: write or print plans only. No live registry write, shortcut change, icon cache refresh, install, or `/usr/share` write should occur.

## Apply-Capable Commands

Do not run these without an explicit user request:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/apply/windows_apply_icons.ps1 -Apply
```

```bash
bash scripts/apply/linux_install_user_theme.sh --apply
```

## Rollback Commands

Dry-run rollback:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1
```

```bash
bash scripts/rollback/linux_rollback_user_theme.sh
```

Apply rollback, only with explicit user request:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1 -Apply
```

```bash
bash scripts/rollback/linux_rollback_user_theme.sh --apply
```

## Command Routing

- Asset changes: use [development.md](development.md), then regenerate proof only when intended.
- Documentation-only changes: use docs-safe checks and link validation.
- Release archive work: do not modify `VERSIONS/` unless requested.
- Live OS apply or rollback: re-read [security-model.md](security-model.md), [deployment.md](deployment.md), and the exact script before running anything.
