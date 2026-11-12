# Amazon Product Database Search API

Find Amazon products using detailed price, sales, size, and shipping filters.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-database-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-database-search.json)

[Repository API reference](../../../../docs/data/amazon-product-database-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-kp/amazon-product-database-search
node demos/clients/node/run.mjs demos/amazon/data-kp/amazon-product-database-search
java demos/clients/java/Run.java demos/amazon/data-kp/amazon-product-database-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-database-search/run`.
