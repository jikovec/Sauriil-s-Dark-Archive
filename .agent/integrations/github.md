# GitHub source and work state

Binding: the origin remote for `jikovec/Sauriil-s-Dark-Archive`, as represented in
[project.yaml](../project.yaml). This is a public personal-account repository;
no organization is bound. Git remotes and live repository settings are canonical
for source hosting and required checks, not old snapshots in reports.

Use Git plus an authenticated `gh` CLI or available GitHub connector. Credentials
come from the user's existing credential manager/CLI/connector session and never
from repository files. Read access does not prove write access.

Reads: repository metadata, relevant Issues/PRs/Projects, refs, checks, protections
and releases. Mutations: only scoped source/work-state actions allowed by
[authorization](../contracts/authorization.md) and [Git workflow](../contracts/git-github.md).
No connector install, repository settings change or Project enrollment is implied.
Release records/assets have separate scope; no Actions pipeline is assumed.
