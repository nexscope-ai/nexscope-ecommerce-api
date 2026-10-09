# Nexscope TikTok Creator Search API

Nexscope TikTok Creator Search with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-creator-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Creator Search. Known row fields: account_type, author_avg_engagement_rate, bio_email, category_label, country_code, ecom_video_avg_play_count, facebook_url, follower_count, follower_count_growth_for_last_7_days, has_live_product, has_shop_product, has_video_product, id, ins_id, live_30d_gmv, live_30d_gpm, nickname, product_category_label_list, total_favorited, total_video_live_30d_gmv, unique_id, user_avatar, user_sell_product_l3_category, video_30d_gmv, video_30d_gpm, video_avg_like_count, video_avg_play_count, video_total_like_count_to_follower_count_ratio, youtube_channel_id. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-creator-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 10, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `keyword` | string | No | Creator search keyword. | {"type": "string", "description": "Creator search keyword.", "example": "beauty"} |
| `category` | string | No | Creator category. | {"description": "Creator category.", "type": "string"} |
| `hasContact` | boolean | No | Filter by availability of public contact information. | {"type": "boolean", "description": "Filter by availability of public contact information.", "example": true} |
| `sort` | string | No | Provider sort field and direction (field:asc or field:desc). | {"type": "string", "pattern": "^[A-Za-z0-9_]+:(asc\|desc)$", "default": "gmv_30d:desc", "example": "gmv_30d:desc", "description": "Provider sort field and direction (field:asc or field:desc)."} |
| `minFollowers` | number | No | Minimum follower count. | {"description": "Minimum follower count.", "type": "number"} |
| `maxFollowers` | number | No | Maximum follower count. | {"description": "Maximum follower count.", "type": "number"} |
| `minGmv30d` | number | No | Minimum 30-day GMV. | {"description": "Minimum 30-day GMV.", "type": "number"} |
| `maxGmv30d` | number | No | Maximum 30-day GMV. | {"description": "Maximum 30-day GMV.", "type": "number"} |
| `minAvgViews` | number | No | Minimum average view count. | {"description": "Minimum average view count.", "type": "number"} |
| `maxAvgViews` | number | No | Maximum average view count. | {"description": "Maximum average view count.", "type": "number"} |
| `minEngagement` | number | No | Minimum engagement rate. | {"description": "Minimum engagement rate.", "type": "number"} |
| `maxEngagement` | number | No | Maximum engagement rate. | {"description": "Maximum engagement rate.", "type": "number"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-creator-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-creator-search request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-creator-search request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-creator-search request.json
```

### Published request example

```json
{
  "country": "us",
  "keyword": "beauty",
  "pageSize": 5
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errmsg": "ok",
  "data": {
    "items": [
      {
        "account_type": null,
        "author_avg_engagement_rate": null,
        "bio_email": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-creator-search.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-creator-search.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-creator-search.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-creator-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_creator_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
