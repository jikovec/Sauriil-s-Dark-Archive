# Codex compatibility pointer

Native discovery adapters live in [`.agents/skills`](../../.agents/skills/).
Canonical workflows live in [`skills/`](../../skills/).

This directory intentionally contains no duplicate SKILL.md adapters. Native
Codex discovery in the bootstrap environment scans both locations and would
otherwise expose each name twice. Older clients which only scan `.codex/skills`
can read canonical workflows directly through AGENTS.md; their automatic skill
discovery is not claimed. Do not copy policy here.
