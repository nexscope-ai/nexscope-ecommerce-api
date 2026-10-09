# Nexscope TikTok Product Search API

Nexscope TikTok Product Search with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-product-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Product Search. Known row fields: id, product_name, product_images, floor_price, ceiling_price, product_rating, product_sold_count, product_gmv, seller_id, shop_name. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 10, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `keyword` | string | No | Product search keyword. | {"type": "string", "description": "Product search keyword.", "example": "beauty"} |
| `category` | string | No | Product category ID. | {"description": "Product category ID.", "type": "string"} |
| `sellerType` | string | No | Seller type: 1 overseas non-brand, 2 local, 3 brand, 4 non-brand. | {"enum": ["1", "2", "3", "4"], "type": "string", "example": "2", "description": "Seller type: 1 overseas non-brand, 2 local, 3 brand, 4 non-brand."} |
| `freeShipping` | boolean | No | Filter by free shipping availability. | {"type": "boolean", "description": "Filter by free shipping availability.", "example": true} |
| `sort` | string | No | Provider sort field and direction (field:asc or field:desc). | {"type": "string", "pattern": "^(daily_sold\|gmv_30d\|gmv_7d\|price\|rating\|sold_30d\|sold_7d):(asc\|desc)$", "default": "gmv_7d:desc", "example": "gmv_7d:desc", "description": "Provider sort field and direction (field:asc or field:desc)."} |
| `minPrice` | number | No | Minimum price in USD. | {"description": "Minimum price in USD.", "type": "number"} |
| `maxPrice` | number | No | Maximum price in USD. | {"description": "Maximum price in USD.", "type": "number"} |
| `minRating` | number | No | Minimum product rating. | {"maximum": 5, "type": "number", "description": "Minimum product rating.", "minimum": 0} |
| `maxRating` | number | No | Maximum product rating. | {"maximum": 5, "type": "number", "description": "Maximum product rating.", "minimum": 0} |
| `minSold7d` | number | No | Minimum 7-day sales. | {"description": "Minimum 7-day sales.", "type": "number"} |
| `maxSold7d` | number | No | Maximum 7-day sales. | {"description": "Maximum 7-day sales.", "type": "number"} |
| `minSold30d` | number | No | Minimum 30-day sales. | {"description": "Minimum 30-day sales.", "type": "number"} |
| `maxSold30d` | number | No | Maximum 30-day sales. | {"description": "Maximum 30-day sales.", "type": "number"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-product-search request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-product-search request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-product-search request.json
```

### Published request example

```json
{
  "country": "us",
  "keyword": "beauty",
  "minRating": 4,
  "freeShipping": true,
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
        "product_name": null,
        "product_images": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-product-search.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-product-search.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-product-search.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
