// Node.js 22+. Submit once or query an existing task; no automatic POST retries.
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

try {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const clean = args.filter(a => a !== '--dry-run');
  const [slug, value, taskId] = clean;
  const isTask = value === '--task';
  if (!slug || (!isTask && (!value || clean.length !== 2)) || (isTask && (!taskId || clean.length !== 3))) {
    throw new Error('Usage: node examples/javascript/run.mjs SLUG PAYLOAD.json [--dry-run]\n       node examples/javascript/run.mjs SLUG --task TASK_ID [--dry-run]');
  }
  const catalog = JSON.parse(await readFile(fileURLToPath(new URL('../../catalog/apis.json', import.meta.url)), 'utf8'));
  const api = catalog.apis.find(a => a.slug === slug);
  if (!api) throw new Error('Unknown API slug. See catalog/apis.json.');
  let method = 'POST', endpoint = api.endpoint, body;
  if (isTask) {
    if (!api.asyncTask || !/^[A-Za-z0-9_-]+$/.test(taskId)) throw new Error('Use a valid task ID with an asynchronous API.');
    method = 'GET'; endpoint = api.taskResultEndpoint.replace('{taskId}', encodeURIComponent(taskId));
  } else {
    body = JSON.parse(await readFile(value, 'utf8'));
    if (!body || Array.isArray(body) || typeof body !== 'object') throw new Error('The request body must be a JSON object.');
    const placeholder = value => {
      if (typeof value === 'string') {
        try { const h = new URL(value).hostname.toLowerCase(); return ['example.com', 'example.org', 'example.net'].includes(h) || h.endsWith('.example.com'); }
        catch { return false; }
      }
      if (value && typeof value === 'object') return Object.values(value).some(placeholder);
      return false;
    };
    if (placeholder(body)) throw new Error('Replace example.com/example.org/example.net media URLs with your real public asset URLs.');
  }
  if (dryRun) {
    console.log(JSON.stringify({ method, endpoint, body: body ?? null }, null, 2));
  } else {
    const key = process.env.NEXSCOPE_API_KEY?.trim();
    if (!key) throw new Error('Set NEXSCOPE_API_KEY before calling the API.');
    const response = await fetch(endpoint, {
      method, headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }), signal: AbortSignal.timeout(120000),
    });
    const text = await response.text();
    if (!response.ok) throw new Error(`HTTP ${response.status}: ${text}`);
    const result = JSON.parse(text);
    console.log(JSON.stringify(result, null, 2));
    if ((result && Object.hasOwn(result, 'code') && ![0, '0'].includes(result.code)) || ['FAILED', 'TIMEOUT'].includes(result?.status)) process.exitCode = 1;
  }
} catch (error) {
  console.error(error.message); process.exitCode = 1;
}
