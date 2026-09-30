# Windows 11 Plan

## Status

This file defines the accepted Windows target plan. It is not proof that current apply/rollback scripts already conform to the plan.

Current implementation gap [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3) tracks stable icon storage, backup verification, prior-state recording, and lossless rollback. Do not run live registry apply based on this plan alone.

## Strategy

Use a native-first, backup-first Windows strategy. Windows is not a true OS-wide icon-theme platform, so the project separates native targets from registry-backed and third-party-assisted targets.

## Stable Icon Storage Path

Before any registry/shortcut reference is applied, icons should be staged in:

```text
%LOCALAPPDATA%\SauriilDarkArchive\icons\
```

Do not point persistent Windows configuration at repository, temporary, build, or removable paths.

## Native-First Targets

Prefer native Windows methods for:
- desktop/Start-menu Win32 shortcuts;
- pinned taskbar items via their source shortcut;
- project folders;
- Desktop Icon Settings targets;
- Windows Terminal profile icons.

These are preferable to broad shell/resource patching because their scope and rollback are easier to reason about.

## Registry-Backed Targets

Registry-backed changes are limited to documented narrow targets such as:
- selected `ProgID\DefaultIcon` values;
- `Explorer\DriveIcons\<DriveLetter>\DefaultIcon`.

Before the first mutation, the implementation must:
1. validate every required source/mapping/input;
2. stage icons at the stable user-owned path;
3. capture whether each managed key/value existed and its exact prior value;
4. verify backup/state capture succeeded;
5. construct the apply plan;
6. only then mutate registry state.

The `-Apply` flag is an authorization gate, not a substitute for these invariants.

## Backup And Rollback Contract

Rollback must restore an existing prior value exactly or remove state created by Sauriil when no prior value existed. A failed backup/preflight must cause no registry mutation.

See [rollback.md](rollback.md) and #3.

## Third-Party Tool Risk Order

Preferred order:
1. Native Windows methods.
2. CustomFolder / FolderIco for folder-specific styling.
3. IconPackager for broader icon-pack experiments.
4. Winaero Tweaker for narrow reversible tweaks.
5. Start11 / StartAllBack for Start/taskbar layout only.
6. Windhawk for isolated shell behavior experiments.
7. ExplorerPatcher only if behavior restoration becomes a separate requirement.
8. 7TSP only in a VM or after a full system image backup.

Third-party tools are not required for the current v0.0.2 asset/proof baseline.
