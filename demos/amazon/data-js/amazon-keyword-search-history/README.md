# Amazon Keyword Search History API

Track exact Amazon keyword search volume in seven-day periods across 10 marketplaces.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-keyword-search-history?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-keyword-search-history.json)

[Repository API reference](../../../../docs/data/amazon-keyword-search-history.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-js/amazon-keyword-search-history
node demos/clients/node/run.mjs demos/amazon/data-js/amazon-keyword-search-history
java demos/clients/java/Run.java demos/amazon/data-js/amazon-keyword-search-history
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-search-history/run`.
