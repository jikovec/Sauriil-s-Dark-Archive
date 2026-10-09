# Linux / KDE Plasma Plan

## Status

This file defines the accepted Linux/KDE target plan. It is not proof that the current installer already satisfies every preflight/rollback invariant.

Current implementation gap [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2) tracks preflight-before-mutation and desktop-override mapping semantics. Do not use live install as repository validation.

## Primary Target

Arch Linux with KDE Plasma is the primary Linux target. The project uses a freedesktop/XDG icon-theme layout so the asset structure remains broadly portable, while KDE is the first intended verification target.

## Per-User Install Boundary

Install only to user scope:

```text
$HOME/.local/share/icons/Sauriil-Dark-Archive
```

Desktop overrides, when actually defined and managed, belong only under:

```text
$HOME/.local/share/applications
```

Do not write to `/usr/share/icons` or `/usr/share/applications`.

## Theme Metadata

The theme metadata is:

```text
linux/Sauriil-Dark-Archive/index.theme
```

It inherits `breeze,hicolor` so missing icons can fall back rather than requiring modification of system-owned themes.

## Directory Model

The repository includes scalable placeholder contexts plus fixed PNG fallback directories from `16x16` through `256x256`. `v0.0.2` does not claim true scalable SVG artwork.

## Desktop Override Contract

For a future managed override:
1. define a real source override in repository mappings/source;
2. validate every required/active row and source before any installed-theme mutation;
3. copy only the managed override to user scope;
4. record exactly what the project installed so rollback cannot delete unrelated files;
5. rebuild relevant user caches only after successful install.

Empty/missing required override paths must have one explicit schema meaning and must not trigger a failure after the theme has already been replaced. Resolution is tracked in #2.

## MIME Icon Strategy

Use standard MIME-style icon names where `/` becomes `-`, such as:
- `application-x-rar`
- `application-zip`
- `text-x-python`
- `text-x-script`

## Cache Refresh

After a future authorized and successful install:

```bash
gtk-update-icon-cache -f -t "$HOME/.local/share/icons/Sauriil-Dark-Archive" || true
kbuildsycoca6 --noincremental || true
```

Cache deletion is troubleshooting, not the default workflow.

## Rollback

Rollback is user-scoped and must remove only state actually managed by this project. See [rollback.md](rollback.md).

Current live install/rollback behavior remains unproven until #2 and the related regression-verification work in [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4) are resolved and verified.
