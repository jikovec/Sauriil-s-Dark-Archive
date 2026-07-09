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
