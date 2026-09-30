# Rollback

Rollback is a live-state operation when run in apply mode. It requires explicit authorization and must be verified separately from repository delivery.

## Current Caveats

- Windows lossless rollback is not yet established for registry keys/values that did not exist before apply. See [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).
- Non-destructive regression verification for apply/rollback invariants is tracked in [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).
- Linux install/preflight consistency is tracked in [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2).

Do not treat the commands below as proof that these gaps are resolved.

## Windows Registry Rollback

Current dry-run:

```powershell
pwsh ./scripts/rollback/windows_rollback_icons.ps1
```

Current apply mode:

```powershell
pwsh ./scripts/rollback/windows_rollback_icons.ps1 -Apply
```

The accepted target behavior is to restore the exact pre-apply state, including the distinction between an existing value and a value/key created by Sauriil. Current implementation work to reach that contract is tracked in #3.

## Windows Shortcut / Cache Recovery

Shortcut recovery remains manual unless a work item introduces explicit backed-up shortcut state. For pinned items, restore the source shortcut then re-pin if needed.

After an authorized rollback, refresh Explorer/icon cache only when necessary:

```bat
ie4uinit.exe -show
taskkill /F /IM explorer.exe
start explorer.exe
```

Aggressive cache deletion is not the default path.

## Linux Theme Rollback

Dry-run:

```bash
bash scripts/rollback/linux_rollback_user_theme.sh
```

Apply mode:

```bash
bash scripts/rollback/linux_rollback_user_theme.sh --apply
```

The intended boundary is user scope only:
- `$HOME/.local/share/icons/Sauriil-Dark-Archive`
- explicitly managed overrides under `$HOME/.local/share/applications`

Do not delete unrelated user `.desktop` files. Future verified rollback evidence must demonstrate that only artifacts actually managed by this project are removed.

## Evidence

A rollback is not verified merely because the script exits successfully. Record pre-state, action, resulting state, and—where applicable—restoration/removal of exactly the state introduced by apply.
