# Patent References API

Retrieve patent documents and non-patent literature cited by one or more patents for prior-art, citation, and technology.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-references?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-references.json)

[Repository API reference](../../../../docs/data/patent-references.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-references
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-references
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-references
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-references/run`.
