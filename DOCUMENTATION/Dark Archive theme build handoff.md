# Sauriil Dark Archive — WinRAR Theme Build Handoff

## Purpose

This document explains how the `Sauriil Dark Archive` WinRAR theme was created, what worked, what did not work, how the icons were generated/processed, and how the final `.theme.rar` should be built.

It is intended as a handoff for the next GPT or developer continuing the theme work.

---

## Final target

Theme name:

```txt
Sauriil Dark Archive
```

Preferred final theme archive name:

```txt
SauriilDarkArchive.48x48.HQ.theme.rar
```

Chosen toolbar size:

```txt
48x48
```

Reason: `128x128` icons looked huge in WinRAR’s toolbar. `48x48` was the best balance between readability and visual richness.

---

## WinRAR theme format facts used

A WinRAR theme is a real **RAR archive** with a `.theme.rar` extension.

It must contain this file in the archive root:

```txt
winrar_theme_description.txt
```

Toolbar icons go inside:

```txt
Toolbar/
```

The toolbar button size is detected from:

```txt
Toolbar/Add.png
```

or, in older BMP-based themes:

```txt
Toolbar/Add.bmp
```

PNG toolbar graphics are supported by modern WinRAR versions.

Important: a renamed ZIP is not technically correct. It may open in WinRAR, but a proper final theme should be built as a real RAR archive using WinRAR itself.

Official references used during the process:

```txt
https://www.win-rar.com/themes-new.html
https://www.rarlab.com/themes.htm
```

---

## Major limitation discovered

A WinRAR theme does **not** fully reskin the whole WinRAR window.

It can replace graphics such as:

```txt
Toolbar icons
RAR.ico
SFX.ico
REV.ico
Setup.ico
DiskOn.ico
DiskOff.ico
PasswordOn.ico
PasswordOff.ico
AboutLogo
WizardLogo
SFXLogo
Estimate
FolderUp
DragCopy.cur
DragMove.cur
DragNo.cur
```

It cannot normally replace:

```txt
the file-list background
the menu bar styling
the full titlebar/window frame
the table rows and columns
the full application chrome
```

So the realistic target is:

```txt
dark WinRAR mode + complete Sauriil icon/logo/status asset replacement
```

not a full custom parchment/metal UI skin.

---

## Process summary

### 1. Concept board phase

A visual concept board was generated first.

It showed the intended direction:

```txt
black forged steel
ash parchment
red ritual seals
Daedric-like angular engraving
Velothi / Tribunal occult geometry
faint Aetherius cyan edge-light
restrained pale-gold Aldmeri refinement
```

The concept board looked close to the desired fantasy/UI direction, but it was only an art-direction preview. It could not be installed as a WinRAR theme.

---

### 2. First installable theme attempt

A rough theme folder was created with:

```txt
winrar_theme_description.txt
Toolbar/*.png
root ICO files
preview/logo placeholders
```

A `.theme.rar` file was also produced, but the environment could not write real RAR archives, so it was effectively a ZIP-format archive renamed to `.theme.rar`.

This was useful as a prototype but not a proper final theme.

The user rebuilt the source as a real RAR using WinRAR, which allowed the theme to install.

---

### 3. Size correction

The first toolbar icons were `128x128`.

Result:

```txt
icons were enormous in the WinRAR toolbar
```

Reason:

```txt
WinRAR detects toolbar icon size from Toolbar/Add.png
```

So smaller variants were created:

```txt
32x32
48x48
64x64
```

The user chose:

```txt
48x48
```

---

### 4. Taskbar/icon issue

The toolbar icons worked, but the Windows taskbar/running-app icon looked tiny.

Reason:

```txt
Toolbar PNGs do not control the Windows taskbar/running application icon.
The root ICO files, especially RAR.ico, affect archive/app/file icon behavior.
The pinned WinRAR taskbar shortcut may still use WinRAR.exe or Windows icon cache.
```

A taskbar-focused standalone icon was created:

```txt
SauriilDarkArchive_taskbar_icon.ico
```

and a taskbar-fixed source package was created.

For pinned taskbar use, the practical fix is:

```txt
Create or edit a WinRAR shortcut
Properties > Change Icon
select SauriilDarkArchive_taskbar_icon.ico
unpin old WinRAR shortcut
pin the corrected shortcut
```

---

### 5. High-quality icon generation phase

A higher-quality icon sheet was generated to push the result closer to the concept board.

The icon style target was:

```txt
semi-realistic premium dark fantasy icon art
black forged steel
red wax / blood seals
pale-gold trim
cyan magical system glow
clear silhouettes
48x48 readability
```

A chroma-green background was used for extraction:

```txt
#00FF00
```

The reason was to make the icons easier to isolate from the sheet.

Generated sprite sheets were grouped as:

```txt
Add, ExtractTo, Test, View, Delete
Find, Print, Wizard, Convert, Info
Exit, Repair, Extract, VirusScan, Comment
Protect, Lock, SFX, Report, Benchmark
RAR, SFX, REV, Setup, DiskOn, DiskOff, PasswordOn, PasswordOff
```

