# Sauriil-s-Dark-Archive

This repo root is configured as an Obsidian vault for project documentation and working context.

## Entry Points
- [README.md](README.md)
- [AGENTS.md](AGENTS.md)

## Project Overview
- [README.md](README.md)
- [docs/project-overview.md](docs/project-overview.md)
- [docs/current-state.md](docs/current-state.md)

## Architecture
- [docs/architecture.md](docs/architecture.md)

## Security And Compliance
- [docs/security-model.md](docs/security-model.md)
- [docs/third-party-risk.md](docs/third-party-risk.md)

## Commands Setup And Operations
- [docs/commands.md](docs/commands.md)

## Testing And Verification
- [docs/testing.md](docs/testing.md)
- [docs/proof-checklist.md](docs/proof-checklist.md)
- [proof/v0.0.2-validation-report.md](proof/v0.0.2-validation-report.md)
- [proof/validation-report.md](proof/validation-report.md)
- [proof/dry-run-report.md](proof/dry-run-report.md)
- [proof/known-gaps.md](proof/known-gaps.md)

## Releases And Changelogs
- [README.md](README.md)
- [docs/v0.0.2-asset-batch.md](docs/v0.0.2-asset-batch.md)

## Reports And Handoffs
- No handoff files are currently present under handoffs/.
- [reports/2026-07-07-memory-workflow-validation.md](reports/2026-07-07-memory-workflow-validation.md)

## Other Existing Notes
- [docs/asset-guidelines.md](docs/asset-guidelines.md)
- [docs/icon-name-mapping.md](docs/icon-name-mapping.md)
- [docs/linux-plan.md](docs/linux-plan.md)
- [docs/rollback.md](docs/rollback.md)
- [docs/v0.0.2-asset-batch.md](docs/v0.0.2-asset-batch.md)
- [docs/windows-plan.md](docs/windows-plan.md)
- [DOCUMENTATION/001 Dark Archive theme WinRAR build.md](<DOCUMENTATION/001 Dark Archive theme WinRAR build.md>)
- [DOCUMENTATION/002 Dark Archive cross-platform ic.md](<DOCUMENTATION/002 Dark Archive cross-platform ic.md>)
- [DOCUMENTATION/003 v0.0.1 skeleton creation.md](<DOCUMENTATION/003 v0.0.1 skeleton creation.md>)

## Working Notes
- [[docs/project-overview|Project overview]]
- [[docs/architecture|Architecture]]
- [[docs/commands|Commands]]
- [[docs/current-state|Current state]]
- [[docs/decisions|Decisions]]
- [[docs/security-model|Security model]]
- [[docs/testing|Testing]]

## Maintenance
- Keep this index additive. Link existing docs instead of moving, renaming, or duplicating them.
- Store handoff notes in handoffs/ and generated review summaries in reports/ when they are useful to keep in the repo.


<!-- codex-memory-scaffold:project-map -->
## Project Map

### Purpose
- Sauriil Dark Archive is a non-destructive cross-platform icon-theme asset project for Windows 11 and Arch Linux/KDE Plasma.

### Apparent Stack
- Python asset/validation scripts.
- PowerShell Windows dry-run/apply/rollback scripts.
- Bash Linux dry-run/apply/rollback scripts.
- No standard package manifest was found during memory validation.

### Key Source And Project Folders
- docs
- DOCUMENTATION
- handoffs
- linux
- mappings
- proof
- reports
- scripts
- source
- VERSIONS
- windows

### Memory Notes
- [[docs/current-state|Current state]]
- [[docs/decisions|Decisions]]
- [[docs/commands|Commands]]
- [[docs/testing|Testing]]
- [[docs/security-model|Security model]]
- handoffs/ for future handoff notes.
- reports/ for future review and validation reports.

### Existing Docs Linked During Setup
- [AGENTS.md](AGENTS.md)
- [README.md](README.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/asset-guidelines.md](docs/asset-guidelines.md)
- [docs/commands.md](docs/commands.md)
- [docs/current-state.md](docs/current-state.md)
- [docs/decisions.md](docs/decisions.md)
- [docs/icon-name-mapping.md](docs/icon-name-mapping.md)
- [docs/linux-plan.md](docs/linux-plan.md)
- [docs/project-overview.md](docs/project-overview.md)
- [docs/proof-checklist.md](docs/proof-checklist.md)
- [docs/rollback.md](docs/rollback.md)
- [docs/security-model.md](docs/security-model.md)
- [docs/testing.md](docs/testing.md)
- [docs/third-party-risk.md](docs/third-party-risk.md)
- [docs/v0.0.2-asset-batch.md](docs/v0.0.2-asset-batch.md)
- [docs/windows-plan.md](docs/windows-plan.md)
- [DOCUMENTATION/001 Dark Archive theme WinRAR build.md](<DOCUMENTATION/001 Dark Archive theme WinRAR build.md>)
- [DOCUMENTATION/002 Dark Archive cross-platform ic.md](<DOCUMENTATION/002 Dark Archive cross-platform ic.md>)
- [DOCUMENTATION/003 v0.0.1 skeleton creation.md](<DOCUMENTATION/003 v0.0.1 skeleton creation.md>)

### Reports And Handoffs
- No handoff files are currently present under handoffs/.
- [reports/2026-07-07-memory-workflow-validation.md](reports/2026-07-07-memory-workflow-validation.md)
- Current release proof reports live under proof/.

### README, Changelogs, And Release Notes
- [README.md](README.md)
- [docs/v0.0.2-asset-batch.md](docs/v0.0.2-asset-batch.md)

### Testing Commands
- See [docs/testing.md](docs/testing.md) and [docs/commands.md](docs/commands.md).
- Validation/proof scripts may append to or rewrite files under proof/.
<!-- /codex-memory-scaffold:project-map -->
