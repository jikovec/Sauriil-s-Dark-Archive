# Icon Name Mapping

## Mapping status values

Mapping CSV rows use `status` to control validation severity:

- `example`: documentation sample only; missing assets are expected gaps.
- `optional`: future optional target; missing assets are reported as gaps.
- `required`: real target; missing assets fail validation.
- `active`: installed or apply-ready target; missing assets fail validation.
- `deprecated`: ignored by apply scripts.

The starter CSV files contain only `example` rows.

## Windows shortcut mapping

`mappings/windows-shortcuts.csv` documents planned shortcut and profile icon targets. It does not scan the live system and does not assume installed applications.

Important fields:

- `shortcut_hint`: human-readable future path or settings file hint.
- `planned_icon_path`: repository-relative future `.ico` path.
- `backup_hint`: manual or scripted backup expectation.

## Windows file type mapping

`mappings/windows-filetypes.csv` documents selected future file type icon overrides.

Important fields:

- `extension`
- `prog_id`
- `registry_path`
- `planned_icon_path`
- `scope`

The scripts read planned registry paths from the CSV and print backup/export commands in dry-run mode.

## Windows drive mapping

`mappings/windows-drives.csv` documents future drive icon overrides. HKLM paths require explicit apply mode, registry export, and administrative awareness.

## Linux desktop icon mapping

`mappings/linux-desktop-icons.csv` documents future `.desktop` overrides. Only user-scope override paths are allowed. Do not edit `/usr/share/applications`.

## Linux MIME mapping

`mappings/linux-mimetypes.csv` maps MIME types to icon-theme names and future SVG/PNG asset paths.

## Linux standard names mapping

`mappings/linux-standard-names.csv` tracks standard names for contexts such as `apps`, `places`, `devices`, `actions`, and `status`.

## Missing assets

Missing assets are reported in `proof/known-gaps.md`. Missing future assets are not fatal for `example` rows. Missing assets fail validation only when the row status is `required` or `active`.
