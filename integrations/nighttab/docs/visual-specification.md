# Proposed NightTab visual specification

#sauriil/theme #repo/architecture

Status: design proposal only. Authority: [asset guidelines](../../../docs/asset-guidelines.md), [README identity](../../../README.md), and [asset mapping](../../../mappings/icon-assets.csv). Those authorities establish materials, accents, silhouettes and 48px readability; they do not establish a numeric UI palette. Every numeric token below is a **new NightTab proposal**, not an existing repository value or applied setting.

## Semantic colours

| Role | Proposed value | Intended use |
| --- | --- | --- |
| background | `#090C10` | fallback behind retained space/Earth image |
| surface-primary | `#15191E` | forged-steel shortcut/search surfaces |
| surface-secondary | `#20262C` | group framing and raised controls |
| border | `#46515A` | restrained frame edge |
| text-primary | `#E7E0D2` | ash-parchment text |
| text-muted | `#ABA79E` | date and secondary metadata |
| accent-blood | `#A52D39` | limited ritual-seal accents |
| accent-cyan | `#73C7CF` | secondary magical/system detail |
| accent-gold | `#C8B47E` | sparse filigree in original art |
| focus | `#73C7CF` | desired visible keyboard focus |
| hover | `#2B343C` | subtle raised surface |
| danger | `#E66D75` | destructive-control semantic target |

These are design roles, not twelve independent NightTab settings. NightTab 7.3.0 generates shade ranges and exposes one global accent plus section colours. Use a low-saturation steel base, high text contrast and one restrained accent. Cyan/gold may live in generic icon art. Native focus/hover/danger rendering remains upstream-owned; do not claim exact independent colour control. If a desired semantic role cannot be mapped, document the native approximation instead of injecting CSS or escalating to a fork.

Test text at >=4.5:1 and meaningful non-text/focus detail at >=3:1 against actual composited surfaces. Blood red is decorative, not assumed readable body text. Transparency must not make text unreadable over Earth highlights.

## Geometry and layout

- Replace pill geometry with compact rectangular slabs. Start `state.theme.radius = 20`; upstream CSS commonly computes radius as `value * 0.01em`, so this is 0.2em (about 3.2px at 16px), not 20px. Verify individual components at actual sizes.
- Target a 1px perceived frame and a restrained shadow. Calibrate `theme.bookmark.item.border` in the native control; do not assume its stored value is pixels. Per-bookmark border/colour overrides may win and need separately scoped private edits.
- Preserve current links and grouping. Prefer tiles over long list pills only in a later explicit layout step. Keep a 40–48px minimum actionable height, 12–16px perceived inter-tile space, 24–32px between major sections, and a restrained search rectangle. Translate these visual targets through native scale/gutter controls in the disposable profile.
- Center the clock/date header above bookmarks. Preserve greeting text, clock semantics and search provider. Proposed clock display 40–56px, date 14–16px, UI labels >=14px at normal zoom; reduce size at narrow widths rather than clip.
- Native hover/focus must remain visible without relying on colour alone. Avoid enlarged hover motion where it disturbs layout. Native settings do not promise arbitrary ornamental frame nodes, custom focus CSS or independent geometry for every control.
- Occult circles belong in original icon silhouettes or optional future background artwork; avoid adding visual noise to every field.

## Typography

Use the installed extension's existing UI and display roles first: upstream CSS fallback stacks are `"Open Sans", sans-serif` and `"Fjalla One", sans-serif`. Upstream clock, date and greeting use the display role; other text follows upstream component styles. A separate metadata font is a design preference, not an independent native setting. Keep custom font names empty initially. A nonempty name invokes Google's WebFont loader, not an offline system-font selector.

Do not redistribute any new font files in this pass or require a proprietary font. Any later bundled font needs its exact license and provenance reviewed. Upstream bundles its default fonts through local-first @font-face declarations; verify actual offline rendering in the disposable profile. Native configuration reuses those fonts without redistributing their binaries. Avoid elaborate fantasy lettering for small dates, search text and bookmark labels.

## Generic icon reuse

Reuse existing normalized PNGs under `source/png/48/` and `source/png/128/` after inspecting both sizes; retain master provenance in `source/master/raster/`.

| Need | Existing generic candidate | Limit |
| --- | --- | --- |
| browser/new-tab/navigation | `sauriil-browser.png` | original navigation orb; no browser logo |
| coding/terminal | `sauriil-code-editor.png`, `sauriil-terminal.png` | category association, not site identity |
| files/documents/downloads | `sauriil-file-manager.png`, `folder-documents.png`, `folder-downloads.png` | generic category choices |
| home/general fallback | `user-home.png`, `folder.png` | select by user intent, no automatic URL mapping |
| search | native search affordance initially | no dedicated Sauriil search asset exists; optional original search sigil later |

No new art is required to qualify native colours and geometry. Optional search/fallback art must be original and separately reviewed at 16/24/48px. Do not copy site logos, official symbols or third-party marks. Assigning images to real bookmarks is private per-item state and is outside a theme-only import.

## Background

Preserve the user-requested space/Earth direction and the current private image reference. Persisted state proves image mode and a populated reference, not rendered Earth content or its license. No screenshot was supplied/automated, and no private image was fetched or copied into Git.

Keep Earth/space visible between UI groups; avoid opaque full-page panels. An astronomical archive-machine treatment can use restrained circles in future original artwork, but this task creates no image. Native 7.3.0 uses image/video URLs; local-directory references and data-URI rendering are not verified. Do not replace the background to work around that uncertainty. Never redistribute the current background without source/license review.

See the [implementation plan](implementation-plan.md) for explicit preservation and import boundaries.
