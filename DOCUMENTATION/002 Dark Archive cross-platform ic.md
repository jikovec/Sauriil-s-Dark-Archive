# Sauriil Dark Archive Cross-Platform Icon Customization Research + Implementation Plan

## 1. Executive Summary

**Assumptions:** This plan targets Windows 11 current stable behavior as of **2026-05-03**, meaning the Windows 11 24H2/25H2 servicing era. Microsoft lists Windows 11 25H2 as available to eligible devices, while 26H1 is scoped to new devices rather than a normal feature update path for existing 24H2/25H2 machines. ([Microsoft Learn][1]) For Linux, this assumes current Arch Linux with KDE Plasma 6-class behavior.

**Windows 11 realistic result:** high visual coverage is possible for **shortcuts, desktop icons, folders, many file types, drive icons, user-facing app shortcuts, Windows Terminal profiles, and selected shell objects**. Full control over **Explorer navigation glyphs, Settings icons, taskbar system status icons, packaged-app internal icons, and shell chrome** is not reliably supported without fragile shell hooks or system-resource patching.

**Arch Linux / KDE Plasma realistic result:** KDE is the stronger target. A proper XDG icon theme can affect **Dolphin, Plasma panels, launchers, application icons, MIME type icons, folders/places, devices, actions, status icons, and symbolic icons**, as long as applications respect the icon theme. KDE’s icon module explicitly applies Plasma icon themes across the desktop, panel, Dolphin, and toolbars. ([KDE Documentation][2])

**Safest strategy:** build a cross-platform asset system, then apply it in this order:

1. **Linux/KDE:** per-user XDG icon theme in `~/.local/share/icons`.
2. **Windows:** native shortcut/folder/Desktop Icon Settings methods first.
3. **Windows registry:** documented, reversible registry keys for file types and drives.
4. **Third-party tools:** only after backups; prefer tools that do not patch system resources.
5. **Avoid as default:** 7TSP-style system-resource patching.

**Main limitations:** Windows is not an OS-wide icon-theme platform. Linux is closer to one through the freedesktop/XDG icon theme model, but app-bundled icons, Flatpak/Snap confinement, tray/status icons, symbolic recoloring, and toolkit-specific behavior still limit full coverage.

---

## 2. Best Target Choice for Arch Linux

**Primary target: KDE Plasma on Arch Linux.**

KDE Plasma is the best Linux target for this project because it is visually icon-rich, exposes icon-theme selection directly in System Settings, and uses the standard Linux icon theme structure while still giving strong desktop-level coverage. KDE’s documentation says Plasma icons are used across the desktop, panel, Dolphin, and toolbars, and the Icons module lets users choose and install icon themes. ([KDE Documentation][2]) Arch Wiki’s KDE guidance also points users to **System Settings → Colors & Themes → Icons** for installing and changing icon themes. ([Arch Wiki][3])

**GNOME comparison:** GNOME also uses icon themes through GTK/freedesktop mechanisms, and the icon theme can be set with `org.gnome.desktop.interface icon-theme`, but GNOME is less favorable for this project because modern GNOME/libadwaita applications often keep stricter app identity and desktop-icon behavior is extension-dependent. ([Arch Wiki][4])

**XFCE comparison:** XFCE is highly compatible with GTK/XDG icon themes and exposes icon selection through its Appearance settings. It is easier to theme broadly than GNOME, but less visually central to this project than KDE Plasma. XFCE’s documentation states that its Icons tab affects icons in the panel, desktop, file manager, and menus. ([Xfce Docs][5])

**XDG compatibility:** most of the KDE plan remains portable because the core is a standard freedesktop icon theme: `index.theme`, named icon lookup, inheritance, `apps`, `mimetypes`, `places`, `devices`, `actions`, and `status`. KDE-specific work should stay limited to activation, cache refresh, and optional Plasma-specific testing.

---

## 3. Source Precedent: Sauriil Dark Archive

The WinRAR handoff establishes the current source truth: **48x48 toolbar PNGs**, transparent RGBA processing, trimming, proportional scaling, padding, and multi-size `.ico` exports were the working path. It also records the main practical lesson: `128x128` toolbar icons were too large, while `48x48` preserved usable visual richness. 

Carry forward these design rules:

* black forged steel base
* ash parchment contrast
* blood-red ritual seals
* subtle cyan magical/system glow
* restrained pale-gold filigree
* occult circular geometry
* strong silhouettes
* semi-realistic premium dark fantasy rendering
* readable small-size icons
* no copied official Elder Scrolls, Microsoft, KDE, GNOME, Arch, WinRAR, or other protected marks

**48x48 readability lesson:** treat `48x48` as the “identity proof” size. If an icon cannot read at `48x48`, it is too detailed. Microsoft’s app icon guidance similarly emphasizes scalable silhouettes and careful detail management around a `48x48` icon grid. ([Microsoft Learn][6])

**Windows `.ico` needs:** Windows icons should be exported as multi-size `.ico` files. Microsoft’s Windows app icon guidance recommends multiple sizes because Windows exact-matches icon sizes first and scales from the next larger size when needed. ([Microsoft Learn][7])

**Linux SVG/PNG needs:** Linux should use an XDG icon theme with scalable SVGs plus PNG fallbacks. The freedesktop icon theme model uses `index.theme`, directories, inheritance, and the `hicolor` fallback theme. ([specifications.freedesktop.org][8])

**Why exact app/window skinning is not always possible:** many applications draw their own UI, ship bundled assets, use packaged resources, or ignore system icon names. WinRAR already proved the pattern: the icon theme could replace toolbar/root assets, but not fully repaint the file-list background, titlebar, menu bar, or table chrome. 

---

## 4. Windows 11 Icon Customization Map

