# Walmart Keyword Research API

Walmart Keyword Research public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/walmart-keyword-research?view=api&co-from=github-ecommerce-api)

Category: Walmart Marketplace Intelligence · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/walmart-keyword-research/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operation` | string | Yes | Walmart keyword research operation | {} |
| `name` | string | No | Keyword name required by searchByName | {} |
| `keyword` | string | No | Keyword required by searchProducts, detail, or relatedKeywords | {} |
| `productId` | string | No | Product ID required by productKeywords | {} |
| `command` | string | No | Read-only favoriteList command: all, dict, or dict=<value> | {} |
| `pattern` | object | No | Optional marketQuery filter object | {} |
| `pattern.keyword` | string | No | Keyword filter inside pattern | {} |
| `pattern.rankCondition` | array | No | One- or two-value rank range | {} |
| `pattern.searchVolumeCondition` | array | No | One- or two-value search-volume range | {} |
| `pageIndex` | integer | No | Page number, starting at 1 | {} |
| `pageSize` | integer | No | Page size from 20 to 200 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/walmart-keyword-research.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh walmart-keyword-research request.json
# Or: node examples/javascript/run.mjs walmart-keyword-research request.json
# Or: python3 examples/python/run.py walmart-keyword-research request.json
```

### Published request example

```json
{
  "pageIndex": 1,
  "operation": "searchByName",
  "name": "wireless earbuds"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "requestConsumed": 1,
  "value": [
    {
      "Keyword": "wireless earbuds",
      "Rank": 1,
      "SearchVolume": 1
    }
  ],
  "operation": "searchByName"
}
```

## Full definitions

- [Request definition](../../schemas/walmart-keyword-research.request.json) — json-schema
- [Response definition](../../schemas/walmart-keyword-research.response.json) — json-schema
- [Editable request sample](../../payloads/walmart-keyword-research.json)
- [Response fixture](../../examples/responses/walmart-keyword-research.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_walmart_keyword_research`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
