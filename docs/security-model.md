<!-- codex-memory-scaffold:security-model -->
# Security Model

#repo/security #sauriil/windows #sauriil/linux

## Confirmed Boundaries

- `v0.0.2` is an asset/conversion/proof package and does not install or apply icons to the live OS by default.
- Windows apply script refuses to run without `-Apply`.
- Linux install script refuses to run without `--apply`.
- Windows dry-run planning writes proof output and should not modify registry, shortcuts, or icon cache.
- Linux scripts are user-scoped and contain explicit `/usr/share` refusal checks.
- Required or active mapped icon assets are intended to fail validation when missing.

## Sensitive Data Rules

- Do not copy secrets, credentials, private keys, tokens, private certificates, production config, `.env` contents, private URLs, account IDs, or sensitive machine-specific paths into docs, reports, or indexes.
- Keep `.obsidian/` ignored and untracked because it can contain local workspace and plugin state.
- Treat [../VERSIONS](../VERSIONS) ZIP files as release archives. Do not inspect, rewrite, regenerate, or normalize them unless explicitly requested.
- Do not add cloud sync, account integration, encryption setup, sharing, or company integration to the Obsidian workflow.

## Apply And Rollback Risk

- Windows registry-backed file-type and drive-icon changes are higher risk than shortcut or folder icon changes. They require backup/export and explicit apply mode.
- Linux install and rollback paths are intended to operate only under `$HOME/.local/share/icons/Sauriil-Dark-Archive` and `$HOME/.local/share/applications`.
- Apply-capable scripts can modify the local OS. Re-read the current script before any apply run, even if docs say the path is gated.

## Verifiable References

- Project safety model: [../README.md](../README.md)
- Windows plan: [windows-plan.md](windows-plan.md)
- Linux plan: [linux-plan.md](linux-plan.md)
- Rollback plan: [rollback.md](rollback.md)
- Third-party risk order: [third-party-risk.md](third-party-risk.md)
- Deployment and release boundaries: [deployment.md](deployment.md)
- Current known gaps: [../proof/known-gaps.md](../proof/known-gaps.md)

## Unknowns

- No authentication, authorization, network service, remote deployment, or account boundary was identified in this asset repository.
- Live Windows apply, Linux install, and apply rollback behavior are not proven by the current `v0.0.2` proof set.
