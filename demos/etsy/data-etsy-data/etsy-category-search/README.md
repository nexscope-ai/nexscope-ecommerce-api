# Etsy Category Search API

Find Etsy category IDs by category name, ID, or parent ID for product and store filtering.

[Official API documentation](https://www.nexscope.ai/api-docs/etsy-category-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/etsy-category-search.json)

[Repository API reference](../../../../docs/data/etsy-category-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/etsy/data-etsy-data/etsy-category-search
node demos/clients/node/run.mjs demos/etsy/data-etsy-data/etsy-category-search
java demos/clients/java/Run.java demos/etsy/data-etsy-data/etsy-category-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/etsy-category-search/run`.
