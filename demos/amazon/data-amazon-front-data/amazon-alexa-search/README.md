# Amazon Alexa Search API

Ask Amazon storefront Alexa for shopping guidance, recommended product groups, ASIN lists, and follow-up questions.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-alexa-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-alexa-search.json)

[Repository API reference](../../../../docs/data/amazon-alexa-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-amazon-front-data/amazon-alexa-search
node demos/clients/node/run.mjs demos/amazon/data-amazon-front-data/amazon-alexa-search
java demos/clients/java/Run.java demos/amazon/data-amazon-front-data/amazon-alexa-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-alexa-search/run`.
