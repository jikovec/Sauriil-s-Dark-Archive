# Windows 11 Plan

## Strategy

Use a native-first, backup-first Windows strategy. Windows is not a true OS-wide icon-theme platform, so the skeleton separates safe native targets from registry-backed and third-party-assisted targets.

## Stable icon storage path

Future real icons should be copied to a stable user-owned path before applying them:

```txt
%LOCALAPPDATA%\SauriilDarkArchive\icons\
```

Do not point shortcuts or registry values at temporary build folders.

## Native-first targets

Use native Windows methods first:

- Desktop and Start-menu Win32 shortcuts: Shortcut Properties → Change Icon.
- Pinned taskbar icons: change the source shortcut icon, unpin the old item, then pin the corrected shortcut.
- Project folders: Folder Properties → Customize → Change Icon.
- Desktop system icons: Settings → Personalization → Themes → Desktop icon settings.
- Windows Terminal profiles: profile `icon` property in Terminal settings.

These targets are the first real rollout phase because they are reversible and do not require registry edits in this skeleton.

## Registry-backed targets

Use registry-backed changes only after backup/export and only for documented, narrow targets:

- File type icons through selected `ProgID\DefaultIcon` values.
- Drive icons through `Explorer\DriveIcons\<DriveLetter>\DefaultIcon`.

The mapping CSVs define planned registry paths. Dry-run scripts read those paths and report missing future icon files. The apply script is gated behind `-Apply`.

## Backup/export expectations

Before future registry changes, export relevant keys to `windows/registry/rollback/` or another explicit backup folder:

```powershell
reg export HKCU\Software\Classes windows\registry\rollback\hkcu-classes-before-sauriil.reg /y
reg export HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\DriveIcons windows\registry\rollback\driveicons-before-sauriil.reg /y
```

If a restore point is used, create it manually before apply mode.

## Third-party tool risk order

Preferred order:

1. Native Windows methods.
2. CustomFolder / FolderIco for folder-specific styling.
3. IconPackager for broader icon-pack experiments.
4. Winaero Tweaker for narrow reversible tweaks.
5. Start11 / StartAllBack for Start/taskbar layout only.
6. Windhawk for specific shell behavior experiments.
7. ExplorerPatcher only if behavior restoration is needed, not for icon identity.
8. 7TSP only in a VM or after a full system image backup.

## Rollback expectations

Rollback must restore shortcut backups, import `.reg` backups, remove drive-icon overrides, restore folder defaults, revert Windows Terminal profile icon entries, and refresh Explorer/icon cache. The rollback script is also dry-run gated.
