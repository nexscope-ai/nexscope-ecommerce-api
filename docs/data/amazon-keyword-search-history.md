# Amazon Keyword Search History API

Jungle Scout keyword historical search volume query, returning Amazon keyword exact search volume trends in 7-day periods, covering 10 marketplaces including US, UK, DE, JP, etc.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-search-history?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Jungle Scout keyword historical search volume query, returning Amazon keyword exact search volume trends in 7-day periods, covering 10 marketplaces including US, UK, DE, JP, etc.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-search-history/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Target marketplace code. Options: us, uk, de, in, ca, fr, it, es, mx, jp | {} |
| `keyword` | string | Yes | Keyword to query | {} |
| `startDate` | string | Yes | Start date (format: YYYY-MM-DD) | {} |
| `endDate` | string | Yes | End date (format: YYYY-MM-DD); max interval from startDate is 366 days | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-search-history.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-search-history request.json
# Or: node examples/javascript/run.mjs amazon-keyword-search-history request.json
# Or: python3 examples/python/run.py amazon-keyword-search-history request.json
```

### Published request example

```json
{
  "startDate": "2026-01-01",
  "keyword": "phone case",
  "endDate": "2026-01-31",
  "marketplace": "us"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costToken": 1,
  "historicalSearchVolumeList": [
    {
      "id": "example-id",
      "estimateStartDate": "2026-01-01",
      "estimateEndDate": "2026-01-01",
      "estimatedExactSearchVolume": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-search-history.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-search-history.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-search-history.json)
- [Response fixture](../../examples/responses/amazon-keyword-search-history.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_search_history`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
