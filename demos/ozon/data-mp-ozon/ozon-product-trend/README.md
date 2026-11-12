# Ozon Product Trend API

Track daily Ozon SKU sales, price, stock, rating, and optional search visibility to analyze growth, seasonality, and anomalies.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-product-trend?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-product-trend.json)

[Repository API reference](../../../../docs/data/ozon-product-trend.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-mp-ozon/ozon-product-trend
node demos/clients/node/run.mjs demos/ozon/data-mp-ozon/ozon-product-trend
java demos/clients/java/Run.java demos/ozon/data-mp-ozon/ozon-product-trend
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-trend/run`.
