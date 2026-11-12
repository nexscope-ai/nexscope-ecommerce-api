# TikTok Product Search API

Search TikTok Shop products across 16 markets using sales, creator-sales, pricing, and commission data.

[Official API documentation](https://www.nexscope.ai/api-docs/tiktok-product-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/tiktok-product-search.json)

[Repository API reference](../../../../docs/data/tiktok-product-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/tiktok/data-et-tiktok/tiktok-product-search
node demos/clients/node/run.mjs demos/tiktok/data-et-tiktok/tiktok-product-search
java demos/clients/java/Run.java demos/tiktok/data-et-tiktok/tiktok-product-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-product-search/run`.
