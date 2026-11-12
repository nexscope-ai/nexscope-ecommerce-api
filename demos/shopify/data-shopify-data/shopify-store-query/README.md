# Shopify Store Query API

Find Shopify stores by country, product range, sales, and audience size.

[Official API documentation](https://www.nexscope.ai/api-docs/shopify-store-query?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/shopify-store-query.json)

[Repository API reference](../../../../docs/data/shopify-store-query.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/shopify/data-shopify-data/shopify-store-query
node demos/clients/node/run.mjs demos/shopify/data-shopify-data/shopify-store-query
java demos/clients/java/Run.java demos/shopify/data-shopify-data/shopify-store-query
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/shopify-store-query/run`.
