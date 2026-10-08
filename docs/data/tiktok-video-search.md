# TikTok Video Search API

Search and analyze TikTok video data, filter videos by region, creator, product, category, views, duration, publish time, selling/ad/AI video flags, and return views, likes, comments, shares, favorites, video sales and GMV metrics across 16 TikTok Shop sites.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-video-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search and analyze TikTok video data, filter videos by region, creator, product, category, views, duration, publish time, selling/ad/AI video flags, and return views, likes, comments, shares, favorites, video sales and GMV metrics across 16 TikTok Shop sites.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-video-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | Yes | Region code. Options: US (United States), ID (Indonesia), TH (Thailand), PH (Philippines), MY (Malaysia), VN (Vietnam), GB (United Kingdom), MX (Mexico), SG (Singapore), SA (Saudi Arabia), BR (Brazil), ES (Spain), JP (Japan), DE (Germany), IT (Italy), FR (France) | {} |
| `userId` | string | No | Creator ID filter. Max length 1000 | {} |
| `productId` | string | No | Associated product ID. Max length 1000 | {} |
| `productCategoryId` | string | No | Associated product category ID. Max length 1000 | {} |
| `minTotalViewsCnt` | integer | No | Video view count filter (minimum) | {} |
| `maxTotalViewsCnt` | integer | No | Video view count filter (maximum) | {} |
| `minDuration` | integer | No | Video duration range filter (seconds) - minimum | {} |
| `maxDuration` | integer | No | Video duration range filter (seconds) - maximum | {} |
| `minCreateTime` | integer | No | Publish time range filter (seconds-level timestamp) - minimum | {} |
| `maxCreateTime` | integer | No | Publish time range filter (seconds-level timestamp) - maximum | {} |
| `salesFlag` | integer | No | Whether a promotional video: 0=non-promotional video, 1=promotional video | {} |
| `isAd` | integer | No | Whether an ad video: 0=non-ad video, 1=ad video | {} |
| `createdByAi` | string | No | Whether AI video, string "true"=AI video, "false"=non-AI video (regex ^(true | {} |
| `videoSortField` | integer | No | Sort field: 1=total_digg_cnt (likes), 2=create_time (publish time), 3=total_views_cnt (views) | {} |
| `sortType` | integer | No | Sort direction: 0=ascending, 1=descending | {} |
| `pageNum` | integer | No | Page number, starting from 1 | {} |
| `pageSize` | integer | No | Items per page. Must be a multiple of 10, max 100; the third-party API limit is 10 per page, internally the gateway fetches 10 per page in multiple rounds and merges | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-video-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-video-search request.json
# Or: node examples/javascript/run.mjs tiktok-video-search request.json
# Or: python3 examples/python/run.py tiktok-video-search request.json
```

### Published request example

```json
{
  "pageNumber": 1,
  "keyword": "phone case",
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
  "total": 1,
  "data": [],
  "columns": [
    {
      "videoId": "example-id",
      "officialUrl": "https://example.com/image.jpg",
      "coverUrl": "https://example.com/image.jpg",
      "duration": 1,
      "createDate": "2026-01-01",
      "userId": "example-id",
      "uniqueId": "example-id",
      "totalViewsCnt": 1,
      "totalViews1dCnt": 1,
      "totalViews7dCnt": 1,
      "totalViews30dCnt": 1,
      "totalDiggCnt": 1,
      "totalDigg1dCnt": 1,
      "totalDigg7dCnt": 1,
      "totalDigg30dCnt": 1,
      "totalCommentsCnt": 1,
      "totalSharesCnt": 1,
      "totalFavoritesCnt": 1,
      "totalVideoSaleCnt": 1,
      "totalVideoSaleGmvAmt": 1,
      "region": "US"
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-video-search.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-video-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-video-search.json)
- [Response fixture](../../examples/responses/tiktok-video-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_video_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
