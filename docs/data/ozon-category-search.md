# Ozon Category Search API

Seerfar Ozon category product search: fetches the product list for a given Ozon category ID, returning category-level aggregates (total sales, total revenue, average price, average rating, seasonality) and per-product sales, price, rating, review count, brand, seller, and fulfillment method. Use for category selection analysis, category bestseller mining, category capacity and price band analysis, seasonality assessment.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-category-search?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Seerfar Ozon category product search: fetches the product list for a given Ozon category ID, returning category-level aggregates (total sales, total revenue, average price, average rating, seasonality) and per-product sales, price, rating, review count, brand, seller, and fulfillment method. Use for category selection analysis, category bestseller mining, category capacity and price band analysis, seasonality assessment.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-category-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `categoryId` | string | Yes | Ozon category ID, obtained from Ozon category documentation or other Seerfar Ozon tools. Format like 15621032_15621049_115951147 (multi-level categories joined by _) | {} |
| `page` | object | Yes | Pagination & sorting: {page, pageSize, orders[]} | {} |
| `page.page` | integer | No | Page number, starting from 1, default 1 | {} |
| `page.pageSize` | integer | No | Items per page, default 20, maximum 20 (exceeding returns errcode 1002) | {} |
| `page.orders` | array | No | Sort rules, elements {field, direction} (both required); direction takes DESC (descending) / ASC (ascending). Common sort fields: sales, price, revenue, reviewRating | {} |
| `date` | string | No | Query historical month, format yyyy-MM (e.g., 2026-02); defaults to last 30 days if omitted | {} |
| `fulfillment` | string | No | Fulfillment method filter, fixed options: FBO, FBS, RFBS, FBP, OZON; queries all if omitted. Note: single string, not an array | {} |
| `uId` | string | No | User ID (max 1000) | {} |
| `memberId` | string | No | Member ID (a unique member identifier; a user can belong to multiple teams; data is attributed to memberId, max 1000) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-category-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-category-search request.json
# Or: node examples/javascript/run.mjs ozon-category-search request.json
# Or: python3 examples/python/run.py ozon-category-search request.json
```

### Published request example

```json
{
  "page": {
    "pageSize": 10,
    "page": 1
  },
  "date": "2026-01",
  "categoryId": "15621042_17028650_97011"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "id": "example-id",
  "total": 1,
  "totalSales": 1,
  "totalRevenue": 1,
  "avgPrice": 1,
  "rating": 1,
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "sellerType": {},
  "categoryInfo": {},
  "data": [
    {
      "sku": 1,
      "productId": 1,
      "price": 1,
      "sales": 1,
      "monthlySalesUnits": 1,
      "revenue": 1,
      "monthlySalesRevenue": 1,
      "reviewRating": 1,
      "rating": 1,
      "reviewCount": 1,
      "fulfillment": [],
      "imageUrl": "https://example.com/image.jpg",
      "productUrl": "https://example.com/image.jpg",
      "productPageUrl": "https://example.com/image.jpg",
      "categoryInfo": {}
    }
  ],
  "products": [
    {
      "fullCategoryId": [],
      "category": {}
    }
  ],
  "hasNextPage": false,
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-category-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-category-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-category-search.json)
- [Response fixture](../../examples/responses/ozon-category-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_category_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
