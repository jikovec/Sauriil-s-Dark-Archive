# Agent Index

#agent/orientation #repo/index #sauriil/theme

## Start Workflow

1. Check `git status --short`.
2. Read [../README.md](../README.md), [../AGENTS.md](../AGENTS.md), [../00_Index.md](../00_Index.md), [INDEX.md](INDEX.md), [current-state.md](current-state.md), and [decisions.md](decisions.md).
3. For command work, read [commands.md](commands.md), [testing.md](testing.md), and [security-model.md](security-model.md).
4. For asset or mapping work, read [source-map.md](source-map.md), [connections.md](connections.md), [asset-guidelines.md](asset-guidelines.md), and [icon-name-mapping.md](icon-name-mapping.md).
5. Inspect [../reports/INDEX.md](../reports/INDEX.md) and [../handoffs/INDEX.md](../handoffs/INDEX.md) for durable context.

## Source-Truth Order

1. Source/config/scripts/mappings/assets: `scripts/`, `mappings/`, `source/`, `windows/`, `linux/Sauriil-Dark-Archive/index.theme`.
2. Proof reports, especially [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md).
3. Root orientation: [../README.md](../README.md), [../00_Index.md](../00_Index.md), [../AGENTS.md](../AGENTS.md).
4. Active docs under `docs/`.
5. Historical docs under `DOCUMENTATION/`.
6. Clearly marked inference.

## Task Routing

- Documentation/indexing: update [INDEX.md](INDEX.md), [current-state.md](current-state.md), [source-map.md](source-map.md), [connections.md](connections.md), and [agent-index.json](agent-index.json).
- Asset pipeline: inspect `mappings/`, `source/master/raster`, conversion scripts, and proof reports before edits.
- Windows behavior: inspect [windows-plan.md](windows-plan.md), [security-model.md](security-model.md), and current PowerShell scripts.
- Linux behavior: inspect [linux-plan.md](linux-plan.md), [security-model.md](security-model.md), `index.theme`, and current Bash scripts.
- Reports/handoffs: add durable reports under `reports/` and unfinished-work notes under `handoffs/`.

## Safety Notes

- Do not run live apply or rollback commands without an explicit user request.
- Do not edit `VERSIONS/` archives unless explicitly requested.
- Do not trust skeleton-era wording when source/proof reports disagree.
- Do not put secrets or private local state into docs or JSON indexes.

## Machine Index

Use [agent-index.json](agent-index.json) for machine-readable routing. Update it when paths, commands, tags, risks, or entry points change.

## Repository agent toolkit

- [Canonical toolkit](../.agent/README.md)
- [Stable project metadata](../.agent/project.yaml)
- [Project workflow](../skills/project/sauriil-dark-archive-workflow/SKILL.md)
- [Routing evaluations](../.agent/evals/skill-routing.md)

Inspect live related Issues, PRs and required checks before reconstructing unfinished work.
