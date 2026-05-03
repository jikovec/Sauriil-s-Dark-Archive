# Third-Party Tool Risk

## Native Windows methods

Use native methods first. They are easiest to understand and reverse: shortcut icon changes, folder customization, Desktop Icon Settings, and Windows Terminal profile icons.

## CustomFolder / FolderIco

Useful for folder-specific icon styling. Risk is low to medium because changes are usually folder metadata or tool-managed folder icon assignments. They do not solve file type icons or shell chrome.

## IconPackager

Best candidate for broad Windows icon-pack experiments after native proof. Risk is medium because it changes broader shell icon associations and may need tool-level rollback.

## Winaero Tweaker

Useful for narrow shell and registry-backed cosmetic tweaks. It is not the core icon-pack solution. Use only with documented rollback and registry backup.

## Start11 / StartAllBack

Useful for Start/taskbar layout and shell behavior. They are not true icon artwork replacement systems. Treat them as optional UI-layout tools.

## Windhawk

Runtime shell modification framework. Use only for specific, isolated behavior experiments. Do not treat it as a safe full icon-theme mechanism.

## ExplorerPatcher

Behavior restoration and shell-patching utility. Not recommended for icon identity. Use only if shell behavior itself becomes a separate project requirement.

## 7TSP

VM/full-backup-only. It is excluded from the normal path because it belongs to system-resource patching territory and can break after Windows updates.

## Project order

1. Native Windows methods.
2. CustomFolder / FolderIco.
3. IconPackager.
4. Winaero Tweaker.
5. Start11 / StartAllBack.
6. Windhawk.
7. ExplorerPatcher.
8. 7TSP only in VM or after full image backup.
