# Ozon Product Search API

Search Ozon products by Russian keyword or SKU and return product ID, title, brand, and seller data for discovery.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-product-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-product-search.json)

[Repository API reference](../../../../docs/data/ozon-product-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-mp-ozon/ozon-product-search
node demos/clients/node/run.mjs demos/ozon/data-mp-ozon/ozon-product-search
java demos/clients/java/Run.java demos/ozon/data-mp-ozon/ozon-product-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-search/run`.
