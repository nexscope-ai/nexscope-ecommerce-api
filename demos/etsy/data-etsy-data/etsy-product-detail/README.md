# Etsy Product Detail API

Retrieve public Etsy listing details from a validated marketplace URL for product, pricing, shop, and competitive research.

[Official API documentation](https://www.nexscope.ai/api-docs/etsy-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/etsy-product-detail.json)

[Repository API reference](../../../../docs/data/etsy-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/etsy/data-etsy-data/etsy-product-detail
node demos/clients/node/run.mjs demos/etsy/data-etsy-data/etsy-product-detail
java demos/clients/java/Run.java demos/etsy/data-etsy-data/etsy-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/etsy-product-detail/run`.
