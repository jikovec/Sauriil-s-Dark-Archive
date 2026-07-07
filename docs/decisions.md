<!-- codex-memory-scaffold:decisions -->
# Decisions

## Active Decisions
- Preserve the project as a non-destructive asset/conversion/proof package unless the user explicitly asks for live OS apply behavior.
- Keep Windows changes native-first and backup-first; registry-backed changes require explicit apply mode and rollback proof.
- Keep Linux installation user-scoped under `$HOME/.local/share/icons/Sauriil-Dark-Archive`; scripts must not write to `/usr/share`.
- Use raster PNG fallbacks for v0.0.2 instead of wrapping raster art in fake scalable SVG files.
- Avoid copied official symbols or protected product marks; use original Sauriil Dark Archive icon concepts.

## Decision Log
Add future decisions here using this structure:

### YYYY-MM-DD - Decision Title
- Context:
- Decision:
- Consequences:
- References:

## Linked Decision Records
- [README.md](../README.md)
- [docs/v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- [docs/windows-plan.md](windows-plan.md)
- [docs/linux-plan.md](linux-plan.md)
- [docs/asset-guidelines.md](asset-guidelines.md)
- [proof/known-gaps.md](../proof/known-gaps.md)
