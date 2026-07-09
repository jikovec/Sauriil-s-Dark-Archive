# Deployment And Release Boundaries

#repo/release #sauriil/release-archive #sauriil/windows #sauriil/linux

This repository has no cloud deployment, hosted service, package registry deployment, or CI release workflow.

## Release Artifacts

- Release ZIP archives live under [../VERSIONS](../VERSIONS).
- Existing proof manifests live under [../proof](../proof).
- Do not edit, inspect, rewrite, or regenerate release archives unless the user explicitly asks.

## Windows Apply Boundary

Windows apply behavior is intentionally gated:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/apply/windows_apply_icons.ps1 -Apply
```

Do not run this command during normal docs, proof, or planning work. Re-read the current script and [windows-plan.md](windows-plan.md) before any user-approved apply run.

## Linux Install Boundary

Linux install behavior is intentionally gated:

```bash
bash scripts/apply/linux_install_user_theme.sh --apply
```

The intended install target is user-scoped:

```txt
$HOME/.local/share/icons/Sauriil-Dark-Archive
```

Scripts must not write to `/usr/share`.

## Rollback Boundary

Rollback dry-runs are documented in [rollback.md](rollback.md). Apply rollback commands still modify local state and require an explicit user request.

## Current Non-Goals

- No cloud or account integration.
- No Obsidian sync setup.
- No encryption setup.
- No system-resource patching.
- No live Windows registry or Linux desktop activation proof for `v0.0.2`.
