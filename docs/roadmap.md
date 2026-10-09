# Roadmap

#repo/release #repo/development #sauriil/theme

This roadmap records bounded candidate work. Current GitHub Issues and pull requests are the operational work ledger; this file is not a substitute for live work state and does not authorize live OS changes.

## Current Baseline

- `v0.0.2` contains 12 accepted raster source icons.
- Windows ICO outputs exist for apps, file types, and folders.
- Linux PNG fallbacks exist for apps, places, and mimetypes.
- Historical v0.0.2 proof records successful asset/structure/mapping/`index.theme`/Linux-dry-run checks for its recorded revision and environment.
- Live OS apply/rollback safety is not established.
- Current implementation/safety defects are tracked in GitHub Issues; see [current-state.md](current-state.md).

## Candidate v0.0.3 Asset Batch

Existing `v0.0.2` docs suggest a bounded candidate batch:

- `drive-harddisk`
- `drive-removable-media`
- `user-trash`
- `folder-pictures`
- `folder-music`
- `folder-videos`
- `application-pdf`
- `text-html`

Before implementation, re-check current source, mappings, live work state, and user intent.

## Documentation Maintenance

- Keep [current-state.md](current-state.md), [source-map.md](source-map.md), [connections.md](connections.md), and [agent-index.json](agent-index.json) current after meaningful changes.
- Add handoffs under `handoffs/` only for unfinished work needing continuation context.
- Add reports under `reports/` when durable validation, implementation, or review evidence is warranted.

## Deferred / Future Work

- True scalable SVG icon set.
- Verified live Windows apply/rollback.
- Verified Linux user-theme install/rollback and KDE activation.
- Device, status, action, shell, symbolic, GNOME-specific, and XFCE-specific coverage.
- Broader release packaging process.

## Non-Goals Without Separate Authorization

- Cloud deployment.
- Obsidian sync/account setup.
- System-wide Linux install.
- Unrequested registry modification.
- Editing release ZIP archives without explicit approval.


## Separate planned NightTab integration

Complete the supported private current export, then follow the [bounded implementation plan](../integrations/nighttab/docs/implementation-plan.md): native 7.3.0 tokens/preset qualification, preserved private candidate, optional original asset reuse, disposable import/rollback and visual tests. Live apply remains a later scoped operation. No fork required for the current proposal. This work is not included automatically in either icon release batch.
