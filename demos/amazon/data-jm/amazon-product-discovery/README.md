# Amazon Product Discovery API

Discover potential Amazon bestsellers for product research.

[Official API documentation](https://www.nexscope.ai/api-docs/amazon-product-discovery?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/amazon-product-discovery.json)

[Repository API reference](../../../../docs/data/amazon-product-discovery.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/amazon/data-jm/amazon-product-discovery
node demos/clients/node/run.mjs demos/amazon/data-jm/amazon-product-discovery
java demos/clients/java/Run.java demos/amazon/data-jm/amazon-product-discovery
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-discovery/run`.
