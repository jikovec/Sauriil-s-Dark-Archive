# Asset Guidelines

## Visual identity

Future real icons must preserve:

- black forged steel
- ash parchment
- blood-red ritual seals
- subtle cyan magical/system glow
- restrained pale-gold filigree
- occult circular geometry
- strong silhouettes
- readable small-size icons
- semi-realistic premium dark fantasy rendering

Avoid generic neon gamer styling, cartoon styling, copied Elder Scrolls symbols, copied Dark Brotherhood handprints, copied Aldmeri crests, copied Microsoft/KDE/GNOME/Arch/WinRAR marks, and unreadable filigree noise.

## Skeleton art status

This skeleton contains no icon art. It contains no PNG, SVG, ICO, CUR, or placeholder image files.

## Windows `.ico` matrix

Future Windows icons should be exported as multi-size `.ico` files with at least:

```txt
16, 24, 32, 48, 64, 128, 256
```

Premium exports may later add intermediate sizes if Windows scaling tests prove a need.

## Linux SVG + PNG fallback matrix

Future Linux assets should include:

- scalable SVG in the correct context directory
- PNG fallbacks at `16, 24, 32, 48, 64, 128, 256`
- simplified symbolic SVGs for symbolic/action/status use cases

## 48x48 readability rule

`48x48` is the identity proof size. If the object does not read at `48x48`, the design is too detailed for this project.

## 16/24 simplification rule

`16x16` and `24x24` variants should not be blind downscales of painterly masters. Use simplified silhouettes, fewer interior cuts, less glow, and stronger contrast.

## Padding and safe area

Use transparent padding. Keep the main silhouette inside a safe area of roughly 80–88% of the canvas. Avoid excessive padding because it makes icons look tiny in Explorer, taskbar, Dolphin, and panels.

## Contact sheets

Future real icons should be rendered into contact sheets at `16, 24, 32, 48, 64, 128, 256` and tested on dark, gray, parchment, light, and transparent backgrounds.
