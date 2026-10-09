<!-- codex-memory-scaffold:commands -->
# Commands

#repo/development #repo/testing #sauriil/proof

Run commands from the repository root. There is no package manifest, Makefile, or CI workflow.

## Docs-Safe Checks

Use these for documentation/governance work in a local checkout:

```bash
git status --short --branch
git diff --check
python -m json.tool docs/agent-index.json
```

Run a Markdown relative-link scan over changed documentation. Resolve links relative to the containing file.

## Asset Conversion

These commands write generated assets only when `--apply` is present:

```bash
python scripts/convert/normalize_pngs.py --apply
python scripts/convert/export_windows_ico.py --context apps --apply
python scripts/convert/export_windows_ico.py --context filetypes --apply
python scripts/convert/export_windows_ico.py --context folders --apply
python scripts/convert/export_linux_png_fallbacks.py --context apps --apply
python scripts/convert/export_linux_png_fallbacks.py --context mimetypes --apply
python scripts/convert/export_linux_png_fallbacks.py --context places --apply
python scripts/test-render/render_contact_sheet.py --apply
```

Pillow is required when image sources are present.

Current exporter behavior has a tracked context-fallback defect for unmapped contexts; see [#6](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/6).

## Validation And Proof Generation

```bash
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
```

These are not pure read-only tests: validators can append to or rewrite files under `proof/`.

Known limitation: `validate_mappings.py` currently overwrites `proof/known-gaps.md` with obsolete skeleton-era wording. See [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7). Do not treat a newly regenerated `known-gaps.md` as trustworthy without reconciling that defect.

Also, `validate_structure.py` checks for apply-gate tokens; that check is not behavioral proof of safe apply/rollback ordering or recoverability. See [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).

## Dry-Run Planners

Windows, on a Windows/PowerShell-capable environment:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

Linux:

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Dry-run scripts may write proof files but should not perform live OS changes. The captured v0.0.2 proof did not execute the Windows PowerShell planner; see [#5](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/5).

## Apply-Capable Commands

These modify user/OS state and are not repository validation commands. Do not run them without explicit authorization:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/apply/windows_apply_icons.ps1 -Apply
```

```bash
bash scripts/apply/linux_install_user_theme.sh --apply
```

Current Linux and Windows apply implementations have tracked safety gaps: [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2) and [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).

## Rollback Commands

Dry-run rollback:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1
```

```bash
bash scripts/rollback/linux_rollback_user_theme.sh
```

Apply rollback requires explicit authorization:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/rollback/windows_rollback_icons.ps1 -Apply
```

```bash
bash scripts/rollback/linux_rollback_user_theme.sh --apply
```

## Routing

- Asset changes: use [development.md](development.md), then regenerate proof only when intended.
- Documentation-only changes: use docs-safe checks and link validation.
- Release archive work: do not modify `VERSIONS/` unless requested.
- Live OS apply or rollback: re-read [security-model.md](security-model.md), [deployment.md](deployment.md), and the exact script before running anything.

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