| Target                                                            | Native method                                                               | Registry method                                                                                                                                   | Third-party method                                                                 | Required format                        | Persistence after updates                            | Risk level                              | Rollback method                                                                                                             | Notes                                                                                                          |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Desktop shortcut icons                                            | Shortcut Properties → Change Icon                                           | Shell links can store icon path/index; Microsoft exposes this through `IShellLink::SetIconLocation`. ([Microsoft Learn][9])                       | Usually unnecessary                                                                | `.ico`, `.exe`, `.dll,index`           | High if icon path is stable                          | Low                                     | Change icon back or restore shortcut backup                                                                                 | Best first Windows target.                                                                                     |
| Pinned taskbar icons                                              | Change the source shortcut icon, unpin old shortcut, pin corrected shortcut | Managed taskbar layout XML can pin apps, but it is deployment policy, not icon artwork control. ([Microsoft Learn][10])                           | StartAllBack/Start11 can affect taskbar style/size; not a full icon-theme solution | `.ico` for shortcut                    | Medium; repinning may be needed                      | Low–Medium                              | Unpin/repin original shortcut                                                                                               | Avoid editing taskbar internal pinned data directly.                                                           |
| Start menu icons                                                  | Classic Win32 shortcuts can inherit changed shortcut icons                  | Windows 11 Start pins policy uses JSON for pinned layout, not arbitrary icon replacement. ([Microsoft Learn][11])                                 | Start11 can restyle Start; not a true icon-pack tool                               | `.ico`; packaged apps use app assets   | Medium                                               | Remove/re-pin app; restore shortcut     | Packaged/UWP/MSIX apps are harder.                                                                                          |                                                                                                                |
| Desktop system icons: This PC, Recycle Bin, Network, User’s Files | Settings → Personalization → Themes → Desktop icon settings                 | CLSID icon overrides exist but are less clean than native settings                                                                                | IconPackager                                                                       | `.ico`                                 | Medium–High                                          | Desktop Icon Settings → Restore Default | Microsoft documents native customization for This PC, Recycle Bin, Network, and User’s Files. ([support.microsoft.com][12]) |                                                                                                                |
| Folder icons                                                      | Folder Properties → Customize → Change Icon                                 | `desktop.ini` with `IconFile` and `IconIndex`; Microsoft documents `.ico` as preferred. ([Microsoft Learn][13])                                   | CustomFolder, FolderIco                                                            | `.ico`                                 | High for normal folders; medium for known folders    | Low                                     | Restore default; delete/reset `desktop.ini`                                                                                 | Best native method for themed project folders.                                                                 |
| User folders: Documents, Downloads, Pictures, etc.                | Folder Properties if exposed                                                | `desktop.ini`                                                                                                                                     | IconPackager / folder tools                                                        | `.ico`                                 | Medium; Windows may regenerate known-folder metadata | Low–Medium                              | Restore default `desktop.ini`                                                                                               | Test carefully before mass applying.                                                                           |
| File type icons                                                   | Default app Settings changes association, not artwork                       | `HKCR\<ProgID>\DefaultIcon`; use proper ProgID and avoid hard-coded paths. ([Microsoft Learn][14])                                                | IconPackager, Winaero Tweaker                                                      | `.ico`, `.exe`, `.dll,index`           | Medium; app updates can reset ProgIDs                | Medium                                  | Export registry first; import backup                                                                                        | Use only for selected file types.                                                                              |
| Default app deployment                                            | Settings UI for one user                                                    | DISM default association XML / policy CSP for managed deployment                                                                                  | Enterprise tools                                                                   | XML + registry-backed app declarations | High in managed contexts                             | Medium                                  | Remove policy/import previous XML                                                                                           | Microsoft documents exporting/importing default app associations with DISM and policy. ([Microsoft Learn][15]) |
| Drive icons                                                       | No broad modern Settings UI                                                 | `HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\DriveIcons\<DriveLetter>\DefaultIcon`; Microsoft documents this. ([Microsoft Learn][16]) | Winaero Tweaker                                                                    | `.ico`, `.exe`, `.dll,index`           | Medium                                               | Delete registry key/import backup       | Use for fixed drives only after registry export.                                                                            |                                                                                                                |
| Removable drive icons                                             | Limited AutoRun-era behavior                                                | `autorun.inf` can specify label/icon for AutoRun-enabled drives                                                                                   | Usually unnecessary                                                                | `.ico`                                 | Low–Medium; security policy dependent                | Low                                     | Remove `autorun.inf`                                                                                                        | Not reliable enough for main identity. ([Microsoft Learn][17])                                                 |
| Application shortcuts                                             | Shortcut Properties → Change Icon                                           | Shell link icon path/index                                                                                                                        | Usually unnecessary                                                                | `.ico`                                 | High                                                 | Restore shortcut                        | Good for VS Code, browsers, Git tools, editors, launchers.                                                                  |                                                                                                                |
| Windows Terminal / PowerShell profiles                            | Windows Terminal profile settings support custom profile icons              | Settings JSON profile `icon` property                                                                                                             | Not needed                                                                         | `.ico`, `.png` path                    | High if icon path stable                             | Low                                     | Remove `icon` property                                                                                                      | Terminal profile icons appear in tab, dropdown, jumplist, and switcher. ([Microsoft Learn][18])                |
| Explorer sidebar/navigation icons                                 | Mostly no supported global method                                           | Undocumented shell namespace/CLSID routes exist but are fragile                                                                                   | ExplorerPatcher/Windhawk may style behavior, not reliable icon identity            | Mixed                                  | Low after updates                                    | Medium–High                             | Disable tool/import registry backup                                                                                         | Treat as hard boundary unless testing in VM.                                                                   |
| System tray/status icons                                          | App/system controlled                                                       | Not cleanly supported                                                                                                                             | Windhawk can hide/tweak some tray system icons, not replace the full artwork set   | Mixed                                  | Low–Medium                                           | Medium–High                             | Disable Windhawk mod                                                                                                        | Do not plan full tray replacement. ([windhawk.net][19])                                                        |
| Icon cache refresh                                                | Restart Explorer; wait for cache rebuild                                    | Delete icon cache files only when needed                                                                                                          | Winaero/other tools may expose reset buttons                                       | N/A                                    | N/A                                                  | Low–Medium                              | Reboot / restore cache naturally                                                                                            | Use after icon changes; avoid aggressive cache deletion unless stuck. ([NinjaOne][20])                         |
| Full icon packs                                                   | No native system-wide icon pack feature                                     | Registry + shell association changes                                                                                                              | IconPackager                                                                       | `.ico` package assets                  | Medium                                               | Medium                                  | Use tool restore/default package                                                                                            | Best “broad Windows icon pack” option without system-file patching. ([stardock.com][21])                       |
| Deep shell/system-resource icons                                  | Not supported                                                               | Unsafe if manually editing system resources                                                                                                       | 7TSP                                                                               | Patched resources / icon pack          | Low after updates                                    | High–Very High                          | Restore point/image backup                                                                                                  | Not recommended as normal path; 7TSP-style packs patch resource files. ([deviantart.com][22])                  |

---

## 5. Arch Linux / KDE Plasma Icon Customization Map

