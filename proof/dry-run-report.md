# Dry-Run Report

Generated: 2026-05-03T20:58:45.696959+00:00

## Safety assertions

- Repository structure validation is recorded in `proof/validation-report.md`.
- v0.0.2 image/icon assets are expected and are confined to project directories.
- No live Windows registry modification was performed by validation: yes.
- No Linux system directory modification was performed by validation: yes.
- Apply-capable scripts are dry-run gated: yes.
- Missing mapped required icon assets are treated as validation failures: yes.

## Dry-run commands

```bash
python scripts/validate/validate_structure.py
python scripts/validate/validate_mappings.py
python scripts/validate/validate_index_theme.py
python scripts/validate/generate_dry_run_report.py
bash scripts/dry-run/linux_plan_install.sh
```

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

## Image asset scan

- Image/icon files found in repository: 221
- `linux/Sauriil-Dark-Archive/128x128/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/128x128/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/128x128/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/128x128/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/128x128/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/128x128/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/128x128/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/128x128/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/128x128/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/128x128/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/128x128/places/folder.png`
- `linux/Sauriil-Dark-Archive/128x128/places/user-home.png`
- `linux/Sauriil-Dark-Archive/16x16/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/16x16/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/16x16/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/16x16/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/16x16/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/16x16/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/16x16/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/16x16/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/16x16/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/16x16/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/16x16/places/folder.png`
- `linux/Sauriil-Dark-Archive/16x16/places/user-home.png`
- `linux/Sauriil-Dark-Archive/24x24/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/24x24/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/24x24/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/24x24/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/24x24/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/24x24/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/24x24/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/24x24/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/24x24/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/24x24/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/24x24/places/folder.png`
- `linux/Sauriil-Dark-Archive/24x24/places/user-home.png`
- `linux/Sauriil-Dark-Archive/256x256/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/256x256/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/256x256/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/256x256/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/256x256/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/256x256/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/256x256/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/256x256/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/256x256/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/256x256/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/256x256/places/folder.png`
- `linux/Sauriil-Dark-Archive/256x256/places/user-home.png`
- `linux/Sauriil-Dark-Archive/32x32/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/32x32/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/32x32/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/32x32/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/32x32/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/32x32/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/32x32/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/32x32/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/32x32/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/32x32/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/32x32/places/folder.png`
- `linux/Sauriil-Dark-Archive/32x32/places/user-home.png`
- `linux/Sauriil-Dark-Archive/48x48/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/48x48/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/48x48/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/48x48/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/48x48/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/48x48/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/48x48/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/48x48/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/48x48/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/48x48/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/48x48/places/folder.png`
- `linux/Sauriil-Dark-Archive/48x48/places/user-home.png`
- `linux/Sauriil-Dark-Archive/64x64/apps/sauriil-browser.png`
- `linux/Sauriil-Dark-Archive/64x64/apps/sauriil-code-editor.png`
- `linux/Sauriil-Dark-Archive/64x64/apps/sauriil-file-manager.png`
- `linux/Sauriil-Dark-Archive/64x64/apps/sauriil-terminal.png`
- `linux/Sauriil-Dark-Archive/64x64/mimetypes/application-x-rar.png`
- `linux/Sauriil-Dark-Archive/64x64/mimetypes/application-zip.png`
- `linux/Sauriil-Dark-Archive/64x64/mimetypes/text-x-python.png`
- `linux/Sauriil-Dark-Archive/64x64/mimetypes/text-x-script.png`
- `linux/Sauriil-Dark-Archive/64x64/places/folder-documents.png`
- `linux/Sauriil-Dark-Archive/64x64/places/folder-downloads.png`
- `linux/Sauriil-Dark-Archive/64x64/places/folder.png`
- `linux/Sauriil-Dark-Archive/64x64/places/user-home.png`
- `source/master/contact-sheets/v0.0.2-contact-sheet-16.png`
- `source/master/contact-sheets/v0.0.2-contact-sheet-24.png`
- `source/master/contact-sheets/v0.0.2-contact-sheet-256.png`
- `source/master/contact-sheets/v0.0.2-contact-sheet-32.png`
- `source/master/contact-sheets/v0.0.2-contact-sheet-48.png`
- `source/master/raster/application-x-rar.png`
- `source/master/raster/application-zip.png`
- `source/master/raster/folder-documents.png`
- `source/master/raster/folder-downloads.png`
- `source/master/raster/folder.png`
- `source/master/raster/sauriil-browser.png`
- `source/master/raster/sauriil-code-editor.png`
- `source/master/raster/sauriil-file-manager.png`
- `source/master/raster/sauriil-terminal.png`
- `source/master/raster/text-x-python.png`
- `source/master/raster/text-x-script.png`
- `source/master/raster/user-home.png`
- `source/png/1024/application-x-rar.png`
- `source/png/1024/application-zip.png`
- `source/png/1024/folder-documents.png`
- `source/png/1024/folder-downloads.png`
- `source/png/1024/folder.png`
- `source/png/1024/sauriil-browser.png`
- `source/png/1024/sauriil-code-editor.png`
- `source/png/1024/sauriil-file-manager.png`
- `source/png/1024/sauriil-terminal.png`
- `source/png/1024/text-x-python.png`
- `source/png/1024/text-x-script.png`
- `source/png/1024/user-home.png`
- `source/png/128/application-x-rar.png`
- `source/png/128/application-zip.png`
- `source/png/128/folder-documents.png`
- `source/png/128/folder-downloads.png`
- `source/png/128/folder.png`
- `source/png/128/sauriil-browser.png`
- `source/png/128/sauriil-code-editor.png`
- `source/png/128/sauriil-file-manager.png`
- `source/png/128/sauriil-terminal.png`
- `source/png/128/text-x-python.png`
- `source/png/128/text-x-script.png`
- `source/png/128/user-home.png`
- `source/png/16/application-x-rar.png`
- `source/png/16/application-zip.png`
- `source/png/16/folder-documents.png`
- `source/png/16/folder-downloads.png`
- `source/png/16/folder.png`
- `source/png/16/sauriil-browser.png`
- `source/png/16/sauriil-code-editor.png`
- `source/png/16/sauriil-file-manager.png`
- `source/png/16/sauriil-terminal.png`
- `source/png/16/text-x-python.png`
- `source/png/16/text-x-script.png`
- `source/png/16/user-home.png`
- `source/png/24/application-x-rar.png`
- `source/png/24/application-zip.png`
- `source/png/24/folder-documents.png`
- `source/png/24/folder-downloads.png`
- `source/png/24/folder.png`
- `source/png/24/sauriil-browser.png`
- `source/png/24/sauriil-code-editor.png`
- `source/png/24/sauriil-file-manager.png`
- `source/png/24/sauriil-terminal.png`
- `source/png/24/text-x-python.png`
- `source/png/24/text-x-script.png`
- `source/png/24/user-home.png`
- `source/png/256/application-x-rar.png`
- `source/png/256/application-zip.png`
- `source/png/256/folder-documents.png`
- `source/png/256/folder-downloads.png`
- `source/png/256/folder.png`
- `source/png/256/sauriil-browser.png`
- `source/png/256/sauriil-code-editor.png`
- `source/png/256/sauriil-file-manager.png`
- `source/png/256/sauriil-terminal.png`
- `source/png/256/text-x-python.png`
- `source/png/256/text-x-script.png`
- `source/png/256/user-home.png`
- `source/png/32/application-x-rar.png`
- `source/png/32/application-zip.png`
- `source/png/32/folder-documents.png`
- `source/png/32/folder-downloads.png`
- `source/png/32/folder.png`
- `source/png/32/sauriil-browser.png`
- `source/png/32/sauriil-code-editor.png`
- `source/png/32/sauriil-file-manager.png`
- `source/png/32/sauriil-terminal.png`
- `source/png/32/text-x-python.png`
- `source/png/32/text-x-script.png`
- `source/png/32/user-home.png`
- `source/png/48/application-x-rar.png`
- `source/png/48/application-zip.png`
- `source/png/48/folder-documents.png`
- `source/png/48/folder-downloads.png`
- `source/png/48/folder.png`
- `source/png/48/sauriil-browser.png`
- `source/png/48/sauriil-code-editor.png`
- `source/png/48/sauriil-file-manager.png`
- `source/png/48/sauriil-terminal.png`
- `source/png/48/text-x-python.png`
- `source/png/48/text-x-script.png`
- `source/png/48/user-home.png`
- `source/png/512/application-x-rar.png`
- `source/png/512/application-zip.png`
- `source/png/512/folder-documents.png`
- `source/png/512/folder-downloads.png`
- `source/png/512/folder.png`
- `source/png/512/sauriil-browser.png`
- `source/png/512/sauriil-code-editor.png`
- `source/png/512/sauriil-file-manager.png`
- `source/png/512/sauriil-terminal.png`
- `source/png/512/text-x-python.png`
- `source/png/512/text-x-script.png`
- `source/png/512/user-home.png`
- `source/png/64/application-x-rar.png`
- `source/png/64/application-zip.png`
- `source/png/64/folder-documents.png`
- ... 21 additional image/icon files omitted from this report preview.

## Missing mapped assets

- Mapping gaps detected: 0
