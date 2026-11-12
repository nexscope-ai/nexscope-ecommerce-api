# Amazon Product History API

Retrieve Amazon product attributes and up to 12 months of sales history by ASIN.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-history?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-history.json)

[Repository API reference](../../../../docs/data/amazon-product-history.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-kp/amazon-product-history
node demos/clients/node/run.mjs demos/amazon/data-kp/amazon-product-history
java demos/clients/java/Run.java demos/amazon/data-kp/amazon-product-history
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-history/run`.
