# Roadmap

#repo/release #repo/development #sauriil/theme

This roadmap records bounded next steps from current docs and proof. It is not a commitment to live OS changes.

## Current Baseline

- `v0.0.2` generated 12 accepted raster source icons.
- Windows ICO outputs exist for apps, file types, and folders.
- Linux PNG fallbacks exist for apps, places, and mimetypes.
- Proof reports record passing structure, mapping, `index.theme`, contact sheet, and dry-run checks.
- Live OS apply/install is not proven.

## Candidate v0.0.3 Asset Batch

Existing `v0.0.2` docs suggest a bounded next batch:

- `drive-harddisk`
- `drive-removable-media`
- `user-trash`
- `folder-pictures`
- `folder-music`
- `folder-videos`
- `application-pdf`
- `text-html`

Before implementation, re-check current source, mappings, and user intent.

## Documentation Roadmap

- Keep [current-state.md](current-state.md), [source-map.md](source-map.md), [connections.md](connections.md), and [agent-index.json](agent-index.json) current after meaningful changes.
- Add task-specific handoffs under `handoffs/` only when work is incomplete or needs continuation context.
- Add reports under `reports/` when validation evidence, implementation notes, or review findings should remain durable.

## Deferred Work

- True scalable SVG icon set.
- Live Windows apply proof.
- Linux user-theme install and KDE activation proof.
- Device, status, action, shell, symbolic, GNOME, and XFCE coverage.
- Broader release packaging process.

## Non-Goals

- Cloud deployment.
- Obsidian sync or account setup.
- System-wide Linux install.
- Unrequested registry modification.
- Editing release ZIP archives without explicit approval.
