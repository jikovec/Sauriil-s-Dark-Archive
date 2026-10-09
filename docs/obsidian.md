# Obsidian Guide

#obsidian/local #obsidian/graph #repo/index

This repository can be opened as a local Obsidian vault for documentation and working context.

## Local-Only Rule

- Keep `.obsidian/` ignored and untracked.
- Do not add Obsidian sync, cloud sharing, account coupling, encryption setup, or company integration.
- Do not store secrets, credentials, tokens, private URLs, private account IDs, or sensitive local paths in notes.

## Link Conventions

- Use normal Markdown links as the canonical format in committed docs.
- Wiki links are acceptable in [../00_Index.md](../00_Index.md) for local graph navigation.
- Resolve Markdown links relative to the containing file.
- Prefer links to docs, source maps, proof reports, and indexes over duplicated prose.

## Graph Hubs

- [../00_Index.md](../00_Index.md) - root vault hub.
- [INDEX.md](INDEX.md) - GitHub-compatible docs hub.
- [agent-index.md](agent-index.md) - future-agent hub.
- [source-map.md](source-map.md) - source and output hub.
- [connections.md](connections.md) - cross-link hub.
- [../reports/INDEX.md](../reports/INDEX.md) - report hub.
- [../handoffs/INDEX.md](../handoffs/INDEX.md) - handoff hub.

## Tag Taxonomy

Global tags:

- `#repo/index`
- `#repo/architecture`
- `#repo/development`
- `#repo/testing`
- `#repo/security`
- `#repo/release`
- `#repo/decision`
- `#repo/source-map`
- `#repo/connection-map`
- `#agent/orientation`
- `#agent/handoff`
- `#agent/report`
- `#obsidian/local`
- `#obsidian/graph`

Repo tags:

- `#sauriil/theme`
- `#sauriil/assets`
- `#sauriil/v0-0-2`
- `#sauriil/windows`
- `#sauriil/linux`
- `#sauriil/kde`
- `#sauriil/mappings`
- `#sauriil/proof`
- `#sauriil/rollback`
- `#sauriil/release-archive`

Do not use tags that imply unsupported behavior:

- `#obsidian/sync`
- `#deployment/cloud`
- `#windows/live-registry-applied`
- `#linux/system-install`
- `#security/guarantee`

## Tagging Rules

- Tag durable hubs, reports, and handoffs.
- Do not tag every generated proof row or CSV-derived fact.
- Use tags to create graph clusters, not to replace direct Markdown links.

<!-- local-graph-scope-2026-07-21:start -->
## Default Local Graph View

The local `.obsidian/graph.json` uses this knowledge-only Global Graph filter:

```text
path:docs OR path:DOCUMENTATION OR path:reports OR path:handoffs OR file:00_Index OR file:AGENTS
```

| Control | Local default | Purpose |
| --- | --- | --- |
| Attachments | off | Removes source, media, generated, dependency, and evidence-file noise. |
| Tags | off | Keeps normal Markdown links as the visible relationship model. |
| Existing files only | on | Hides unresolved targets until a real note exists. |
| Orphans | on | Keeps genuine degree-zero Markdown notes visible for maintenance. |

The filter keeps maintained documentation, evidence, handoffs, and stable root hubs visible while source, dependencies, generated output, and attachments stay outside the normal knowledge view.

A large outer ring of isolated colored nodes usually means attachments were enabled with an empty or overly broad filter; it does not by itself prove missing documentation backlinks. Keep Orphans enabled, classify each remaining Markdown orphan, and connect it through the narrowest real owner, archive, report, handoff, release, or specification index. Do not create decorative backlinks only to improve the metric.

The graph JSON is local UI state, not repository truth. If an old force layout remains visible after this setting changes, close and reopen Global Graph once so Obsidian reloads the filter. Re-run the Markdown link/component audit after adding or moving documentation.
<!-- local-graph-scope-2026-07-21:end -->
