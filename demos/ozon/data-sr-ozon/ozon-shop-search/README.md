# Ozon Shop Search API

Analyze an Ozon shop's products by shop ID. Results come back as structured JSON. Call the Ozon Shop Search API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-shop-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-shop-search.json)

[Repository API reference](../../../../docs/data/ozon-shop-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-sr-ozon/ozon-shop-search
node demos/clients/node/run.mjs demos/ozon/data-sr-ozon/ozon-shop-search
java demos/clients/java/Run.java demos/ozon/data-sr-ozon/ozon-shop-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-shop-search/run`.
