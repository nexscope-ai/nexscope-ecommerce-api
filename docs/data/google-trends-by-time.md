# Google Trends By Time API

Query and analyze Google Trends real-time hot topics and trending searches for a specified time range and country/region. Triggered by: Google Trends, hot topics, real-time trending, popular trends, current hot searches, recent trending, viral topics, trending searches, trend discovery, market trends, what's popular, trending now, breakout topics.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/google-trends-by-time?view=api&co-from=github-ecommerce-api)

Category: Search & Trend Intelligence · Data API

Query and analyze Google Trends real-time hot topics and trending searches for a specified time range and country/region. Triggered by: Google Trends, hot topics, real-time trending, popular trends, current hot searches, recent trending, viral topics, trending searches, trend discovery, market trends, what's popular, trending now, breakout topics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/google-trends-by-time/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `days` | integer | No | Time range, query trend data for the last N days, default 7. Common values: 1, 2, 7 | {} |
| `region` | string | No | Country/region code, default US. Options: US, GB, JP, CA, MX, DE, FR, IT, ES, NL, AU, SG, AE, BR, IN, TR, PL, SE | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/google-trends-by-time.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh google-trends-by-time request.json
# Or: node examples/javascript/run.mjs google-trends-by-time request.json
# Or: python3 examples/python/run.py google-trends-by-time request.json
```

### Published request example

```json
{
  "region": "US",
  "days": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costToken": 1,
  "chartOption": {
    "data": [],
    "fieldY": []
  },
  "trendValues": [
    {
      "query": "phone case",
      "searchVolume": 1,
      "increasePercentage": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/google-trends-by-time.request.json) — field-descriptors
- [Response definition](../../schemas/google-trends-by-time.response.json) — field-descriptors
- [Editable request sample](../../payloads/google-trends-by-time.json)
- [Response fixture](../../examples/responses/google-trends-by-time.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_google_trends_by_time`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
