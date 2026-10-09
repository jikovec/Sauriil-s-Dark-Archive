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
- Keep [agent-index.json](agent-index.json) as detailed navigation; [.agent/project.yaml](../.agent/project.yaml) owns stable identity. `.agents/skills/` contains discovery adapters; no separate `.agents/index.json` is needed.
- Keep this decision log in `docs/decisions.md`; omit `docs/adr/` until decisions become large enough to need separate records.

## Decision Log

### 2026-10-09 - Explicit Claude invocation for release, deploy and publish

- Context: The owner requested that Claude Code never invoke deployment, publication or release skills automatically, without a second copy of the workflows.
- Decision: Only the Claude adapters for `release`, `deploy` and `publish` add `disable-model-invocation: true`. They stay discoverable and run on an explicit `/release`, `/deploy` or `/publish`. Canonical skills and Codex adapters keep portable name/description metadata.
- Consequences: The toolkit validator requires the field on exactly those three Claude adapters and rejects it elsewhere. Claude can still read canonical workflows routed by AGENTS.md; release and deployment authority is unchanged.
- References: [toolkit index](../.agent/README.md), [toolkit validator](../scripts/validate/validate_agent_toolkit.py).

### 2026-10-07 - Portable repository agent toolkit

- Context: The owner requested durable canonical workflows and thin Codex/Claude adapters, including a standing ordinary source-delivery grant for user-owned repositories.
- Decision: Adopt [AGENTS.md](../AGENTS.md), [.agent contracts](../.agent/README.md) and `skills/` as canonical. Ordinary requested source work may proceed through merge; local-only requests narrow it. Release, protected archives, memory writes and OS activation retain separate authority requirements.
- Identity: Use `github:jikovec/Sauriil-s-Dark-Archive`, preserving the established repository and Sauriil’s theme display identity. No organization is established. Existing registry discovery found no matching configured entry; no verified memory binding exists, so Mind-Seed remains disabled.
- Consequences: Native providers load thin adapters, and `docs/agent-workflow.md` is a compatibility pointer. Scope promotion is explicit and memory remains contextual. Existing local environment and NightTab work are not imported from the dirty checkout. PR #12 remains separate overlapping governance work.
- References: [bootstrap report](../reports/2026-10-07-agent-toolkit-bootstrap.md), [authorization](../.agent/contracts/authorization.md).


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
