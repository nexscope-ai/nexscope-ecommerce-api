"""Offline behavior checks; no authenticated or billable requests."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('client', ROOT / 'examples/python/run.py')
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)

class Clients(unittest.TestCase):
    def invoke(self, args, env=None):
        out, err = io.StringIO(), io.StringIO()
        with patch('sys.argv', ['run.py', *args]), patch.dict(os.environ, env or {}, clear=True), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = client.main()
        return code, out.getvalue(), err.getvalue()

    def test_python_dry_run_never_calls_network(self):
        with patch.object(client, 'urlopen') as network:
            code, out, _ = self.invoke(['amazon-search', str(ROOT/'payloads/amazon-search.json'), '--dry-run'])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)['body'], {'keyword': 'phone case', 'includeSellerSpriteData': False, 'page': 1})
            network.assert_not_called()

    def test_missing_key_does_not_send(self):
        with patch.object(client, 'urlopen') as network:
            self.assertEqual(self.invoke(['amazon-search', str(ROOT/'payloads/amazon-search.json')])[0], 1)
            network.assert_not_called()

    def test_media_sample_does_not_send(self):
        with patch.object(client, 'urlopen') as network:
            code, _, error = self.invoke(['background-remover', str(ROOT/'payloads/background-remover.json')])
            self.assertEqual(code, 1)
            self.assertIn('Replace example.com', error)
            network.assert_not_called()

    def test_task_query_uses_get_and_rejects_sync(self):
        method, endpoint, body = client.prepare('background-remover', task='task-123')
        self.assertEqual(method, 'GET'); self.assertIsNone(body)
        self.assertTrue(endpoint.endswith('/background-remover/tasks/task-123'))
        with self.assertRaises(ValueError): client.prepare('amazon-search', task='task-123')
        with self.assertRaises(ValueError): client.prepare('background-remover', task='../other')

    def test_http_error_is_not_retried(self):
        error = HTTPError('https://api.nexscope.ai', 429, 'Limited', {}, io.BytesIO(b'{"error":"limited"}'))
        with patch.object(client, 'urlopen', side_effect=error) as network:
            code, _, stderr = self.invoke(['amazon-search', str(ROOT/'payloads/amazon-search.json')], {'NEXSCOPE_API_KEY': 'test-only'})
            self.assertEqual(code, 1); self.assertIn('HTTP 429', stderr); self.assertEqual(network.call_count, 1)

    def test_failed_task_returns_nonzero(self):
        with patch.object(client, 'urlopen') as network:
            network.return_value.__enter__.return_value.read.return_value = b'{"status":"FAILED","taskId":"task-123"}'
            self.assertEqual(self.invoke(['background-remover', '--task', 'task-123'], {'NEXSCOPE_API_KEY': 'test-only'})[0], 1)
            self.assertEqual(network.call_args.args[0].get_method(), 'GET')

    def test_js_dry_run_and_invalid_media(self):
        script = str(ROOT/'examples/javascript/run.mjs')
        result = subprocess.run(['node',script,'amazon-search',str(ROOT/'payloads/amazon-search.json'),'--dry-run'],capture_output=True,text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['body']['keyword'],'phone case')
        result = subprocess.run(['node',script,'background-remover',str(ROOT/'payloads/background-remover.json'),'--dry-run'],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0);self.assertIn('Replace example.com', result.stderr)

    def test_js_task_endpoint(self):
        result = subprocess.run(['node',str(ROOT/'examples/javascript/run.mjs'),'background-remover','--task','task-123','--dry-run'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['method'],'GET')


    def test_woocommerce_short_routes_prepare_without_network(self):
        apis = json.loads((ROOT / 'catalog/apis.json').read_text())['apis']
        woo = [api for api in apis if api['slug'].startswith('woocommerce-')]
        self.assertEqual(len(woo), 11)
        with patch.object(client, 'urlopen') as network:
            for api in woo:
                with self.subTest(slug=api['slug']):
                    method, endpoint, body = client.prepare(api['slug'], ROOT / api['payload'])
                    self.assertEqual(method, 'POST')
                    self.assertEqual(endpoint, api['endpoint'])
                    self.assertTrue(endpoint.startswith('https://api.nexscope.ai/woocommerce/'))
                    self.assertIn('storeUrl', body)
                    result = subprocess.run(['node', str(ROOT / 'examples/javascript/run.mjs'),
                                             api['slug'], str(ROOT / api['payload']), '--dry-run'],
                                            capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(json.loads(result.stdout)['endpoint'], endpoint)
            network.assert_not_called()

    def test_woocommerce_business_failure_is_not_reported_as_success(self):
        with patch.object(client, 'urlopen') as network:
            network.return_value.__enter__.return_value.read.return_value = b'{"code":99000,"msg":"fixture failure","data":null}'
            code, _, _ = self.invoke(['woocommerce-products', str(ROOT/'payloads/woocommerce-products.json')],
                                     {'NEXSCOPE_API_KEY':'fixture-only'})
            self.assertEqual(code, 1)
            self.assertEqual(network.call_count, 1)


    def test_js_woocommerce_business_envelope_and_single_request(self):
        with tempfile.TemporaryDirectory() as directory:
            preload = Path(directory) / 'peer.mjs'
            for code in (0, 99000):
                preload.write_text("let calls=0;globalThis.fetch=async(url)=>{if(url!=='https://api.nexscope.ai/woocommerce/products')throw Error('wrong route');calls++;return new Response(JSON.stringify({code:" + str(code) + ",msg:null,data:null}),{status:200})};process.on('exit',()=>{if(calls!==1)process.exitCode=7});", encoding='utf-8')
                result = subprocess.run(['node','--import',preload.as_uri(),str(ROOT/'examples/javascript/run.mjs'),
                                         'woocommerce-products',str(ROOT/'payloads/woocommerce-products.json')],
                                        env={**os.environ,'NEXSCOPE_API_KEY':'fixture-only'},capture_output=True,text=True)
                self.assertEqual(result.returncode, 0 if code == 0 else 1, result.stderr)

if __name__ == '__main__': unittest.main()
