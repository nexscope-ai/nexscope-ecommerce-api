"""Offline checks for released 1688 procurement paths and safe documentation examples."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('procurement_client', ROOT / 'examples/python/run.py')
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)


class ProcurementDistribution(unittest.TestCase):
    def test_all_fourteen_clients_prepare_actual_short_routes_without_network(self):
        apis = json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))['apis']
        selected = [a for a in apis if a['category'] == '1688 Procurement']
        self.assertEqual(len(selected), 14)
        with patch.object(client, 'urlopen') as network:
            for api in selected:
                with self.subTest(slug=api['slug']):
                    expected = json.loads((ROOT / api['payload']).read_text(encoding='utf-8'))
                    method, endpoint, body = client.prepare(api['slug'], ROOT / api['payload'])
                    self.assertEqual((method, endpoint, body), ('POST', api['endpoint'], expected))
                    self.assertTrue(endpoint.startswith('https://api.nexscope.ai/alibaba1688/'))
                    for command in ([sys.executable, ROOT / 'examples/python/run.py'], ['node', ROOT / 'examples/javascript/run.mjs']):
                        result = subprocess.run([*map(str, command), api['slug'], str(ROOT / api['payload']), '--dry-run'], capture_output=True, text=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(json.loads(result.stdout), {'method': method, 'endpoint': endpoint, 'body': body})
            network.assert_not_called()

    def test_sensitive_samples_require_new_confirmation(self):
        for slug, field in [('create-order', 'confirmCreateOrder'), ('payment-url', 'confirmGetPaymentUrl'), ('confirm-receive', 'confirmReceive'), ('cancel-order', 'confirmCancel'), ('invoice-apply', 'confirmApplyInvoice')]:
            with self.subTest(slug=slug):
                payload = json.loads((ROOT / f'payloads/1688-{slug}.json').read_text())
                self.assertIs(payload[field], False)

    def test_procurement_responses_keep_nexscope_envelope(self):
        apis = json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))['apis']
        for api in apis:
            if api['category'] != '1688 Procurement':
                continue
            response = json.loads((ROOT / api['responseExample']).read_text())
            self.assertEqual(response['code'], 0)
            self.assertTrue({'data', 'code', 'msg', 'ts', 'time', 'cost', 'traceId'} <= response.keys())


if __name__ == '__main__':
    unittest.main()
