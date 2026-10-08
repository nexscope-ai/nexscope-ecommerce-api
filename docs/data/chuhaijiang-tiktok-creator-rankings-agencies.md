# Chuhaijiang TikTok Creator Agencies API

Chuhaijiang TikTok Creator Agencies with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-creator-rankings-agencies?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Chuhaijiang TikTok Creator Agencies. Known row fields: avg_commission_rate, follower_count, has_email_address, has_phone, has_whats_app, id, partner_icon, partner_id, partner_name, partner_top3_category, partner_top3_category_list, total_30d_video_live_gmv, total_30d_video_live_sold_count, total_related_creator_count, total_related_product_count, total_related_seller_count, video_count. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-creator-rankings-agencies/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 20, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `sort` | string | No | Provider sort field and direction (field:asc or field:desc). | {"type": "string", "pattern": "^[A-Za-z0-9_]+:(asc\|desc)$", "default": "gmv_30d:desc", "example": "gmv_30d:desc", "description": "Provider sort field and direction (field:asc or field:desc)."} |
| `category` | string | No | Agency category. | {"description": "Agency category.", "type": "string"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-creator-rankings-agencies.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-creator-rankings-agencies request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-creator-rankings-agencies request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-creator-rankings-agencies request.json
```

### Published request example

```json
{
  "country": "us",
  "pageSize": 10
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
        "avg_commission_rate": null,
        "follower_count": null,
        "has_email_address": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-creator-rankings-agencies.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-creator-rankings-agencies.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-creator-rankings-agencies.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-creator-rankings-agencies.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_creator_rankings_agencies`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
