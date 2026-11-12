# Ozon Product Detail API

Retrieve full details for up to 100 Ozon SKUs. Call the Ozon Product Detail API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/ozon-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/ozon-product-detail.json)

[Repository API reference](../../../../docs/data/ozon-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/ozon/data-mp-ozon/ozon-product-detail
node demos/clients/node/run.mjs demos/ozon/data-mp-ozon/ozon-product-detail
java demos/clients/java/Run.java demos/ozon/data-mp-ozon/ozon-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-detail/run`.
