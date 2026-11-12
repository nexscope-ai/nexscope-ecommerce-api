# Temu Category Search API

Find synced Temu category names and IDs by keyword for use in product and store filtering.

[Official API documentation](https://www.nexscope.ai/api-docs/temu-category-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/temu-category-search.json)

[Repository API reference](../../../../docs/data/temu-category-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/temu/data-temu-data/temu-category-search
node demos/clients/node/run.mjs demos/temu/data-temu-data/temu-category-search
java demos/clients/java/Run.java demos/temu/data-temu-data/temu-category-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/temu-category-search/run`.
