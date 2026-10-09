# Nexscope TikTok Shop Search API

Nexscope TikTok Shop Search with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-shop-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Shop Search. Known row fields: id, shop_name, region, shop_rating, shop_product_count, shop_total_sold_count, shop_total_gmv, shop_sold_count_for_last_7_days, shop_gmv_for_last_7_days. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-shop-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 10, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `keyword` | string | No | Shop search keyword. | {"type": "string", "description": "Shop search keyword.", "example": "beauty"} |
| `category` | string | No | Product category ID. | {"description": "Product category ID.", "type": "string"} |
| `sellerType` | string | No | Provider-supported seller type. | {"description": "Provider-supported seller type.", "type": "string"} |
| `sort` | string | No | Provider sort field and direction (field:asc or field:desc). | {"type": "string", "pattern": "^[A-Za-z0-9_]+:(asc\|desc)$", "default": "gmv_7d:desc", "example": "gmv_7d:desc", "description": "Provider sort field and direction (field:asc or field:desc)."} |
| `minRating` | number | No | Minimum shop rating. | {"description": "Minimum shop rating.", "type": "number"} |
| `maxRating` | number | No | Maximum shop rating. | {"description": "Maximum shop rating.", "type": "number"} |
| `minSold7d` | number | No | Minimum 7-day sales. | {"description": "Minimum 7-day sales.", "type": "number"} |
| `maxSold7d` | number | No | Maximum 7-day sales. | {"description": "Maximum 7-day sales.", "type": "number"} |
| `minGmv7d` | number | No | Minimum 7-day GMV. | {"description": "Minimum 7-day GMV.", "type": "number"} |
| `maxGmv7d` | number | No | Maximum 7-day GMV. | {"description": "Maximum 7-day GMV.", "type": "number"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-shop-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-shop-search request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-shop-search request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-shop-search request.json
```

### Published request example

```json
{
  "country": "us",
  "keyword": "beauty",
  "minRating": 4,
  "pageSize": 3
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
        "shop_name": null,
        "region": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-shop-search.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-shop-search.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-shop-search.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-shop-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_shop_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
