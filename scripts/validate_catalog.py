#!/usr/bin/env python3
"""Validate offline coverage, catalog links, definitions and attribution."""
import ast
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WOO_ENDPOINTS = {'woocommerce-products': 'https://api.nexscope.ai/woocommerce/products', 'woocommerce-product-detail': 'https://api.nexscope.ai/woocommerce/productDetail', 'woocommerce-product-variations': 'https://api.nexscope.ai/woocommerce/productVariations', 'woocommerce-product-categories': 'https://api.nexscope.ai/woocommerce/productCategories', 'woocommerce-product-tags': 'https://api.nexscope.ai/woocommerce/productTags', 'woocommerce-product-brands': 'https://api.nexscope.ai/woocommerce/productBrands', 'woocommerce-product-attributes': 'https://api.nexscope.ai/woocommerce/productAttributes', 'woocommerce-product-attribute-detail': 'https://api.nexscope.ai/woocommerce/productAttributeDetail', 'woocommerce-product-attribute-terms': 'https://api.nexscope.ai/woocommerce/productAttributeTerms', 'woocommerce-product-reviews': 'https://api.nexscope.ai/woocommerce/productReviews', 'woocommerce-product-collection-data': 'https://api.nexscope.ai/woocommerce/productCollectionData'}

def validate():
    catalog = json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))
    apis = catalog['apis']
    assert len(apis) == catalog['count'] == 236
    assert len({a['slug'] for a in apis}) == 236
    assert Counter(a['family'] for a in apis) == catalog['counts'] == {'data': 183, 'creative': 53}
    assert Counter(a['category'] for a in apis) == {c['name']: c['count'] for c in catalog['categories']}
    assert len(catalog['categories']) == 21
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    referenced = set()
    for api in apis:
        slug = api['slug']
        assert re.fullmatch(r'[a-z0-9-]+', slug)
        expected = WOO_ENDPOINTS.get(slug, f'https://api.nexscope.ai/api/skill-api/v1/skills/{slug}/run')
        assert api['endpoint'] == expected
        assert api['method'] == 'POST'
        assert f'[{api["name"]}]({api["localDoc"]})' in readme
        assert api['asyncTask'] == (api['family'] == 'creative')
        if api['asyncTask']:
            assert api['taskResultEndpoint'] == f'https://api.nexscope.ai/api/skill-api/v1/skills/{slug}/tasks/{{taskId}}'
        for field in ('localDoc', 'requestSchema', 'responseSchema', 'payload', 'responseExample'):
            path = ROOT / api[field]
            assert path.is_file(), path
            referenced.add(path)
        for kind in ('request', 'response'):
            schema = json.loads((ROOT / api[kind + 'Schema']).read_text(encoding='utf-8'))
            assert ('field-descriptors' if 'fields' in schema else 'json-schema') == api[kind + 'SchemaFormat']
    assert {a['slug'] for a in apis if a['slug'].startswith('woocommerce-')} == set(WOO_ENDPOINTS)
    actual = set((ROOT/'docs/data').glob('*.md')) | set((ROOT/'docs/creative').glob('*.md'))
    actual |= set((ROOT/'schemas').glob('*.json')) | set((ROOT/'payloads').glob('*.json')) | set((ROOT/'examples/responses').glob('*.json'))
    assert referenced == actual, 'Missing or orphaned API artifacts'
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(p in ('.git','__pycache__') for p in path.parts): continue
        if path.suffix == '.json': json.loads(path.read_text(encoding='utf-8'))
        if path.suffix == '.py': ast.parse(path.read_text(encoding='utf-8'))
        if path.suffix == '.md':
            text = path.read_text(encoding='utf-8')
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                if link.startswith(('https://', 'http://', '#')): continue
                assert (path.parent / link.split('#')[0]).exists(), (path, link)
            for url in re.findall(r'https://www\.nexscope\.ai/[^\s)]+', text):
                attribution = 'co-from=cline' if path == ROOT / 'llms-install.md' else 'co-from=github-ecommerce-api'
                assert attribution in url, (path, url)
    print('PASS: 236 APIs, 21 categories, 236 docs, 472 definitions, 236 payloads, 236 response fixtures; links and attribution checked.')

if __name__ == '__main__':
    validate()
