# Release, deployment and publication

[Native boundaries](../../docs/deployment.md), [security model](../../docs/security-model.md)
and [rollback](../../docs/rollback.md) retain their domain rules.

**Release** creates versioned release state: notes, tags, archives and records
where actually requested/configured. It does not make the theme live. Discover
mechanics from existing version/proof sources; no automated release pipeline is
assumed. `VERSIONS/` inspection/regeneration needs explicit archive scope.

**Deploy** follows the normal governed procedure, all required checks, provider
controls, backup/migration/health requirements and rollback preparation. Here the
real deployment effects are target-specific OS apply/install and rollback; no
hosted service or cloud deployment is configured. Require explicit target-OS
scope, current script review and live verification. Never silently switch to publish.
Windows needs explicit `-Apply`; Linux needs `--apply` and user-scope targets.
Known defects or historical proof cannot be represented as safe live acceptance.

**Publish** means an expressly requested force-publication path. First identify
the normal blocker, classify it, and name any eligible repository-controlled or
deployment-process-controlled gate to bypass. Use only the minimum necessary
force path within authorized target scope; preserve failed/skipped evidence and
verify resulting live state. No force-publication mechanism is currently defined
for this asset project: do not invent one or treat a request to push as publish.

Never bypass or administratively circumvent GitHub branch protection/Rulesets,
externally required checks or reviews, environment approvals, organization
policy, hosting protections, IAM or cloud policy, even with admin credentials.
Publication semantics cannot supply missing authority for OS changes, data
exposure or archive mutation. Report external blockers and the legitimate route.
