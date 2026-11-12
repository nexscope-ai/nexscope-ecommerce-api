# Amazon Market Product Detail API

Look up product details and historical trends by ASIN.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-market-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-market-product-detail.json)

[Repository API reference](../../../../docs/data/amazon-market-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-st/amazon-market-product-detail
node demos/clients/node/run.mjs demos/amazon/data-st/amazon-market-product-detail
java demos/clients/java/Run.java demos/amazon/data-st/amazon-market-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-product-detail/run`.
