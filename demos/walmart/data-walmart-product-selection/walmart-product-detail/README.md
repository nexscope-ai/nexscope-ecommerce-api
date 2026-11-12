# Walmart Product Detail API

Look up Walmart product details, price history, and sales trends.

[Official API documentation](https://www.nexscope.ai/api-docs/walmart-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/walmart-product-detail.json)

[Repository API reference](../../../../docs/data/walmart-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/walmart/data-walmart-product-selection/walmart-product-detail
node demos/clients/node/run.mjs demos/walmart/data-walmart-product-selection/walmart-product-detail
java demos/clients/java/Run.java demos/walmart/data-walmart-product-selection/walmart-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/walmart-product-detail/run`.
