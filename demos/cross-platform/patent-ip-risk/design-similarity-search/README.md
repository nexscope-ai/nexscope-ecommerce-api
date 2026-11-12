# Design Similarity Search API

Find similar design-registration candidates from a product image with region, Locarno and legal-status filters.

[Official API documentation](https://www.nexscope.ai/api-docs/design-similarity-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/design-similarity-search.json)

[Repository API reference](../../../../docs/data/design-similarity-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/patent-ip-risk/design-similarity-search
node demos/clients/node/run.mjs demos/cross-platform/patent-ip-risk/design-similarity-search
java demos/clients/java/Run.java demos/cross-platform/patent-ip-risk/design-similarity-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/ai/designSimilaritySearch`.
