# GeekBI Temu Product Detail API

Look up details for a Temu product. Results come back as structured JSON. Call the Temu Product Detail API via REST or MCP with your Nexscope API key.

[Official API documentation](https://www.nexscope.ai/api-docs/geekbi-temu-goods-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/geekbi-temu-goods-detail.json)

[Repository API reference](../../../../docs/data/geekbi-temu-goods-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/temu/data-gb-temu/geekbi-temu-goods-detail
node demos/clients/node/run.mjs demos/temu/data-gb-temu/geekbi-temu-goods-detail
java demos/clients/java/Run.java demos/temu/data-gb-temu/geekbi-temu-goods-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-goods-detail/run`.
