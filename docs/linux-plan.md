# Linux / KDE Plasma Plan

## Primary target

Arch Linux with KDE Plasma is the primary Linux target. The project uses a standard freedesktop/XDG icon-theme layout so that most of the work remains portable to GNOME and XFCE, but KDE is the first verification target.

## Per-user install path

Install only to user scope:

```txt
$HOME/.local/share/icons/Sauriil-Dark-Archive
```

Do not write to `/usr/share/icons` in this skeleton or its scripts.

## Theme metadata

The starter theme file is:

```txt
linux/Sauriil-Dark-Archive/index.theme
```

It declares:

```ini
Name=Sauriil Dark Archive
Comment=Dark fantasy archive-machine icon theme skeleton
Inherits=breeze,hicolor
```

The theme inherits `breeze,hicolor` so missing icons fall back cleanly instead of vandalizing system-owned themes.

## Directory model

The skeleton includes:

- `scalable/apps`
- `scalable/mimetypes`
- `scalable/places`
- `scalable/devices`
- `scalable/status`
- `scalable/actions`
- `scalable/symbolic`
- fixed PNG fallback directories for `16x16` through `256x256`, grouped by context.

## Desktop override strategy

Do not edit `/usr/share/applications`.

For future app overrides:

1. Copy a system `.desktop` file into `linux/desktop-overrides/` for source control.
2. Change only the copied file's `Icon=` key to a theme icon name.
3. Install the override only to `$HOME/.local/share/applications` in explicit apply mode.
4. Rebuild KDE cache.

## MIME icon strategy

Use standard MIME-style icon names where `/` becomes `-`, for example:

```txt
application-x-rar
application-zip
text-x-python
text-x-script
```

Place future scalable MIME art in `scalable/mimetypes/` and PNG fallbacks under fixed-size `mimetypes/` directories.

## Cache refresh commands

After a real future install:

```bash
gtk-update-icon-cache -f -t "$HOME/.local/share/icons/Sauriil-Dark-Archive" || true
kbuildsycoca6 --noincremental || true
```

If KDE still shows stale icons, log out and back in. Cache deletion is a troubleshooting step, not the default workflow.

## Rollback

Rollback is user-scope only:

```bash
rm -rf "$HOME/.local/share/icons/Sauriil-Dark-Archive"
kbuildsycoca6 --noincremental || true
```

Remove only explicitly managed `.desktop` overrides from `$HOME/.local/share/applications`.
