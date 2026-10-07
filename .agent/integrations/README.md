# Integrations

[GitHub](github.md) is the existing source/work integration. Native theme targets
are documented in [deployment](../../docs/deployment.md), not modeled as hosted
services. Local-first Obsidian remains in [its existing guide](../../docs/obsidian.md).

Each real integration must identify canonical configuration, external service,
read/mutation effects, dependencies, project/organization binding and credential
source. Never copy tokens/secrets or infer authorization from tool availability.
Configured does not mean authenticated. Add specific documents only for actual
integrations; no placeholder Jira, cloud or memory services.
