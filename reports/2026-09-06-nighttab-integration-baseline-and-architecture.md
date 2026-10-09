# 2026-09-06 — NightTab integration baseline and architecture

#agent/report #repo/architecture #sauriil/theme

## Result and scope

**NATIVE_CONFIGURATION_PLUS_SAURIIL_ASSETS**; fork **NOT REQUIRED** for the bounded [visual proposal](../integrations/nighttab/docs/visual-specification.md). Integration is researched/planned, not implemented or live-applied. Native export prerequisite: **BLOCKED_PENDING_HUMAN_NIGHTTAB_EXPORT**.

NightTab remains the upstream application/runtime. Sauriil owns generic visual identity, reusable original assets and integration documentation. Aetheris UI is not the authority. This is separate from the existing v0.0.2 release and candidate v0.0.3 icon batch. No live theme, browser setting, import, extension-storage write, OS installation, release archive regeneration, Git staging, commit or publication occurred.

## Repository baseline and preservation

- Branch: `main`; HEAD: `1246dde9fa9956351bfd54fe43ccae2da1217c3a`.
- Origin: [jikovec/Sauriil-s-Dark-Archive](https://github.com/jikovec/Sauriil-s-Dark-Archive). Remote was recorded, not fetched/synchronized; this report makes no current remote-equivalence claim.
- Starting modified paths: `.gitignore`, `AGENTS.md`, `DOCUMENTATION/002 Dark Archive cross-platform ic.md`, `docs/agent-index.json`, `docs/agent-index.md`, `docs/current-state.md`, `docs/obsidian.md`, `proof/validation-report.md`, `reports/multi-repo-finalization-2026-07-07.md`.
- Starting untracked paths: `.agents/`, `.codex/`, `docs/agent-workflow.md`.
- Worked directly in the requested checkout. Additive edits preserve overlapping current-state/index work; exact pre-edit documentation copies and repository content hashes were stored privately. Other inherited changes remain untouched.
- Read root instructions/index/README; docs index, current state, architecture, development, testing, security model, source map, connections, roadmap, decisions, agent indexes, commands, Obsidian conventions and AI workflow; proof known gaps; report/handoff indexes; asset guidelines and icon mapping.
- Protected paths: `VERSIONS/` release archives, generated PNG/ICO/Linux outputs/contact sheets and proof reports, private `.obsidian/` state. No asset/proof regeneration was in scope. Release archives were not opened or modified.
- Documentation conventions: normal relative Markdown links, tags on hubs/reports, durable evidence in `reports/`, continuation in `handoffs/`, machine routing in `docs/agent-index.json`.

## Private preservation evidence

Private authority is `$HOME/.local/share/nighttab/`, with historical exports in `backups/`. No relocation was performed. Eight historical files were verified as readable JSON: seven declare version 7.3.0 and one declares 7.5.0. All have top-level `nightTab`, `version`, `state`, `bookmark`. This proves two version labels with a shared envelope, not complete schema equality or current-state equivalence.

Private inventory records exact filenames, UTC modification timestamps, sizes and SHA-256 hashes. Historical bookmark values, URLs, names and filenames are excluded from this report. The obsolete backup source was not needed or recreated.

A fresh **SQLite online backup** of the discovered NightTab local-storage database was created using a read-only SQLite source connection and its backup API. `PRAGMA integrity_check` returned `ok`. Snapshot size: **11,264 bytes**; creation time: **2026-09-06T01:48:26.280315+00:00**. Its private receipt records the exact destination and SHA-256; these are delivered directly to the user, not as a public browser-data inventory.

The snapshot includes localStorage keys `nightTab`, `nightTabBackup`, `nightTabStyle`. Compressed values were decoded only from the snapshot using Snappy, verified against stored UTF-16 lengths and parsed as JSON. The parsed snapshot is separately labelled forensic/persisted state, **not a native export**. An installed-XPI copy and selected discovery metadata were kept privately. Files are restricted under a private evidence directory.

SQLite backup gives a consistent database snapshot. It does not prove unflushed/in-memory page state or that a currently rendered tab matches it. No supported non-interactive export command was found; upstream export requires page interaction. Required human step: **Menu → Data → Backup → Export data**, then save/verify the file in the private backup authority. Do not substitute the decoded JSON or SQLite snapshot for that supported export. See the [handoff](../handoffs/2026-09-06-nighttab-native-export.md).

## Installed/persisted baseline

Installed add-on metadata reports NightTab **7.3.0**, active and visible, sourced from Mozilla Add-ons. The XPI manifest independently confirms version 7.3.0, Manifest V2 and `chrome_url_overrides.newtab = index.html`. Public extension ID: `{47bf427e-c83d-457d-9b3d-3db4118574bd}`. The profile-specific UUID and filesystem path remain private.

Discovery followed Firefox's existing profile metadata, `extensions.json`, and its `extensions.webextensions.uuids` preference to the matching origin directory. The discovered persistence mechanism is Firefox localStorage `ls/data.sqlite`, not an assumed IndexedDB path or `browser.storage.local`. Mozilla's [localStorage database implementation](https://searchfox.org/firefox-main/source/dom/localstorage/ActorsParent.cpp) describes the stored conversion/compression fields. A process-name observation occurred, but later descriptor inspection did not establish a live page/profile association; profile lock presence alone is not live proof.

| Property | Proven persisted state |
| --- | --- |
| Data version | 7.3.0 |
| Shortcuts/groups | 10 entries; 1 expanded group; bookmark display enabled |
| Layout | centered; vertical; header before bookmarks; both areas centered at width 100 |
| Native layout controls | size 104, width 85, padding 50, gutter 31, breakpoint xxl; values are control units, not pixels |
| Bookmark presentation | list style, bottom orientation, size 100; URL/line/shadow/hover scale enabled |
| Search | one enabled search field; built-in provider; custom width control 30 and size 80; provider value intentionally omitted |
| Clock | 24-hour numeric hours/minutes/seconds; no meridiem |
| Date | short weekday, ordinal date, long month, year; new line enabled |
| Greeting | custom greeting enabled; private wording omitted |
| Background | image mode with populated reference; blur 2, grayscale 4, opacity 100, vignette opacity 18 |
| Theme | dark; radius 500; shadow 81; accent RGB (145,33,33); accent randomization/cycling off |
| Typography | empty custom font names, weight 400, normal style for UI/display |
| Icons | 4 letter visuals and 6 native icon visuals; no image visuals |
| Tile shape | no wide/tall flags |
| Saved themes | custom theme collection present; names/content remain private |

These are persisted settings, not a rendered screenshot or live visual acceptance. The user's large-red-pill description is consistent with the stored radius/accent, but rendered shape is not independently observed. Space/Earth is retained as the requested design direction; a populated image URL does not prove its actual visible content. No screenshot/persisted discrepancy can be assessed because no screenshot was supplied or captured. No arbitrary CSS field was found; `theme.custom` is a theme collection, not CSS injection.

## Upstream findings and evidence

Inspected public source in temporary research checkouts, without modifying upstream:

- Current `main`: `4f66b871369d266982f16ec4847d8219d6da6b9b`, commit dated 2024-08-10. Package/manifest version **7.6.0**, Manifest V3. This is **source version**, not the latest published Firefox/GitHub release. [Pinned manifest](https://github.com/zombieFox/nightTab/blob/4f66b871369d266982f16ec4847d8219d6da6b9b/src/manifest.json).
- Latest published GitHub release: **v7.3.0 Delightful Komodo Dragon**, 2021-10-03; tag commit `b2ceaffc87141ffb7144480b330cebc21deb93ea`. [Release](https://github.com/zombieFox/nightTab/releases/tag/v7.3.0).
- Current [Mozilla Add-ons listing](https://addons.mozilla.org/en-US/firefox/addon/nighttab/) offers **7.3.0**, updated 2021-10-02. Installed version matches this release, but not current main's source version. Historical 7.5.0 backup is not evidence of the installed version.

| Question | Source-grounded finding |
| --- | --- |
| Architecture | static JavaScript/CSS components bundled with Webpack; extension replaces new-tab HTML; state and bookmark models rendered into DOM |
| Persistence | `data.save()` serializes `{nightTab:true, version, state, bookmark}` to localStorage; `data.load()` reads and may migrate older data |
| Export | `data.export()` serializes `data.load()` into a JSON download; full data, not a privacy-safe theme-only export |
| Restore | separate Settings, Theme and Bookmarks include flags; **all default true** |
| Theme-only | `state.set.restore.theme()` assigns all of `state.theme`; background and saved themes are included |
| Settings | `state.set.restore.setup()` assigns layout/header/bookmark/group/toolbar; private search/greeting can be affected |
| Theme engine | generated CSS variables, palette shades/contrast, one accent, section colours/opacity, radius/shadow, image/video/gradient background |
| Layout | alignment/direction/order, header arrangement, width/padding/gutter, group and bookmark presentation; distinct from theme-only category |
| Portable preset | JSON configuration envelope can carry portable native settings; synthetic compatibility and import-category tests required before use |
| Custom CSS | no native arbitrary CSS injection control found; saved themes are not CSS |
| Custom icons | native letter/Font Awesome visuals or per-bookmark image URL; per-item icons are outside theme-only import |
| Fonts | default Open Sans/Fjalla One are bundled; custom names invoke Google WebFont loader |
| External directory | no supported mapping to an arbitrary filesystem directory established; do not assume `file://` works |
| Local assets | local upload removed in v7; documented image/video URL path. Small encoded data URI is source-compatible in principle, but Firefox rendering/CSP/storage must be tested |
| Rebuild/signing | native settings require neither; modified XPI distribution adds Firefox signing/update burden |

Pinned Firefox 7.3.0 evidence:

- [Data implementation](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/data/index.js): `data.import.state`, `data.export`, `data.restore`, `data.save`, `data.load`.
- [State schema/restore](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/state/index.js): defaults/options; `state.set.restore.setup`, `state.set.restore.theme`.
- [Theme renderer](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/theme/index.js): `theme.font.display.load`, `theme.font.ui.load`, background rendering and CSS variables. Image strings are split on whitespace and used in CSS URLs; raw whitespace-containing SVG is not a safe assumed input.
- [Bookmark image renderer](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/bookmarkTile/index.js): `display.visual.image.url`.
- [Menu labels/export controls](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/menuContent/dataSetting/index.js).
- [Bundled font CSS](https://github.com/zombieFox/nightTab/blob/b2ceaffc87141ffb7144480b330cebc21deb93ea/src/component/base/font/index.css): local-first declarations then bundled WOFF/WOFF2/TTF. No font redistribution is proposed; exact older binary licenses need separate review if later copied.
- [Backup/restore guide](https://github.com/zombieFox/nightTab/wiki/Data-backup-and-restore), [local background limitations](https://github.com/zombieFox/nightTab/wiki/Local-background-image), [Mozilla signing requirements](https://extensionworkshop.com/documentation/publish/signing-and-distribution-overview/). Wiki/store pages are current observations, not immutable source revisions.

## Mechanism decision

| Approach | Maintenance/update compatibility | Privacy and reproducibility | Rollback/portability | Rebuild/signing |
| --- | --- | --- | --- | --- |
| A — native configuration | lowest burden; version pin and import tests still needed | generic tokens safe; full exports private | native export/restore; layout separate | none |
| B — native + Sauriil generic assets | low burden plus asset transport qualification | original assets versionable; remote references add requests; data URIs have size constraints | native restore; embedded small assets potentially portable, unproven in Firefox | none |
| C — integration layer | moderate tooling/schema burden; useful only for deterministic preservation merges | can enforce allowlists/private outputs; must fail closed | full private export plus synthetic tests | none if producing native JSON |
| D — fork | highest burden; track upstream/browser/security/distribution changes | no inherent privacy benefit; additional code to audit | separate installation/migration/recovery | normal Firefox distribution requires signing |

**Select B: NATIVE_CONFIGURATION_PLUS_SAURIIL_ASSETS.** Native settings meet the essential dark palette, reduced radius, opacity and layout direction. Existing original category icons support the optional visual extension. An offline merge helper may package B safely; it is not required as a new runtime. No concrete essential requirement forces a fork. Arbitrary CSS effects, exact independent semantic colours and ornamental DOM geometry are outside the bounded native specification. Asset transport remains an explicit disposable qualification; native geometry can proceed without copying assets into the runtime.

Personal bookmarks can remain separate in Git, but NightTab's native full export still combines them with theme data. Do not mistake a portable full backup for a generic public preset. Preserve the existing private background and saved themes when creating a future private candidate.

## Repository changes and next pass

New integration files: [README](../integrations/nighttab/README.md), [visual specification](../integrations/nighttab/docs/visual-specification.md), [implementation plan](../integrations/nighttab/docs/implementation-plan.md). These contain proposed tokens, geometry/typography/icon/background boundaries, exact future file names, private candidate path, synthetic/disposable tests, native import steps, rollback and live acceptance.

New evidence/continuation: this report and the [native-export handoff](../handoffs/2026-09-06-nighttab-native-export.md). Updated navigation/authority routing: README, root index, docs index/current-state/architecture/source-map/connections/roadmap/decisions/agent-index Markdown and JSON, reports index and handoffs index. Existing release claims and asset/proof files are preserved.

The next pass first verifies a supported fresh export; then builds generic tokens and a versioned native overlay, an offline preservation merge/validator, and synthetic tests. It qualifies theme-only import and rollback in a separate profile, optionally tests existing PNG image transport, and records sanitized rendered proof. Real import/layout/icon changes require their own apply scope and human review. No Firefox restart or rebuild is expected for native configuration; test page reload/persistence before relying on it.

## Verification and limitations

Verification results are recorded below after final review. Documentation-only checks apply; asset validators and conversions were deliberately skipped because they rewrite proof/generated files. No live visual acceptance, native import round trip, Firefox restart, signing, publication, OS apply or backup restore was performed.

### Final check results

- Baseline commands: `pwd`, `git status --short`, `git branch --show-current`, `git rev-parse HEAD`, `git remote -v`; completed and recorded above. Working-directory alias resolves to the existing repository; no checkout switch or synchronization.
- `python3` was initially unavailable on PATH (exit 127). Read-only checks used the already installed Nix-store Python **3.13.9** by absolute executable path, plus existing Snappy **1.2.2** for private snapshot decoding. No package/environment installation was performed. The original SQLite metadata query used an incorrect column spelling; `PRAGMA` schema inspection corrected it. Snapshot integrity and decode-length/JSON checks then passed; the snapshot was not relabelled as a native export.
- `git diff --check`: exit **2**; complete output exactly matches the captured pre-edit failure. Inherited CRLF/trailing-whitespace findings occur in `.gitignore`, `AGENTS.md`, the historical cross-platform document, `proof/validation-report.md` and the prior multi-repo report. These were not normalized.
- `git diff --check -- README.md 00_Index.md docs/INDEX.md docs/current-state.md docs/architecture.md docs/source-map.md docs/connections.md docs/roadmap.md docs/decisions.md docs/agent-index.md docs/agent-index.json reports/INDEX.md handoffs/INDEX.md`: **pass**.
- `python -m json.tool docs/agent-index.json` using the explicit Python 3.13.9 executable: **pass**. Existing machine-index keys/values remain unchanged; one integration record added.
- A temporary Python Markdown-link/whitespace/privacy/preservation scanner over all **18 task files**: **pass**. Relative Markdown targets exist; task files have no trailing whitespace. Original overlapping Markdown content remains an exact byte prefix. Other pre-existing repository files retain their captured SHA-256 values (release archives and local `.obsidian/` were excluded from content inspection).
- Private-value scan: **pass** for exact private URLs, historical filenames, profile path/UUID and task-added credential/export-payload patterns. All **14** HTTP(S) references across the task scope are classified as public upstream, Mozilla, or repository documentation URLs. No personal export, bookmark payload, profile copy or private backup entered the repository.
- All eight historical backup hashes rechecked unchanged. SQLite integrity is `ok`; decoded strings match recorded UTF-16 lengths and parse as JSON. Snapshot receipt includes size, UTC timestamp and SHA-256. Private artifacts remain outside Git with restricted permissions.
- Final Git status and scoped diff were reviewed. Five new Markdown documents plus thirteen existing documentation/index files form this task; unrelated starting work remains present. No staged changes, commit, push, merge or release action.
- Skipped by scope: asset/proof validators that write outputs, conversion/contact sheets, release packaging, browser UI automation, native export/import round trip, live rendering, extension rebuild/signing and OS apply. These skips are not successful runtime checks.

**Final state: BLOCKED_PENDING_HUMAN_NIGHTTAB_EXPORT**.
