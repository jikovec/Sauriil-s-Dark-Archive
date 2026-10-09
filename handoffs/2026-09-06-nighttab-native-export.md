# 2026-09-06 — NightTab native export prerequisite

#agent/handoff #sauriil/theme

Status: **BLOCKED_PENDING_HUMAN_NIGHTTAB_EXPORT**.

Baseline/research and architecture are complete; theme implementation/apply was outside this pass. A private integrity-checked SQLite snapshot preserves discovered persisted state, but is not a supported native export or live-page proof.

The remaining human preservation step is **Menu → Data → Backup → Export data** in the existing NightTab page. Save the full JSON under `$HOME/.local/share/nighttab/backups/` with a distinct timestamp. Do not import anything or change the appearance. The next pass must hash, size-check, parse and compare it privately, retain the eight historical exports, and resolve any baseline differences.

Read the [research report](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md), [implementation plan](../integrations/nighttab/docs/implementation-plan.md), [current state](../docs/current-state.md) and [agent guide](../docs/agent-index.md). Exact private artifact receipts are outside Git in the private authority's evidence area.

Architecture: native configuration plus original generic Sauriil assets; no fork required. Target installed Firefox 7.3.0, not current main's 7.6.0 schema. Before any later import, explicitly inspect all category toggles: Settings/Bookmarks/Theme default enabled. Theme-only replaces the complete theme including background and saved themes. Preserve those fields in a private candidate and qualify rollback in a disposable profile.

No publication or live apply was performed. All repository edits remain uncommitted. See the report for check results and inherited whitespace failures.
