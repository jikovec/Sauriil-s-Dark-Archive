<!-- codex-memory-scaffold:security-model -->
# Security Model

#repo/security #sauriil/windows #sauriil/linux

## Confirmed Boundaries

- The repository is an asset/conversion/platform-output/proof project, not a network service.
- Windows live apply refuses to run without `-Apply`.
- Linux live install refuses to run without `--apply`.
- Linux paths are designed for user scope and include explicit `/usr/share` refusal checks.
- Routine documentation, conversion, and static validation work does not require live OS apply.
- `VERSIONS/` contains protected release/history archives and is outside routine regeneration scope.

These are boundary facts, not a claim that current apply/rollback behavior is fully safe.

## Current Safety Gaps

Source inspection has identified nonconformance with accepted safety plans:

- Linux install mutates the user theme before validating all required desktop-override inputs: [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2).
- Windows apply currently writes icon references to repository paths instead of the documented stable user-owned icon location and does not establish lossless rollback for prior absence state: [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3).
- Non-destructive behavioral regression verification is still missing: [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).

Therefore, the presence of apply gates must not be described as proof of safe mutation semantics.

## Sensitive Data Rules

- Do not commit secrets, credentials, private keys, tokens, private certificates, production configuration, `.env` contents, private URLs, account identifiers, or sensitive machine-specific state.
- Keep `.obsidian/` ignored and untracked because it can contain local workspace/plugin state.
- Do not add cloud sync, account integration, encryption setup, sharing, or company integration to the Obsidian workflow without explicit scope.
- Follow [../SECURITY.md](../SECURITY.md) for reporting vulnerabilities; sensitive details do not belong in public Issues.

## Apply And Rollback Authority

Live OS mutation requires explicit user authorization in the current task. Repository access, filesystem access, an apply flag, or an existing script is capability, not authorization.

Before any future authorized live apply:
1. inspect current source and live work items;
2. ensure relevant safety blockers are resolved;
3. capture backup/preflight evidence required by the accepted platform plan;
4. verify readback and rollback separately.

## Trust Boundaries

- Source/configuration/scripts/mappings are higher technical authority than stale prose.
- Proof is authoritative only for the revision, command, and environment actually recorded.
- GitHub Issues/PRs describe work state; they are not proof that implementation is fixed.
- Historical `DOCUMENTATION/` may describe superseded skeleton-era behavior.

## References

- Public reporting policy: [../SECURITY.md](../SECURITY.md)
- Windows target plan: [windows-plan.md](windows-plan.md)
- Linux target plan: [linux-plan.md](linux-plan.md)
- Rollback plan: [rollback.md](rollback.md)
- Deployment/release boundary: [deployment.md](deployment.md)
- Testing/evidence rules: [testing.md](testing.md)
- Current state: [current-state.md](current-state.md)
