# Amazon Category Lookup API

Find Amazon category IDs by marketplace or category name.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-category-lookup?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-category-lookup.json)

[Repository API reference](../../../../docs/data/amazon-category-lookup.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/amazon-marketplace-intelligence/amazon-category-lookup
node demos/clients/node/run.mjs demos/amazon/amazon-marketplace-intelligence/amazon-category-lookup
java demos/clients/java/Run.java demos/amazon/amazon-marketplace-intelligence/amazon-category-lookup
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-category-lookup/run`.
