# Nexscope TikTok Creator Growth API

Nexscope TikTok Creator Growth with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-creator-rankings-growth?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Creator Growth. Known row fields: bio_email, category_label, channel_id, creator_oecuid, follower_count, handle, id, interval_new_follower, nickname, tioktok_creator_growth_interval_new_follower_ratio, uid, unique_id, user_avatar, user_sell_product_l1_category, video_count. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-creator-rankings-growth/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 20, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `date` | string | Yes | Ranking date in YYYYMMDD format. | {"pattern": "^[0-9]{8}$", "type": "string", "example": "20260824", "description": "Ranking date in YYYYMMDD format."} |
| `granularity` | string | Yes | Ranking period. | {"enum": ["daily", "weekly", "monthly", "0", "1", "2"], "type": "string", "example": "daily", "description": "Ranking period."} |
| `sort` | string | No | Provider sort field and direction (field:asc or field:desc). | {"type": "string", "pattern": "^[A-Za-z0-9_]+:(asc\|desc)$", "default": "new_follower_count:desc", "example": "new_follower_count:desc", "description": "Provider sort field and direction (field:asc or field:desc)."} |
| `creatorCategory` | string | No | Creator category. | {"description": "Creator category.", "type": "string"} |
| `productCategory` | string | No | Product category. | {"description": "Product category.", "type": "string"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-creator-rankings-growth.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-creator-rankings-growth request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-creator-rankings-growth request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-creator-rankings-growth request.json
```

### Published request example

```json
{
  "country": "us",
  "pageSize": 10,
  "date": "20260828",
  "granularity": "daily"
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
        "bio_email": null,
        "category_label": null,
        "channel_id": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-creator-rankings-growth.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-creator-rankings-growth.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-creator-rankings-growth.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-creator-rankings-growth.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_creator_rankings_growth`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
