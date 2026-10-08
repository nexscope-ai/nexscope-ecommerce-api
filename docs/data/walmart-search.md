# Walmart Search API

Search and browse Walmart product listings by keyword, category, price range, and other conditions.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/walmart-search?view=api&co-from=github-ecommerce-api)

Category: Walmart Marketplace Intelligence · Data API

Search and browse Walmart product listings by keyword, category, price range, and other conditions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/walmart-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Search keyword, max length 1024 characters. *At least one of keyword and categoryId must be provided | {} |
| `categoryId` | string | No | Category ID. *At least one of keyword and categoryId must be provided. 0 means all departments. For example: 976759_976787 means "Cookies" | {} |
| `sort` | string | No | Sort method. Options: price_low (price low to high), price_high (price high to low), best_seller (best seller), best_match (best match) | {} |
| `page` | integer | No | Page number for pagination, default 1, max 100 | {} |
| `minPrice` | number | No | Minimum price | {} |
| `maxPrice` | number | No | Maximum price | {} |
| `spelling` | boolean | No | Enable spelling correction, default true. true includes spelling correction, false excludes it | {} |
| `softSort` | boolean | No | Sort by relevance, default true. Set to false to disable relevance sorting | {} |
| `storeId` | string | No | Store ID, used to filter products by a specific store | {} |
| `device` | string | No | Device type, default desktop. Options: desktop, tablet, mobile | {} |
| `facet` | string | No | Filter conditions, format as key:value pairs separated by \ | {} |
| `nextDayEnabled` | boolean | No | Only show NextDay delivery results, default false. true to enable, false to disable | {} |
| `jsonRestrictor` | string | No | JSON field restrictor | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/walmart-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh walmart-search request.json
# Or: node examples/javascript/run.mjs walmart-search request.json
# Or: python3 examples/python/run.py walmart-search request.json
```

### Published request example

```json
{
  "page": 1,
  "spelling": true,
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "products": [
    {
      "productId": "example-id",
      "usItemId": "example-id",
      "price": 1,
      "wasPrice": 1,
      "minPrice": 1,
      "rating": 1,
      "reviews": 1,
      "sellerId": "example-id",
      "imageUrl": "https://example.com/image.jpg",
      "productPageUrl": "https://example.com/image.jpg",
      "sponsored": false,
      "outOfStock": false,
      "freeShipping": false,
      "twoDayShipping": false,
      "freeShippingWithWalmartPlus": false,
      "shippingPrice": 1,
      "multipleOptionsAvailable": false,
      "variantSwatches": []
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/walmart-search.request.json) — field-descriptors
- [Response definition](../../schemas/walmart-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/walmart-search.json)
- [Response fixture](../../examples/responses/walmart-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_walmart_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
