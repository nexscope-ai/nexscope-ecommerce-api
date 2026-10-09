# Ozon Product Report Search API

Nexscope Ozon product report search: filters Ozon products by multi-dimensional metrics including sales, revenue, sales/revenue growth rate, cart conversion rate, order conversion rate, price, rating, review count, QA count, variant count, page views, gross margin, return/cancellation rate, ad spend share, weight/volume, listing time, brand, seller, fulfillment method, and labels. Returns each product's SKU, title, price (RUB), sales, revenue, lost revenue, conversion rate, rating, reviews, brand, seller, fulfillment method, listing days/months, and complete product report fields. Use for Ozon product selection, competitor product analysis, best-seller mining, price/conversion band filtering.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-product-report-search?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Nexscope Ozon product report search: filters Ozon products by multi-dimensional metrics including sales, revenue, sales/revenue growth rate, cart conversion rate, order conversion rate, price, rating, review count, QA count, variant count, page views, gross margin, return/cancellation rate, ad spend share, weight/volume, listing time, brand, seller, fulfillment method, and labels. Returns each product's SKU, title, price (RUB), sales, revenue, lost revenue, conversion rate, rating, reviews, brand, seller, fulfillment method, listing days/months, and complete product report fields. Use for Ozon product selection, competitor product analysis, best-seller mining, price/conversion band filtering.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-report-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `page` | object | Yes | Pagination & sorting: {page, pageSize, orders[]} | {} |
| `page.page` | integer | No | Page number, starting from 1, default 1 | {} |
| `page.pageSize` | integer | No | Items per page, default 20 | {} |
| `page.orders` | array | No | Sort rules, elements {field, direction}; direction takes DESC (descending) / ASC (ascending). field is a metric field in the response (e.g., sales, revenue, price, reviewRating, reviewCount, salesRate) | {} |
| `skus` | array | No | SKU array (max 10), for precise lookup of specified products | {} |
| `keywords` | array | No | Keyword array, filters by product title | {} |
| `categoryIds` | array | No | Category ID array (Nexscope category IDs, not category names) | {} |
| `sellerName` | array | No | Seller name array | {} |
| `brand` | object | No | Brand filter: {brandName: array<string>, type: integer}; type takes 0 include brand, 1 exclude brand, 2 unbranded | {} |
| `fulfillment` | array | No | Fulfillment method array, fixed options: OZON, FBO, FBS, RFBS, FBP | {} |
| `labels` | array | No | Label array, fixed options: 0 new product, 1 genuine product, 2 best seller | {} |
| `creationDate` | integer | No | Listing time filter (months), fixed options: 1 last 30 days, 3 last 90 days, 6 last 180 days, 12 last year, 24 last two years; no filtering if omitted | {} |
| `variationsMerge` | integer | No | Whether to merge variants: 0 do not merge, 1 merge | {} |
| `searchDate` | string | No | Query date yyyy-MM-dd (e.g., 2026-04-01); defaults to last 30 days if omitted; passing 2026-04-01 queries March 2026 data | {} |
| `tag` | string | No | Tag word | {} |
| `uId` | string | No | User ID | {} |
| `memberId` | string | No | Member ID (a unique member identifier; data is attributed to memberId) | {} |
| `monthlySales` | object | No | Monthly sales range: {min, max}; either bound may be omitted | {} |
| `monthlySalesRate` | object | No | Sales growth-rate range: {min, max}; either bound may be omitted | {} |
| `monthlyRevenue` | object | No | Monthly revenue range in RUB: {min, max}; either bound may be omitted | {} |
| `price` | object | No | Price range in RUB: {min, max}; either bound may be omitted | {} |
| `convToCartPdp` | object | No | Cart conversion-rate range: {min, max}; either bound may be omitted | {} |
| `reviewRating` | object | No | Rating range from 0 to 5: {min, max}; either bound may be omitted | {} |
| `reviewCount` | object | No | Review-count range: {min, max}; either bound may be omitted | {} |
| `questionsAndAnswers` | object | No | Question-and-answer count range: {min, max}; either bound may be omitted | {} |
| `variants` | object | No | Variant-count range: {min, max}; either bound may be omitted | {} |
| `drr` | object | No | Advertising cost-share range: {min, max}; either bound may be omitted | {} |
| `grossMargin` | object | No | Gross-margin range: {min, max}; either bound may be omitted | {} |
| `returnCancellationRate` | object | No | Return and cancellation-rate range: {min, max}; either bound may be omitted | {} |
| `weight` | object | No | Weight range in grams: {min, max}; either bound may be omitted | {} |
| `volume` | object | No | Volume range in liters: {min, max}; either bound may be omitted | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-product-report-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-product-report-search request.json
# Or: node examples/javascript/run.mjs ozon-product-report-search request.json
# Or: python3 examples/python/run.py ozon-product-report-search request.json
```

### Published request example

```json
{
  "skus": [
    "1664362124"
  ],
  "page": {
    "pageSize": 10,
    "page": 1
  }
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "total": 1,
  "data": [
    {
      "sku": 1,
      "productId": 1,
      "imageUrl": "https://example.com/image.jpg",
      "productUrl": "https://example.com/image.jpg",
      "productPageUrl": "https://example.com/image.jpg",
      "sales": 1,
      "monthlySalesUnits": 1,
      "revenue": 1,
      "monthlySalesRevenue": 1,
      "missedRevenue": 1,
      "price": 1,
      "convToCartPdp": 1,
      "orderConversionRate": 1,
      "salesRate": 1,
      "revenueRate": 1,
      "drr": 1,
      "grossMargin": 1,
      "returnCancellationRate": 1,
      "views": 1,
      "reviewRating": 1,
      "rating": 1,
      "reviewCount": 1,
      "questionsAndAnswers": 1,
      "variants": 1,
      "fulfillment": [],
      "weight": 1,
      "volume": 1,
      "upTime": 1,
      "upDays": 1,
      "upMonths": 1,
      "brandId": 1,
      "brandUrl": "https://example.com/image.jpg",
      "sellerId": 1,
      "categoryInfo": {}
    }
  ],
  "products": [],
  "columns": [
    {
      "fullCategoryId": [],
      "category": {}
    }
  ],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-product-report-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-product-report-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-product-report-search.json)
- [Response fixture](../../examples/responses/ozon-product-report-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_product_report_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
