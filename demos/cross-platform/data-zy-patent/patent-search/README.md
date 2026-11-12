# Patent Search API

Find patents and their publication numbers for product research.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-search.json)

[Repository API reference](../../../../docs/data/patent-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-search
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-search
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-search/run`.
