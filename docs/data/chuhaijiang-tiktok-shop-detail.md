# Chuhaijiang TikTok Shop Detail API

Chuhaijiang TikTok Shop Detail with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-shop-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Chuhaijiang TikTok Shop Detail. Known row fields: id, seller_id, shop_name, region, shop_rating, shop_total_gmv. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-shop-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `id` | string | Yes | Shop ID, preserved as a string. | {"minLength": 1, "type": "string", "example": "7495205878591949358", "description": "Shop ID, preserved as a string."} |
| `include` | string | No | Comma-separated optional detail sections: core, channel. | {"pattern": "^(core\|channel)(,(core\|channel))*$", "type": "string", "example": "core,channel", "description": "Comma-separated optional detail sections: core, channel."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-shop-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-shop-detail request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-shop-detail request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-shop-detail request.json
```

### Published request example

```json
{
  "country": "us",
  "id": "7495205878591949358",
  "include": "core,channel"
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
        "seller_id": null,
        "shop_name": null
      }
    ],
    "channel": {
      "items": [
        {
          "id": null,
          "channel_seller_id": null,
          "channel_seller_sold_count_for_last_30_days": null
        }
      ]
    },
    "core": {
      "items": [
        {
          "id": null,
          "core_seller_id": null,
          "core_region": null
        }
      ]
    }
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-shop-detail.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-shop-detail.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-shop-detail.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-shop-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_shop_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
