<!-- codex-memory-scaffold:architecture -->
# Architecture

#repo/architecture #sauriil/theme #sauriil/assets

## System Shape

The repository is an asset pipeline and proof package, not an application runtime. It has four main layers:

- Source assets: accepted raster masters in [source/master/raster](../source/master/raster), reference notes in [source/references](../source/references), and generated normalized PNGs in [source/png](../source/png).
- Mapping data: CSV manifests in [mappings](../mappings) define required assets, platform contexts, and planned Windows/Linux targets.
- Platform outputs: Windows ICO files in [windows/ico](../windows/ico) and Linux XDG icon-theme files in [linux/Sauriil-Dark-Archive](../linux/Sauriil-Dark-Archive).
- Proof and documentation: validation scripts write evidence under [proof](../proof); durable planning/review reports live under [reports](../reports).

## Pipeline

1. Source art is accepted under `source/master/raster`.
2. [mappings/icon-assets.csv](../mappings/icon-assets.csv) routes assets to Windows and Linux contexts.
3. Python conversion scripts generate normalized PNG, Windows ICO, and Linux PNG fallback outputs.
4. Validation scripts check repository structure, mapping references, and `index.theme` structure.
5. Dry-run scripts document planned platform actions without intentionally applying live OS changes.
6. Apply/rollback scripts are a separate live-mutation boundary and require explicit authorization.

## Platform Boundaries

Accepted target constraints:
- Windows is native-first and backup-first; registry-backed targets should use stable user-owned icon storage and recoverable pre-apply state.
- Linux is user-scoped under `$HOME/.local/share/icons/Sauriil-Dark-Archive` and `$HOME/.local/share/applications`; system-wide `/usr/share` writes are out of scope.

Current implementation does not yet satisfy every accepted safety invariant. See [current-state.md](current-state.md), [security-model.md](security-model.md), and live Issues [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2) and [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).

## State And Trust Boundaries

- Generated assets are intentionally tracked as repository outputs/proof inputs.
- `VERSIONS/` contains intentional release/history archives and is not disposable build output.
- `proof/` contains evidence, but proof is valid only for the recorded revision/command/environment.
- GitHub Issues/PRs are the operational work ledger; they are not implementation evidence.

## Key References

- Current release: [v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- Source map: [source-map.md](source-map.md)
- Commands: [commands.md](commands.md)
- Testing/evidence: [testing.md](testing.md)
- Validation evidence: [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)

## Known Limits

- No package manifest, Makefile, CI workflow, or unit-test framework.
- `v0.0.2` uses raster PNG fallbacks and has no true scalable SVG assets.
- Live apply/rollback remains a separately tracked, unproven boundary.
