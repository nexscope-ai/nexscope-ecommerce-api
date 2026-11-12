#!/usr/bin/env python3
"""Validate the linkable demo index and its repository-owned sources offline."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / 'demos'


def main():
    canonical = {item['slug']: item for item in json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))['apis']}
    index = (DEMOS / 'README.md').read_text(encoding='utf-8')
    files = list(DEMOS.rglob('example.json'))
    tracked = set(subprocess.check_output(['git', 'ls-files', '--cached', '-z'], cwd=ROOT).decode('utf-8').split('\0'))
    slugs = set()
    source_count = {'repository catalog': 0, 'live API Docs': 0}
    for path in files:
        config = json.loads(path.read_text(encoding='utf-8'))
        slug = config['slug']
        assert slug not in slugs, slug
        slugs.add(slug)
        folder = path.parent
        relative = folder.relative_to(DEMOS).as_posix()
        readme = folder / 'README.md'
        assert readme.is_file(), readme
        assert f']({relative}/README.md)' in index, slug
        text = readme.read_text(encoding='utf-8')
        assert f'/api-docs/{slug}?co-from=github-ecommerce-api' in text, slug
        payload = (ROOT / config['payload']).resolve()
        assert payload.is_relative_to(ROOT) and payload.is_file(), payload
        assert payload.relative_to(ROOT).as_posix() in tracked, f'Payload is not tracked by Git: {payload}'
        json.loads(payload.read_text(encoding='utf-8'))
        source_count[config['source']] += 1
        if config['source'] == 'repository catalog':
            api = canonical[slug]
            assert config['endpoint'] == api['endpoint'], slug
            assert config['payload'] == api['payload'], slug
            assert config['mode'] == 'rest', slug
        else:
            assert config['source'] == 'live API Docs', slug
            assert config['mode'] in ('mcp', 'rest'), slug
            if config['mode'] == 'mcp':
                assert config['mcpToolName'] and config['endpoint'].endswith('/mcp'), slug
    assert len(files) == 257, len(files)
    assert source_count == {'repository catalog': 196, 'live API Docs': 61}, source_count
    assert len(list(DEMOS.rglob('request.json'))) == 61
    print(f'PASS: {len(files)} unique demo pages; {source_count}; payloads and links checked.')


if __name__ == '__main__':
    main()
