"""Offline SIF distribution checks; no authenticated or billable requests."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sif_client', ROOT/'examples/python/run.py')
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)

class SifDistribution(unittest.TestCase):
    def test_both_clients_prepare_short_routes_without_network(self):
        cases = [('design-similarity-search', 'designSimilaritySearch'),
                 ('design-registration-details', 'designRegistrationDetails')]
        with tempfile.TemporaryDirectory() as directory, patch.object(client, 'urlopen') as network:
            for slug, route in cases:
                with self.subTest(slug=slug):
                    body = json.loads((ROOT/f'payloads/{slug}.json').read_text(encoding='utf-8'))
                    if 'imageUrl' in body:
                        # A local fixture URL avoids the clients' reserved-domain guard.
                        body['imageUrl'] = 'https://assets.nexscope.ai/fixture-only.png'
                    payload = Path(directory)/'request.json'
                    payload.write_text(json.dumps(body), encoding='utf-8')
                    method, endpoint, prepared = client.prepare(slug, payload)
                    self.assertEqual(method, 'POST')
                    self.assertEqual(endpoint, 'https://api.nexscope.ai/ai/'+route)
                    self.assertEqual(prepared, body)
                    for command in [['node', str(ROOT/'examples/javascript/run.mjs')],
                                    ['python', str(ROOT/'examples/python/run.py')]]:
                        result = subprocess.run([*command, slug, str(payload), '--dry-run'], capture_output=True, text=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(json.loads(result.stdout), {'method': method, 'endpoint': endpoint, 'body': body})
            network.assert_not_called()

    def test_illustrative_image_cannot_be_submitted_accidentally(self):
        with patch.object(client, 'urlopen') as network:
            with self.assertRaisesRegex(ValueError, 'Replace example.com'):
                client.prepare('design-similarity-search', ROOT/'payloads/design-similarity-search.json')
            network.assert_not_called()

    def test_search_fixture_preserves_source_score_images_and_classification(self):
        response = json.loads((ROOT/'examples/responses/design-similarity-search.json').read_text(encoding='utf-8'))
        self.assertEqual(response['code'], 0)
        business = response['data']['data']['data']
        self.assertEqual(business['total'], 1)
        candidate = business['candidates'][0]
        self.assertEqual(len(candidate), 29)
        self.assertEqual(candidate['similarity'], 99.88)
        self.assertEqual(candidate['locarno_classes'], ['06.01'])
        self.assertEqual(candidate['image_url'], candidate['images'][0])
        self.assertIn('signature=example%2Bsignature&expires=', candidate['images'][0])
        self.assertIn('signature=second&expires=', candidate['images'][1])
        self.assertEqual(candidate['tro_cases'], [])
        self.assertIsNone(candidate['estimated_expiration_date'])

    def test_details_fixture_keeps_exact_id_and_items_without_generated_images(self):
        response = json.loads((ROOT/'examples/responses/design-registration-details.json').read_text(encoding='utf-8'))
        self.assertEqual(response['code'], 0)
        source = response['data']['data']
        self.assertEqual(source['request_id'], 'example-request')
        self.assertNotIn('candidates', source['data'])
        item = source['data']['items'][0]
        self.assertEqual(item['primary_identifier'], '001431738')
        self.assertEqual(item['image_count'], 5)
        self.assertNotIn('image_url', item)
        self.assertNotIn('images', item)

if __name__ == '__main__':
    unittest.main()
