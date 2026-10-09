<!-- codex-memory-scaffold:architecture -->
# Architecture

#repo/architecture #sauriil/theme #sauriil/assets

## System Shape

The repository is an asset pipeline and proof package, not an application runtime. It has four main layers:

- Source assets: accepted raster masters in [source/master/raster](../source/master/raster), reference notes in [source/references](../source/references), and generated normalized PNGs in [source/png](../source/png).
- Mapping data: CSV manifests in [mappings](../mappings) define which assets are required, which platform context they belong to, and which planned Windows/Linux targets they map to.
- Platform outputs: Windows ICO files in [windows/ico](../windows/ico) and Linux XDG icon-theme files in [linux/Sauriil-Dark-Archive](../linux/Sauriil-Dark-Archive).
- Proof and documentation: validation scripts write evidence under [proof](../proof), while durable planning and implementation reports live under [reports](../reports).

## Pipeline

1. Source art is accepted under `source/master/raster`.
2. [mappings/icon-assets.csv](../mappings/icon-assets.csv) routes assets to Windows and Linux contexts.
3. Python conversion scripts generate normalized PNG, Windows ICO, and Linux PNG fallback outputs.
4. Validation scripts check required files, mapping references, unsafe paths, and `index.theme` structure.
5. Dry-run scripts document planned Windows and Linux actions without applying live OS changes.

## Platform Boundaries

- Windows support is native-first and backup-first. Apply paths are gated by `-Apply` and focus on selected shortcut, file type, and registry-backed plans.
- Linux support is user-scoped. Apply paths are gated by `--apply` and target `$HOME/.local/share/icons/Sauriil-Dark-Archive` and `$HOME/.local/share/applications`.
- No script should write to `/usr/share`, and no Windows registry change should happen during normal documentation or proof work.

## Key References

- Current release: [v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- Source map: [source-map.md](source-map.md)
- Connection map: [connections.md](connections.md)
- Commands: [commands.md](commands.md)
- Validation evidence: [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)

## Known Limits

- There is no package manifest, Makefile, CI workflow, or unit-test framework.
- `v0.0.2` uses raster PNG fallbacks and does not include true scalable SVG assets.
- Live OS apply and rollback behavior must be re-inspected before any future apply-capable run.


## Planned NightTab surface

[NightTab](../integrations/nighttab/README.md) remains the upstream runtime. Sauriil owns generic visual tokens, original assets and integration documentation; Aetheris UI is not the authority. Private configuration/exports remain outside the repository under `$HOME/.local/share/nighttab/`. Native configuration plus assets is selected; no fork required for the bounded design. No theme implementation or live application is claimed. See the [architecture evidence](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md).
