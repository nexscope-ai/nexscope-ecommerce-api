# Amazon Sales Estimates API

Get daily estimated Amazon ASIN sales and latest known price for a selected date range across 10 marketplaces.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-sales-estimates?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-sales-estimates.json)

[Repository API reference](../../../../docs/data/amazon-sales-estimates.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-js/amazon-sales-estimates
node demos/clients/node/run.mjs demos/amazon/data-js/amazon-sales-estimates
java demos/clients/java/Run.java demos/amazon/data-js/amazon-sales-estimates
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-sales-estimates/run`.
