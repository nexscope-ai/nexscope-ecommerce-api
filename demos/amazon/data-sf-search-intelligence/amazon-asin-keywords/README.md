# Amazon ASIN Keywords API

Find keywords driving traffic to an Amazon ASIN.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-asin-keywords?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-asin-keywords.json)

[Repository API reference](../../../../docs/data/amazon-asin-keywords.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-sf-search-intelligence/amazon-asin-keywords
node demos/clients/node/run.mjs demos/amazon/data-sf-search-intelligence/amazon-asin-keywords
java demos/clients/java/Run.java demos/amazon/data-sf-search-intelligence/amazon-asin-keywords
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-asin-keywords/run`.
