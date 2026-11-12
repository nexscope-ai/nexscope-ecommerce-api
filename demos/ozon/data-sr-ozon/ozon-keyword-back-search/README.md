# Ozon Keyword Back Search API

Reverse-lookup Ozon and Wildberries search terms for up to 20 SKUs, with volume, rank, exposure, competition, and conversion.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-keyword-back-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-keyword-back-search.json)

[Repository API reference](../../../../docs/data/ozon-keyword-back-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-sr-ozon/ozon-keyword-back-search
node demos/clients/node/run.mjs demos/ozon/data-sr-ozon/ozon-keyword-back-search
java demos/clients/java/Run.java demos/ozon/data-sr-ozon/ozon-keyword-back-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-keyword-back-search/run`.
