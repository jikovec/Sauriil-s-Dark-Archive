# Repository agent toolkit bootstrap — 2026-10-07

## Implementation plan and authority

The owner requested the Repository Agent Toolkit Bootstrap, including policy authoring and ordinary source delivery through merge. The standing source-workflow grant is adopted atomically with the toolkit in AGENTS.md and the authorization contract. It does not extend to releases, OS activation, external protection bypass, private-state publication or memory writes.

- [x] Establish stable identity from current source/remotes and reconcile available registry bindings.
- [x] Add .agent contracts and eleven canonical skills; reconcile the existing project workflow into skills/project.
- [x] Wire thin Codex and Claude discovery adapters; update existing orientation and decision surfaces.
- [x] Verify structure, metadata, links, adapter parity, routing boundaries and original-checkout preservation.
Delivery acceptance: review, commit, push, create PR, satisfy applicable requirements, merge and verify default-branch identity. GitHub and the final handoff record the resulting endpoint.

Architecture: portable policy in .agent, reasoning workflows in skills, native discovery adapters without copied policy. Mind-Seed bindings are conditional on verified existing enrollment. Documentation and asset commands remain the project's native execution surface.

Review focus: dirty-checkout isolation; authorization versus release scope; memory promotion and identity; provider discovery versus static conformance; overlap with existing PR #12.

## Discovery baseline

Default branch main at 1246dde9fa9956351bfd54fe43ccae2da1217c3a; public repository jikovec/Sauriil-s-Dark-Archive, personal owner jikovec. No organization binding established. GitHub has no Actions workflows or releases at discovery. PR #12 is separate overlapping governance work and is not imported or merged by this task. Issues #1–#8 describe existing safety/proof/archive concerns; #9–#11 concern governance and reporting.

The original checkout contains 20 modified tracked paths and seven untracked top-level entries. Work proceeds in an isolated branch from origin/main; the original checkout is retained, including its local NightTab work, environment actions and project workflow. No unrelated source is staged. Existing local workflow semantics are reconciled into the canonical project skill; its old discovery path is retained as a thin adapter in the delivery tree.

No monolithic development-prompt.md or CLAUDE.md existed in the inspected baseline. Historical DOCUMENTATION remains historical; the existing docs/agent-index.json remains the detailed navigation index.

## Verification and delivery

### Identity and memory reconciliation

The configured default Mind-Seed project registry was inspected read-only using
SQLite read-only/query-only mode. Its installed projects, repositories, workspaces
and candidates tables had no matching Sauriil records. No project-local metadata
or configured federated-memory registry was established. The MemPalace status
connector returned unavailable (SSE probe HTTP 404). This is bounded discovery,
not proof that no identity exists elsewhere.

Portable identity is `github:jikovec/Sauriil-s-Dark-Archive`; organization fields
are null and ownership is user-owned, supported by the live personal-account
remote and the owner's bootstrap grant. Mind-Seed remains disabled with null
binding. No `.mind-seed/`, registry entry, memory content or mutation permission
was invented. No external registry or persistent memory was changed.

### Delivered architecture

Eight shared contracts define execution, authorization, verification, Git/GitHub,
deployment, handoff, memory and scopes. Eleven baseline skills and the existing
Sauriil workflow live canonically under `skills/`; aliases remain semantic only.
The project-specific shared asset-proof workflow links native commands without
copying them. GitHub is the real integration; no speculative cloud/Jira integration
or automatic hook was added. A standard-library read-only validator follows the
existing `scripts/validate/` convention.

`CLAUDE.md` imports AGENTS.md. There are 12 adapters per active provider in
`.agents/skills/` and `.claude/skills/`. Native Codex initially exposed duplicate
entries when `.codex/skills/` also held adapters. It therefore retains only a
compatibility README, following the bootstrap's currently-verified-native-location
rule. Older Codex clients which only scan that path have no automatic discovery
claim; canonical workflows remain directly readable. No permission configuration
or global provider setup changed.

The existing local workflow has been reconciled into the project skill and shared
contracts; `docs/agent-workflow.md` is a concise compatibility pointer. The original
checkout's pre-existing uncommitted version remains preserved rather than silently
replaced. No old monolithic development prompt was present to retire.

### Verification matrix

| Check | Result | Evidence and limits |
|---|---|---|
| Toolkit validator | passed | Python 3 standard library; stable metadata/index, 12 canonical skills, 24 adapters, case coverage and 64 Markdown files |
| Negative validator fixtures | passed | Invalid schema, frontmatter key, adapter target, missing routing positive and broken link each exit 1; pristine copy exits 0 |
| Agent index JSON | passed | `python3 -m json.tool docs/agent-index.json` |
| Whitespace | passed | `git diff --check`; staged check repeated before commit |
| Semantic routing review | passed | Independent review of 60 cases, all seven neighbor boundaries and six authority scenarios; reasoning review, not end-to-end model execution |
| Contract/diff review | passed | Independent review found no blocking defects; project trigger and preparation-only wording tightened |
| Codex native discovery | passed | Native app-server `skills/list` returns exactly 12 repository entries without duplicate names or repository errors |
| Claude native discovery | passed | Native stream initialization exposes all 12 repository skills with their canonical descriptions and project marker; no model task or side-effect workflow executed |
| Public diff hygiene | passed | Added-line sensitive-path/secret heuristic and protected-output path allowlist; no asset/runtime output paths changed |
| Original checkout preservation | passed | 388 file SHA-256 values and tracked binary diff unchanged after implementation |
| Asset/proof generation | not required | Toolkit/docs scope; generated evidence and assets unchanged |
| Windows/Linux live apply and rollback | not required | No target-OS request; existing safety Issues remain separate |
| Hosted Actions checks | not required | Live repository has no workflow; no hosted-check success inferred |
| External memory availability | blocked/unavailable | MemPalace probe HTTP 404; no verified binding or writes |

Metadata/frontmatter deliberately use JSON-compatible YAML scalars and the JSON
subset of YAML 1.2, avoiding an undeclared YAML dependency. The validator checks
that constrained representation rather than claiming to parse arbitrary YAML.
Live remote identity is read back separately; static validation alone cannot prove it.

### Source delivery boundary

The task branch starts from main independently of PR #12. No adjacent Issue is
closed and PR #12 is not merged. Its overlapping governance work will require
reconciliation against this toolkit when continued. The existing original checkout
stays at its pre-task HEAD with its dirty content; fetching a new origin/main does
not mean it has been synchronized. The isolated delivery checkout holds the toolkit.

Final PR/merge identity is recorded by Git history and the task handoff. No release,
tag, archive regeneration, deployment, OS activation or live acceptance is claimed.
