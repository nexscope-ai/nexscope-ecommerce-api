# Product Description Generator API

Generate product descriptions from writing instructions and product images.

[Official API documentation](https://www.nexscope.ai/api-docs/product-description-generator?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/product-description-generator.json)

[Repository API reference](../../../../docs/data/product-description-generator.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/ai-content-generation/product-description-generator
node demos/clients/node/run.mjs demos/cross-platform/ai-content-generation/product-description-generator
java demos/clients/java/Run.java demos/cross-platform/ai-content-generation/product-description-generator
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/product-description-generator/run`.
