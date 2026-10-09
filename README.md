# Sauriil Dark Archive Icons

Sauriil Dark Archive is a cross-platform icon-theme asset, conversion, platform-output, and proof project for Windows 11 and Arch Linux/KDE Plasma.

Current documented release: `v0.0.2`.

## Status

`v0.0.2` contains the first real asset batch:

```text
apps:       sauriil-terminal, sauriil-browser, sauriil-code-editor, sauriil-file-manager
places:     folder, folder-documents, folder-downloads, user-home
mimetypes:  application-zip, application-x-rar, text-x-script, text-x-python
```

Generated outputs include normalized PNGs, Windows multi-size ICOs, Linux PNG fallbacks, contact sheets, and proof reports.

Apply-capable Windows and Linux scripts exist, but live apply/rollback behavior is not established as safe by the current proof set. Concrete implementation and verification gaps are tracked in [GitHub Issues](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues), including the platform safety tracker [#1](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/1). Routine asset, documentation, and validation work must not require live OS changes.

## Visual identity

The icon direction is dark fantasy archive-machine utility design: black forged steel, ash parchment, blood-red ritual seals, subtle cyan magical/system glow, restrained pale-gold filigree, occult circular geometry, strong silhouettes, and small-size readability.

The project avoids copied Elder Scrolls, Dark Brotherhood, Aldmeri, Microsoft, KDE, GNOME, Arch, WinRAR, Python, browser, file-manager, editor, and other protected official symbols.

## Repository model

- Accepted raster masters: `source/master/raster/`
- Generated normalized PNGs: `source/png/<size>/`
- Windows outputs: `windows/ico/`
- Linux XDG theme outputs: `linux/Sauriil-Dark-Archive/`
- Routing/configuration manifests: `mappings/`
- Conversion, validation, dry-run, apply, and rollback tools: `scripts/`
- Validation/proof evidence: `proof/`
- Active documentation: `docs/`
- Historical implementation context: `DOCUMENTATION/`
- Protected release archives: `VERSIONS/`

See [docs/architecture.md](docs/architecture.md) and [docs/source-map.md](docs/source-map.md) for the canonical structure.

## Prerequisites

The repository has no package manifest, installer, Makefile, or CI workflow.

Relevant tools depend on the task:

- Python 3 for validation and conversion scripts.
- Pillow for image conversion/contact-sheet operations when source images are present.
- Bash for Linux dry-run/apply/rollback scripts.
- Windows PowerShell for Windows dry-run/apply/rollback scripts.

Do not infer platform compatibility beyond what current source and proof establish.

## Validation

For documentation/index changes, start with:

```bash
git status --short --branch
git diff --check
python -m json.tool docs/agent-index.json
```

Then run a Markdown relative-link scan over changed documentation.

Asset/proof commands and their mutation boundaries are documented in [docs/commands.md](docs/commands.md) and [docs/testing.md](docs/testing.md). Some current validators have tracked defects; read those documents and the live Issues before regenerating proof.

## Live OS boundary

Do not run apply or apply-rollback commands merely to validate the repository.

- Linux installer preflight ordering is tracked in [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2).
- Windows stable icon storage and lossless rollback are tracked in [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).
- Non-destructive regression coverage is tracked in [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).

An explicit `-Apply` or `--apply` gate is an authorization guard, not evidence that the underlying mutation is correct.

## Documentation

Start with:

- `00_Index.md`
- `docs/INDEX.md`
- `docs/agent-index.md`
- `docs/source-map.md`
- `docs/connections.md`
- `docs/v0.0.2-asset-batch.md`
- `proof/v0.0.2-source-asset-inventory.md`
- `proof/v0.0.2-generated-assets.md`
- `proof/v0.0.2-contact-sheet-report.md`
- `proof/v0.0.2-validation-report.md`
- `proof/known-gaps.md`


## Planned NightTab integration

NightTab is a researched new integration surface, separate from v0.0.2 and the candidate v0.0.3 icon batch. See the [integration guide](integrations/nighttab/README.md). No theme has been implemented or live-applied; personal browser state stays private outside Git.