| Target                     | Recommended method                                           | File/theme location                                                          | Required format                     | Cache refresh needed                       | Persistence after updates                           | Risk level       | Notes                                                                                                                        |
| -------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------ | --------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Per-user global icon theme | Install custom XDG theme                                     | `~/.local/share/icons/Sauriil-Dark-Archive/`                                 | SVG + PNG fallbacks + `index.theme` | Yes, plus KDE refresh                      | High                                                | Low              | Safest main path.                                                                                                            |
| System-wide icon theme     | Optional root install                                        | `/usr/share/icons/Sauriil-Dark-Archive/`                                     | Same as per-user                    | Yes                                        | Medium; package manager/admin changes may affect it | Medium           | Only after per-user proof.                                                                                                   |
| KDE Plasma activation      | System Settings → Colors & Themes → Icons                    | KDE config                                                                   | Theme directory                     | KDE refresh / relog if needed              | High                                                | Low              | KDE’s official Icons module is the primary activation path. ([KDE Documentation][2])                                         |
| Application icons          | Theme `apps/` names and/or `.desktop` overrides              | Theme: `apps/`; overrides: `~/.local/share/applications/`                    | SVG/PNG; `Icon=name` preferred      | `kbuildsycoca6` useful                     | High for per-user override                          | Low              | Desktop Entry `Icon=` uses absolute path directly or resolves themed names. ([specifications.freedesktop.org][23])           |
| `.desktop` files           | Copy system `.desktop` file to user scope and change `Icon=` | `~/.local/share/applications/*.desktop`                                      | Text file + themed icon name        | `kbuildsycoca6 --noincremental`            | High                                                | Low              | Never edit `/usr/share/applications` directly unless packaging.                                                              |
| MIME type icons            | Provide named MIME icons in theme                            | `mimetypes/`, e.g. `application-x-rar.svg`                                   | SVG + PNG fallback                  | `gtk-update-icon-cache`; KDE service cache | High                                                | Low–Medium       | MIME icon names map `/` to `-`; freedesktop documents MIME `icon` and `generic-icon`. ([specifications.freedesktop.org][24]) |
| Folder/place icons         | Replace standard place names                                 | `places/`, `scalable/places/`, size dirs                                     | SVG/PNG                             | Yes                                        | High                                                | Low              | Covers folder, home, documents, downloads, desktop, trash, network locations where theme-respected.                          |
| Device icons               | Provide device names                                         | `devices/`                                                                   | SVG/PNG                             | Yes                                        | High                                                | Low              | Covers drives, removable media, optical media, where theme-respected.                                                        |
| Status icons               | Provide status names                                         | `status/`                                                                    | SVG/PNG + symbolic variants         | Yes                                        | Medium                                              | Low–Medium       | Apps may use bundled tray icons instead.                                                                                     |
| Action icons               | Provide action names                                         | `actions/`                                                                   | SVG/PNG + symbolic variants         | Yes                                        | Medium–High                                         | Low              | Useful for toolbar identity in KDE/Qt apps that respect theme icons.                                                         |
| Symbolic icons             | Provide monochrome symbolic SVGs                             | `symbolic/`, `actions`, `status`, or `*-symbolic.svg` depending theme layout | Simple SVG                          | Yes                                        | Medium                                              | Low              | Must be readable as one-color/recolorable glyphs.                                                                            |
| Scalable SVG icons         | Main Linux master assets                                     | `scalable/apps`, `scalable/mimetypes`, etc.                                  | SVG                                 | Usually yes after install/change           | High                                                | Low              | Best for KDE/Dolphin scaling.                                                                                                |
| PNG fallback sizes         | Add raster fallbacks                                         | `16x16`, `24x24`, `32x32`, `48x48`, `64x64`, `128x128`, `256x256`            | PNG RGBA                            | Yes                                        | High                                                | Low              | Required for highly detailed painterly icons.                                                                                |
| `index.theme`              | Define theme metadata, directories, inheritance              | Theme root                                                                   | INI-like text                       | Yes                                        | High                                                | Low              | Must declare directories and inherit `breeze`/`hicolor` fallback.                                                            |
| `hicolor` fallback         | Inherit; do not overwrite by default                         | `/usr/share/icons/hicolor`                                                   | Existing system fallback            | Cache if touched                           | High but system-owned                               | Medium if edited | Arch Wiki notes many apps deposit icons in `hicolor`; custom theme should inherit it, not vandalize it. ([Arch Wiki][25])    |
| KDE cache refresh          | Rebuild service/icon visibility                              | User cache + KDE service cache                                               | N/A                                 | `kbuildsycoca6`; possible relog            | N/A                                                 | Low              | `kbuildsycoca6` builds KDE service cache for `.desktop` and MIME data. ([man.archlinux.org][26])                             |
| GTK icon cache             | Generate GTK icon cache                                      | Theme directory                                                              | `icon-theme.cache`                  | `gtk-update-icon-cache`                    | N/A                                                 | Low              | The GTK tool expects a theme directory with `index.theme`. ([linux.die.net][27])                                             |

---

## 6. Secondary Linux Desktop Notes

### GNOME

GNOME supports freedesktop/GTK icon themes, so core `apps`, `mimetypes`, `places`, and `devices` assets remain useful. The theme can be set through GNOME tooling or `gsettings set org.gnome.desktop.interface icon-theme <theme-name>`. ([Arch Wiki][4])

Limitations:

* GNOME desktop icons are not a core default experience and usually require an extension. ([Red Hat Documentation][28])
* GNOME/libadwaita applications may preserve their own application identity more strongly than KDE apps.
* Tray/status coverage is weaker without extensions.

### XFCE

XFCE is a good secondary target because it uses GTK/XDG icon themes and exposes icon-theme selection through Appearance settings. XFCE’s documentation states that its Icons tab controls icons in the panel, desktop, file manager, and menus, and it also documents `gtk-update-icon-cache`. ([Xfce Docs][5])

### Generic XDG / freedesktop behavior

Portable parts:

* `index.theme`
* icon inheritance
* named lookup through `Icon=`
* `apps`, `mimetypes`, `places`, `devices`, `actions`, `status`
* `hicolor` fallback
* MIME icon naming

Desktop-specific parts:

* settings UI
* cache refresh behavior
* panel/tray implementation
* symbolic icon recoloring
* desktop-icons behavior
* Flatpak/Snap sandbox interaction

Wayland/X11 note: the core icon theme lookup is not fundamentally Wayland- or X11-specific. The visible differences are more likely in panel/tray/status protocols and desktop-environment integration.

---

## 7. Recommended Asset Format Matrix

