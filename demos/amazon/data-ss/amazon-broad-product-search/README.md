# Amazon Broad Product Search API

Find Amazon products by sales, price, ratings, and fulfillment.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-broad-product-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-broad-product-search.json)

[Repository API reference](../../../../docs/data/amazon-broad-product-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-ss/amazon-broad-product-search
node demos/clients/node/run.mjs demos/amazon/data-ss/amazon-broad-product-search
java demos/clients/java/Run.java demos/amazon/data-ss/amazon-broad-product-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-broad-product-search/run`.
