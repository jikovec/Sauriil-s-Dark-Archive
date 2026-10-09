# Persistent memory contract

**Memory is contextual state, not repository truth.** It must never override current
source, configuration, tests, schemas, manifests, Git state, GitHub work state,
live evidence or accepted decisions. Durable technical decisions belong in the
repository first, normally in [docs/decisions.md](../../docs/decisions.md).

Read only configured scopes with available tool permissions. Establish backend,
read visibility and freshness using [scopes](scopes.md) and verified bindings.
Reconcile memory pointers against current sources; stale summaries remain context.
Do not correct external memory merely because a conflict is found.

Writes require a writable destination, mutation authority, appropriate information
and explicit promotion semantics. This toolkit grants no memory mutation authority;
current session/provider rules can further narrow it. Mere access is insufficient.
Never persist ordinary work, temporary failure, hypotheses or unverified interpretations
automatically. Never store secrets or unnecessary sensitive runtime data.

Memory may aid discovery, retain user-approved durable context and point to accepted
ADRs/specs/Issues/PRs without copying their entire content. Prefer repository decision
→ accepted/committed state → authorized pointer or summary. Mutable memory stays
in the configured external backend; Git holds only verified bindings when enabled.

Conditional Mind-Seed enrollment requires existing metadata, canonical registry
membership, verified memory bindings, a repository designation or explicit enrollment.
Connector availability and an enclosing directory name establish none of these.
No registry/scope IDs or write permissions may be invented if reconciliation fails.