| Asset class                   | Recommended format                     | Sizes / rules                                                                                       | Notes                                                                                                                                        |
| ----------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows primary `.ico`        | Multi-size `.ico`                      | Practical set: `16, 24, 32, 48, 64, 128, 256`; premium set may add `20, 30, 36, 40, 60, 72, 80, 96` | Microsoft recommends multiple versions because Windows exact-matches sizes and otherwise scales from a larger size. ([Microsoft Learn][7])   |
| Windows source PNG            | Transparent RGBA PNG                   | Master at `512` or `1024`; export clean `256` and hand-check smaller sizes                          | Use transparent backgrounds; Microsoft notes transparent backgrounds generally look best. ([Microsoft Learn][7])                             |
| Windows shortcut/taskbar icon | `.ico`                                 | Must contain `32`, `48`, and `256` at minimum                                                       | Prevents tiny-looking pinned icons.                                                                                                          |
| Linux scalable icon           | SVG                                    | `scalable/<context>/<name>.svg`                                                                     | Best for KDE/Dolphin scaling.                                                                                                                |
| Linux PNG fallback            | PNG RGBA                               | `16, 24, 32, 48, 64, 128, 256`                                                                      | Needed because painterly fantasy icons may not reduce cleanly from SVG alone.                                                                |
| Linux symbolic icon           | Simple SVG                             | Usually `16`/`24` design grid; one-color or recolorable                                             | Avoid gradients, glow, tiny ornament.                                                                                                        |
| MIME icons                    | SVG + PNG fallback                     | Names such as `application-x-rar`, `application-zip`, `text-x-script`                               | Follow freedesktop MIME icon naming behavior. ([specifications.freedesktop.org][24])                                                         |
| Padding / safe area           | Transparent safe area                  | Outer padding around `8–12%`; silhouette should occupy roughly `80–88%`                             | Prevents tiny-looking icons.                                                                                                                 |
| Small-size testing            | Render sheet                           | Test at `16, 24, 32, 48, 64, 128, 256`                                                              | At `16/24`, silhouette beats detail. At `48`, identity must still read.                                                                      |
| Conversion tools              | ImageMagick, Inkscape, Pillow, icotool | Use toolchain only after source normalization                                                       | ImageMagick supports ICO multi-size writing; Pillow supports ICO save sizes; `icotool` can create/extract `.ico`/`.cur`. ([ImageMagick][29]) |

---

## 8. Recommended Cross-Platform Project Structure

```txt
sauriil-dark-archive-icons/
├─ source/
│  ├─ master/
│  │  ├─ raster/
│  │  ├─ vector/
│  │  └─ contact-sheets/
│  ├─ png/
│  │  ├─ 1024/
│  │  ├─ 512/
│  │  ├─ 256/
│  │  ├─ 128/
│  │  ├─ 64/
│  │  ├─ 48/
│  │  ├─ 32/
│  │  ├─ 24/
│  │  └─ 16/
│  ├─ svg/
│  │  ├─ full-color/
│  │  └─ symbolic/
│  └─ references/
│     ├─ sauriil-dark-archive-winrar/
│     ├─ palettes/
│     └─ visual-rules.md
├─ mappings/
│  ├─ windows-filetypes.csv
│  ├─ windows-shortcuts.csv
│  ├─ windows-drives.csv
│  ├─ linux-desktop-icons.csv
│  ├─ linux-mimetypes.csv
│  └─ linux-standard-names.csv
├─ windows/
│  ├─ ico/
│  │  ├─ apps/
│  │  ├─ filetypes/
│  │  ├─ folders/
│  │  ├─ drives/
│  │  └─ shell/
│  ├─ shortcuts/
│  ├─ registry/
│  │  ├─ dry-run/
│  │  ├─ apply/
│  │  └─ rollback/
│  ├─ iconpackager/
│  ├─ winaero/
│  └─ third-party-tool-notes/
├─ linux/
│  ├─ Sauriil-Dark-Archive/
│  │  ├─ index.theme
│  │  ├─ scalable/
│  │  │  ├─ apps/
│  │  │  ├─ mimetypes/
│  │  │  ├─ places/
│  │  │  ├─ devices/
│  │  │  ├─ status/
│  │  │  ├─ actions/
│  │  │  └─ symbolic/
│  │  ├─ 16x16/
│  │  ├─ 24x24/
│  │  ├─ 32x32/
│  │  ├─ 48x48/
│  │  ├─ 64x64/
│  │  ├─ 128x128/
│  │  └─ 256x256/
│  ├─ desktop-overrides/
│  ├─ mime-overrides/
│  ├─ kde/
│  ├─ gnome/
│  └─ xfce/
├─ scripts/
│  ├─ dry-run/
│  ├─ apply/
│  ├─ rollback/
│  ├─ convert/
│  ├─ test-render/
│  └─ validate/
└─ docs/
   ├─ windows-plan.md
   ├─ linux-plan.md
   ├─ asset-guidelines.md
   ├─ icon-name-mapping.md
   ├─ third-party-risk.md
   ├─ rollback.md
   └─ proof-checklist.md
```

Key rule: **source art and generated artifacts stay separate**. Never hand-edit generated `.ico` or theme fallback files without recording the source-layer reason.

---

## 9. Generation Pipeline Plan

### Source art preparation

Use a hybrid pipeline:

* **PNG-first** for semi-realistic premium fantasy icons.
* **SVG-first** for symbolic, action, status, and clean scalable Linux icons.
* Keep master art larger than target size, then manually inspect exports.

The WinRAR precedent already proved that high-detail assets need trimming, transparent RGBA, proportional scaling, and padding. 

### SVG-first tradeoff

Pros:

* crisp scaling
* good for Linux themes
* easy recoloring for symbolic icons
* clean integration with KDE/freedesktop themes

Cons:

* difficult to preserve painterly forged-metal/parchment richness
* complex SVGs can render inconsistently
* symbolic variants must be simplified anyway

### PNG-first tradeoff

Pros:

* best for premium semi-realistic visual identity
* predictable rendered result
* matches the existing WinRAR process

Cons:

* each size needs testing
* downscaling can blur details
* small icons may need separate simplified art

### Windows ICO generation concept

1. Start from transparent RGBA source.
2. Trim empty pixels.
3. Fit into square canvas with controlled safe area.
4. Export size layers.
5. Build `.ico` containing all required sizes.
6. Test in Explorer, taskbar, Start, shortcut Properties, and file association views.

Pillow supports `.ico` saving with a `sizes` list, and its documented default list includes `16, 24, 32, 48, 64, 128, 256`. ([Pillow (PIL Fork)][30]) ImageMagick can also write multi-size ICO files using `icon:auto-resize`. ([ImageMagick][29])

### Linux icon-theme generation concept

1. Generate full-color SVGs where practical.
2. Export PNG fallbacks for `16–256`.
3. Create symbolic variants separately.
4. Place assets into standard context directories.
5. Declare directories and inheritance in `index.theme`.
6. Inherit `breeze` and `hicolor`.
7. Refresh GTK/KDE caches.
8. Validate in Dolphin, Kickoff/Kicker, panel, file picker, and MIME views.

