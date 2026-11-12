# 1688 Product Search API

Search 1688 wholesale products for sourcing, supplier discovery, and product selection across Alibaba's domestic B2B marketplace.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-product-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-product-search.json)

[Repository API reference](../../../../docs/data/1688-product-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-sourcing/1688-product-search
node demos/clients/node/run.mjs demos/1688/data-1688-sourcing/1688-product-search
java demos/clients/java/Run.java demos/1688/data-1688-sourcing/1688-product-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-search/run`.
