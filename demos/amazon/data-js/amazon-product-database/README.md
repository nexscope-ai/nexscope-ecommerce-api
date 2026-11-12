# Amazon Product Database API

Find Amazon products by category, price, sales, reviews, and seller type.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-database?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-database.json)

[Repository API reference](../../../../docs/data/amazon-product-database.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-js/amazon-product-database
node demos/clients/node/run.mjs demos/amazon/data-js/amazon-product-database
java demos/clients/java/Run.java demos/amazon/data-js/amazon-product-database
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-database/run`.
