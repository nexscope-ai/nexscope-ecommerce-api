# TikTok Video Analytics API

Search TikTok e-commerce trending promotional video leaderboards via Kalodata and query detailed data for specific videos. Supports viewing high-ranking/high-view/hot-selling promotional videos by region, currency, language, and date range, and using videoId to retrieve views, likes, comments, shares, revenue, GPM, and advertising metrics.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-video-analytics?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search TikTok e-commerce trending promotional video leaderboards via Kalodata and query detailed data for specific videos. Supports viewing high-ranking/high-view/hot-selling promotional videos by region, currency, language, and date range, and using videoId to retrieve views, likes, comments, shares, revenue, GPM, and advertising metrics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-video-analytics/run`

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
| `sortField` | object | No | Sort criteria; omitted to use default rank order | {} |
| `videoId` | string | No | TikTok video ID, e.g., 7659161409279806734, obtainable from the video_id in the video rank response | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-video-analytics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-video-analytics request.json
# Or: node examples/javascript/run.mjs tiktok-video-analytics request.json
# Or: python3 examples/python/run.py tiktok-video-analytics request.json
```

### Published request example

```json
{
  "dateRange": "last30Day",
  "sortField": {},
  "videoId": "6768504823336815877",
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
      "video_id": "example-id",
      "views": 1,
      "digg_count": 1,
      "comment_count": 1,
      "share_count": 1,
      "revenue": 1,
      "revenue_growth_rate": 1,
      "ad": 1,
      "ad_view_ratio": 1,
      "ad_revenue_ratio": 1,
      "ads_roas": 1,
      "belonged_creator_id": "example-id",
      "sales_volumn": 1,
      "video_gpm": 1,
      "ads_views": 1,
      "ad_cpa": 1,
      "ads_period": 1,
      "duration": 1,
      "product_number": 1
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-video-analytics.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-video-analytics.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-video-analytics.json)
- [Response fixture](../../examples/responses/tiktok-video-analytics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_video_analytics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
