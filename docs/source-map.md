# Source Map

#repo/source-map #sauriil/assets #sauriil/mappings

## Asset Sources

- [../source/master/raster](../source/master/raster) - accepted raster master icons for `v0.0.2`.
- [../source/master/contact-sheets](../source/master/contact-sheets) - generated visual proof sheets.
- [../source/references](../source/references) - reference inventory and historical source notes.
- [../source/svg](../source/svg) - placeholder SVG folders; `v0.0.2` does not contain true scalable SVG artwork.

## Generated PNGs

- [../source/png](../source/png) - normalized generated PNGs by size.
- Sizes currently include `16`, `24`, `32`, `48`, `64`, `128`, `256`, `512`, and `1024`.

## Windows Outputs

- [../windows/ico/apps](../windows/ico/apps) - app ICO outputs.
- [../windows/ico/filetypes](../windows/ico/filetypes) - file type ICO outputs.
- [../windows/ico/folders](../windows/ico/folders) - folder ICO outputs.
- [../windows/ico/drives](../windows/ico/drives) - placeholder drive ICO output folder; no current `v0.0.2` drive icons.
- [../windows/ico/shell](../windows/ico/shell) - placeholder shell ICO output folder; no current `v0.0.2` shell icons.
- [../windows/registry](../windows/registry) - registry apply/dry-run/rollback staging folders.
- [../windows/shortcuts](../windows/shortcuts) - shortcut staging folder.

## Linux Outputs

- [../linux/Sauriil-Dark-Archive](../linux/Sauriil-Dark-Archive) - XDG icon theme root.
- [../linux/Sauriil-Dark-Archive/index.theme](../linux/Sauriil-Dark-Archive/index.theme) - theme metadata and directory declarations.
- [../linux/Sauriil-Dark-Archive/scalable](../linux/Sauriil-Dark-Archive/scalable) - placeholder scalable context folders; no true scalable `v0.0.2` artwork.
- [../linux/desktop-overrides](../linux/desktop-overrides) - user-scope desktop override staging.
- [../linux/mime-overrides](../linux/mime-overrides) - MIME override staging.

## Mapping Files

- [../mappings/icon-assets.csv](../mappings/icon-assets.csv) - source asset routing manifest.
- [../mappings/windows-shortcuts.csv](../mappings/windows-shortcuts.csv) - Windows shortcut icon targets.
- [../mappings/windows-filetypes.csv](../mappings/windows-filetypes.csv) - Windows file type icon targets.
- [../mappings/windows-drives.csv](../mappings/windows-drives.csv) - Windows drive icon targets, currently header-only.
- [../mappings/linux-desktop-icons.csv](../mappings/linux-desktop-icons.csv) - Linux desktop icon targets.
- [../mappings/linux-mimetypes.csv](../mappings/linux-mimetypes.csv) - Linux MIME icon targets.
- [../mappings/linux-standard-names.csv](../mappings/linux-standard-names.csv) - Linux standard place icon names.

## Scripts

- [../scripts/convert](../scripts/convert) - asset conversion scripts.
- [../scripts/test-render](../scripts/test-render) - contact sheet rendering.
- [../scripts/validate](../scripts/validate) - structure, mapping, `index.theme`, and dry-run report validation.
- [../scripts/dry-run](../scripts/dry-run) - Windows and Linux dry-run planners.
- [../scripts/apply](../scripts/apply) - apply-capable scripts; explicit user request required.
- [../scripts/rollback](../scripts/rollback) - rollback scripts; apply rollback requires explicit user request.

## Proof Links

- [../proof/v0.0.2-source-asset-inventory.md](../proof/v0.0.2-source-asset-inventory.md)
- [../proof/v0.0.2-generated-assets.md](../proof/v0.0.2-generated-assets.md)
- [../proof/v0.0.2-contact-sheet-report.md](../proof/v0.0.2-contact-sheet-report.md)
- [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)


## Planned NightTab integration

- [Integration entry point](../integrations/nighttab/README.md) — researched/planned native integration.
- [Visual proposal](../integrations/nighttab/docs/visual-specification.md) — proposed tokens and generic asset reuse.
- [Implementation plan](../integrations/nighttab/docs/implementation-plan.md) — future file paths, private boundary and qualification gates.

No presets, copied icons, backgrounds or integration scripts are implemented yet; private browser state is never a source area in this repository.
