<!-- codex-memory-scaffold:current-state -->
# Current State

#repo/index #sauriil/v0-0-2

Last reviewed: 2026-10-09 (Claude invocation gate only; asset proof not rerun).

## Agent Toolkit

The [portable toolkit](../.agent/README.md) provides eleven baseline workflows and
one reconciled theme workflow under `skills/`. Stable metadata lives in
[.agent/project.yaml](../.agent/project.yaml); native adapters contain no policy.
Codex uses `.agents/skills/`, `.codex/skills/` provides a compatibility pointer, and
Claude uses `.claude/skills/` plus the AGENTS import in `CLAUDE.md`. Claude loads
`release`, `deploy` and `publish` only on an explicit `/release`, `/deploy` or
`/publish` (`disable-model-invocation: true` in those three adapters).

Mind-Seed is disabled: bounded registry discovery found no matching entry and no
verified memory-scope binding. No mutable memory is stored in Git or written by
this setup. See [bootstrap evidence](../reports/2026-10-07-agent-toolkit-bootstrap.md).

The owner-adopted authorization contract covers ordinary requested source delivery
through merge. Explicit release/archive and target-OS boundaries remain. Retrieve
live Issues and PRs for work state; PR #12 overlaps governance files and was kept
separate during bootstrap. Historical safety proof below is not live qualification;
Issues #1–#8 track existing source/proof/archive concerns.

## Project Purpose

**Sauriil’s theme** is the display name of this Sauriil Dark Archive non-destructive cross-platform icon-theme asset project for Windows 11 and Arch Linux/KDE Plasma. Elder Scrolls gameplay and creative lore remain separate. See the [current project card](project-overview.md) for ownership, commands, tools, lifecycle and gaps.

## Current Release State

- Current documented release: `v0.0.2`.
- `v0.0.2` contains 12 accepted raster source icons and generated Windows ICO/Linux PNG fallback assets.
- Captured release proof records successful structure, mapping, `index.theme`, contact-sheet, Linux dry-run, and asset-generation checks for that release.
- The captured Windows PowerShell dry-run was skipped because PowerShell was unavailable in the validation environment.
- Apply-capable scripts exist, but current proof does not establish live Windows/Linux apply or rollback safety.
- `VERSIONS/` contains intentional release ZIP archives and is protected from routine regeneration.

## Current Known Implementation Gaps

Current source inspection and the GitHub work ledger track these material gaps:

- [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2): Linux install can mutate the user theme before all required desktop-override inputs are validated.
- [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3): Windows apply uses repository icon paths instead of the accepted stable user-owned location and does not yet prove lossless rollback for previously absent registry state.
- [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4): apply/rollback safety invariants lack non-destructive regression coverage.
- [#5](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/5): Windows PowerShell dry-run proof still needs capture on a Windows-capable environment.
- [#6](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/6): exporters can fall back to unrelated assets for an unmapped context.
- [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7): mapping validation can overwrite current known-gap evidence with obsolete skeleton-era text.
- [#8](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/8): the protected WinRAR archive change in the current main commit needs provenance review.

Check live Issues and pull requests before relying on this dated snapshot.

## Tooling

- Python scripts for asset conversion, contact-sheet generation, and validation.
- Pillow is required by image-processing scripts when source images are present.
- PowerShell scripts for Windows dry-run, apply, and rollback workflows.
- Bash scripts for Linux dry-run, user-scope install, and rollback workflows.
- CSV mapping manifests for asset and platform routing.
- XDG icon-theme metadata in [../linux/Sauriil-Dark-Archive/index.theme](../linux/Sauriil-Dark-Archive/index.theme).
- No standard package manifest, Makefile, or CI workflow is present.

## Key Folders

- [../docs](.) — active documentation and agent/Obsidian indexes.
- [../DOCUMENTATION](../DOCUMENTATION) — historical handoffs and implementation/research notes.
- [../handoffs](../handoffs) — unfinished-work handoffs.
- [../linux](../linux) — Linux icon-theme output and install/desktop-override staging.
- [../mappings](../mappings) — CSV manifests and platform mapping data.
- [../proof](../proof) — validation evidence and generated proof reports.
- [../reports](../reports) — durable review, planning, and implementation reports.
- [../scripts](../scripts) — conversion, validation, dry-run, apply, and rollback scripts.
- [../source](../source) — source raster assets, generated PNGs, contact sheets, and references.
- [../VERSIONS](../VERSIONS) — intentional release archives.
- [../windows](../windows) — Windows ICO outputs and registry/shortcut staging folders.

## Work State

Repository source/configuration and current verification evidence are technical truth. Current GitHub Issues and pull requests are the operational work ledger. Historical reports and conversations do not prove current implementation or current work status.

## Entry Points

- Root vault index: [../00_Index.md](../00_Index.md)
- Agent workflow: [../AGENTS.md](../AGENTS.md)
- Human docs hub: [INDEX.md](INDEX.md)
- Agent guide: [agent-index.md](agent-index.md)
- Machine index: [agent-index.json](agent-index.json)
- Contribution policy: [../CONTRIBUTING.md](../CONTRIBUTING.md)
- Security policy: [../SECURITY.md](../SECURITY.md)
- Support policy: [../SUPPORT.md](../SUPPORT.md)

## Command Boundary

Current continuation material is indexed under [handoffs/INDEX.md](../handoffs/INDEX.md), including the existing NightTab export gate. The [2026-09-09 orientation report](../reports/2026-09-09-project-orientation.md) is the durable handoff for this completed local task.

## Owner Decisions

- Live Windows apply, Linux install, and rollback apply behavior are not proven by current proof reports.
- Some historical docs under `DOCUMENTATION/` may use skeleton-era wording.
- No package manifest or CI workflow exists, so verification is script and docs driven.
- Release archives remain protected; historical archive observations are not a current dirty-state assertion.
- Linux apply can partially replace the user theme before dependency/mapping failure; see the project card.
- Current shell PATH lacks Python/Python3 and PowerShell. Existing environment actions are defined, but Python actions are not ready on this PATH.


## NightTab baseline — 2026-09-06

NightTab is researched/planned, not implemented or live-applied. Architecture: **NATIVE_CONFIGURATION_PLUS_SAURIIL_ASSETS**; fork **NOT REQUIRED** for the bounded proposal. Installed/persisted version is 7.3.0; current upstream main is 7.6.0, while AMO/latest GitHub release remains 7.3.0. Personal state remains outside Git. Private SQLite preservation is verified; supported current native export still requires a human step. This is separate from icon releases. See the [report](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md), [integration](../integrations/nighttab/README.md) and [handoff](../handoffs/2026-09-06-nighttab-native-export.md). Earlier no-handoff statements above describe their historical review.
