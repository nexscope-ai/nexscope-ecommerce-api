# Amazon Product Price Series API

Track an Amazon product's price, best-seller rank, ratings, and sales over time.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-price-series?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-price-series.json)

[Repository API reference](../../../../docs/data/amazon-product-price-series.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-kp/amazon-product-price-series
node demos/clients/node/run.mjs demos/amazon/data-kp/amazon-product-price-series
java demos/clients/java/Run.java demos/amazon/data-kp/amazon-product-price-series
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-price-series/run`.
