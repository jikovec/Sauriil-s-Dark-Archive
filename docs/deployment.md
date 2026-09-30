# Deployment And Release Boundaries

#repo/release #sauriil/release-archive #sauriil/windows #sauriil/linux

This repository has no cloud deployment, hosted service, package registry deployment, or CI release workflow.

## Git Merge Versus Deployment

```text
merge != deployment
```

Merging repository changes does not apply the theme to Windows or Linux. Live OS customization is a separate, explicitly authorized action performed by apply-capable scripts or manual platform steps.

## Release Artifacts

- Intentional release ZIP archives live under [../VERSIONS](../VERSIONS).
- Proof manifests and validation evidence live under [../proof](../proof).
- Do not edit, rewrite, regenerate, or normalize release archives unless release-archive work is explicitly authorized.
- A protected WinRAR archive change on current `main` has a provenance-review work item: [#8](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/8).

The repository currently has no documented automated release trigger.

## Windows Apply Boundary

Windows apply is gated by `-Apply`, but current source does not yet conform to the accepted stable-storage/lossless-rollback contract. See [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).

Do not use a repository merge or passing static validation as evidence that Windows apply is safe.

## Linux Install Boundary

Linux install is gated by `--apply` and targets user scope, but current source can mutate the theme before all required desktop-override inputs are validated. See [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2).

Do not run it as part of routine repository verification.

## Rollback Boundary

Rollback dry-runs are documented in [rollback.md](rollback.md). Apply rollback commands modify local state and require explicit authorization. Current Windows lossless-rollback work remains tracked in #3.

## Verification After Any Future Authorized Release/Apply

A successful Git commit, pull request, or merge is not live verification. Future release/apply work must separately record:
- the exact artifact/revision;
- exact command or manual action;
- target environment;
- result;
- rollback/readback result where applicable.

## Non-Goals

- No cloud/account integration.
- No Obsidian sync setup.
- No encryption setup.
- No system-resource patching.
- No implicit live registry, desktop, or theme activation from repository delivery.
