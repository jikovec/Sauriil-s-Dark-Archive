<!-- codex-memory-scaffold:agents-workflow -->
## Codex Project Memory Workflow

This repository is a local-first documentation and asset vault for the Sauriil Dark Archive icon theme. Treat it as a non-destructive asset/conversion/proof project unless the user explicitly asks for live OS apply or rollback behavior.

## Start Here

Before meaningful work, read:

1. [00_Index.md](00_Index.md)
2. [docs/INDEX.md](docs/INDEX.md)
3. [docs/current-state.md](docs/current-state.md)
4. [docs/decisions.md](docs/decisions.md)
5. [docs/agent-index.md](docs/agent-index.md)

Then inspect the task-specific source of truth:

- Commands and validation: [docs/commands.md](docs/commands.md), [docs/testing.md](docs/testing.md), [docs/proof-checklist.md](docs/proof-checklist.md)
- Architecture and source layout: [docs/architecture.md](docs/architecture.md), [docs/source-map.md](docs/source-map.md), [docs/connections.md](docs/connections.md)
- Security and apply boundaries: [docs/security-model.md](docs/security-model.md), [docs/deployment.md](docs/deployment.md), [docs/rollback.md](docs/rollback.md)
- Obsidian conventions: [docs/obsidian.md](docs/obsidian.md)
- Reports and handoffs: [reports/INDEX.md](reports/INDEX.md), [handoffs/INDEX.md](handoffs/INDEX.md)

## Source Of Truth

- Prefer source/config/scripts/mappings/assets over docs when they conflict: `scripts/`, `mappings/`, `source/`, `windows/`, `linux/Sauriil-Dark-Archive/index.theme`.
- Prefer proof reports over inferred notes for validation status, especially [proof/v0.0.2-validation-report.md](proof/v0.0.2-validation-report.md).
- Treat [README.md](README.md), this file, [00_Index.md](00_Index.md), and active docs under `docs/` as the human orientation layer.
- Treat `DOCUMENTATION/` as historical context unless a current doc or proof report points to it.
- Mark inferred information clearly.

## Safety Rules

- Preserve runtime and product behavior unless the user explicitly asks for a behavior change.
- Do not commit, push, tag, release, deploy, publish, reset, stash, or discard changes unless explicitly requested.
- Do not edit or regenerate `VERSIONS/` release archives unless explicitly requested.
- Do not copy secrets, credentials, tokens, private keys, account identifiers, private URLs, `.env` contents, or sensitive local paths into docs or indexes.
- Keep Obsidian local-first and plaintext. Keep `.obsidian/` ignored and untracked.
- Do not add Obsidian sync, cloud sharing, account coupling, encryption setup, or company integrations.

## Command Boundaries

- Proof and conversion commands can mutate generated assets or proof files. Run them only when regeneration is in scope.
- Windows apply requires `-Apply`; Linux install/rollback apply requires `--apply`. Do not run apply-capable commands without an explicit user request.
- Prefer docs-safe checks for documentation work: `git diff --check`, JSON validation for `docs/agent-index.json`, and Markdown link scans.

## After Meaningful Changes

- Update [docs/current-state.md](docs/current-state.md) when repo status or source-of-truth routing changes.
- Update [docs/agent-index.json](docs/agent-index.json) when entry points, commands, safety rules, paths, tags, or known risks change.
- Add a dated note under `handoffs/` when work is intentionally left unfinished.
- Add a report under `reports/` when durable evidence or implementation context should stay in the repo.
<!-- /codex-memory-scaffold:agents-workflow -->
