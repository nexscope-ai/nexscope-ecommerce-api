# Ozon Product Detail Search API

Retrieve a single Ozon SKU's pricing, sales, stock, ranking, trend, brand, seller, fulfillment, weight, and listing-age data.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-product-detail-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-product-detail-search.json)

[Repository API reference](../../../../docs/data/ozon-product-detail-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-sr-ozon/ozon-product-detail-search
node demos/clients/node/run.mjs demos/ozon/data-sr-ozon/ozon-product-detail-search
java demos/clients/java/Run.java demos/ozon/data-sr-ozon/ozon-product-detail-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-detail-search/run`.