### Readability test protocol

For every icon:

* render at `16, 24, 32, 48, 64, 128, 256`
* test on black, dark gray, parchment, light, and transparent backgrounds
* compare against original silhouette
* reject icons where the object cannot be identified at `32`
* reject icons where the identity does not feel premium at `48`
* simplify `16/24` variants instead of blindly downscaling

Common failures to prevent:

* icons look tiny because padding is too large
* icons look blurry because only `256` was supplied
* red/cyan glow dominates object shape
* fine filigree becomes noise
* black-on-transparent disappears in dark UI
* symbolic icons contain too much full-color detail

---

## 10. Windows 11 Implementation Plan

### Native-only path

1. Create stable icon storage:

```txt
%LOCALAPPDATA%\SauriilDarkArchive\icons\
```

2. Copy `.ico` files there.
3. Change desktop shortcuts through Properties → Change Icon.
4. Change project folder icons through Properties → Customize.
5. Change This PC / Recycle Bin / User’s Files / Network through Desktop Icon Settings. Microsoft documents this native route under Personalization → Themes → Desktop icon settings. ([support.microsoft.com][12])
6. For Windows Terminal, set per-profile icons in Terminal settings or `settings.json`; Terminal supports an `icon` profile property. ([Microsoft Learn][18])
7. Rebuild/refresh icon cache only after verifying source paths are stable.

### Registry-assisted path

Use only for targets that native Settings cannot cover cleanly:

* file type icons via `ProgID\DefaultIcon`
* drive icons via `DriveIcons`
* selected shell object overrides only if fully backed up

Before registry changes:

```bat
reg export HKCU\Software\Classes "%USERPROFILE%\Desktop\sauriil-hkcu-classes-backup.reg"
reg export HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\DriveIcons "%USERPROFILE%\Desktop\sauriil-driveicons-backup.reg"
```

Optional restore point:

```powershell
Checkpoint-Computer -Description "Before Sauriil Dark Archive icon changes" -RestorePointType "MODIFY_SETTINGS"
```

Use `REG_EXPAND_SZ` and environment variables where possible. Microsoft’s file association guidance specifically warns against hard-coded paths and recommends expandable strings for paths under Windows directories. ([Microsoft Learn][31])

### Third-party-tool-assisted path

Recommended order:

1. **IconPackager** for broad icon-package behavior.
2. **CustomFolder / FolderIco** for mass folder styling.
3. **Winaero Tweaker** for narrow registry-backed cosmetic tweaks.
4. **Start11 / StartAllBack** only for Start/taskbar visual behavior, not icon pack replacement.
5. **Windhawk** only for specific shell behavior mods.
6. **7TSP** only in VM or after full image backup.

### Icon cache reset path

First try:

```bat
ie4uinit.exe -show
taskkill /F /IM explorer.exe
start explorer.exe
```

If still stale, use a more aggressive icon-cache rebuild. Current Windows maintenance guides commonly remove `%LocalAppData%\Microsoft\Windows\Explorer\iconcache*.db` after stopping Explorer, then restart Explorer or reboot. ([NinjaOne][20])

### Rollback plan

Rollback must be prepared before applying:

* restore shortcut backups
* restore default folder icons
* import `.reg` backups
* remove `DriveIcons` keys
* revert Windows Terminal profile `icon` entries
* switch IconPackager/Winaero/third-party tools back to default
* rebuild icon cache
* reboot if shell icons remain stale

### Safest phased rollout

**Windows Phase 1:** shortcuts, desktop icons, folder icons, Windows Terminal profile icons.

**Windows Phase 2:** selected file type icons and drive icons with registry exports.

**Windows Phase 3:** IconPackager package experiment.

**Windows Phase 4:** optional shell tools in VM only.

---

## 11. Arch Linux / KDE Plasma Implementation Plan

### Per-user install first

Install only to:

```txt
~/.local/share/icons/Sauriil-Dark-Archive/
```

Do not start with `/usr/share/icons`.

### Expected icon-theme folder layout

```txt
~/.local/share/icons/Sauriil-Dark-Archive/
├─ index.theme
├─ scalable/
│  ├─ apps/
│  ├─ mimetypes/
│  ├─ places/
│  ├─ devices/
│  ├─ status/
│  ├─ actions/
│  └─ symbolic/
├─ 16x16/
│  ├─ apps/
│  ├─ mimetypes/
│  ├─ places/
│  ├─ devices/
│  ├─ status/
│  └─ actions/
├─ 24x24/
├─ 32x32/
├─ 48x48/
├─ 64x64/
├─ 128x128/
└─ 256x256/
```

`index.theme` should declare directories and inherit fallback themes:

```ini
[Icon Theme]
Name=Sauriil Dark Archive
Comment=Dark fantasy archive-machine icon theme
Inherits=breeze,hicolor
Directories=scalable/apps,scalable/mimetypes,scalable/places,scalable/devices,scalable/status,scalable/actions,16x16/apps,24x24/apps,32x32/apps,48x48/apps,64x64/apps,128x128/apps,256x256/apps
```

The full file would need every generated directory declared, not only the shortened example above.

### KDE activation steps

1. Copy theme to `~/.local/share/icons`.
2. Open **System Settings → Colors & Themes → Icons**.
3. Select **Sauriil Dark Archive**.
4. Apply.
5. Test Dolphin, panel launcher, Kickoff/Kicker, file picker, MIME files, mounted devices, and common apps.

KDE’s official documentation supports choosing and installing icon themes through the Icons module. ([KDE Documentation][2])

### Cache refresh steps

Recommended after changes:

```bash
gtk-update-icon-cache -f -t ~/.local/share/icons/Sauriil-Dark-Archive
kbuildsycoca6 --noincremental
```

`gtk-update-icon-cache` creates an icon theme cache for a theme directory with `index.theme`, and `kbuildsycoca6` rebuilds KDE service cache for desktop/MIME service data. ([linux.die.net][27])

If KDE remains stale, log out/in. Only if still stuck, consider removing KDE icon cache files such as `~/.cache/icon-cache.kcache` and rebuilding, but treat that as a troubleshooting step, not normal workflow. ([bugs.kde.org][32])

### `.desktop` override strategy

For app icons:

1. Copy the target file:

```bash
cp /usr/share/applications/org.example.App.desktop ~/.local/share/applications/
```

2. Edit only the user copy:

```ini
Icon=sauriil-example-app
```

3. Place the icon in:

```txt
~/.local/share/icons/Sauriil-Dark-Archive/scalable/apps/sauriil-example-app.svg
```

4. Rebuild KDE cache:

```bash
kbuildsycoca6 --noincremental
```

