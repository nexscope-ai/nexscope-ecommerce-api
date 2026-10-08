# Chuhaijiang TikTok Creator Detail API

Chuhaijiang TikTok Creator Detail with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-creator-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Chuhaijiang TikTok Creator Detail. Known row fields: id, nickname, unique_id, user_avatar, category_label. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-creator-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `id` | string | Yes | Creator ID, preserved as a string. | {"minLength": 1, "type": "string", "example": "7302162228386776110", "description": "Creator ID, preserved as a string."} |
| `include` | string | No | Comma-separated optional detail sections: core, channel, portrait. | {"pattern": "^(core\|channel\|portrait)(,(core\|channel\|portrait))*$", "type": "string", "example": "core,channel,portrait", "description": "Comma-separated optional detail sections: core, channel, portrait."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-creator-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-creator-detail request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-creator-detail request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-creator-detail request.json
```

### Published request example

```json
{
  "country": "us",
  "id": "7302162228386776110",
  "include": "core,channel,portrait"
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
        "id": null,
        "nickname": null,
        "unique_id": null
      }
    ],
    "core": {
      "items": [
        {
          "core_author_avg_engagement_rate": null,
          "core_follower_count": null,
          "core_product_count": null
        }
      ]
    },
    "channel": {
      "items": [
        {
          "channel_country_code": null,
          "channel_ec_video_30d_avg_engagement_rate": null,
          "channel_ec_video_30d_avg_play_count": null
        }
      ]
    },
    "portrait": {
      "items": [
        {
          "id": null,
          "portrait_age_distribution": null,
          "portrait_follower_count": null
        }
      ]
    }
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-creator-detail.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-creator-detail.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-creator-detail.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-creator-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_creator_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
