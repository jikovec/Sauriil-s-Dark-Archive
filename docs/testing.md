<!-- codex-memory-scaffold:testing -->
# Testing

#repo/testing #sauriil/proof

## Verification Layers

- Docs-only verification: whitespace, JSON validity, and Markdown link checks.
- Static asset proof: `validate_structure.py`, `validate_mappings.py`, and `validate_index_theme.py`.
- Regeneration proof: conversion and contact-sheet commands that write generated assets.
- Dry-run proof: Windows and Linux planners that document planned changes without applying them.

## Docs-Only Checks

Use these when only documentation or indexes changed:

```powershell
git diff --check
python -m json.tool docs/agent-index.json
```

Run a Markdown link scan over changed `.md` files. Links are resolved relative to the containing file, not the repository root.

## Asset And Proof Checks

Use these only when regenerating assets or proof evidence is intended:

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

Expected result: generated assets exist, mapping rows point only to existing required assets, `linux/Sauriil-Dark-Archive/index.theme` is structurally valid, and no live OS install/apply action occurs.

## Dry-Run Proof

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Expected result: commands write or print planned changes only. No registry write, shortcut change, `/usr/share` write, or install occurs.

## Current Evidence

- [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md) records passing `v0.0.2` structure, mapping, `index.theme`, contact sheet, and dry-run safety checks.
- [../proof/known-gaps.md](../proof/known-gaps.md) records remaining release gaps.
- [../reports/2026-07-09-docs-indexing-implementation.md](../reports/2026-07-09-docs-indexing-implementation.md) records docs/indexing verification for the local Obsidian and agent-orientation system.

## Notes

- There is no separate unit-test framework or package manifest.
- Proof commands can mutate files under `proof/`; do not run them during a docs-only pass unless proof regeneration is explicitly part of the task.

## Agent Toolkit Checks

```bash
python3 scripts/validate/validate_agent_toolkit.py
python3 -m json.tool docs/agent-index.json
git diff --check
```

The toolkit check reads files only and uses Python 3's standard library. It checks
constrained JSON-compatible YAML metadata/frontmatter, required files, thin adapter
parity, repository-relative links and routing-example coverage. It does not prove
provider discovery, model routing behavior, visual acceptance or live safety.
