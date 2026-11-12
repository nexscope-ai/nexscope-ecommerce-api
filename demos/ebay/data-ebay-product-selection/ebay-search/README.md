# eBay Search API

Search and browse product listings across multiple international eBay sites.

[Official API documentation](https://www.nexscope.ai/api-docs/ebay-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ebay-search.json)

[Repository API reference](../../../../docs/data/ebay-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ebay/data-ebay-product-selection/ebay-search
node demos/clients/node/run.mjs demos/ebay/data-ebay-product-selection/ebay-search
java demos/clients/java/Run.java demos/ebay/data-ebay-product-selection/ebay-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ebay-search/run`.
