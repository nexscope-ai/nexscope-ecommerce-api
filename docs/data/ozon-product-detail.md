# Ozon Product Detail API

Nexscope Ozon Russia SKU full detail query for one product ID per call, returning price, discount, Ozon Card price, rating, review count, stock, sales, revenue, revenue potential/lost revenue, listing date, images, and the complete product card.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-product-detail?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Nexscope Ozon Russia SKU full detail query for one product ID per call, returning price, discount, Ozon Card price, rating, review count, stock, sales, revenue, revenue potential/lost revenue, listing date, images, and the complete product card.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productIds` | array | Yes | Exactly one Ozon product ID (integer or string); multiple IDs are currently unsupported | {"maxItems": 1, "minItems": 1} |
| `startDate` | string | No | Statistics start date, format YYYY-MM-DD; latest is yesterday | {} |
| `endDate` | string | No | Statistics end date, format YYYY-MM-DD; latest is yesterday | {} |
| `includeFbs` | boolean | No | Whether to include FBS data for the requested SKU | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-product-detail request.json
# Or: node examples/javascript/run.mjs ozon-product-detail request.json
# Or: python3 examples/python/run.py ozon-product-detail request.json
```

### Published request example

```json
{
  "includeFbs": false,
  "startDate": "2025-03-01",
  "productIds": [
    1786874757
  ],
  "endDate": "2025-03-31"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 200,
  "total": 1,
  "successCount": 1,
  "failedCount": 0,
  "failures": [],
  "products": [
    {
      "productId": 1786874757,
      "sellerId": 1,
      "sellerIsBestSeller": false,
      "nicheId": 1,
      "firstDate": "2025-03-01",
      "updated": "2025-03-31 12:00:00",
      "imageUrl": "https://example.com/image.jpg",
      "imageCount": 1,
      "productImageUrls": [],
      "productPageUrl": "https://example.com/image.jpg",
      "price": 1,
      "oldPrice": 1,
      "ozonCardPrice": 1,
      "discount": 1,
      "rating": 1,
      "reviewCount": 1,
      "balance": 1,
      "salesPerDay": 1,
      "salesPerDayWithStock": 1,
      "dailySalesRevenue": 1,
      "dailySalesRevenueWithStock": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "previousSalesUnits": 1,
      "previousRevenue": 1,
      "revenuePotential": 1,
      "lostProfit": 1,
      "lostProfitPercent": 1
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-product-detail.json)
- [Response fixture](../../examples/responses/ozon-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
