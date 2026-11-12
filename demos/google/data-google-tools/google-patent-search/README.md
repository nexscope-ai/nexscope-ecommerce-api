# Google Patent Search API

Search Google patent and related scholarly records with structured results, pagination details, and search summaries.

[Official API documentation](https://www.nexscope.ai/api-docs/google-patent-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/google-patent-search.json)

[Repository API reference](../../../../docs/data/google-patent-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/google/data-google-tools/google-patent-search
node demos/clients/node/run.mjs demos/google/data-google-tools/google-patent-search
java demos/clients/java/Run.java demos/google/data-google-tools/google-patent-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/google-patent-search/run`.
