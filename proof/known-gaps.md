# Known Gaps

Current release: `v0.0.2`.

`v0.0.2` contains generated raster source icons, normalized PNGs, Windows ICO outputs, Linux PNG fallbacks, contact sheets, and validation proof. No required mapping gaps are currently reported.

## Remaining Gaps

- No live Windows registry modification, shortcut modification, Windows Terminal profile modification, or icon cache refresh proof.
- No Linux user-theme installation, KDE activation, desktop override installation, or MIME cache refresh proof.
- No system-wide Linux install path; scripts must not write to `/usr/share`.
- No true scalable SVG icon set for `v0.0.2`; raster PNGs are not wrapped in fake SVG containers.
- No drive, shell, device, status, action, symbolic, GNOME-specific, or XFCE-specific icon coverage.
- No 7TSP or system-resource patching support.

## Current Validation Evidence

- [v0.0.2-validation-report.md](v0.0.2-validation-report.md)
- [v0.0.2-generated-assets.md](v0.0.2-generated-assets.md)
- [v0.0.2-contact-sheet-report.md](v0.0.2-contact-sheet-report.md)
- [dry-run-report.md](dry-run-report.md)