The Desktop Entry spec states that an absolute `Icon=` path is used directly, while a non-absolute value is resolved through the Icon Theme Specification. Use themed names rather than absolute paths where possible. ([specifications.freedesktop.org][23])

### MIME icon strategy

1. Map priority file types:

   * archives
   * documents
   * scripts
   * images
   * code files
   * config files
   * project files

2. Provide icons under:

```txt
scalable/mimetypes/
48x48/mimetypes/
32x32/mimetypes/
16x16/mimetypes/
```

3. Use standard MIME-style icon names, such as:

```txt
application-x-rar.svg
application-zip.svg
text-x-script.svg
text-x-python.svg
image-x-generic.svg
```

The shared MIME-info spec defines MIME icon behavior and maps MIME type separators to icon-name hyphens. ([specifications.freedesktop.org][24])

### Rollback plan

1. In KDE Settings, switch back to Breeze/Breeze Dark.
2. Remove:

```txt
~/.local/share/icons/Sauriil-Dark-Archive/
```

3. Remove or restore user `.desktop` overrides:

```txt
~/.local/share/applications/*.desktop
```

4. Rebuild cache:

```bash
gtk-update-icon-cache -f -t ~/.local/share/icons/hicolor
kbuildsycoca6 --noincremental
```

5. Log out/in if needed.

### Safest phased rollout

**Linux Phase 1:** per-user theme with only `apps`, `places`, and `mimetypes`.

**Linux Phase 2:** add devices, actions, status, symbolic icons.

**Linux Phase 3:** add `.desktop` overrides for priority applications.

**Linux Phase 4:** optional system-wide packaging only after per-user proof.

---

## 12. Third-Party Tool Risk Review for Windows

| Tool            | What it can customize                                                      | What it cannot customize                                                          | Mechanism                                                        | Update fragility | Rollback path                                    | Risk           | Appropriate for this project                                                                                                                                                                   |
| --------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------- | ------------------------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IconPackager    | Broad Windows icon packages; individual file type icons; default icon sets | App-internal icons, many packaged app icons, system tray artwork, Explorer chrome | Icon package / shell icon association layer                      | Medium           | Restore default package in tool; registry backup | Medium         | Yes, best broad Windows option after native proof. Stardock describes it as replacing default Windows icons and file type icons. ([stardock.com][21])                                          |
| CustomFolder    | Folder icons/colors/emblems                                                | File types, taskbar, Start, shell resources                                       | Folder metadata/tool-managed icon assignment                     | Low–Medium       | Restore default folder icon                      | Low–Medium     | Yes for themed folders only. ([gdzsoft.com][33])                                                                                                                                               |
| FolderIco       | Folder icons, colors, stickers                                             | Full system theme                                                                 | Folder icon customization                                        | Low–Medium       | Restore folder defaults                          | Low–Medium     | Yes as alternative to CustomFolder. ([folderico.com][34])                                                                                                                                      |
| Winaero Tweaker | Shortcut arrows, overlay tweaks, various shell/registry cosmetics          | Full icon-pack replacement                                                        | Mostly registry/system setting frontend                          | Medium           | Revert tweak; registry backup                    | Medium-Low     | Useful for narrow tweaks, not core icon pack. ([winaerotweaker.com][35])                                                                                                                       |
| Start11         | Start menu/taskbar style, spacing, icon sizing behavior                    | True OS-wide icon theme                                                           | Shell UI replacement/customization                               | Medium           | Disable/uninstall                                | Medium         | Optional if Start visual layout matters. ([stardock.com][36])                                                                                                                                  |
| StartAllBack    | Taskbar/Explorer/Start behavior, icon sizing/margins                       | Actual icon artwork replacement                                                   | Shell UI hooks/replacement behavior                              | Medium           | Disable/uninstall                                | Medium         | Optional for taskbar layout, not icon theme. ([startallback.com][37])                                                                                                                          |
| Windhawk        | Explorer/taskbar/tray behavior mods; can hide/tweak some tray icons        | Full icon theme; safe guaranteed shell icon replacement                           | Runtime code-injection/mod framework                             | Medium–High      | Disable mod; exit/uninstall Windhawk             | Medium–High    | Only for specific shell behavior experiments. Windhawk itself is a customization marketplace, and tray mods focus on hiding/tweaking status icons, not replacing all art. ([windhawk.net][38]) |
| ExplorerPatcher | Taskbar/Start/Explorer behavior restoration and shell options              | Full custom icon pack                                                             | Explorer/taskbar shell behavior patching                         | High             | Disable/uninstall; restore point                 | Medium–High    | Not recommended as an icon solution. It is more relevant to shell behavior than icon identity. ([GitHub][39])                                                                                  |
| 7TSP            | Deep system icon/resource replacement                                      | App-controlled icons; safe update-proof theming                                   | Patches resources, including system resource areas in some packs | Very High        | Restore point or full image restore              | High–Very High | Not appropriate for the normal path. VM-only or full-backup experiment. 7TSP packs are associated with resource patching and `.mun`/system resource modification. ([deviantart.com][22])       |

**Safety/usefulness ranking for this project:**

1. Native Windows methods
2. Folder metadata tools: CustomFolder / FolderIco
3. IconPackager
4. Winaero Tweaker
5. Start11 / StartAllBack
6. Windhawk
7. ExplorerPatcher
8. 7TSP

---

## 13. Limitations and Hard Boundaries

### Cannot be themed reliably

* Windows Settings app internal icons
* Explorer sidebar/navigation glyphs
* taskbar system status icons as a full art set
* notification center system icons
* Windows Security / protected system surfaces
* Store/UWP/MSIX app internal assets
* app-bundled Electron/Qt/GTK icons that ignore OS theme
* websites/PWAs unless their shortcuts/icons are separately changed
* thumbnails and previews generated from file contents

### Requires unsafe or fragile patching

* replacing `shell32.dll`, `imageres.dll`, or modern `.mun` resources
* editing `C:\Windows\SystemResources`
* resource-hacking packaged app assets
* 7TSP-style full shell resource packs on a daily machine

### Breaks after OS or app updates

* system-resource patches
* undocumented CLSID icon overrides
* shell hooks
* Explorer/taskbar patchers
* app `.desktop` files edited directly under `/usr/share/applications`
* Linux system-wide theme files owned by packages

### App-controlled, not OS-controlled

* many tray icons
* in-app toolbar icons
* app-specific sidebars
* app splash screens
* app window chrome
* browser website favicons
* terminal prompt symbols
* icons embedded inside executable resources unless the app exposes customization

### Should be left alone

