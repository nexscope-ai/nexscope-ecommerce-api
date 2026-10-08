# TikTok Livestream Analytics API

Search TikTok e-commerce livestream leaderboards via Kalodata and query detailed data for specific livestreams. Supports viewing high-ranking, high-sales TikTok shopping livestreams by region, currency, language, and date range, and using livestreamId to retrieve revenue, viewers, duration, GPM, and number of products sold.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-livestream-analytics?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search TikTok e-commerce livestream leaderboards via Kalodata and query detailed data for specific livestreams. Supports viewing high-ranking, high-sales TikTok shopping livestreams by region, currency, language, and date range, and using livestreamId to retrieve revenue, viewers, duration, GPM, and number of products sold.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-livestream-analytics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | No | Region/market code, e.g., US. Max length 1000 | {} |
| `dateRange` | string | No | Time range, e.g., last7Day (last 7 days), last30Day (last 30 days). Max length 1000 | {} |
| `pageNumber` | integer | No | Page number, value range 1-5 (out of range returns errcode 501) | {} |
| `pageSize` | integer | No | Items per page, value range 5-100 | {} |
| `language` | string | No | Return language, e.g., zh-CN, en-US. Max length 1000 | {} |
| `currency` | string | No | Currency unit, e.g., USD. Max length 1000 | {} |
| `sortField` | object | No | Sort criteria, structure defined by the gateway; pass an empty object {} for default rank order when not sorting | {} |
| `livestreamId` | string | No | Target livestream unique ID (camelCase), e.g., 7661409374878878494. Typically obtained from the livestream_id in the livestream rank endpoint. Max length 1000 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-livestream-analytics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-livestream-analytics request.json
# Or: node examples/javascript/run.mjs tiktok-livestream-analytics request.json
# Or: python3 examples/python/run.py tiktok-livestream-analytics request.json
```

### Published request example

```json
{
  "sortField": {},
  "pageNumber": 1,
  "dateRange": "last30Day",
  "pageSize": 10,
  "region": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "data": [
    {
      "livestream_start_time": 1,
      "livestream_end_time": 1,
      "livestream_duration": 1,
      "livestream_id": "example-id",
      "creator_id": "example-id",
      "views": 1,
      "viewers": 1,
      "gpm": 1,
      "product_number": 1
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-livestream-analytics.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-livestream-analytics.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-livestream-analytics.json)
- [Response fixture](../../examples/responses/tiktok-livestream-analytics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_livestream_analytics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
