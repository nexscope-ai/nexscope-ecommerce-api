# Etsy Store Query API

Search Etsy stores using keyword, category, country, status, performance, and date filters.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/etsy-store-query?view=api&co-from=github-ecommerce-api)

Category: Etsy Marketplace · Data API

Returns Etsy store profiles and marketplace performance metrics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/etsy-store-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKey` | string | No | Store name, keyword, or Etsy store URL. | {} |
| `category` | string | No | Primary store category. | {} |
| `country` | string | No | Store country or region. | {} |
| `status` | integer | No | Store status: 1 active, 0 inactive. | {} |
| `isRaving` | integer | No | Raving store flag: 1 yes. | {} |
| `isStar` | integer | No | Star store flag: 1 yes. | {} |
| `beginFavorites` | integer | No | Minimum total favorites. | {} |
| `endFavorites` | integer | No | Maximum total favorites. | {} |
| `beginFavoritesWeekly` | integer | No | Minimum weekly favorites. | {} |
| `endFavoritesWeekly` | integer | No | Maximum weekly favorites. | {} |
| `beginReviews` | integer | No | Minimum total reviews. | {} |
| `endReviews` | integer | No | Maximum total reviews. | {} |
| `beginReviewsWeekly` | integer | No | Minimum weekly reviews. | {} |
| `endReviewsWeekly` | integer | No | Maximum weekly reviews. | {} |
| `beginSales` | integer | No | Minimum total sales. | {} |
| `endSales` | integer | No | Maximum total sales. | {} |
| `beginSalesWeekly` | integer | No | Minimum weekly sales. | {} |
| `endSalesWeekly` | integer | No | Maximum weekly sales. | {} |
| `beginStoreOpenedAt` | string | No | Opening date range start in YYYY-MM-DD format. | {} |
| `endStoreOpenedAt` | string | No | Opening date range end in YYYY-MM-DD format. | {} |
| `sortBy` | integer | No | Sort field: 8 total sales, 9 weekly sales, 10 reviews, 11 favorites. | {} |
| `sortDesc` | integer | No | Sort direction: 1 descending, 0 ascending. | {} |
| `page` | integer | No | Page number starting from 1. | {} |
| `pageSize` | integer | No | Items per page from 1 to 100. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/etsy-store-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh etsy-store-query request.json
# Or: node examples/javascript/run.mjs etsy-store-query request.json
# Or: python3 examples/python/run.py etsy-store-query request.json
```

### Published request example

```json
{
  "page": 1,
  "searchKey": "Lewshop1",
  "pageSize": 20
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "storeNum": 1,
  "stores": [
    {
      "storeId": "123456",
      "storeName": "Lewshop1",
      "storeUrl": "https://www.etsy.com/shop/Lewshop1",
      "country": [],
      "category": [],
      "salesTotal": 1,
      "salesWeekly": 1,
      "reviews": 1,
      "favorites": 1,
      "rating": 4.8,
      "status": 1
    }
  ],
  "columns": [],
  "costToken": 3600
}
```

## Full definitions

- [Request definition](../../schemas/etsy-store-query.request.json) — field-descriptors
- [Response definition](../../schemas/etsy-store-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/etsy-store-query.json)
- [Response fixture](../../examples/responses/etsy-store-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_etsy_store_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