* Windows system files
* Windows protected resource directories
* KDE/GTK packaged system themes unless copied to user scope
* `/usr/share/applications` originals
* `/usr/share/icons/hicolor` as a primary customization target
* signed app package contents

---

## 14. Recommended Final Strategy

### Best overall path

**Windows 11:** build a curated `.ico` library and apply it through native methods first. Add registry-backed file type and drive icons only after backups. Use IconPackager only after the native/registry plan is proven. Do not use 7TSP on the daily system.

**Arch Linux / KDE Plasma:** build a full XDG icon theme named `Sauriil-Dark-Archive`, install it per-user, inherit `breeze,hicolor`, activate it through KDE Settings, then add `.desktop` overrides and MIME mappings.

### Phase 1 — Asset and skeleton proof

* Create folder structure.
* Create mapping files.
* Create placeholder icons.
* Build conversion scripts in dry-run mode.
* Validate naming and output paths.
* Produce contact sheets for size review.

### Phase 2 — Safe user-scope application

Windows:

* shortcuts
* desktop icons
* folders
* Windows Terminal profiles
* selected development tools

Linux/KDE:

* per-user icon theme
* KDE activation
* app icons
* MIME icons
* places/folders/devices

### Phase 3 — Controlled deeper coverage

Windows:

* file type registry icons
* drive icons
* IconPackager experiment
* Winaero/CustomFolder support
* no 7TSP unless VM/full backup

Linux:

* symbolic icons
* status/action icons
* curated `.desktop` overrides
* optional system-wide package only after proof

### “Done” for Windows 11

Done means:

* all priority desktop shortcuts use Sauriil icons
* pinned taskbar shortcuts use corrected `.ico` files
* Start menu classic shortcuts use corrected icons where possible
* This PC / Recycle Bin / User’s Files / Network are themed through native settings or safely reverted overrides
* priority folders use themed icons
* priority file types use documented ProgID-backed icons
* fixed drives use documented `DriveIcons` overrides if desired
* Windows Terminal profiles show themed icons
* icon cache refresh works
* rollback has been tested

### “Done” for Arch Linux / KDE Plasma

Done means:

* `Sauriil-Dark-Archive` appears in KDE icon settings
* theme activates without errors
* Dolphin shows themed folders, MIME types, devices, and places
* launcher/menu shows themed app icons for priority apps
* `.desktop` overrides work from user scope
* symbolic/action/status icons are present and readable
* `breeze,hicolor` fallback works
* rollback to Breeze works cleanly

---

## 15. Next Implementation Prompt

```txt
You are GPT-5.5 Extended Thinking acting as a cross-platform desktop-icon-theme implementation planner, Windows 11 icon customization engineer, KDE Plasma/XDG icon-theme engineer, reversible tooling author, and documentation maintainer.

Your task is to create the first non-destructive implementation skeleton for the “Sauriil Dark Archive” cross-platform icon customization project.

This is a skeleton + tooling + documentation task only.

Do not create final icon art.
Do not apply changes to the current machine.
Do not modify Windows registry live.
Do not modify `/usr/share/icons`.
Do not modify `/usr/share/applications`.
Do not patch Windows system files.
Do not use 7TSP or any system-resource patching.
Do not claim the theme is installed unless proof files show it.

The project must be non-destructive by default and every apply-capable script must require dry-run mode first.

Target platforms:

1. Windows 11 current stable behavior
2. Arch Linux with KDE Plasma as the primary Linux target
3. Secondary compatibility notes for GNOME and XFCE

Design identity:

- Sauriil Dark Archive
- black forged steel
- ash parchment
- blood-red ritual seals
- subtle cyan magical/system glow
- restrained pale-gold filigree
- occult circular geometry
- strong silhouettes
- readable small-size icons
- semi-realistic premium dark fantasy style
- no generic neon gamer look
- no cartoon style
- no copied protected official symbols

Source precedent to preserve:

- WinRAR theme process used 48x48 toolbar PNGs because 128x128 was too large.
- Windows root/app/archive icons required multi-size `.ico` files.
- The working process used transparent RGBA PNGs, trimming, proportional scaling, padding, and multi-size ICO export.
- Small-size readability testing is mandatory.

Create this repository structure:

source/
  master/
  png/
  svg/
  references/
mappings/
windows/
  ico/
  shortcuts/
  registry/
  iconpackager/
  third-party-tool-notes/
linux/
  Sauriil-Dark-Archive/
    index.theme
    scalable/
      apps/
      mimetypes/
      places/
      devices/
      status/
      actions/
      symbolic/
    16x16/
    24x24/
    32x32/
    48x48/
    64x64/
    128x128/
    256x256/
  desktop-overrides/
  mime-overrides/
  kde/
  gnome/
  xfce/
scripts/
  dry-run/
  apply/
  rollback/
  convert/
  test-render/
  validate/
docs/
  windows-plan.md
  linux-plan.md
  asset-guidelines.md
  icon-name-mapping.md
  third-party-risk.md
  rollback.md
  proof-checklist.md

Required deliverables:

1. Create the folder structure.
2. Create documentation files:
   - `docs/windows-plan.md`
   - `docs/linux-plan.md`
   - `docs/asset-guidelines.md`
   - `docs/icon-name-mapping.md`
   - `docs/third-party-risk.md`
   - `docs/rollback.md`
   - `docs/proof-checklist.md`
3. Create mapping CSV files:
   - `mappings/windows-shortcuts.csv`
   - `mappings/windows-filetypes.csv`
   - `mappings/windows-drives.csv`
   - `mappings/linux-desktop-icons.csv`
   - `mappings/linux-mimetypes.csv`
   - `mappings/linux-standard-names.csv`
4. Create a starter `linux/Sauriil-Dark-Archive/index.theme`.
5. Create placeholder README files in empty asset directories so the skeleton can be committed.
6. Create conversion scripts, but they must only process files inside the repository:
   - PNG normalization plan
   - ICO export plan
   - Linux PNG fallback export plan
   - SVG validation plan
7. Create Windows backup/rollback script skeletons:
   - must default to dry-run
   - must export registry targets before any future apply mode
   - must not write registry unless explicitly passed an apply flag
8. Create Linux install/rollback script skeletons:
   - must default to dry-run
   - must install only to `~/.local/share/icons`
   - must not write to `/usr/share/icons`
   - must not edit `/usr/share/applications`
   - must copy `.desktop` overrides only to `~/.local/share/applications`
9. Create validation scripts:
   - check required folders
   - check `index.theme`
   - check icon filename conventions
   - check missing mapped assets
   - generate a dry-run report
10. Create a first package skeleton archive, but only containing placeholders and docs.

Implementation constraints:

- Use clear, reversible code.
- Prefer Python for cross-platform conversion/validation helpers.
- Use PowerShell for Windows dry-run/backup/rollback scripts.
- Use Bash for Linux dry-run/install/rollback scripts.
- All scripts must print exactly what they would do in dry-run mode.
- Apply mode must require an explicit flag such as `--apply`.
- No script may silently modify system files.
- No script may depend on icons that do not exist; missing icons must be reported as gaps.
- Include exact commands in documentation, but mark destructive commands as apply-only.
- Include a proof checklist showing how to verify Windows shortcuts, file type icons, drive icons, KDE theme activation, KDE cache refresh, and rollback.

Verification required:

- Run the validation scripts.
- Show dry-run output.
- Confirm no live registry or system icon directories were modified.
- Confirm the package skeleton does not include generated final art.
- List all known gaps.

Final response must include:

- files created
- scripts created
- dry-run verification output
- known gaps
- exact next step for adding real icon assets
```

