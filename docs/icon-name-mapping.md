# Icon Name Mapping

## Mapping status values

Mapping CSV rows use `status` to control validation severity:

- `example`: documentation sample only; missing assets are expected gaps.
- `optional`: future optional target; missing assets are reported as gaps.
- `required`: real generated target; missing assets fail validation.
- `active`: installed or apply-ready target; missing assets fail validation.
- `deprecated`: ignored by apply scripts.

v0.0.2 replaces the skeleton example rows with required rows only where the referenced generated assets exist.

## Asset routing manifest

`mappings/icon-assets.csv` is the v0.0.2 routing manifest used by the conversion scripts.

Important fields:

- `icon_name`
- `source_master_path`
- `windows_context`
- `linux_context`
- `concept`
- `notes`

The Windows and Linux exporters use this file to avoid exporting every source PNG into every context.

## Windows shortcut mapping

`mappings/windows-shortcuts.csv` documents generated app `.ico` targets. It does not scan or modify the live system.

v0.0.2 rows:

```txt
sauriil-terminal
sauriil-browser
sauriil-code-editor
sauriil-file-manager
```

## Windows file type mapping

`mappings/windows-filetypes.csv` documents selected generated filetype `.ico` targets. Registry paths are planning/dry-run data only.

v0.0.2 rows:

```txt
.zip  -> application-zip
.rar  -> application-x-rar
.ps1  -> text-x-script
.py   -> text-x-python
```

## Windows drive mapping

`mappings/windows-drives.csv` is header-only in v0.0.2 because no drive icons are included.

## Linux desktop icon mapping

`mappings/linux-desktop-icons.csv` maps generated app icon names to Linux PNG fallback paths. `.desktop` overrides are not installed in v0.0.2.

## Linux MIME mapping

`mappings/linux-mimetypes.csv` maps MIME names to generated PNG fallback paths. SVG paths are blank in v0.0.2 because no true vector sources exist.

## Linux standard names mapping

`mappings/linux-standard-names.csv` maps generated place icons:

```txt
folder
folder-documents
folder-downloads
user-home
```

## Missing assets

Missing assets are reported in `proof/known-gaps.md`. Missing required/active assets fail validation.
