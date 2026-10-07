# Repository agent toolkit

Start at [AGENTS.md](../AGENTS.md) and [project.yaml](project.yaml). The metadata
uses the JSON subset of YAML 1.2 so Python's standard library can validate it
without installing a YAML parser. It contains stable identity, not current status.

| Layer | Responsibility |
|---|---|
| [Contracts](contracts/core.md) | Shared policy, loaded by task concern |
| [Skills](../skills/) | Portable reasoning workflows |
| [Project skill](../skills/project/sauriil-dark-archive-workflow/SKILL.md) | Existing theme workflow reconciled into canonical form |
| [Workflows](workflows/README.md) | Shared project procedures |
| [Integrations](integrations/README.md) | Real service bindings and configuration references |
| [Hooks](hooks/README.md) | Deterministic validation; no automatic hook installed |
| [Routing evaluations](evals/skill-routing.md) | Positive and neighboring negative cases |

Use `build`, `investigate`, `research`, `verify`, `review`, `fix`, `release`,
`deploy`, `publish`, `push` or `pull`. `develop` means `build`; `reconcile` means
`fix` with reconciliation intent. Aliases have no duplicate implementation.
Claude exposes `/name`; Codex supports `$name` when the adapter is discovered.
An ambiguous UI name can be disambiguated by the repository's canonical path.

## Provider discovery

The current [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills)
uses `.agents/skills/`. Native discovery here also scans `.codex/skills/`, so that
directory contains a compatibility README only to avoid duplicate skill entries.
The [Claude skill location](https://code.claude.com/docs/en/skills) is
`.claude/skills/`; [CLAUDE imports](https://code.claude.com/docs/en/memory) reuse
AGENTS.md without copying policy. No provider permission configuration is changed.

Read memory/scope contracts only for persistent context, registry, relationships
or promotion. No external registry identity is inferred from a filesystem path,
GitHub board or available connector. See the bootstrap report for discovery limits.

Run `python3 scripts/validate/validate_agent_toolkit.py` from the repository root
for metadata, frontmatter, adapter parity, links and routing-case structure.
This proves static conformance; provider discovery and semantic routing require
separate evidence. [Bootstrap evidence](../reports/2026-10-07-agent-toolkit-bootstrap.md).
