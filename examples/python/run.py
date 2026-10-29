#!/usr/bin/env python3
"""Send one request or check one task; never automatically resubmit paid work."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]

def prepare(slug, payload_path=None, task=None):
    catalog = json.loads((ROOT / 'catalog/apis.json').read_text(encoding='utf-8'))
    api = next((a for a in catalog['apis'] if a['slug'] == slug), None)
    if api is None:
        raise ValueError('Unknown API slug. See catalog/apis.json.')
    if task:
        if not api['asyncTask'] or not re.fullmatch(r'[A-Za-z0-9_-]+', task):
            raise ValueError('Use a valid task ID with an asynchronous API.')
        return 'GET', api['taskResultEndpoint'].replace('{taskId}', quote(task, safe='')), None
    if not payload_path:
        raise ValueError('Provide a JSON payload file, or --task TASK_ID.')
    body = json.loads(Path(payload_path).read_text(encoding='utf-8'))
    if not isinstance(body, dict):
        raise ValueError('The request body must be a JSON object.')
    def placeholder(value):
        if isinstance(value, dict): return any(placeholder(v) for v in value.values())
        if isinstance(value, list): return any(placeholder(v) for v in value)
        if not isinstance(value, str): return False
        host = (urlsplit(value).hostname or '').lower()
        return host in ('example.com', 'example.org', 'example.net') or host.endswith('.example.com')
    if placeholder(body):
        raise ValueError('Replace example.com/example.org/example.net media URLs with your real public asset URLs.')
    return 'POST', api['endpoint'], body

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('slug')
    p.add_argument('payload', nargs='?')
    p.add_argument('--task', help='Check an existing task once (GET).')
    p.add_argument('--dry-run', action='store_true', help='Show method, endpoint and body without sending.')
    p.add_argument('--endpoint-only', action='store_true', help=argparse.SUPPRESS)
    a = p.parse_args()
    try:
        if a.task and a.payload: raise ValueError('Use a payload or --task, not both.')
        method, endpoint, body = prepare(a.slug, a.payload, a.task)
        if a.dry_run:
            print(json.dumps({'method': method, 'endpoint': endpoint, 'body': body}, indent=2)); return 0
        if a.endpoint_only:
            print(endpoint); return 0
        key = os.environ.get('NEXSCOPE_API_KEY', '').strip()
        if not key: raise ValueError('Set NEXSCOPE_API_KEY before calling the API.')
        request = Request(endpoint, data=json.dumps(body).encode() if body is not None else None,
                          headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}, method=method)
        with urlopen(request, timeout=120) as response:
            text = response.read().decode()
        try: result = json.loads(text)
        except json.JSONDecodeError: raise ValueError('The API returned a non-JSON response.')
        print(json.dumps(result, indent=2))
        if isinstance(result, dict) and ('code' in result and result['code'] not in (0, '0') or result.get('status') in ('FAILED', 'TIMEOUT')): return 1
        return 0
    except HTTPError as error:
        print(f'HTTP {error.code}: {error.read().decode(errors="replace")}', file=sys.stderr); return 1
    except (ValueError, OSError, URLError) as error:
        print(str(error), file=sys.stderr); return 1

if __name__ == '__main__':
    sys.exit(main())
