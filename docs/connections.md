# Connection Map

#repo/connection-map #sauriil/theme

## Docs To Source

- [architecture.md](architecture.md) explains source, mapping, output, proof, and live-mutation boundaries.
- [source-map.md](source-map.md) links source folders, generated outputs, mapping files, scripts, and proof reports.
- [development.md](development.md) routes work through source, mappings, generation, verification, and pull-request delivery.
- [current-state.md](current-state.md) reconciles accepted plans with currently observed implementation gaps.

## Source To Verification

- `source/master/raster` and `mappings/icon-assets.csv` connect to the conversion exporters.
- `linux/Sauriil-Dark-Archive/index.theme` connects to `scripts/validate/validate_index_theme.py`.
- Mapping CSVs connect to `scripts/validate/validate_mappings.py`; its known proof-clobbering defect is tracked in [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7).
- Repository structure connects to `scripts/validate/validate_structure.py`; its apply-gate check is structural/token-level, not behavioral apply-safety proof.
- Live apply/rollback safety work is tracked separately under [#1](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/1).

## Proof To Release

- [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md) is historical validation evidence for the recorded v0.0.2 run.
- [../proof/v0.0.2-generated-assets.md](../proof/v0.0.2-generated-assets.md) documents generated assets.
- [../proof/v0.0.2-contact-sheet-report.md](../proof/v0.0.2-contact-sheet-report.md) documents visual proof outputs.
- [../proof/known-gaps.md](../proof/known-gaps.md) records checked-in current gaps, subject to the #7 regeneration defect.
- [../VERSIONS](../VERSIONS) contains intentional release archives; do not treat it as disposable generated storage.

## Work State

- Current repository source/configuration and verification evidence define technical truth.
- Current GitHub Issues and pull requests define operational work status.
- Historical reports, handoffs, and conversations provide context but do not prove current status.

## Decisions To Files

- Non-destructive boundary: [decisions.md](decisions.md), [security-model.md](security-model.md), [deployment.md](deployment.md), current `scripts/apply/`, current `scripts/rollback/`.
- Raster fallback decision: [decisions.md](decisions.md), [asset-guidelines.md](asset-guidelines.md), [v0.0.2-asset-batch.md](v0.0.2-asset-batch.md).
- Obsidian local-only decision: [decisions.md](decisions.md), [obsidian.md](obsidian.md), [../.gitignore](../.gitignore).

## Reports And Handoffs

- [../reports/INDEX.md](../reports/INDEX.md) lists durable reports.
- [../handoffs/INDEX.md](../handoffs/INDEX.md) defines handoff conventions.

## Machine And Human Indexes

- Human root hub: [../00_Index.md](../00_Index.md).
- Docs hub: [INDEX.md](INDEX.md).
- Agent guide: [agent-index.md](agent-index.md).
- Machine index: [agent-index.json](agent-index.json).


## NightTab ownership and preservation

[Existing identity and assets](asset-guidelines.md) inform the [NightTab specification](../integrations/nighttab/docs/visual-specification.md). [Research evidence](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md) routes to the [implementation plan](../integrations/nighttab/docs/implementation-plan.md) and [export handoff](../handoffs/2026-09-06-nighttab-native-export.md). Runtime belongs to upstream NightTab; generic visual material belongs to Sauriil; personal exports/configuration remain external and private.
