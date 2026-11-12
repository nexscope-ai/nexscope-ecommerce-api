# Etsy Product Query API

Filter Etsy products by keyword, URL, price, sales, favorites, reviews, listing date, category, product type, and marketplace.

[Official API documentation](https://www.nexscope.ai/api-docs/etsy-product-query?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/etsy-product-query.json)

[Repository API reference](../../../../docs/data/etsy-product-query.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/etsy/data-etsy-data/etsy-product-query
node demos/clients/node/run.mjs demos/etsy/data-etsy-data/etsy-product-query
java demos/clients/java/Run.java demos/etsy/data-etsy-data/etsy-product-query
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/etsy-product-query/run`.
