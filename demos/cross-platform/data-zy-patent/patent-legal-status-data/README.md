# Patent Legal Status Data API

Check a patent's recorded legal status. Results come back as structured JSON. Call the Patent Legal Status API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/patent-legal-status-data?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/patent-legal-status-data.json)

[Repository API reference](../../../../docs/data/patent-legal-status-data.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-zy-patent/patent-legal-status-data
node demos/clients/node/run.mjs demos/cross-platform/data-zy-patent/patent-legal-status-data
java demos/clients/java/Run.java demos/cross-platform/data-zy-patent/patent-legal-status-data
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/patent-legal-status-data/run`.
