# Amazon Reviews List API

Retrieve customer reviews for an Amazon product.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-reviews-list?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-reviews-list.json)

[Repository API reference](../../../../docs/data/amazon-reviews-list.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-amazon-front-data/amazon-reviews-list
node demos/clients/node/run.mjs demos/amazon/data-amazon-front-data/amazon-reviews-list
java demos/clients/java/Run.java demos/amazon/data-amazon-front-data/amazon-reviews-list
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-reviews-list/run`.
