# Patent Description Data Translation API

Read translated patent descriptions. Call the Patent Description Translation API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-description-data-translation?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-description-data-translation.json)

[Repository API reference](../../../../docs/data/patent-description-data-translation.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-description-data-translation
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-description-data-translation
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-description-data-translation
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-description-data-translation/run`.