The processing script:

1. detected green background pixels,
2. converted them to alpha,
3. found connected non-background components,
4. cropped each icon,
5. fit each toolbar icon into a `48x48` transparent PNG canvas,
6. fit root icons into multi-size `.ico` files.

---

### 6. Final user-provided asset phase

The user later uploaded a ZIP containing manually prepared/high-quality transparent PNGs:

```txt
New Project (27).zip
```

It contained 28 PNGs:

```txt
20 toolbar icons
8 root/archive/app/status icons
```

Those assets were structured into the final source package:

```txt
SauriilDarkArchive_HQ_48x48_structured.zip
```

This is currently the best working source package.

---

## Final structured package

Current best package:

```txt
SauriilDarkArchive_HQ_48x48_structured.zip
```

Preview:

```txt
SauriilDarkArchive_HQ_48x48_structured_preview.png
```

Expected internal structure:

```txt
SauriilDarkArchive_HQ_48x48_structured/
├─ SauriilDarkArchive/
│  ├─ winrar_theme_description.txt
│  ├─ RAR.ico
│  ├─ SFX.ico
│  ├─ REV.ico
│  ├─ Setup.ico
│  ├─ DiskOn.ico
│  ├─ DiskOff.ico
│  ├─ PasswordOn.ico
│  ├─ PasswordOff.ico
│  └─ Toolbar/
│     ├─ Add.png
│     ├─ Benchmark.png
│     ├─ Comment.png
│     ├─ Convert.png
│     ├─ Delete.png
│     ├─ Exit.png
│     ├─ Extract.png
│     ├─ ExtractTo.png
│     ├─ Find.png
│     ├─ Info.png
│     ├─ Lock.png
│     ├─ Print.png
│     ├─ Protect.png
│     ├─ Repair.png
│     ├─ Report.png
│     ├─ SFX.png
│     ├─ Test.png
│     ├─ View.png
│     ├─ VirusScan.png
│     └─ Wizard.png
├─ SourcePNGs/
│  ├─ Toolbar/
│  └─ RootIcons/
├─ asset_mapping.csv
└─ README_INSTALL.txt
```

---

## Final asset mapping

The final upload used generic file names like `New Project (15).png`. These were mapped into WinRAR theme names as follows.

### Toolbar icons

| Source file | Final file |
|---|---|
| `New Project (15).png` | `Toolbar/Add.png` |
| `New Project (16).png` | `Toolbar/ExtractTo.png` |
| `New Project (17).png` | `Toolbar/Test.png` |
| `New Project (18).png` | `Toolbar/View.png` |
| `New Project (19).png` | `Toolbar/Delete.png` |
| `New Project (10).png` | `Toolbar/Find.png` |
| `New Project (11).png` | `Toolbar/Print.png` |
| `New Project (12).png` | `Toolbar/Wizard.png` |
| `New Project (13).png` | `Toolbar/Convert.png` |
| `New Project (14).png` | `Toolbar/Info.png` |
| `New Project (5).png` | `Toolbar/Exit.png` |
| `New Project (6).png` | `Toolbar/Repair.png` |
| `New Project (7).png` | `Toolbar/Extract.png` |
| `New Project (8).png` | `Toolbar/VirusScan.png` |
| `New Project (9).png` | `Toolbar/Comment.png` |
| `New Project.png` | `Toolbar/Protect.png` |
| `New Project (1).png` | `Toolbar/Lock.png` |
| `New Project (2).png` | `Toolbar/SFX.png` |
| `New Project (3).png` | `Toolbar/Report.png` |
| `New Project (4).png` | `Toolbar/Benchmark.png` |

### Root ICO files

| Source file | Final file |
|---|---|
| `New Project (20).png` | `RAR.ico` |
| `New Project (21).png` | `SFX.ico` |
| `New Project (22).png` | `REV.ico` |
| `New Project (23).png` | `Setup.ico` |
| `New Project (24).png` | `DiskOn.ico` |
| `New Project (25).png` | `DiskOff.ico` |
| `New Project (26).png` | `PasswordOn.ico` |
| `New Project (27).png` | `PasswordOff.ico` |

---

## Image processing details

### Toolbar PNG processing

Each uploaded source PNG was:

```txt
opened as RGBA
trimmed to non-transparent content
scaled proportionally into a 48x48 canvas
kept transparent
saved as PNG
```

Final toolbar files are:

```txt
48x48
PNG
RGBA / transparent background
```

### ICO processing

Each root icon source PNG was:

```txt
opened as RGBA
trimmed to non-transparent content
fit into a 256x256 transparent canvas
saved as a multi-size ICO
```

ICO sizes included:

```txt
16x16
24x24
32x32
48x48
64x64
128x128
256x256
```

This was done for:

