<!-- codex-memory-scaffold:architecture -->
# Architecture

## Observed Project Shape
- docs
- DOCUMENTATION
- handoffs
- linux
- mappings
- proof
- reports
- scripts
- source
- VERSIONS
- windows

## Stack Signals
- Python scripts handle asset conversion, contact sheet generation, and validation.
- PowerShell scripts handle Windows dry-run, apply, and rollback workflows.
- Bash scripts handle Linux dry-run, user-scope install, and rollback workflows.
- No standard package manifest was found.

## Architecture Docs
- [README.md](../README.md)
- [docs/architecture.md](architecture.md)
- [docs/v0.0.2-asset-batch.md](v0.0.2-asset-batch.md)
- [proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)

## Unknowns
- Confirm runtime boundaries against current source before changing behavior.
