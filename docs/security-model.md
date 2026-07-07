<!-- codex-memory-scaffold:security-model -->
# Security Model

## Verifiable Security Signals
- Project safety model: [README.md](../README.md)
- Windows plan and registry backup expectations: [docs/windows-plan.md](windows-plan.md)
- Linux user-scope install plan: [docs/linux-plan.md](linux-plan.md)
- Rollback plan: [docs/rollback.md](rollback.md)
- Third-party risk order: [docs/third-party-risk.md](third-party-risk.md)
- Current known gaps: [proof/known-gaps.md](../proof/known-gaps.md)

## Confirmed Safety Properties
- v0.0.2 is an asset/conversion/proof package and does not install or apply icons to the live OS by default.
- Windows apply script refuses to run without `-Apply`.
- Linux install script refuses to run without `--apply`.
- Windows dry-run planning writes proof output and does not modify registry, shortcuts, or icon cache.
- Linux scripts are user-scoped and contain explicit `/usr/share` refusal checks.
- Required or active mapped icon assets are intended to fail validation when missing.

## Sensitive Data Handling
- Do not copy secrets, credentials, private keys, tokens, private certificates, production config, or .env contents into Obsidian notes.
- Environment files other than documented examples were not read during scaffolding.
- Generated dependency folders and build outputs should stay outside project memory notes unless a maintainer explicitly asks to document them.
- Treat VERSIONS/ ZIP files as release archives; do not inspect or rewrite them unless explicitly requested.

## Unknowns
- No authentication, authorization, network service, or deployment boundary was identified in this asset repository.
- Live Windows apply and Linux install/rollback behavior was not executed during the 2026-07-07 memory validation.
- Future work should re-check scripts before running apply-capable commands, because those paths can modify local OS state.
