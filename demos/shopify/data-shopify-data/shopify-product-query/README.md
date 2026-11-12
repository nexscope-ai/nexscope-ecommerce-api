# Shopify Product Query API

Find Shopify products by keyword, price, sales, and other product filters.

[Official API documentation](https://www.nexscope.ai/api-docs/shopify-product-query?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/shopify-product-query.json)

[Repository API reference](../../../../docs/data/shopify-product-query.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/shopify/data-shopify-data/shopify-product-query
node demos/clients/node/run.mjs demos/shopify/data-shopify-data/shopify-product-query
java demos/clients/java/Run.java demos/shopify/data-shopify-data/shopify-product-query
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/shopify-product-query/run`.
