# TikTok Creator Analytics API

Search TikTok e-commerce creator leaderboards via Kalodata and query detailed profiles for specific creators. Supports viewing top-performing influencer-sellers by region, currency, language, and date range, and using creatorId to retrieve follower count, video/live revenue and GPM, contact information, and associated shops.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-creator-analytics?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search TikTok e-commerce creator leaderboards via Kalodata and query detailed profiles for specific creators. Supports viewing top-performing influencer-sellers by region, currency, language, and date range, and using creatorId to retrieve follower count, video/live revenue and GPM, contact information, and associated shops.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-creator-analytics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | No | Region/market code, e.g., US | {} |
| `dateRange` | string | No | Time range, e.g., last7Day, last30Day | {} |
| `pageNumber` | integer | No | Page number, value range 1-5 | {} |
| `pageSize` | integer | No | Items per page, value range 5-100 | {} |
| `language` | string | No | Return language, e.g., zh-CN, en-US | {} |
| `currency` | string | No | Currency unit, e.g., USD | {} |
| `sortField` | object | No | Sort criteria; pass an empty object {} for default rank order when not sorting | {} |
| `creatorId` | string | No | Creator unique ID, e.g., 7153432386608251946, obtainable from the creator_id in the creator rank response | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-creator-analytics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-creator-analytics request.json
# Or: node examples/javascript/run.mjs tiktok-creator-analytics request.json
# Or: python3 examples/python/run.py tiktok-creator-analytics request.json
```

### Published request example

```json
{
  "dateRange": "last30Day",
  "sortField": {},
  "creatorId": "68616495085350913",
  "region": "US",
  "pageNumber": 1,
  "pageSize": 10
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
      "creator_id": "example-id",
      "sales_volumn": 1,
      "revenue": 1,
      "video_revenue": 1,
      "live_revenue": 1,
      "revenue_growth_rate": 1,
      "creator_belonged_shop_id": "example-id",
      "new_followers": 1,
      "unit_price": 1,
      "video_number": 1,
      "video_views": 1,
      "video_gpm": 1,
      "live_number": 1,
      "live_views": 1,
      "live_gpm": 1,
      "product_number": 1,
      "shop_number": 1
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-creator-analytics.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-creator-analytics.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-creator-analytics.json)
- [Response fixture](../../examples/responses/tiktok-creator-analytics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_creator_analytics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
