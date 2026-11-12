# Amazon Market Product Search API

Filter Amazon products using market data and monthly snapshots.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-market-product-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-market-product-search.json)

[Repository API reference](../../../../docs/data/amazon-market-product-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-st/amazon-market-product-search
node demos/clients/node/run.mjs demos/amazon/data-st/amazon-market-product-search
java demos/clients/java/Run.java demos/amazon/data-st/amazon-market-product-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-product-search/run`.
