# Amazon Policy Feed API

Browse Amazon policy updates by marketplace and date, with AI-generated Chinese summaries.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-policy-feed?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-policy-feed.json)

[Repository API reference](../../../../docs/data/amazon-policy-feed.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-amazon-business-insight/amazon-policy-feed
node demos/clients/node/run.mjs demos/amazon/data-amazon-business-insight/amazon-policy-feed
java demos/clients/java/Run.java demos/amazon/data-amazon-business-insight/amazon-policy-feed
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-policy-feed/run`.
