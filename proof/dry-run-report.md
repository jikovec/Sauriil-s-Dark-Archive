# Dry-Run Report

Generated: 2026-05-03T20:00:47.248717+00:00

## Safety assertions

- Skeleton directories exist: see `proof/validation-report.md`.
- No final icon art is included: yes
- No live Windows registry modification was performed by validation: yes.
- No Linux system directory modification was performed by validation: yes.
- Apply-capable scripts are dry-run gated: yes.
- Missing icon assets are expected gaps for the next phase: yes.

## Dry-run commands

```bash
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
bash scripts/dry-run/linux_plan_install.sh
```

```powershell
pwsh ./scripts/dry-run/windows_plan_changes.ps1
```

## Image asset scan

- Image-like files found in repository: 0

## Missing future assets

- Mapping gaps detected: 19
- mappings/windows-shortcuts.csv:2: `windows/ico/apps/example-editor.ico` missing (example)
- mappings/windows-shortcuts.csv:3: `windows/ico/apps/example-terminal.ico` missing (example)
- mappings/windows-filetypes.csv:2: `windows/ico/filetypes/example-file.ico` missing (example)
- mappings/windows-filetypes.csv:3: `windows/ico/filetypes/example-archive.ico` missing (example)
- mappings/windows-drives.csv:2: `windows/ico/drives/example-drive.ico` missing (example)
- mappings/linux-desktop-icons.csv:2: `linux/Sauriil-Dark-Archive/scalable/apps/sauriil-example-app.svg` missing (example)
- mappings/linux-desktop-icons.csv:2: `linux/desktop-overrides/org.example.App.desktop` missing (example)
- mappings/linux-desktop-icons.csv:3: `linux/Sauriil-Dark-Archive/scalable/apps/sauriil-example-terminal.svg` missing (example)
- mappings/linux-desktop-icons.csv:3: `linux/desktop-overrides/org.example.Terminal.desktop` missing (example)
- mappings/linux-mimetypes.csv:2: `linux/Sauriil-Dark-Archive/48x48/mimetypes/application-x-example.png` missing (example)
- mappings/linux-mimetypes.csv:2: `linux/Sauriil-Dark-Archive/scalable/mimetypes/application-x-example.svg` missing (example)
- mappings/linux-mimetypes.csv:3: `linux/Sauriil-Dark-Archive/48x48/mimetypes/application-x-rar.png` missing (example)
- mappings/linux-mimetypes.csv:3: `linux/Sauriil-Dark-Archive/scalable/mimetypes/application-x-rar.svg` missing (example)
- mappings/linux-standard-names.csv:2: `linux/Sauriil-Dark-Archive/48x48/places/folder.png` missing (example)
- mappings/linux-standard-names.csv:2: `linux/Sauriil-Dark-Archive/scalable/places/folder.svg` missing (example)
- mappings/linux-standard-names.csv:3: `linux/Sauriil-Dark-Archive/48x48/devices/drive-harddisk.png` missing (example)
- mappings/linux-standard-names.csv:3: `linux/Sauriil-Dark-Archive/scalable/devices/drive-harddisk.svg` missing (example)
- mappings/linux-standard-names.csv:4: `linux/Sauriil-Dark-Archive/48x48/actions/document-open.png` missing (example)
- mappings/linux-standard-names.csv:4: `linux/Sauriil-Dark-Archive/scalable/actions/document-open.svg` missing (example)
