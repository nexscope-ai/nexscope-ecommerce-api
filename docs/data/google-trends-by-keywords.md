# Google Trends By Keywords API

Google Trends keyword search popularity comparison and trend analysis, supporting global regions and custom time ranges. Triggered by: Google Trends, keyword popularity over time, search interest comparison, keyword trend analysis, seasonal trend detection, regional search popularity, keyword heatmap, multi-keyword comparison on Google, keyword research, market trend analysis, search trends, seasonal analysis, regional popularity.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/google-trends-by-keywords?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Google Trends keyword search popularity comparison and trend analysis, supporting global regions and custom time ranges. Triggered by: Google Trends, keyword popularity over time, search interest comparison, keyword trend analysis, seasonal trend detection, regional search popularity, keyword heatmap, multi-keyword comparison on Google, keyword research, market trend analysis, search trends, seasonal analysis, regional popularity.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/google-trends-by-keywords/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword (the keyword must be in the language of the target country! For example, use English keywords for the US, German keywords for Germany. If not in the corresponding country's language, please translate first.) Max length 100 characters | {} |
| `region` | string | No | Country/region, default US. Options: US, GB, JP, CA, MX, DE, FR, IT, ES, NL, AU, SG, AE, BR, IN, TR, PL, SE | {} |
| `dayRangeStart` | string | No | Time range start ( | {} |
| `dayRangeEnd` | string | No | Time range end ( | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/google-trends-by-keywords.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh google-trends-by-keywords request.json
# Or: node examples/javascript/run.mjs google-trends-by-keywords request.json
# Or: python3 examples/python/run.py google-trends-by-keywords request.json
```

### Published request example

```json
{
  "region": "US",
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "trendInfoForKeys": [
    {
      "keyword": "phone case",
      "trendValues": []
    }
  ],
  "chartOption": {
    "fieldY": [],
    "data": []
  },
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/google-trends-by-keywords.request.json) — field-descriptors
- [Response definition](../../schemas/google-trends-by-keywords.response.json) — field-descriptors
- [Editable request sample](../../payloads/google-trends-by-keywords.json)
- [Response fixture](../../examples/responses/google-trends-by-keywords.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_google_trends_by_keywords`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
