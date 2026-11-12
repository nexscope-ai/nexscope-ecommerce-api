# Amazon Product Detail API

Retrieve product details, pricing, and ratings by ASIN.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-detail.json)

[Repository API reference](../../../../docs/data/amazon-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-amazon-front-data/amazon-product-detail
node demos/clients/node/run.mjs demos/amazon/data-amazon-front-data/amazon-product-detail
java demos/clients/java/Run.java demos/amazon/data-amazon-front-data/amazon-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-detail/run`.
