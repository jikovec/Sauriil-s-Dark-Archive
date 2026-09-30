# Changelog

This changelog records notable project-version changes supported by the repository's canonical release documentation and proof. It is not reconstructed from commit subjects.

## Unreleased

### Changed

- Repository governance, contributor, security, support, metadata, and work-ledger documentation is being reconciled without changing icon assets or live OS behavior.

## v0.0.2

### Added

- First real asset batch: 12 accepted raster source icons across apps, places, and MIME/file-type concepts.
- Normalized PNG outputs across the documented size matrix.
- Windows multi-size ICO outputs for apps, file types, and folders.
- Linux PNG fallbacks for apps, places, and MIME types.
- Contact-sheet and validation proof for the asset batch.

### Known limitations

- No true scalable SVG asset set is included.
- Captured release proof does not establish live Windows or Linux apply/rollback safety.
- The Windows PowerShell dry-run planner was skipped in the captured v0.0.2 validation environment because PowerShell was unavailable.

See [docs/v0.0.2-asset-batch.md](docs/v0.0.2-asset-batch.md), [proof/v0.0.2-validation-report.md](proof/v0.0.2-validation-report.md), and [proof/known-gaps.md](proof/known-gaps.md).

## v0.0.1

### Added

- Initial non-destructive cross-platform repository skeleton.
- Windows/Linux planning, mapping CSVs, validation/conversion script skeletons, rollback documentation, and XDG `index.theme` structure.
- Proof/report structure for dry-run and package validation.

### Known limitations

- The release intentionally contained no final icon art.
- No live Windows registry changes, Linux system installation, or live desktop activation were part of the release.

See [DOCUMENTATION/003 v0.0.1 skeleton creation.md](<DOCUMENTATION/003 v0.0.1 skeleton creation.md>).
