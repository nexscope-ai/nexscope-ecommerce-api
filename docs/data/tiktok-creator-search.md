# TikTok Creator Search API

Search TikTok ecommerce creator rankings.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-creator-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Queries Kalodata creator rankings by region and date range.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-creator-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | No | Optional TikTok Shop market region. | {} |
| `dateRange` | string | No | Relative date range. | {} |
| `pageNumber` | integer | No | Page number. | {} |
| `pageSize` | integer | No | Rows per page. | {} |
| `currency` | string | No | Currency code. | {} |
| `language` | string | No | Response language. | {} |
| `sortField` | object | No | Optional provider sort object. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-creator-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-creator-search request.json
# Or: node examples/javascript/run.mjs tiktok-creator-search request.json
# Or: python3 examples/python/run.py tiktok-creator-search request.json
```

### Published request example

```json
{
  "dateRange": "last30Day",
  "pageNumber": 1,
  "pageSize": 10,
  "region": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": [
    {
      "creator_id": "68616495085350913",
      "creator_nickname": "Example creator",
      "creator_handle": "@creator",
      "creator_followers": "100000",
      "content_views": "1000000",
      "sales_volumn": 100,
      "revenue": 1000,
      "video_revenue": 600,
      "live_revenue": 400,
      "revenue_growth_rate": 12.5,
      "creator_region": "US",
      "creator_status": "active",
      "new_followers": 1000,
      "video_number": 20,
      "live_number": 5,
      "product_number": 10,
      "shop_number": 3
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-creator-search.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-creator-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-creator-search.json)
- [Response fixture](../../examples/responses/tiktok-creator-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_creator_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
