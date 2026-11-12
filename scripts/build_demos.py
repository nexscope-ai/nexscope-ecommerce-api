#!/usr/bin/env python3
"""Refresh per-API demo pages from the current public and API Docs catalogs."""
import json
from collections import Counter
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / 'demos'
PUBLIC_URL = 'https://www.nexscope.ai/api/public-apis/directory'
DOCS_URL = 'https://api.nexscope.ai/api/skill-api/v1/api-docs'


def fetch(url):
    with urlopen(url, timeout=30) as response:
        return json.load(response)


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    public = fetch(PUBLIC_URL)
    docs_response = fetch(DOCS_URL)
    if docs_response.get('code') != 0:
        raise RuntimeError('API Docs returned a business error')
    by_doc_slug = {item['slug']: item for item in docs_response['data']['skills']}
    canonical = {item['slug']: item for item in json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))['apis']}
    ready = [item for item in public['apis'] if (item.get('access') or {}).get('status') == 'ready']
    entries = []
    missing = []
    for item in ready:
        slug = item['slug']
        doc = by_doc_slug.get(slug) or by_doc_slug.get(item['skillSlug'])
        if not doc or doc.get('apiReady') is not True:
            missing.append(slug)
            continue
        platform, category = item['platformSlug'], item['categorySlug']
        folder = DEMOS / platform / category / slug
        folder.mkdir(parents=True, exist_ok=True)
        existing = canonical.get(slug)
        if existing:
            mode = 'rest'
            endpoint = existing['endpoint']
            payload = existing['payload']
            source = 'repository catalog'
        else:
            endpoint = doc['endpoint']
            mode = 'rest' if endpoint.endswith('/run') else 'mcp'
            if mode == 'mcp' and not doc.get('mcpToolName'):
                missing.append(slug)
                continue
            endpoint = endpoint if mode == 'rest' else 'https://api.nexscope.ai/api/skill-api/v1/mcp'
            payload = (folder / 'request.json').relative_to(ROOT).as_posix()
            request = doc.get('requestExample')
            write_json(ROOT / payload, request if isinstance(request, dict) else {})
            source = 'live API Docs'
        name = item['name'].get('en', slug)
        summary = item['summary'].get('en', '')
        config = {
            'slug': slug, 'name': name, 'platform': platform, 'category': category,
            'mode': mode, 'endpoint': endpoint, 'payload': payload,
            'mcpToolName': doc.get('mcpToolName') if mode == 'mcp' else None,
            'source': source, 'documentation': f'https://www.nexscope.ai/api-docs/{slug}?co-from=github-ecommerce-api',
        }
        write_json(folder / 'example.json', config)
        rel = folder.relative_to(ROOT).as_posix()
        payload_link = (Path('../../../..') / payload).as_posix()
        lines = [f'# {name}', '', summary, '',
                 f"[Official API documentation]({config['documentation']}) · [Request payload]({payload_link})", '']
        if existing:
            lines.append(f"[Repository API reference]({(Path('../../../..') / existing['localDoc']).as_posix()})")
            lines.append('')
        lines += [f"This demo uses the {source} request and endpoint. Review the payload and replace sample identifiers with valid inputs.",
                  'Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.', '',
                  'Run from the repository root:', '', '```bash',
                  f'python demos/clients/python/run.py {rel}',
                  f'node demos/clients/node/run.mjs {rel}',
                  f'java demos/clients/java/Run.java {rel}',
                  '```', '', f'Transport: **{mode.upper()}**. Endpoint: `{endpoint}`.', '']
        (folder / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
        entries.append({'slug': slug, 'name': name, 'platform': platform, 'category': category, 'mode': mode, 'path': rel, 'source': source})
    if missing:
        raise RuntimeError('No published runnable contract: ' + ', '.join(missing))
    entries.sort(key=lambda x: (x['platform'], x['category'], x['slug']))
    counts = Counter(x['source'] for x in entries)
    lines = ['# Per-API integration demos', '',
             'Runnable Python, Node.js, and Java demos for public, ready Nexscope APIs.', '',
             f"{len(entries)} demos: {counts['repository catalog']} use this repository's reviewed catalog and payloads; {counts['live API Docs']} use the current published API Docs contract.", '',
             'The older repository catalog also contains snapshot entries that are not currently in the public ready list; they remain in the API reference and are not advertised here as runnable demos.', '',
             'Use the official documentation for current request fields, account access, costs, and availability. Commands preview by default and send only with `--execute`.', '',
             '## Directory', '']
    for platform in sorted(set(x['platform'] for x in entries)):
        subset = [x for x in entries if x['platform'] == platform]
        lines.extend([f'### {platform} ({len(subset)})', ''])
        for category in sorted(set(x['category'] for x in subset)):
            lines.extend([f'**{category}**', ''])
            for entry in (x for x in subset if x['category'] == category):
                path = Path(entry['path']).relative_to('demos').as_posix()
                lines.append(f"- [{entry['name']}]({path}/README.md) · `{entry['slug']}` ({entry['mode'].upper()})")
            lines.append('')
    lines += ['## Refreshing', '',
              'Run `python scripts/build_demos.py`, review the diff and validate all changed contracts before publishing. The website should link to stable per-API README paths.', '']
    (DEMOS / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f"Generated {len(entries)} demos ({dict(counts)})")


if __name__ == '__main__':
    main()