[1]: https://learn.microsoft.com/en-us/windows/release-health/status-windows-11-25h2?utm_source=chatgpt.com "Windows 11, version 25H2 known issues and notifications"
[2]: https://docs.kde.org/stable_kf6/en/plasma-workspace/kcontrol/icons/index.html "Icons"
[3]: https://wiki.archlinux.org/title/KDE?utm_source=chatgpt.com "KDE"
[4]: https://wiki.archlinux.org/title/GNOME?utm_source=chatgpt.com "GNOME - ArchWiki"
[5]: https://docs.xfce.org/xfce/xfce4-settings/appearance "xfce:xfce4-settings:appearance [Xfce Docs]"
[6]: https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-design "Design guidelines for Windows app icons - Windows apps | Microsoft Learn"
[7]: https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-construction "Construct your Windows app's icon - Windows apps | Microsoft Learn"
[8]: https://specifications.freedesktop.org/icon-theme/?utm_source=chatgpt.com "Icon Theme Specification"
[9]: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishelllinka "IShellLinkA (shobjidl_core.h) - Win32 apps | Microsoft Learn"
[10]: https://learn.microsoft.com/en-us/windows/configuration/taskbar/pinned-apps "Configure the Windows Taskbar Pinned Apps with Policy Settings | Microsoft Learn"
[11]: https://learn.microsoft.com/en-us/windows/configuration/start/policy-settings "Start policy settings | Microsoft Learn"
[12]: https://support.microsoft.com/en-us/windows/customize-the-desktop-icons-in-windows-c13270f0-3812-c71d-f27e-29aa32588b20 "Customize the Desktop Icons in Windows - Microsoft Support"
[13]: https://learn.microsoft.com/en-us/windows/win32/shell/how-to-customize-folders-with-desktop-ini "How to Customize Folders with Desktop.ini - Win32 apps | Microsoft Learn"
[14]: https://learn.microsoft.com/en-us/windows/win32/shell/fa-progids "Programmatic Identifiers - Win32 apps | Microsoft Learn"
[15]: https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/export-or-import-default-application-associations?view=windows-11 "Export or Import Default Application Associations | Microsoft Learn"
[16]: https://learn.microsoft.com/en-us/windows/win32/shell/how-to-assign-a-custom-icon-and-label-to-a-drive-letter "Assign a Custom Icon and Label to a Drive Letter - Win32 apps | Microsoft Learn"
[17]: https://learn.microsoft.com/en-us/windows/win32/shell/autorun-cmds?utm_source=chatgpt.com "Autorun.inf Entries - Win32 apps"
[18]: https://learn.microsoft.com/en-us/windows/terminal/customize-settings/profile-general?utm_source=chatgpt.com "Windows Terminal General Profile Settings"
[19]: https://windhawk.net/mods/taskbar-tray-system-icon-tweaks?utm_source=chatgpt.com "Taskbar tray system icon tweaks"
[20]: https://www.ninjaone.com/blog/how-to-rebuild-the-icon-cache-in-windows/?utm_source=chatgpt.com "How to Rebuild the Icon Cache in Windows 10 & 11"
[21]: https://www.stardock.com/products/iconpackager/?utm_source=chatgpt.com "Stardock IconPackager: Change your Windows dekstop ..."
[22]: https://www.deviantart.com/devillnside/art/7TSP-GUI-2019-Edition-804769422?utm_source=chatgpt.com "7TSP GUI 2019 Edition by devillnside on DeviantArt"
[23]: https://specifications.freedesktop.org/desktop-entry/latest/recognized-keys.html "Recognized desktop entry keys | Desktop Entry Specification"
[24]: https://specifications.freedesktop.org/shared-mime-info/latest/ar01s02.html "Unified system | Shared MIME-info Database"
[25]: https://wiki.archlinux.org/title/Icons?utm_source=chatgpt.com "Icons - ArchWiki"
[26]: https://man.archlinux.org/man/kbuildsycoca6.8.en?utm_source=chatgpt.com "kbuildsycoca6(8) - Arch manual pages"
[27]: https://linux.die.net/man/1/gtk-update-icon-cache?utm_source=chatgpt.com "gtk-update-icon-cache(1) - Linux man page"
[28]: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/customizing_the_gnome_desktop_environment/assembly_enabling-desktop-icons_customizing-the-gnome-desktop-environment?utm_source=chatgpt.com "Chapter 1. Enabling desktop icons"
[29]: https://imagemagick.org/defines/ "ImageMagick | Defines"
[30]: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html "Image file formats - Pillow (PIL Fork) 12.2.0 documentation"
[31]: https://learn.microsoft.com/en-us/windows/win32/shell/fa-best-practices "Best Practices for File Associations - Win32 apps | Microsoft Learn"
[32]: https://bugs.kde.org/show_bug.cgi?id=403229&utm_source=chatgpt.com "403229 – Icon cache doesn't get automatically cleaned ..."
[33]: https://www.gdzsoft.com/cf/?utm_source=chatgpt.com "CustomFolder"
[34]: https://www.folderico.com/customize-folders-windows?utm_source=chatgpt.com "How to Customize Folders in Windows 11 & 10"
[35]: https://winaerotweaker.com/?utm_source=chatgpt.com "Winaero Tweaker"
[36]: https://www.stardock.com/products/start11/?utm_source=chatgpt.com "Stardock Start11: Restore the Classic Start Menu ..."
[37]: https://www.startallback.com/?utm_source=chatgpt.com "StartAllBack to fix all Windows 11 deal-breaking UI issues"
[38]: https://windhawk.net/?utm_source=chatgpt.com "Windhawk"
[39]: https://github.com/valinet/explorerpatcher?utm_source=chatgpt.com "valinet/ExplorerPatcher: This project aims to enhance ..."
