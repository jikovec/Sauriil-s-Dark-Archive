# Agent Index

#agent/orientation #repo/index #sauriil/theme

## Start Workflow

1. Inspect the current default branch and run `git status --short --branch` in the working copy you will modify.
2. Read [../README.md](../README.md), [../AGENTS.md](../AGENTS.md), [../00_Index.md](../00_Index.md), [INDEX.md](INDEX.md), [current-state.md](current-state.md), and [decisions.md](decisions.md).
3. Inspect current GitHub Issues and pull requests. Treat them as the operational work ledger, not implementation proof.
4. For command work, read [commands.md](commands.md), [testing.md](testing.md), and [security-model.md](security-model.md).
5. For asset or mapping work, read [source-map.md](source-map.md), [connections.md](connections.md), [asset-guidelines.md](asset-guidelines.md), and [icon-name-mapping.md](icon-name-mapping.md).
6. Inspect [../reports/INDEX.md](../reports/INDEX.md) and [../handoffs/INDEX.md](../handoffs/INDEX.md) for durable context.

## Source-Truth Order

1. Current source/configuration/scripts/mappings/assets and repository state: `scripts/`, `mappings/`, `source/`, `windows/`, `linux/Sauriil-Dark-Archive/index.theme`.
2. Verification evidence from checks actually run against the relevant revision.
3. Active root and `docs/` orientation/policy files.
4. Historical reports and `DOCUMENTATION/`.
5. Clearly marked inference.

GitHub Issues and pull requests define operational work status. Re-check them live before stating what is open, complete, blocked, or superseded.

## Task Routing

- Documentation/indexing: update only the affected canonical hubs and [agent-index.json](agent-index.json).
- Asset pipeline: inspect `mappings/`, `source/master/raster`, conversion scripts, and proof reports before edits.
- Windows behavior: inspect [windows-plan.md](windows-plan.md), [security-model.md](security-model.md), current PowerShell scripts, and live Issues.
- Linux behavior: inspect [linux-plan.md](linux-plan.md), [security-model.md](security-model.md), `index.theme`, current Bash scripts, and live Issues.
- Reports/handoffs: add durable reports under `reports/` and unfinished-work notes under `handoffs/`.
- Material work: use Issue/work object → branch → verification → pull request.

## Current Safety Notes

- Do not run live apply or apply-rollback commands without explicit authorization.
- Apply gates are not proof of behavioral safety; [#1](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/1) tracks current platform safety work.
- Do not edit `VERSIONS/` archives unless explicitly requested.
- Do not trust skeleton-era wording when current source/proof disagrees.
- Do not put secrets or private local state into docs or machine-readable indexes.
- `scripts/validate/validate_mappings.py` currently has a known proof-clobbering defect tracked in [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7).

## Machine Index

Use [agent-index.json](agent-index.json) for machine-readable routing. Update it when paths, commands, tags, risks, or entry points change.

## Repository agent toolkit

- [Canonical toolkit](../.agent/README.md)
- [Stable project metadata](../.agent/project.yaml)
- [Project workflow](../skills/project/sauriil-dark-archive-workflow/SKILL.md)
- [Routing evaluations](../.agent/evals/skill-routing.md)

Inspect live related Issues, PRs and required checks before reconstructing unfinished work.

## NightTab task routing

Start with the [integration guide](../integrations/nighttab/README.md), [evidence](../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md) and [native-export handoff](../handoffs/2026-09-06-nighttab-native-export.md). Current scope is planned/researched only. Never place personal exports, bookmark data, URLs or profile state in Git. Use the installed Firefox version and explicit import-category preservation rules.
