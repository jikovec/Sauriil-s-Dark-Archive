# Next NightTab implementation pass

#repo/development #sauriil/theme

This is a bounded plan, not permission to apply a theme. Read the [baseline report](../../../reports/2026-09-06-nighttab-integration-baseline-and-architecture.md) and [visual proposal](visual-specification.md). Target the installed Firefox NightTab **7.3.0**; re-check the version before building. Do not silently migrate through 7.5/7.6 exports.

## Prerequisite: supported private export

A human must open the existing NightTab page, open its settings menu, choose **Data → Backup → Export data**. Save the full native JSON into `$HOME/.local/share/nighttab/backups/` with a distinct current timestamp. Keep all eight historical files. Hash, timestamp, size-check and parse the new file privately; verify `nightTab`, version, state and bookmark structure. If saved first in Downloads, copy and hash-verify it at the private destination without replacing another file. No appearance change or settings import is needed to export.

Compare it privately with the preserved SQLite state. Explain differences before calling it the same baseline; a native export is the authority for the next import/rollback. The SQLite snapshot is forensic preservation, not a restore file to copy into a live Firefox profile. Never manipulate the database to manufacture a native export.

## Exact repository implementation scope

Add only files that the qualification actually needs:

1. `integrations/nighttab/theme/tokens.json`: generic proposed semantic tokens with schema/version and native mapping/approximation notes.
2. `integrations/nighttab/theme/native-7.3.0.json`: allowlisted native theme changes, derived from public upstream defaults, with no background URL or personal custom theme names. This overlay is not itself a native import.
3. `integrations/nighttab/presets/sauriil-dark-archive-7.3.0.json`: optional complete, synthetic NightTab-compatible envelope for disposable testing, only after proving import acceptance. It must use generic defaults and no personal bookmark records. Never label this safe for blind live import.
4. `integrations/nighttab/scripts/build_private_candidate.py`: offline deterministic JSON merge, no browser access, no network, no default private input discovery. Explicit input/output paths; reject unsupported versions, symlinks/overwrite and output inside the repository. Begin from a verified private native export; modify only approved theme keys. Preserve the entire bookmark array, settings, background object and custom theme collection byte-equivalently at the parsed JSON level unless a separately reviewed change is explicitly selected. Do not log private values. This is a packaging aid for native configuration, not a new runtime or extension patch.
5. `integrations/nighttab/scripts/validate_candidate.py` and `integrations/nighttab/tests/test_preservation.py`: synthetic-fixture schema, allowlist, path-boundary, overwrite, mismatch/version and round-trip tests. Hash/compare the untouched sections. Include a fixture with custom search/greeting/background and per-item overrides; fixture data must be invented, not copied from the user.
6. `integrations/nighttab/icons/README.md` and selected PNG derivatives only if image transport is qualified. Reuse `source/png/48/` and `source/png/128/` browser, terminal, editor, folder, documents, downloads or home assets. Record source hashes and any transformation. Do not regenerate shared icon release outputs.
7. `integrations/nighttab/proof/README.md` plus a dated sanitized report under `reports/`: disposable-profile import/export, reload, rendering, privacy and rollback evidence. Update this integration README, relevant indexes and current-state notes.

No `backgrounds/` is required while retaining the private Earth reference. A new original search icon is optional; palette/geometry qualification can use the native affordance. No release archive changes or existing v0.0.2 proof regeneration.

## Local-private candidate and apply path

Use `$HOME/.local/share/nighttab/staging/<timestamp>/candidate-7.3.0.json` and an adjacent private validation receipt. All private inputs, candidates and full export comparisons stay there. This directory is not part of Git.

Stage native theme changes first. A theme-only import replaces **all `state.theme`**, including background and custom saved themes. Therefore build the private candidate from the verified full export and preserve those subtrees rather than importing a generic replacement blindly.

For the initial real import, only after explicit apply authorization: **Theme selected; Settings and Bookmarks deselected**. All three default to selected upstream. Verify the dialog before confirming. Do not rely on empty bookmark arrays as a privacy/safety control.

Theme-only import cannot change header/group layout or per-bookmark icons. Prefer documented native control changes for the small layout adjustments after a separate backup. If bulk Settings or Bookmarks import is later justified, use a separately reviewed private candidate and exact preservation diff; Settings replaces layout/header/bookmark/group/toolbar and can overwrite greeting/search configuration. Per-item colours and icons must be reviewed privately, with no public site mapping.

## Disposable validation

- Use a separate explicitly created Firefox test profile or disposable copy that cannot modify the real profile. Install the same signed AMO 7.3.0 build; do not patch the XPI or use current MV3 main as a substitute.
- Begin with synthetic groups, bookmarks and custom fields. Use NightTab's native export as fixture; import the candidate with Theme only. Export again and compare untouched sections and intended theme delta.
- Prove behaviour for native palette/radius/opacity first. Test image URLs and small self-contained PNG/SVG data URIs separately in the disposable profile, including after reload and offline; inspect storage size/errors. No arbitrary filesystem directory or local upload support is assumed. If embedding fails, retain native icons or existing artwork until a separately approved public hosting option exists.
- Confirm blank custom font names and acceptable fallback rendering. Do not add Google font names inadvertently.
- Render at 1920×1080, 1366×768 and a narrow viewport; test 100%/200% zoom, keyboard navigation, contrast over bright image regions, focus, hover, scrolling, tile labels and 48px icon readability. Store public screenshots only from synthetic data.
- Reload the new-tab page and re-export to prove persistence. Normal native settings/import should not require rebuilding, signing or Firefox restart; verify page reload behaviour in the disposable profile. Human interactions are required where safe supported automation is unavailable; current task prohibits browser UI automation entirely.

## Rollback and live acceptance

Before any later real apply, retain the supported full native export with hash and timestamp. Roll back through **Data → Restore** using that full file and deliberately restore all three categories to return the complete prior state. This intentionally restores old bookmarks/settings too; account for any newer bookmark edits before doing it. Never overwrite the live SQLite file.

Prove rollback in the disposable profile by exporting again and comparing state/bookmarks (allow only explained upstream normalization). On live apply, privately verify link/group counts, destinations, labels, search provider, greeting, background reference and saved themes are preserved. Then the user must visually accept the retained Earth image, legibility, focus and Sauriil treatment. A build or JSON comparison alone is not live visual acceptance.

Current next-step status: **BLOCKED_PENDING_HUMAN_NIGHTTAB_EXPORT**. The architecture and design can be implemented locally after that prerequisite; asset transport and visual fit are explicit qualification tests, not reasons to fork in advance.
