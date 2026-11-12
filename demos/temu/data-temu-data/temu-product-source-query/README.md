# Temu Product Source Query API

Find Temu products by keyword, category, price, sales, and ratings.

[Official API documentation](https://www.nexscope.ai/api-docs/temu-product-source-query?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/temu-product-source-query.json)

[Repository API reference](../../../../docs/data/temu-product-source-query.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/temu/data-temu-data/temu-product-source-query
node demos/clients/node/run.mjs demos/temu/data-temu-data/temu-product-source-query
java demos/clients/java/Run.java demos/temu/data-temu-data/temu-product-source-query
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/temu-product-source-query/run`.
