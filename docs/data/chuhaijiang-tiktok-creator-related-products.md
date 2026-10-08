# Chuhaijiang TikTok Creator Related Products API

Chuhaijiang TikTok Creator Related Products with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-creator-related-products?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Chuhaijiang TikTok Creator Related Products. Known row fields: id, tiktok_creator_detail_by_live, tiktok_creator_detail_by_shop, tiktok_creator_detail_by_video, tiktok_creator_detail_live_30d_gmv, tiktok_creator_detail_live_30d_sold_count, tiktok_creator_detail_product_country_code, tiktok_creator_detail_product_id, tiktok_creator_detail_product_launch_time, tiktok_creator_detail_total_video_live_30d_gmv, tiktok_creator_detail_total_video_live_30d_sold_count, tiktok_creator_detail_user_id, tiktok_creator_detail_video_30d_gmv, tiktok_creator_detail_video_30d_sold_count, tiktok_product_detail_ceiling_price, tiktok_product_detail_commission_rate, tiktok_product_detail_floor_price, tiktok_product_detail_l1_category, tiktok_product_detail_l2_category, tiktok_product_detail_l3_category, tiktok_product_detail_product_images, tiktok_product_detail_product_name, tiktok_product_detail_product_rating, tiktok_product_detail_product_sku_props, tiktok_product_detail_product_skus, tiktok_product_detail_product_status, tiktok_product_detail_region. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-creator-related-products/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 10, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `id` | string | Yes | Creator ID, preserved as a string. | {"minLength": 1, "type": "string", "example": "7302162228386776110", "description": "Creator ID, preserved as a string."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-creator-related-products.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-creator-related-products request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-creator-related-products request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-creator-related-products request.json
```

### Published request example

```json
{
  "country": "us",
  "id": "7302162228386776110",
  "page": 1,
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
        "id": null,
        "tiktok_creator_detail_by_live": null,
        "tiktok_creator_detail_by_shop": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-creator-related-products.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-creator-related-products.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-creator-related-products.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-creator-related-products.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_creator_related_products`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
