<!-- codex-memory-scaffold:decisions -->
# Decisions

#repo/decision #sauriil/theme

## Active Decisions

- Preserve the project as a non-destructive asset/conversion/proof package unless the user explicitly asks for live OS apply behavior.
- Keep Windows changes native-first and backup-first; registry-backed changes require explicit apply mode and rollback proof.
- Keep Linux installation user-scoped under `$HOME/.local/share/icons/Sauriil-Dark-Archive`; scripts must not write to `/usr/share`.
- Use raster PNG fallbacks for `v0.0.2` instead of wrapping raster art in fake scalable SVG files.
- Avoid copied official symbols or protected product marks; use original Sauriil Dark Archive icon concepts.
- Keep Obsidian integration local-first and plaintext; `.obsidian/` remains ignored.
- Use [agent-index.json](agent-index.json) as the canonical machine-readable agent index; omit `.agents/index.json` until the repo has a real `.agents/` convention.
- Keep this decision log in `docs/decisions.md`; omit `docs/adr/` until decisions become large enough to need separate records.

## Decision Log

### 2026-07-09 - Documentation And Agent Indexing System

- Context: The repo already had a lightweight memory scaffold but lacked complete docs navigation, Obsidian guidance, source maps, connection maps, report/handoff indexes, and a machine-readable agent index.
- Decision: Build the complete docs/indexing layer using GitHub-compatible Markdown, local Obsidian tags, and `docs/agent-index.json`.
- Consequences: Future agents have a deterministic start path, and docs can be browsed as an Obsidian vault without tracking private `.obsidian/` state.
- References: [../reports/obsidian-agent-indexing-plan.md](../reports/obsidian-agent-indexing-plan.md), [../reports/2026-07-09-docs-indexing-implementation.md](../reports/2026-07-09-docs-indexing-implementation.md)

## Template

### YYYY-MM-DD - Decision Title

- Context:
- Decision:
- Consequences:
- References:

## Linked Decision Sources

- [../README.md](../README.md)
- [v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- [windows-plan.md](windows-plan.md)
- [linux-plan.md](linux-plan.md)
- [asset-guidelines.md](asset-guidelines.md)
- [obsidian.md](obsidian.md)
- [../proof/known-gaps.md](../proof/known-gaps.md)
