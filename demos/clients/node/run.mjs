import { readFileSync } from 'node:fs';
import { resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(fileURLToPath(new URL('../../..', import.meta.url)));
const folder = resolve(root, process.argv[2] ?? '');
if (!process.argv[2] || !folder.startsWith(resolve(root, 'demos') + sep)) {
  throw new Error('Pass an example directory inside demos/');
}
const config = JSON.parse(readFileSync(resolve(folder, 'example.json'), 'utf8'));
const payloadPath = resolve(root, config.payload);
if (!payloadPath.startsWith(root + sep)) throw new Error('Payload must be inside repository');
const request = JSON.parse(readFileSync(payloadPath, 'utf8'));
function hasPlaceholder(value) {
  if (Array.isArray(value)) return value.some(hasPlaceholder);
  if (value && typeof value === 'object') return Object.values(value).some(hasPlaceholder);
  if (typeof value !== 'string') return false;
  try {
    const host = new URL(value).hostname.toLowerCase();
    return ['example.com', 'example.org', 'example.net'].includes(host) || host.endsWith('.example.com');
  } catch { return false; }
}
const payload = config.mode === 'mcp'
  ? { jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: config.mcpToolName, arguments: request } }
  : request;
console.log('POST', config.endpoint);
console.log(JSON.stringify(payload, null, 2));
if (!process.argv.includes('--execute')) {
  console.log('Preview only. Add --execute to send.');
} else {
  if (hasPlaceholder(request)) throw new Error('Replace example.com/example.org/example.net URLs before executing');
  const key = process.env.NEXSCOPE_API_KEY;
  if (!key) throw new Error('NEXSCOPE_API_KEY is required');
  const response = await fetch(config.endpoint, {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    redirect: 'manual',
    signal: AbortSignal.timeout(120_000),
  });
  const body = await response.text();
  console.log(body);
  let result;
  try { result = JSON.parse(body); } catch { result = null; }
  if (!response.ok || result?.code !== undefined && result.code !== 0 || result?.error || result?.result?.isError) process.exitCode = 1;
}
