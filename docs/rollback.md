# Rollback

## Windows shortcut rollback

Restore backed-up `.lnk` files or manually change the icon back through Shortcut Properties → Change Icon.

For pinned taskbar icons, unpin the themed shortcut and pin the original shortcut again.

## Windows registry rollback

Before future registry-backed changes, export affected keys. Rollback imports the `.reg` backups from `windows/registry/rollback/`.

Dry-run:

```powershell
pwsh ./scripts/rollback/windows_rollback_icons.ps1
```

Apply mode:

```powershell
pwsh ./scripts/rollback/windows_rollback_icons.ps1 -Apply
```

## Windows icon cache refresh

After rollback, restart Explorer or rebuild icon cache only when necessary:

```bat
ie4uinit.exe -show
taskkill /F /IM explorer.exe
start explorer.exe
```

Use aggressive cache deletion only if Explorer remains stale.

## KDE theme rollback

Switch KDE back to Breeze/Breeze Dark in System Settings first. Then remove only the user-scope theme directory:

```bash
rm -rf "$HOME/.local/share/icons/Sauriil-Dark-Archive"
kbuildsycoca6 --noincremental || true
```

## `.desktop` override rollback

Remove only explicitly managed files from:

```txt
$HOME/.local/share/applications
```

Do not delete unrelated user `.desktop` files. The rollback script reads mapping CSV rows and only plans mapped override names.
