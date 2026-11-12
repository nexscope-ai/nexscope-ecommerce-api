# Patent Claims Translation API

Read translated patent claims. Results come back as structured JSON. Call the Patent Claims Translation API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-claims-translation?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-claims-translation.json)

[Repository API reference](../../../../docs/data/patent-claims-translation.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-claims-translation
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-claims-translation
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-claims-translation
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-claims-translation/run`.
