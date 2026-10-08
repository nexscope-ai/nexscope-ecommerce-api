# Amazon Category Lookup API

Browse Amazon category nodes or search category metadata by name.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-category-lookup?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Supports exact parent-node browsing and label-based category search.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-category-lookup/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operation` | string | No | lookup (default) or like. | {} |
| `marketId` | string | No | Amazon marketplace or site identifier. | {} |
| `nodeId` | string | No | Parent category node identifier. | {} |
| `table` | string | No | Optional upstream category table selector. | {} |
| `nodeLabel` | string | No | Category label required by operation=like. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-category-lookup.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-category-lookup request.json
# Or: node examples/javascript/run.mjs amazon-category-lookup request.json
# Or: python3 examples/python/run.py amazon-category-lookup request.json
```

### Published request example

```json
{
  "marketId": "1",
  "operation": "lookup",
  "nodeId": "0"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "data": [
    {
      "nodeId": "172282",
      "nodeLabel": "Electronics",
      "parentNodeId": "0"
    }
  ],
  "costToken": 150
}
```

## Full definitions

- [Request definition](../../schemas/amazon-category-lookup.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-category-lookup.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-category-lookup.json)
- [Response fixture](../../examples/responses/amazon-category-lookup.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_category_lookup`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
