# Walmart Search API

Search Walmart product listings by keyword, category, price range, and other filters.

[Official API documentation](https://www.nexscope.ai/api-docs/walmart-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/walmart-search.json)

[Repository API reference](../../../../docs/data/walmart-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/walmart/data-walmart-product-selection/walmart-search
node demos/clients/node/run.mjs demos/walmart/data-walmart-product-selection/walmart-search
java demos/clients/java/Run.java demos/walmart/data-walmart-product-selection/walmart-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/walmart-search/run`.
