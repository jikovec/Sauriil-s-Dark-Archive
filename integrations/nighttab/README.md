# Sauriil Dark Archive × NightTab

#sauriil/theme #repo/architecture

Status: **researched/planned; no theme implemented or live-applied**.

Architecture: **NATIVE_CONFIGURATION_PLUS_SAURIIL_ASSETS**. Fork: **NOT REQUIRED** for the bounded specification. Native image transport remains a disposable-profile qualification step; essential palette and geometry do not depend on it.

NightTab remains the upstream new-tab runtime. Sauriil owns only original generic design, reusable assets and integration documentation. Aetheris UI is not the NightTab theme authority. This surface is separate from released v0.0.2 icons and the candidate v0.0.3 batch.

- [Baseline and architecture evidence](../../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md)
- [Proposed visual specification](docs/visual-specification.md)
- [Next implementation and preservation plan](docs/implementation-plan.md)

## Public/private boundary

This directory may contain generic specifications and, in a later task, generic tokens, assets, presets and offline tooling. Personal bookmarks, destinations, labels, search settings, exports, browser profiles and backups must remain outside this repository under `$HOME/.local/share/nighttab/`. Historical exports remain in its `backups/` directory. Never use a personal export as a public preset template.

Only this README and the two justified design/plan documents exist now. Do not create empty `theme/`, `icons/`, `backgrounds/`, `presets/`, `scripts/` or `proof/` scaffolding. Future files and their gates are specified in the implementation plan.

## Preservation gate

A private SQLite snapshot was verified, but a supported current-state native export still requires human action. Do not treat the snapshot or a historical export as that export. See the [handoff](../../handoffs/2026-09-06-nighttab-native-export.md). No browser UI automation, Firefox settings change, extension storage write, import, theme apply or OS installation was performed.