```txt
RAR.ico
SFX.ico
REV.ico
Setup.ico
DiskOn.ico
DiskOff.ico
PasswordOn.ico
PasswordOff.ico
```

---

## `winrar_theme_description.txt`

Current content:

```txt
title=Sauriil Dark Archive 48x48 HQ
about=Sauriil Dark Archive\nHigh-quality dark fantasy archive icon theme\nToolbar: 48x48
```

Note: WinRAR officially expects a plain ASCII description file. Keep this file in the root of the final theme archive.

---

## How to build the final `.theme.rar`

Use the current structured ZIP as the source.

1. Extract:

```txt
SauriilDarkArchive_HQ_48x48_structured.zip
```

2. Open this folder:

```txt
SauriilDarkArchive/
```

3. Select the **contents** of `SauriilDarkArchive/`, not the folder itself.

Correct selected contents should include:

```txt
winrar_theme_description.txt
RAR.ico
SFX.ico
REV.ico
Setup.ico
DiskOn.ico
DiskOff.ico
PasswordOn.ico
PasswordOff.ico
Toolbar/
```

4. Right-click the selected files/folders.

5. Choose:

```txt
WinRAR > Add to archive...
```

6. Set archive format to:

```txt
RAR
```

7. Name it:

```txt
SauriilDarkArchive.48x48.HQ.theme.rar
```

8. Open the created `.theme.rar` file with WinRAR.

9. WinRAR should install the theme.

10. Select it under:

```txt
Options > Themes
```

Optional:

```txt
Options > Themes > Organize themes > Apply to archive icons
```

Use this if the user wants archive file icons to change too.

---

## Common mistakes

### Mistake: building ZIP and renaming it to `.theme.rar`

This is not a proper final theme.

Correct:

```txt
real RAR archive + .theme.rar extension
```

### Mistake: archiving the parent folder

Incorrect root:

```txt
SauriilDarkArchive/
    winrar_theme_description.txt
```

Correct archive root:

```txt
winrar_theme_description.txt
Toolbar/
RAR.ico
...
```

When creating the RAR, select the **contents** of `SauriilDarkArchive/`.

### Mistake: using 128x128 toolbar icons

`128x128` technically works, but it makes the toolbar huge.

Use:

```txt
48x48
```

### Mistake: expecting full window skinning

WinRAR themes cannot fully repaint the application UI. They mostly replace icons and auxiliary graphics.

---

## Current quality assessment

The current theme now works and has a much stronger art direction than the first prototype.

Strengths:

```txt
coherent red/black/cyan/gold visual system
48x48 toolbar scale works
root ICOs are included
archive/taskbar icon issue is partly handled
source PNGs are preserved
mapping is documented
```

Remaining weaknesses:

```txt
the full WinRAR window cannot become parchment/black-metal through theme files alone
some auxiliary graphics are still missing or could be improved
icons are high-detail and may need further readability tuning at 48x48
```

---

## Recommended next improvement pass

The next GPT should create a fuller theme package by adding or refining:

```txt
AboutLogo.png
WizardLogo.png
SFXLogo.png
ThemePreview.png
ToolbarPreview.png
Estimate.png
FolderUp.png
DragCopy.cur
DragMove.cur
DragNo.cur
```

Suggested visual treatments:

```txt
AboutLogo.png      -> dark parchment plaque with Sauriil Dark Archive title
WizardLogo.png     -> masked archivist / Listener bust
SFXLogo.png        -> vertical black reliquary archive-machine
ThemePreview.png   -> small screenshot-like preview board
ToolbarPreview.png -> clean toolbar icon strip
Estimate.png       -> cosmology gauge / archive weight meter
FolderUp.png       -> tiny black-metal upward archive arrow
DragCopy.cur       -> cyan duplicate-rune cursor
DragMove.cur       -> cyan/red transfer-rune cursor
DragNo.cur         -> red void prohibition cursor
```

If continuing, do **not** start from the older rough ZIPs. Start from:

```txt
SauriilDarkArchive_HQ_48x48_structured.zip
```

and treat it as the current source truth.

---

## Design identity to preserve

Core phrase:

```txt
A Sithis-sealed Daedric archive-machine: a black reliquary for compressed worlds.
```

Dominant identity:

```txt
red/black Sithis-Dark Brotherhood ritual
```

Secondary identity:

```txt
Velothi / Tribunal occult archivist
```

Tertiary subtle identity:

```txt
High Elf / Aldmeri elegance through symmetry, pale-gold filigree, disciplined geometry, and refined ornament
```

Avoid:

```txt
generic neon gamer aesthetics
cartoon style
copied Elder Scrolls symbols
copied Dark Brotherhood handprints
copied Aldmeri crests
copied WinRAR branding/icons
unreadable visual clutter
```

Preferred visual ingredients:

```txt
black forged steel
ash parchment
red ritual seals
angular glyph engraving
occult circular geometry
faint cyan edge-light
restrained pale-gold trim
strong silhouettes
48x48 readability
```
