<!-- codex-memory-scaffold:project-overview -->
# Project Overview

#repo/index #sauriil/theme

Sauriil Dark Archive is a cross-platform icon-theme asset, conversion, platform-output, and proof project for Windows 11 and Arch Linux/KDE Plasma. The current documented release is `v0.0.2`.

## What The Repo Contains

- Original raster source icon art under [source/master/raster](../source/master/raster).
- Normalized generated PNGs under [source/png](../source/png).
- Windows multi-size ICO outputs under [windows/ico](../windows/ico).
- Linux XDG icon-theme outputs under [linux/Sauriil-Dark-Archive](../linux/Sauriil-Dark-Archive).
- CSV routing and platform mapping files under [mappings](../mappings).
- Python, PowerShell, and Bash scripts under [scripts](../scripts).
- Validation and proof evidence under [proof](../proof).
- Documentation, reports, and handoffs under [docs](.), [reports](../reports), and [handoffs](../handoffs).
- Intentional release archives under [VERSIONS](../VERSIONS).

## What The Repo Does Not Claim

- Live Windows or Linux apply/rollback safety is not established by the current proof set.
- It does not prove Windows registry/shortcut changes, Linux user-theme activation, or system-wide installation.
- It does not contain true vector SVG artwork for `v0.0.2`.
- It does not use a package manifest, Makefile, CI workflow, hosted deployment, or package-registry release pipeline.
- It does not publish a selected repository license.

Apply-capable scripts exist, but current safety defects are tracked in live GitHub Issues. See [current-state.md](current-state.md).

## Start Points

- Human docs hub: [INDEX.md](INDEX.md)
- Current technical state: [current-state.md](current-state.md)
- Agent orientation: [agent-index.md](agent-index.md)
- Machine-readable index: [agent-index.json](agent-index.json)
- Current release evidence: [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)
- Work ledger: [GitHub Issues](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues)
