# Amazon Advertising API

Manage Amazon Sponsored Products, Sponsored Brands, and Sponsored Display advertising.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-advertising?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-advertising.json)

[Repository API reference](../../../../docs/data/amazon-advertising.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-amazon-ads/amazon-advertising
node demos/clients/node/run.mjs demos/amazon/data-amazon-ads/amazon-advertising
java demos/clients/java/Run.java demos/amazon/data-amazon-ads/amazon-advertising
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-advertising/run`.
