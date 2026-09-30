# Proof Checklist

This checklist distinguishes repository/asset proof from live OS proof. Do not treat a dry-run gate or static token check as evidence that an apply path is transactionally safe.

## v0.0.2 asset validation commands

The documented asset-generation/validation sequence is:

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

These commands mutate generated assets and/or proof. Run them only when regeneration is intended.

Known current defects affect how this sequence must be interpreted:
- exporter fallback behavior: [#6](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/6);
- `validate_mappings.py` can overwrite `proof/known-gaps.md` with obsolete skeleton wording: [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7).

Until #7 is fixed, inspect any `known-gaps.md` change explicitly rather than accepting it as generated truth.

## Script dry-run proof

Linux:

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Windows, where PowerShell is available:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

Dry-run proof may write files under `proof/` but must not modify live registry, shortcuts, system directories, or installed theme state.

The captured v0.0.2 validation skipped the Windows planner because PowerShell was unavailable. Fresh Windows-capable proof is tracked in [#5](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/5).

## Structural proof limits

`validate_structure.py` checks required structure and the presence of apply-gate tokens. It does not prove safe ordering, backup completeness, stable icon storage, or rollback recoverability. Non-destructive behavioral coverage is tracked in [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).

## Live Windows proof

Not established by the current release proof set.

Before any future live Windows proof:
- resolve or explicitly account for [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3);
- use explicit authorization;
- capture pre-apply state/backup, action, readback, and rollback evidence.

## Live Linux proof

Not established by the current release proof set.

Before any future live Linux proof:
- resolve or explicitly account for [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2);
- use explicit authorization;
- capture preflight, action, readback, and rollback evidence.

## Contact Sheet Proof

The documented v0.0.2 contact sheets are under `source/master/contact-sheets/`; the 48px sheet is the primary visual-identity proof size.

## Evidence Reporting

For every check, record the exact revision/environment where material and one of:

```text
passed
failed
blocked
unavailable
not applicable
not run
```

Never convert an unavailable or skipped check into a pass.
