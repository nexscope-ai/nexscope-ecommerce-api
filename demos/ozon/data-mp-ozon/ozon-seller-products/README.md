# Ozon Seller Products API

List an Ozon seller's SKUs with sales, revenue, price, rating, stock, turnover, and lost-revenue metrics for competitor analysis.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-seller-products?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-seller-products.json)

[Repository API reference](../../../../docs/data/ozon-seller-products.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-mp-ozon/ozon-seller-products
node demos/clients/node/run.mjs demos/ozon/data-mp-ozon/ozon-seller-products
java demos/clients/java/Run.java demos/ozon/data-mp-ozon/ozon-seller-products
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-seller-products/run`.
