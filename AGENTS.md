# Sauriil's Dark Archive agent contract

## Identity and start

This is **Sauriil’s theme**, the non-destructive Windows 11 and Arch Linux/KDE
icon-theme asset, conversion and proof project, in `jikovec/Sauriil-s-Dark-Archive`.
It is separate from Elder Scrolls gameplay and lore. Address the owner as Aetheris
for project work and match the request's language.

Stable project/repository identity and environment discovery live in
[.agent/project.yaml](.agent/project.yaml). The toolkit map is
[.agent/README.md](.agent/README.md). No provider adapter owns project policy.

Before meaningful work, read:

1. [00_Index.md](00_Index.md) and [docs/INDEX.md](docs/INDEX.md).
2. [docs/current-state.md](docs/current-state.md).
3. [docs/decisions.md](docs/decisions.md).
4. [docs/agent-index.md](docs/agent-index.md).
5. The relevant canonical skill and applicable scoped instructions.

## Authority and scope

Complete the assigned outcome, relevant verification and its authorized delivery.
Preserve architecture, terminology and unrelated work; follow-ups normally steer
that outcome. Record adjacent findings separately instead of broadening the task.

The owner-adopted [authorization contract](.agent/contracts/authorization.md)
grants ordinary source workflow for requested work in this user-owned repository,
through commit, push, PR, checks/review remediation and merge. Local-only requests
narrow that endpoint. Release, deployment, publication and OS activation require
their own requested scope. Capability and identity labels do not grant authority.

This adoption supersedes the old blanket explicit-per-command Git prohibition
for ordinary source delivery only. It preserves all protected asset, privacy,
release and live-OS boundaries. Revalidate policy before consequential effects.
Never bypass external protections, required reviews, IAM or provider controls.

## Evidence and preservation

Inspect source and current Git state before changes. Retrieve live GitHub Issues,
PRs and relevant checks before reconstructing work; reports are historical context.
[Core](.agent/contracts/core.md) defines technical evidence and preservation;
[Git/GitHub](.agent/contracts/git-github.md) defines source delivery.

Preserve unrelated dirty, untracked and concurrent work. Use isolation when needed;
never broadly stage, reset, stash, discard or rewrite protected history by default.
Use bounded independent agents only when delegation is permitted and useful;
retain responsibility for integration and final verification.

Do not fabricate results. Distinguish local candidate, commit, remote source,
hosted checks, deployment identity and observed live acceptance.

## Project invariants

- Preserve product/runtime behavior unless a behavior change is requested.
- Keep original raster assets and their conversion provenance; no fake SVG wrapping.
- Do not inspect, edit or regenerate `VERSIONS/` without explicit archive scope.
- Proof/conversion commands can write assets and evidence; run only within that scope.
- Live apply and rollback require explicit target-OS scope and current script review.
- Windows apply requires `-Apply`; Linux apply requires `--apply` and stays user-scoped.
- Do not write system icon directories or infer live safety from historical proof.
- Keep `.obsidian/` ignored, local and plaintext; no sync/account/cloud integration.
- Never commit secrets, private exports, account IDs or sensitive machine paths.

## Discovery and checks

Canonical skills are under [skills/](skills/); reusable project reasoning is under
[skills/project/](skills/project/). Codex adapters use `.agents/skills/`, with
a `.codex/skills/` compatibility pointer; Claude adapters use `.claude/skills/`.
`CLAUDE.md` imports this file. Adapters must point to canonical content.

Use [commands](docs/commands.md), [testing](docs/testing.md) and the
[asset-proof workflow](.agent/workflows/asset-proof.md) for relevant native tools.
Missing runtimes are blocked prerequisites, not successful checks. For toolkit
edits, run `python3 scripts/validate/validate_agent_toolkit.py` and `git diff --check`.

Load [memory](.agent/contracts/memory.md) and [scopes](.agent/contracts/scopes.md)
only for persistent context, registry, cross-project or promotion work. Memory is
context, never current authority. Provider availability does not enroll a project.

After meaningful routing changes update `docs/current-state.md` and
`docs/agent-index.json`; record decisions in `docs/decisions.md`, durable evidence
in `reports/`, and unfinished work in `handoffs/`. Use the
[handoff contract](.agent/contracts/handoff.md) to report the actual endpoint.
