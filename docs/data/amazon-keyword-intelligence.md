# Amazon Keyword Intelligence API

Query and analyze Amazon ABA (Brand Analytics) search term data, covering 15 marketplaces with nearly 3 years of weekly data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-intelligence?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Query and analyze Amazon ABA (Brand Analytics) search term data, covering 15 marketplaces with nearly 3 years of weekly data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-intelligence/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `analysisDescription` | string | Yes | Natural language description that precisely expresses the query intent | {} |
| `region` | string | No | Site code, default US. Options: US, DE, BR, CA, AU, JP, AE, ES, FR, IT, SA, TR, MX, SE, NL | {} |
| `createDownloadUrl` | boolean | No | Whether to generate a CSV download link, default false | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-intelligence.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-intelligence request.json
# Or: node examples/javascript/run.mjs amazon-keyword-intelligence request.json
# Or: python3 examples/python/run.py amazon-keyword-intelligence request.json
```

### Published request example

```json
{
  "analysisDescription": "Find Amazon Brand Analytics search demand for phone case in the US marketplace",
  "createDownloadUrl": false,
  "region": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "success": false,
  "tables": [],
  "total": 1,
  "downloadUrl": "https://example.com/image.jpg",
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-intelligence.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-intelligence.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-intelligence.json)
- [Response fixture](../../examples/responses/amazon-keyword-intelligence.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_intelligence`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
