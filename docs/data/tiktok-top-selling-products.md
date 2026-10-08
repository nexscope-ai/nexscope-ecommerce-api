# TikTok Top Selling Products API

Query TikTok global e-commerce market top-selling product rankings via FastMoss data, supporting daily/weekly/monthly dimensions and category-level analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-top-selling-products?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Query TikTok global e-commerce market top-selling product rankings via FastMoss data, supporting daily/weekly/monthly dimensions and category-level analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-top-selling-products/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | Yes | Market region code. Options: US (United States), GB (United Kingdom), MX (Mexico), ES (Spain), ID (Indonesia), VN (Vietnam), MY (Malaysia), TH (Thailand), PH (Philippines) | {} |
| `dateInfo` | object | Yes | Date specification object, containing type and value fields | {} |
| `dateInfo.type` | string | Yes | Time granularity: day, week, month | {} |
| `dateInfo.value` | string | Yes | Date value: day format YYYY-MM-DD, week format YYYY-weekNumber (e.g., 2025-18), month format YYYY-MM | {} |
| `category` | string | No | Product category name (English), matched to TikTok category ID. Non-English input must be translated to English first | {} |
| `orderby` | object | No | Sort rule object, containing field and order fields | {} |
| `orderby.field` | string | No | Sort field: units_sold (sales), gmv (GMV), total_units_sold (total sales), total_gmv (total GMV), growth_rate (growth rate) | {} |
| `orderby.order` | string | No | Sort direction: desc (descending), asc (ascending), default desc | {} |
| `page` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Items per page, max 10, default 10 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-top-selling-products.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-top-selling-products request.json
# Or: node examples/javascript/run.mjs tiktok-top-selling-products request.json
# Or: python3 examples/python/run.py tiktok-top-selling-products request.json
```

### Published request example

```json
{
  "page": 1,
  "dateInfo": {
    "value": "2026-08-01",
    "type": "day"
  },
  "orderby": {
    "field": "units_sold",
    "order": "desc"
  },
  "pageSize": 10,
  "region": "US"
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
      "region": "US",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "totalSaleCnt": 1,
      "totalSale1dCnt": 1,
      "totalSale7dCnt": 1,
      "totalSale30dCnt": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv1dAmt": 1,
      "totalSaleGmv7dAmt": 1,
      "totalSaleGmv30dAmt": 1,
      "growthRate": 1,
      "shopTotalUnitsSold": 1,
      "shopSellerId": "example-id",
      "productCommissionRate": 1,
      "imageUrl": "https://example.com/image.jpg"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-top-selling-products.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-top-selling-products.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-top-selling-products.json)
- [Response fixture](../../examples/responses/tiktok-top-selling-products.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_top_selling_products`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
