# Etsy Product Query API

Query Etsy products with multi-dimensional filters (keyword/URL, price, sales, favorites, reviews, listing date, category, handmade/vintage types, Pick/Bestseller/Raving tags).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/etsy-product-query?view=api&co-from=github-ecommerce-api)

Category: Etsy Marketplace · Data API

Query Etsy products with multi-dimensional filters (keyword/URL, price, sales, favorites, reviews, listing date, category, handmade/vintage types, Pick/Bestseller/Raving tags).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/etsy-product-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `beginFavorites` | integer | No | Favorite count (start), combined with end value to form the upstream favorites range | {} |
| `beginFavoritesWeekly` | integer | No | Weekly new favorites (start), combined with end value to form the upstream favorites_weekly range | {} |
| `beginPrice` | number | No | Price (start), combined with end price to form the upstream price range (e.g., 20~100). When only one side is provided, the upstream returns start~ or ~end | {} |
| `beginReviews` | integer | No | Review count (start), combined with end value to form the upstream reviews range | {} |
| `beginReviewsWeekly` | integer | No | Weekly new reviews (start), combined with end value to form the upstream reviews_weekly range | {} |
| `beginSales` | integer | No | Total sales (start), combined with end value to form the upstream sales range | {} |
| `beginSalesWeekly` | integer | No | Weekly sales (start), combined with end value to form the upstream sales_weekly range (e.g., 1~100) | {} |
| `category` | string | No | Product category ID (single category), see the Category Query API | {} |
| `country` | string | No | Shipping country | {} |
| `currencyCode` | string | No | Currency code | {} |
| `endFavorites` | integer | No | Favorite count (end) | {} |
| `endFavoritesWeekly` | integer | No | Weekly new favorites (end) | {} |
| `endPrice` | number | No | Price (end), combined with start price to form the upstream price range | {} |
| `endReviews` | integer | No | Review count (end) | {} |
| `endReviewsWeekly` | integer | No | Weekly new reviews (end) | {} |
| `endSales` | integer | No | Total sales (end) | {} |
| `endSalesWeekly` | integer | No | Weekly sales (end) | {} |
| `isBestsell` | integer | No | Whether the product is a bestseller | {} |
| `isPick` | integer | No | Whether the product is a Pick item | {} |
| `isRaving` | integer | No | Whether the product is a Raving item | {} |
| `listedTime` | string | No | Listing time no earlier than this date (YYYY-MM-DD) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Items per page, max 100, recommended not to exceed 50 | {} |
| `productType` | string | No | Product type, comma-separated for multiple: 1=Handmade 2=Vintage 3=Digital 4=Custom 9=Other | {} |
| `searchKey` | string | No | Search keyword or Etsy product URL | {} |
| `sortBy` | integer | No | Sort field (corresponds to upstream sort_by, values 1~6) | {} |
| `sortDesc` | integer | No | Sort direction (corresponds to upstream desc). Schema example: descending 1, ascending 2 (encoding differs from store query's sortDesc) | {} |
| `status` | integer | No | Product status (example: 1=active, 0=inactive) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/etsy-product-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh etsy-product-query request.json
# Or: node examples/javascript/run.mjs etsy-product-query request.json
# Or: python3 examples/python/run.py etsy-product-query request.json
```

### Published request example

```json
{
  "page": 1,
  "searchKey": "phone case",
  "pageSize": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "columns": [],
  "costToken": 1,
  "productNum": 1,
  "products": [
    {
      "favorites": 1,
      "favoritesWeekly": 1,
      "imageUrl": "https://example.com/image.jpg",
      "isBestsell": 1,
      "isPick": 1,
      "isRaving": 1,
      "price": 1,
      "productUrl": "https://example.com/image.jpg",
      "reviews": 1,
      "reviewsWeekly": 1,
      "salesTotal": 1,
      "salesWeekly": 1,
      "status": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/etsy-product-query.request.json) — field-descriptors
- [Response definition](../../schemas/etsy-product-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/etsy-product-query.json)
- [Response fixture](../../examples/responses/etsy-product-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_etsy_product_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
