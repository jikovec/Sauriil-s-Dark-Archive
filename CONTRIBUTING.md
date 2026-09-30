# Contributing

Sauriil Dark Archive is a source-asset, conversion, platform-output, documentation, and proof repository. Keep contributions narrow, reversible, and evidence-backed.

## Before changing the repository

1. Read [README.md](README.md), [AGENTS.md](AGENTS.md), and [docs/INDEX.md](docs/INDEX.md).
2. Inspect the current default branch, current source/configuration, and live GitHub Issues and pull requests.
3. Use an existing Issue/work object when one covers the change. For material new work, create one before implementation.
4. Preserve unrelated dirty or untracked work in any local checkout.

Repository source/configuration and current tests/validation scripts define technical truth. GitHub Issues and pull requests define operational work state. Historical documents under `DOCUMENTATION/` are context, not current implementation proof.

## Delivery workflow

For material work, use:

```text
Issue / work object
→ branch
→ implementation
→ verification
→ pull request
```

Do not make feature work directly on `main`. Do not merge, release, publish, deploy, or run live OS apply/rollback actions unless that effect is explicitly authorized.

## Scope and generated artifacts

- Change only what the work item requires.
- Generated assets and proof files may be updated when regeneration is part of the requested work; record the exact command and result.
- Do not edit or regenerate `VERSIONS/` archives unless the task explicitly authorizes release-archive work.
- Do not rewrite historical evidence merely to make old terminology look current. Add a supersession note when necessary.
- Keep `.obsidian/` local and untracked.

## Verification

Use [docs/testing.md](docs/testing.md) and [docs/commands.md](docs/commands.md) to choose proportional checks.

Every pull request should state:
- the work item it addresses;
- what changed and what remained out of scope;
- exact verification commands/checks and their results;
- unavailable or skipped checks;
- documentation/proof impact;
- any live-OS, release, or publication boundary.

Never report an unrun or unavailable check as passing.

## Security-sensitive changes

Follow [SECURITY.md](SECURITY.md). Do not place sensitive vulnerability details in public Issues or pull requests.

## Licensing

The repository does not currently publish a selected license. Owner decision [#11](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/11) tracks that choice. Do not assume permission to reuse or redistribute project contents beyond rights granted by applicable law or an explicit owner statement.
