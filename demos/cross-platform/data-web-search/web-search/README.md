# Web Search API

Search the web for current information, community discussions, external articles, and trending topics.

[Official API documentation](https://www.nexscope.ai/api-docs/web-search?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/web-search.json)

[Repository API reference](../../../../docs/data/web-search.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/data-web-search/web-search
node demos/clients/node/run.mjs demos/cross-platform/data-web-search/web-search
java demos/clients/java/Run.java demos/cross-platform/data-web-search/web-search
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/web-search/run`.
