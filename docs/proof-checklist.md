# Proof Checklist

## Skeleton validation

Run:

```bash
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
```

Expected result: all required directories and files exist, `index.theme` is structurally valid, mapping CSVs contain safe example rows, and no final icon art is present.

## Script dry-run proof

Run:

```powershell
pwsh ./scripts/dry-run/windows_plan_changes.ps1
```

Run:

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Expected result: commands print planned changes only. No registry write, no `/usr/share` write, and no install occurs.

## Package contents proof

Check:

```bash
find . -type f | sort > proof/package-manifest.txt
```

Expected result: package contains docs, mapping CSVs, scripts, `.gitkeep` files, proof files, and `index.theme`; no PNG/SVG/ICO/CUR image assets.

## Windows no-live-registry-modification proof

Only dry-run scripts are executed during skeleton validation. The apply script refuses without `-Apply`, and no `.reg` export from the live machine is bundled.

## Linux no-system-directory-modification proof

Only dry-run scripts are executed during skeleton validation. The Linux install script refuses without `--apply` and contains explicit `/usr/share` refusal checks.

## Apply-gated script proof

Inspect:

- `scripts/apply/windows_apply_icons.ps1`
- `scripts/apply/linux_install_user_theme.sh`
- `scripts/rollback/windows_rollback_icons.ps1`
- `scripts/rollback/linux_rollback_user_theme.sh`

Expected result: live-changing behavior requires explicit apply mode.

## Known gap proof

`proof/known-gaps.md` must state that missing icon assets are expected gaps for the next phase.
