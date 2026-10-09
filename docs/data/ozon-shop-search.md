# Ozon Shop Search API

Nexscope Ozon shop product search: fetches the product list of an Ozon shop (seller) by shop ID, returning each product's 30-day sales, price, rating, weight, fulfillment method (FBO/FBS), seller type (local/cross-border), return/cancellation rate, and the shop's total 30-day sales. Use for competitor shop product analysis, shop bestseller mining, seller product structure analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-shop-search?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Nexscope Ozon shop product search: fetches the product list of an Ozon shop (seller) by shop ID, returning each product's 30-day sales, price, rating, weight, fulfillment method (FBO/FBS), seller type (local/cross-border), return/cancellation rate, and the shop's total 30-day sales. Use for competitor shop product analysis, shop bestseller mining, seller product structure analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-shop-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `id` | integer | Yes | Shop (seller) ID, i.e., the sellerId returned by other Nexscope Ozon tools; negative values are Ozon platform self-operated sellers (e.g., -2 Ozon Express, -4 Ozon Fresh), positive values are third-party sellers | {} |
| `page` | object | Yes | Pagination & sorting: {page, pageSize, orders[]} | {} |
| `page.page` | integer | No | Page number, starting from 1, default 1 | {} |
| `page.pageSize` | integer | No | Items per page, default 20, maximum 20 (exceeding returns errcode 1002) | {} |
| `page.orders` | array | No | Sort rules, elements {field, direction}; direction takes DESC (descending) / ASC (ascending). Common sort fields: sales, price, reviewRating, upTime | {} |
| `uId` | string | No | User ID (max 1000) | {} |
| `memberId` | string | No | Member ID (a unique member identifier; a user can belong to multiple teams; data is attributed to memberId, max 1000) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-shop-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-shop-search request.json
# Or: node examples/javascript/run.mjs ozon-shop-search request.json
# Or: python3 examples/python/run.py ozon-shop-search request.json
```

### Published request example

```json
{
  "page": {
    "pageSize": 10,
    "page": 1
  },
  "id": 1581151
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
  "data": [
    {
      "productId": 1,
      "sku": 1,
      "rating": 1,
      "reviewRating": 1,
      "weight": 1,
      "sales": 1,
      "monthlySalesUnits": 1,
      "upTime": 1,
      "price": 1,
      "imageUrl": "https://example.com/image.jpg",
      "fulfillment": [],
      "sellerType": 1,
      "returnCancellationRate": 1
    }
  ],
  "products": [],
  "hasNextPage": false,
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-shop-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-shop-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-shop-search.json)
- [Response fixture](../../examples/responses/ozon-shop-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_shop_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
