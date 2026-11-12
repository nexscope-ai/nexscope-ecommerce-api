# 1688 Authorize URL API

Generate a 1688 authorization link to connect your store and enable procurement requests.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-authorize-url?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-authorize-url.json)

[Repository API reference](../../../../docs/data/1688-authorize-url.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-authorize-url
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-authorize-url
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-authorize-url
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/authorizeUrl`.
