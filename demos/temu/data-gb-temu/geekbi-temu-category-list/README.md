# GeekBI Temu Category List API

Browse Temu categories for product research. Results come back as structured JSON. Call the Temu Category List API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/geekbi-temu-category-list?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/geekbi-temu-category-list.json)

[Repository API reference](../../../../docs/data/geekbi-temu-category-list.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/temu/data-gb-temu/geekbi-temu-category-list
node demos/clients/node/run.mjs demos/temu/data-gb-temu/geekbi-temu-category-list
java demos/clients/java/Run.java demos/temu/data-gb-temu/geekbi-temu-category-list
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-category-list/run`.
