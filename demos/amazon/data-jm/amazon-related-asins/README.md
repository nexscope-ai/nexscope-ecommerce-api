# Amazon Related ASINs API

Find same-niche Amazon competitors by ASIN using conversion, click, sales, review, rating, price, and margin filters.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-related-asins?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-related-asins.json)

[Repository API reference](../../../../docs/data/amazon-related-asins.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-jm/amazon-related-asins
node demos/clients/node/run.mjs demos/amazon/data-jm/amazon-related-asins
java demos/clients/java/Run.java demos/amazon/data-jm/amazon-related-asins
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-related-asins/run`.
