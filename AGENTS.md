# Agent Instructions

This repository is the Sauriil Dark Archive icon-theme asset/conversion/proof project. Preserve that project boundary. Live OS customization is never implied by routine repository work.

## Required orientation

Before meaningful work:

1. Inspect the current default branch and `git status --short --branch` in the working copy you will modify.
2. Read [README.md](README.md), [00_Index.md](00_Index.md), [docs/INDEX.md](docs/INDEX.md), [docs/current-state.md](docs/current-state.md), and [docs/decisions.md](docs/decisions.md).
3. Inspect current GitHub Issues and pull requests for operational work state and conflicts.
4. Read task-specific source, scripts, mappings, proof, and documentation before changing them.

Useful routes:

- Commands and verification: [docs/commands.md](docs/commands.md), [docs/testing.md](docs/testing.md), [docs/proof-checklist.md](docs/proof-checklist.md)
- Architecture/source: [docs/architecture.md](docs/architecture.md), [docs/source-map.md](docs/source-map.md), [docs/connections.md](docs/connections.md)
- Security/apply boundaries: [SECURITY.md](SECURITY.md), [docs/security-model.md](docs/security-model.md), [docs/deployment.md](docs/deployment.md), [docs/rollback.md](docs/rollback.md)
- Contribution workflow: [CONTRIBUTING.md](CONTRIBUTING.md)
- Reports/handoffs: [reports/INDEX.md](reports/INDEX.md), [handoffs/INDEX.md](handoffs/INDEX.md)

## Authority

Use this order when sources disagree:

1. Current source/configuration/scripts/mappings/assets and repository state.
2. Verification evidence from checks actually run against the relevant revision.
3. Active canonical documentation under the repository root and `docs/`.
4. Historical reports and `DOCUMENTATION/`.
5. Clearly identified inference.

GitHub Issues and pull requests are the operational work ledger: they describe current/queued work, not technical implementation truth. Re-check both before making work-state claims.

Do not convert accepted target plans into implementation claims. Current apply-path defects are tracked in GitHub; an apply gate alone is not proof of safe behavior.

## Work and delivery

For material work, follow:

```text
Issue / work object
→ branch
→ implementation
→ verification
→ pull request
```

- Preserve unrelated dirty and untracked work.
- Do not reset, stash, discard, or rewrite unrelated changes.
- Perform external mutations only when the current task explicitly authorizes them.
- Do not merge, deploy, publish, release, or tag unless that effect is explicitly authorized.
- Do not edit or regenerate `VERSIONS/` archives unless release-archive work is explicitly in scope.

## Verification

- Run the smallest relevant checks from [docs/testing.md](docs/testing.md).
- Never report an unavailable or unrun check as passing.
- Proof/conversion commands can mutate generated assets or `proof/`; run them only when regeneration is in scope.
- Live Windows/Linux apply or apply-rollback commands are not validation commands and require explicit authorization.

## Security and privacy

- Never add secrets, credentials, tokens, private keys, `.env` contents, private URLs, account identifiers, or sensitive local machine state.
- Keep `.obsidian/` ignored and untracked.
- Do not add Obsidian sync, cloud sharing, account coupling, encryption setup, or company integrations unless explicitly requested.
- Follow [SECURITY.md](SECURITY.md) for vulnerability material.

## Documentation obligations

After meaningful changes, update only the canonical documents affected. Keep [docs/agent-index.json](docs/agent-index.json) aligned when entry points, commands, paths, work routing, or known risks change. Prefer links over duplicated prose.

Historical evidence should remain historically accurate; add a supersession note rather than rewriting history.
