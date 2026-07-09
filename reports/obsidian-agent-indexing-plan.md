# Obsidian And Agent Indexing Plan

#agent/report #repo/index #obsidian/local

Date: 2026-07-09

## Summary

Build a complete documentation, local Obsidian, repo-indexing, and future-agent orientation system for Sauriil Dark Archive while preserving runtime behavior.

## Current State

- Existing memory scaffold: `AGENTS.md`, `00_Index.md`, `docs/current-state.md`, `docs/decisions.md`, `docs/commands.md`, `docs/testing.md`, and `docs/security-model.md`.
- Existing proof surfaces: `proof/v0.0.2-validation-report.md`, generated asset reports, dry-run reports, and known gaps.
- Existing source surfaces: `source/`, `mappings/`, `windows/`, `linux/`, and `scripts/`.
- Missing before implementation: docs hub, Obsidian guide, source map, connection map, report/handoff indexes, roadmap, and machine-readable agent index.

## Planned Artifact Set

- Update root orientation: `AGENTS.md`, `00_Index.md`, `README.md`.
- Update active docs: `docs/current-state.md`, `docs/project-overview.md`, `docs/architecture.md`, `docs/commands.md`, `docs/testing.md`, `docs/security-model.md`, `docs/decisions.md`.
- Create docs: `docs/INDEX.md`, `docs/development.md`, `docs/deployment.md`, `docs/obsidian.md`, `docs/agent-index.md`, `docs/source-map.md`, `docs/connections.md`, `docs/roadmap.md`.
- Create indexes: `reports/INDEX.md`, `handoffs/INDEX.md`, `docs/agent-index.json`.
- Correct confirmed stale proof wording in `proof/known-gaps.md`.
- Omit `.agents/index.json` and `docs/adr/` because this repo has no `.agents/` convention and `docs/decisions.md` is enough for current decision volume.

## Rules

- Preserve runtime/product behavior.
- Do not run proof generators unless proof regeneration is in scope.
- Do not run apply-capable commands without explicit user request.
- Do not edit `VERSIONS/` release archives.
- Keep `.obsidian/` ignored and local-only.
- Use GitHub-compatible Markdown as canonical committed docs.

## Verification Plan

- `git status --short`
- `git diff --check`
- `python -m json.tool docs/agent-index.json`
- PowerShell Markdown link scan over changed Markdown files

## Implementation Prompt

Implement the approved docs/indexing system from this report. Re-check current repo state before editing. Prefer the complete artifact set, but omit or merge artifacts only when they are redundant, harmful, stale, or inconsistent with repo conventions, and explain every omission. Preserve runtime behavior, avoid cloud/account/encryption setup, keep `.obsidian/` ignored, add or update `docs/agent-index.json`, run safe verification, and produce a final implementation report.
