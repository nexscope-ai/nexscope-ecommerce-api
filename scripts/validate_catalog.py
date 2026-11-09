#!/usr/bin/env python3
"""Validate offline coverage, catalog links, definitions and attribution."""
import ast
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WOO_ENDPOINTS = {'woocommerce-products': 'https://api.nexscope.ai/woocommerce/products', 'woocommerce-product-detail': 'https://api.nexscope.ai/woocommerce/productDetail', 'woocommerce-product-variations': 'https://api.nexscope.ai/woocommerce/productVariations', 'woocommerce-product-categories': 'https://api.nexscope.ai/woocommerce/productCategories', 'woocommerce-product-tags': 'https://api.nexscope.ai/woocommerce/productTags', 'woocommerce-product-brands': 'https://api.nexscope.ai/woocommerce/productBrands', 'woocommerce-product-attributes': 'https://api.nexscope.ai/woocommerce/productAttributes', 'woocommerce-product-attribute-detail': 'https://api.nexscope.ai/woocommerce/productAttributeDetail', 'woocommerce-product-attribute-terms': 'https://api.nexscope.ai/woocommerce/productAttributeTerms', 'woocommerce-product-reviews': 'https://api.nexscope.ai/woocommerce/productReviews', 'woocommerce-product-collection-data': 'https://api.nexscope.ai/woocommerce/productCollectionData'}

SIF_ENDPOINTS = {'design-similarity-search': 'https://api.nexscope.ai/ai/designSimilaritySearch', 'design-registration-details': 'https://api.nexscope.ai/ai/designRegistrationDetails'}

PROCUREMENT_ENDPOINTS = {'1688-authorize-url': 'https://api.nexscope.ai/alibaba1688/authorizeUrl', '1688-authorized-stores': 'https://api.nexscope.ai/alibaba1688/authorizedStores', '1688-receive-address-list': 'https://api.nexscope.ai/alibaba1688/receiveAddressList', '1688-sku': 'https://api.nexscope.ai/alibaba1688/sku', '1688-order-preview': 'https://api.nexscope.ai/alibaba1688/orderPreview', '1688-create-order': 'https://api.nexscope.ai/alibaba1688/createOrder', '1688-payment-url': 'https://api.nexscope.ai/alibaba1688/paymentUrl', '1688-order-status': 'https://api.nexscope.ai/alibaba1688/orderStatus', '1688-logistics': 'https://api.nexscope.ai/alibaba1688/logistics', '1688-logistics-trace': 'https://api.nexscope.ai/alibaba1688/logisticsTrace', '1688-confirm-receive': 'https://api.nexscope.ai/alibaba1688/confirmReceive', '1688-cancel-order': 'https://api.nexscope.ai/alibaba1688/cancelOrder', '1688-invoice-amount': 'https://api.nexscope.ai/alibaba1688/invoiceAmount', '1688-invoice-apply': 'https://api.nexscope.ai/alibaba1688/invoiceApply'}

def validate():
    catalog = json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))
    apis = catalog['apis']
    assert len(apis) == catalog['count'] == 252
    assert len({a['slug'] for a in apis}) == 252
    assert Counter(a['family'] for a in apis) == catalog['counts'] == {'data': 199, 'creative': 53}
    assert Counter(a['category'] for a in apis) == {c['name']: c['count'] for c in catalog['categories']}
    assert len(catalog['categories']) == 22
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    referenced = set()
    for api in apis:
        slug = api['slug']
        assert re.fullmatch(r'[a-z0-9-]+', slug)
        expected = PROCUREMENT_ENDPOINTS.get(slug, SIF_ENDPOINTS.get(slug, WOO_ENDPOINTS.get(slug, f'https://api.nexscope.ai/api/skill-api/v1/skills/{slug}/run')))
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
    print('PASS: 252 APIs, 22 categories, 252 docs, 504 definitions, 252 payloads, 252 response fixtures; links and attribution checked.')

if __name__ == '__main__':
    validate()
