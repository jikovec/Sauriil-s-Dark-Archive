# Scope and promotion semantics

Scope controls identity, lifetime and visibility; nesting is not a universal
precedence ladder. Data type and its canonical authority decide conflicts.

| Scope | Identity and lifetime | Read visibility | Write authority | Inheritance and promotion |
|---|---|---|---|---|
| global | Owner/platform namespace; durable | Only explicitly exposed global context | Governing owner/platform grant | Contextual defaults descend; policy stays authoritative in its domain; promotion requires global approval |
| organization | Verified organization ID; organization lifetime | Authorized members/services only | Organization governance | Lower scopes may narrow, never widen prohibitions; project-to-organization promotion needs destination authority |
| project | Canonical project ID, potentially multiple repos; project lifetime | Authorized project context | Project governing authority | Shared design context descends; registry owns identity; task-to-project promotion needs accepted repository truth |
| repository | Verified host/owner/name; repository lifetime | Public source or authorized private access | Repository governance and scoped source grant | Current source owns technical truth; repository policy refines generic behavior; commits/decisions precede durable promotion |
| agent | Runtime-assigned agent ID; agent lifetime | Delegated scope only | Delegated rights only | Cannot widen parent grant or redefine project identity; findings remain contextual |
| task | Runtime/task identifier; objective lifetime | Assigned task context | Authorized objective under policy | Can narrow scope; session-to-task promotion is explicit and does not itself authorize persistence |
| session | Runtime session identifier; interaction lifetime | Available session/tool context | Session permissions within task authority | Ephemeral observations remain contextual; no automatic upward promotion |

Lower scopes cannot rewrite higher-scope identity. Session/task state cannot
redefine organization/project identity or invent canonical registry IDs. Current
repository truth supersedes project, agent, task and session memory. Repository
policy refines generic execution; ordinary task text does not silently repeal it.
A valid owner policy-authoring request must adopt a policy change explicitly.

Task intent can grant authority only under the authorization model; stored state
cannot manufacture it. No IDs need persistence for ephemeral scopes.

## Promotion

Session → task, task → project, project → organization, organization → global are
possible transitions, never automatic. Each requires destination write permission,
information appropriate to that scope, mutation authority, supported persistence,
and updating canonical repository/registry truth first when applicable. Acceptance
of a technical decision is normally recorded in the repository before or together
with an authorized memory pointer. A task report is not permission to write a
memory backend. See [memory](memory.md) for storage/read/write rules.
