# Patent Cited By API

Find later patents that cite a patent you are researching.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-cited-by?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-cited-by.json)

[Repository API reference](../../../../docs/data/patent-cited-by.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-cited-by
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-cited-by
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-cited-by
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-cited-by/run`.
