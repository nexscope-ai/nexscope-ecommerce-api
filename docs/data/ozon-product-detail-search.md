# Ozon Product Detail Search API

Nexscope Ozon product detail query: fetches the complete detail of a single Ozon product by SKU, returning title, price (RUB), rating, review count, QA count, total and daily average sales within the stats window, revenue, stock, category ranking, daily sales trend, brand, seller, fulfillment method (FBO/FBS/OZON), weight, and listing time/days/months. Use for single product deep analysis, competitor product teardown, Ozon product selection assessment, listing diagnosis, sales trend and category ranking tracking.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-product-detail-search?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Nexscope Ozon product detail query: fetches the complete detail of a single Ozon product by SKU, returning title, price (RUB), rating, review count, QA count, total and daily average sales within the stats window, revenue, stock, category ranking, daily sales trend, brand, seller, fulfillment method (FBO/FBS/OZON), weight, and listing time/days/months. Use for single product deep analysis, competitor product teardown, Ozon product selection assessment, listing diagnosis, sales trend and category ranking tracking.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-detail-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `sku` | string | Yes | Product SKU (Ozon SKU, e.g., 175924376). This is the sku returned by other Nexscope Ozon tools | {} |
| `dateRange` | string | No | Sales/metrics statistics window, default past_30_days. Options: past_7_days / past_30_days / past_60_days / past_90_days / past_180_days / past_365_days | {} |
| `uId` | string | No | User ID (max 1000) | {} |
| `memberId` | string | No | Member ID (a unique member identifier; a user can belong to multiple teams; data is attributed to memberId, max 1000) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-product-detail-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-product-detail-search request.json
# Or: node examples/javascript/run.mjs ozon-product-detail-search request.json
# Or: python3 examples/python/run.py ozon-product-detail-search request.json
```

### Published request example

```json
{
  "sku": "1664362124",
  "dateRange": "past_30_days"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "total": 1,
  "totalSales": 1,
  "dailySales": 1,
  "totalRevenue": 1,
  "stock": 1,
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "salesTrendVOList": [],
  "categoryRanks": [],
  "products": [
    {
      "sku": 1,
      "productId": 1,
      "price": 1,
      "reviewRating": 1,
      "rating": 1,
      "reviewCount": 1,
      "questionsAndAnswers": 1,
      "brandId": 1,
      "brandUrl": "https://example.com/image.jpg",
      "sellerId": 1,
      "fulfillment": [],
      "upTime": 1,
      "upDays": 1,
      "upMonths": 1,
      "imageUrl": "https://example.com/image.jpg",
      "imageUrls": [],
      "productUrl": "https://example.com/image.jpg",
      "productPageUrl": "https://example.com/image.jpg",
      "categoryInfo": {},
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "weight": 1,
      "grossMargin": 1
    }
  ],
  "data": [],
  "columns": [
    {
      "category": {},
      "fullCategoryId": [],
      "level": 1,
      "id": "example-id",
      "pid": "example-id",
      "crossBorderSellable": false,
      "disabled": false
    }
  ],
  "costTime": 1,
  "costToken": 1,
  "salestrendvolist": [
    {
      "date": "2026-01-01",
      "sales": 1,
      "revenue": 1,
      "price": 1,
      "stock": 1,
      "reviewCount": 1,
      "reviewRating": 1
    }
  ],
  "categoryranks": [
    {
      "date": "2026-01-01",
      "rank": 1,
      "count": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/ozon-product-detail-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-product-detail-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-product-detail-search.json)
- [Response fixture](../../examples/responses/ozon-product-detail-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_product_detail_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
