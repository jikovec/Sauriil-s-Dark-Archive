# Asset Guidelines

## Visual identity

Real icons must preserve:

- black forged steel
- ash parchment
- blood-red ritual seals
- subtle cyan magical/system glow
- restrained pale-gold filigree
- occult circular geometry
- strong silhouettes
- readable small-size icons
- semi-realistic premium dark fantasy rendering

Avoid generic neon gamer styling, cartoon styling, copied Elder Scrolls symbols, copied Dark Brotherhood handprints, copied Aldmeri crests, copied Microsoft/KDE/GNOME/Arch/WinRAR/Python/browser/editor/file-manager marks, and unreadable filigree noise.

## Current art status

v0.0.2 contains the first real raster icon batch. The accepted source art is under `source/master/raster/`. It is generated raster art, not true vector art.

## Windows `.ico` matrix

Windows icons are exported as multi-size `.ico` files with at least:

```txt
16, 24, 32, 48, 64, 128, 256
```

v0.0.2 generated `.ico` outputs for apps, filetypes, and folders only.

## Linux SVG + PNG fallback matrix

Linux assets should ideally include scalable SVGs and PNG fallbacks. v0.0.2 intentionally uses PNG fallbacks only because no true vector source was created. Do not wrap raster PNGs in SVG and call that scalable vector art.

Generated PNG fallback sizes:

```txt
16, 24, 32, 48, 64, 128, 256
```

Generated Linux contexts in v0.0.2:

```txt
apps
places
mimetypes
```

## 48x48 readability rule

`48x48` is the identity proof size. If the object does not read at `48x48`, revise the design before marking it accepted.

v0.0.2 contact sheet:

```txt
source/master/contact-sheets/v0.0.2-contact-sheet-48.png
```

## 16/24 simplification rule

`16x16` and `24x24` variants should preserve the main silhouette and one dominant accent. They should not rely on filigree, text labels, subtle texture, or thin linework.

v0.0.2 uses simplified high-contrast source silhouettes rather than separate small-size master variants.

## Padding and safe area

Use transparent padding. Keep the main silhouette inside a safe area of roughly 80–88% of the canvas unless the concept requires a wider or lower profile. Avoid excessive padding because it makes icons look tiny in Explorer, taskbar, Dolphin, and panels.

## Contact sheets

Contact sheets must be regenerated after any visual asset change:

```bash
python scripts/test-render/render_contact_sheet.py --apply
```

v0.0.2 required sheets:

```txt
source/master/contact-sheets/v0.0.2-contact-sheet-16.png
source/master/contact-sheets/v0.0.2-contact-sheet-24.png
source/master/contact-sheets/v0.0.2-contact-sheet-32.png
source/master/contact-sheets/v0.0.2-contact-sheet-48.png
source/master/contact-sheets/v0.0.2-contact-sheet-256.png
```
