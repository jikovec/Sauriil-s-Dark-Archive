#!/usr/bin/env python3
"""Read-only toolkit conformance checks; Python 3 standard library only.

project.yaml uses YAML 1.2's JSON subset. Skill frontmatter deliberately uses
exactly two YAML scalar fields with JSON-quoted string values, not general YAML.
This checker validates that portable subset rather than accepting arbitrary YAML.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ('build', 'investigate', 'research', 'verify', 'review', 'fix',
            'release', 'deploy', 'publish', 'push', 'pull')
CONTRACTS = ('core', 'authorization', 'verification', 'git-github',
             'deployment', 'handoff', 'memory', 'scopes')
NATIVE = ('.agents', '.claude')
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        ERRORS.append(f'{path.relative_to(ROOT)}: {exc}')
        return ''


def frontmatter(path: Path) -> dict[str, str]:
    text = read(path)
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        ERRORS.append(f'{path.relative_to(ROOT)}: missing frontmatter')
        return {}
    result = {}
    for line in match[1].splitlines():
        key, sep, raw = line.partition(': ')
        if not sep or key not in ('name', 'description') or key in result:
            ERRORS.append(f'{path.relative_to(ROOT)}: invalid or duplicate scalar field')
            continue
        try:
            value = json.loads(raw)
            require(isinstance(value, str) and bool(value.strip()),
                    f'{path.relative_to(ROOT)}: {key} must be a nonempty string')
            result[key] = value
        except ValueError:
            ERRORS.append(f'{path.relative_to(ROOT)}: {key} must be JSON-quoted')
    require(set(result) == {'name', 'description'}, f'{path}: name/description required')
    require(result.get('name') == path.parent.name, f'{path}: name must match directory')
    return result


def links(path: Path) -> None:
    text = re.sub(r'```.*?```', '', read(path), flags=re.S)
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^\s)]+)\)', text):
        target = target.strip('<>')
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        resolved = (path.parent / unquote(parts.path)).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            ERRORS.append(f'{path.relative_to(ROOT)}: link escapes repository: {target}')
            continue
        require(resolved.exists(), f'{path.relative_to(ROOT)}: missing link {target}')


def main() -> int:
    required = ['AGENTS.md', 'CLAUDE.md', '.agent/README.md', '.agent/project.yaml',
                '.agent/evals/skill-routing.md', 'docs/agent-workflow.md', '.codex/skills/README.md']
    required += [f'.agent/contracts/{name}.md' for name in CONTRACTS]
    required += [f'.agent/{name}/README.md' for name in ('integrations', 'workflows', 'hooks')]
    for name in required:
        require((ROOT / name).is_file(), f'Missing required file: {name}')
    try:
        meta = json.loads(read(ROOT / '.agent/project.yaml'))
        require(meta['schema_version'] == 1, 'Unsupported project schema')
        repo = meta['repository']
        require(repo == {'host': 'github', 'owner': 'jikovec', 'name': 'Sauriil-s-Dark-Archive',
                         'default_branch': 'main', 'canonical_remote': 'origin'},
                'Repository metadata differs from adopted binding; reconcile identity')
        require(meta['project']['id'] == 'github:jikovec/Sauriil-s-Dark-Archive',
                'Project identity drift requires explicit reconciliation')
        require(meta['ownership']['class'] == 'user-owned', 'Ownership classification drift')
        require(meta['organization'] == {'id': None, 'name': None}, 'Unverified organization binding')
        require(meta['mind_seed'] == {'enabled': False, 'binding': None},
                'New Mind-Seed binding requires reconciliation and validator extension')
        for name in [*meta['environment']['source_files'], *meta['agent'].values(),
                     meta['integrations']['directory'], meta['workflows']['directory']]:
            require((ROOT / name).exists(), f'Missing metadata source: {name}')
    except (ValueError, KeyError, TypeError) as exc:
        ERRORS.append(f'Invalid project metadata: {exc}')
    try:
        index = json.loads(read(ROOT / 'docs/agent-index.json'))
        for name in [*index['important_paths'].values(), *index['docs_entry_points']]:
            require((ROOT / name).exists(), f'Index references missing path: {name}')
    except (ValueError, KeyError, TypeError) as exc:
        ERRORS.append(f'Invalid agent index: {exc}')
    canonical = [ROOT / f'skills/{name}/SKILL.md' for name in BASELINE]
    canonical += sorted((ROOT / 'skills/project').glob('*/SKILL.md'))
    names = [p.parent.name for p in canonical]
    require(len(names) == len(set(names)), 'Canonical/project skill name collision')
    require(bool(list((ROOT / 'skills/project').glob('*/SKILL.md'))), 'Project workflow missing')
    descriptions = []
    cases = read(ROOT / '.agent/evals/skill-routing.md')
    for skill in canonical:
        fm = frontmatter(skill)
        descriptions.append(fm.get('description'))
        for provider in NATIVE:
            adapter = ROOT / provider / 'skills' / skill.parent.name / 'SKILL.md'
            require(frontmatter(adapter) == fm, f'{adapter}: adapter metadata drift')
            expected = ('Read and follow the [canonical workflow](../../../'
                        + skill.relative_to(ROOT).as_posix() + ') before acting.\n'
                        'Also follow [AGENTS.md](../../../AGENTS.md) and applicable scoped instructions.\n'
                        'Resolve command paths from the repository root. This adapter contains no workflow policy.')
            actual = read(adapter).split('---\n', 2)[-1].strip()
            require(actual == expected, f'{adapter}: adapter must remain a thin canonical pointer')
        section = re.search(r'^## ' + re.escape(skill.parent.name) + r'\n(.*?)(?=^## |\Z)',
                            cases, re.M | re.S)
        require(bool(section), f'{skill.parent.name}: missing routing cases')
        if section:
            require(section[1].count('- Positive: ') >= 3 and section[1].count('- Negative: ') >= 2,
                    f'{skill.parent.name}: requires 3 positive and 2 negative routing cases')
    require(len(descriptions) == len(set(descriptions)), 'Duplicate canonical skill descriptions')
    require(not list((ROOT / '.codex/skills').rglob('SKILL.md')), 'Duplicate Codex compatibility adapters')
    for provider in NATIVE:
        actual = {p.parent.name for p in (ROOT / provider / 'skills').glob('*/SKILL.md')}
        require(actual == set(names), f'{provider}: native/canonical skill sets differ')
    require('@AGENTS.md' in read(ROOT / 'CLAUDE.md').splitlines(), 'Claude import missing')
    markdown = set()
    for folder in ('.agent', 'skills', '.codex', *NATIVE):
        markdown.update((ROOT / folder).rglob('*.md'))
    markdown.update(ROOT / p for p in ('AGENTS.md', 'CLAUDE.md', '00_Index.md',
                    'docs/INDEX.md', 'docs/agent-index.md', 'docs/current-state.md',
                    'docs/decisions.md', 'docs/agent-workflow.md', 'docs/commands.md',
                    'docs/testing.md', 'reports/INDEX.md', 'reports/2026-10-07-agent-toolkit-bootstrap.md'))
    for path in sorted(markdown):
        links(path)
    if ERRORS:
        print('\n'.join(ERRORS), file=sys.stderr)
        print(f'FAIL: {len(ERRORS)} toolkit error(s)', file=sys.stderr)
        return 1
    print(f'PASS: metadata, index, {len(canonical)} canonical skills, '
          f'{len(canonical) * len(NATIVE)} adapters, routing coverage, '
          f'{len(markdown)} Markdown files')
    print('Static conformance only; semantic routing and native discovery are separate checks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
