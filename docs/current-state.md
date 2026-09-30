<!-- codex-memory-scaffold:current-state -->
# Current State

#repo/index #sauriil/v0-0-2

Last reviewed: 2026-09-30 against `main@1246dde9fa9956351bfd54fe43ccae2da1217c3a`.

## Project Purpose

Sauriil Dark Archive is a cross-platform icon-theme asset, conversion, platform-output, and proof project for Windows 11 and Arch Linux/KDE Plasma.

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

See [commands.md](commands.md) and [testing.md](testing.md). Conversion/contact-sheet commands can write generated assets; several validators write proof files. Live apply/apply-rollback commands are not repository validation commands and require explicit authorization.

## Owner Decisions

The repository currently has no selected license, Code of Conduct, or published private vulnerability-reporting route. These decisions are tracked in [#11](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/11).
