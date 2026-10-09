# Connection Map

#repo/connection-map #sauriil/theme

## Docs To Source

- [architecture.md](architecture.md) explains the source, mapping, output, and proof layers.
- [source-map.md](source-map.md) links source folders, generated outputs, mapping files, scripts, and proof reports.
- [development.md](development.md) routes asset work through source assets, mappings, conversion scripts, and proof updates.

## Source To Tests

- `source/master/raster` and `mappings/icon-assets.csv` connect to `scripts/convert/normalize_pngs.py`, `scripts/convert/export_windows_ico.py`, and `scripts/convert/export_linux_png_fallbacks.py`.
- `linux/Sauriil-Dark-Archive/index.theme` connects to `scripts/validate/validate_index_theme.py`.
- Mapping CSVs connect to `scripts/validate/validate_mappings.py`.
- Repository structure and required release files connect to `scripts/validate/validate_structure.py`.

## Proof To Release

- [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md) is the current validation summary.
- [../proof/v0.0.2-generated-assets.md](../proof/v0.0.2-generated-assets.md) documents generated assets.
- [../proof/v0.0.2-contact-sheet-report.md](../proof/v0.0.2-contact-sheet-report.md) documents visual proof outputs.
- [../proof/known-gaps.md](../proof/known-gaps.md) documents what `v0.0.2` does not prove.
- [../VERSIONS](../VERSIONS) contains release archives and should not be changed without explicit request.

## Decisions To Files

- Non-destructive project boundary: [decisions.md](decisions.md), [security-model.md](security-model.md), [deployment.md](deployment.md), `scripts/apply/`, `scripts/rollback/`.
- Raster fallback decision: [decisions.md](decisions.md), [asset-guidelines.md](asset-guidelines.md), [v0.0.2-asset-batch.md](v0.0.2-asset-batch.md).
- Obsidian local-only decision: [decisions.md](decisions.md), [obsidian.md](obsidian.md), [../.gitignore](../.gitignore).

## Reports And Handoffs

- [../reports/INDEX.md](../reports/INDEX.md) lists durable reports.
- [../handoffs/INDEX.md](../handoffs/INDEX.md) defines handoff conventions.
- Reports should link to implemented changes, proof evidence, skipped checks, and known risks.
- Handoffs should link to remaining work, blockers, and the docs/source/proof files needed to resume safely.

## Machine And Human Indexes

- Human root hub: [../00_Index.md](../00_Index.md).
- Docs hub: [INDEX.md](INDEX.md).
- Agent guide: [agent-index.md](agent-index.md).
- Machine index: [agent-index.json](agent-index.json).


## NightTab ownership and preservation

[Existing identity and assets](asset-guidelines.md) inform the [NightTab specification](../integrations/nighttab/docs/visual-specification.md). [Research evidence](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md) routes to the [implementation plan](../integrations/nighttab/docs/implementation-plan.md) and [export handoff](../handoffs/2026-09-06-nighttab-native-export.md). Runtime belongs to upstream NightTab; generic visual material belongs to Sauriil; personal exports/configuration remain external and private.
