# Ozon Brand Products API

MPSTATS Ozon Russia brand drill-down product list. Returns all products under an Ozon brand display name (Russian/Latin) with complete metrics: sales, revenue, price, rating, stock, turnover, lost revenue, supporting multi-dimensional numeric filters, sorting, and currency conversion. Use for brand benchmarking, competitor analysis, brand product structure research, SKU-level bestseller analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-brand-products?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

MPSTATS Ozon Russia brand drill-down product list. Returns all products under an Ozon brand display name (Russian/Latin) with complete metrics: sales, revenue, price, rating, stock, turnover, lost revenue, supporting multi-dimensional numeric filters, sorting, and currency conversion. Use for brand benchmarking, competitor analysis, brand product structure research, SKU-level bestseller analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-brand-products/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `brandName` | string | Yes | Ozon brand display name (Russian or Latin) | {} |
| `startDate` | string | No | Statistics start date, YYYY-MM-DD; latest is yesterday | {} |
| `endDate` | string | No | Statistics end date, YYYY-MM-DD; latest is yesterday | {} |
| `page` | integer | No | Page number, starting from 1 | {} |
| `pageSize` | integer | No | Rows per page, 1-100, default 100 | {} |
| `sortField` | string | No | Sort column name (snake_case), e.g., sales, revenue, final_price, balance, rating | {} |
| `sortDirection` | string | No | asc ascending / desc descending | {} |
| `currency` | string | No | Currency code for result amounts, default RUB, e.g., USD / EUR / CNY | {} |
| `currencyRate` | integer | No | Custom exchange rate (for non-default currency) | {} |
| `includeFbs` | boolean | No | Whether to include FBS data | {} |
| `filters` | array | No | List of numeric filter conditions, each {field, op, value, value2?}, multiple conditions AND | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-brand-products.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-brand-products request.json
# Or: node examples/javascript/run.mjs ozon-brand-products request.json
# Or: python3 examples/python/run.py ozon-brand-products request.json
```

### Published request example

```json
{
  "startDate": "2026-01-01",
  "includeFbs": false,
  "pageSize": 10,
  "endDate": "2026-01-31",
  "page": 1,
  "brandName": "COMMO",
  "currencyRate": 1
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
      "productId": 1,
      "brandId": 1,
      "sellerId": 1,
      "nicheId": 1,
      "firstDate": "2026-01-01",
      "imageUrl": "https://example.com/image.jpg",
      "productPageUrl": "https://example.com/image.jpg",
      "price": 1,
      "oldPrice": 1,
      "ozonCardPrice": 1,
      "minPrice/maxPrice/averagePrice": 1,
      "rating": 1,
      "reviewCount": 1,
      "balance": 1,
      "balanceFbs": 1,
      "frozenStocks": 1,
      "warehousesCount": 1,
      "isFbs": false,
      "salesPerDay": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "lostProfit": 1,
      "daysInSite": 1,
      "daysInStock": 1,
      "turnoverDays": 1,
      "position": 1,
      "categoryPosition": 1,
      "revenueSharePercent": 1
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-brand-products.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-brand-products.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-brand-products.json)
- [Response fixture](../../examples/responses/ozon-brand-products.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_brand_products`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
