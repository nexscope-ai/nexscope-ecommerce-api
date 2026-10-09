# Ozon Product Trend API

Nexscope Ozon Russia single SKU daily time-series performance. Returns daily sales units, price, stock, rating, and optionally search position/visibility data for one Ozon product by date granularity. Use for validating growth trends, seasonality, and anomaly detection.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-product-trend?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

Nexscope Ozon Russia single SKU daily time-series performance. Returns daily sales units, price, stock, rating, and optionally search position/visibility data for one Ozon product by date granularity. Use for validating growth trends, seasonality, and anomaly detection.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-trend/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productId` | integer | Yes | Ozon product SKU | {} |
| `startDate` | string | No | Statistics start date, YYYY-MM-DD; data delayed by T-1, latest is yesterday | {} |
| `endDate` | string | No | Statistics end date, YYYY-MM-DD; data delayed by T-1, latest is yesterday | {} |
| `includeFbs` | boolean | No | Whether to include FBS data | {} |
| `includeSearchStats` | boolean | No | Whether to include search position / visibility; not supported for some niches | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-product-trend.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-product-trend request.json
# Or: node examples/javascript/run.mjs ozon-product-trend request.json
# Or: python3 examples/python/run.py ozon-product-trend request.json
```

### Published request example

```json
{
  "includeSearchStats": false,
  "endDate": "2026-01-31",
  "productId": 1664362124,
  "startDate": "2026-01-01",
  "includeFbs": false
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
      "date": "2026-01-01",
      "hasData": false,
      "price": 1,
      "oldPrice": 1,
      "ozonCardPrice": 1,
      "discount": 1,
      "sales": 1,
      "balance": 1,
      "rating": 1,
      "comments": 1,
      "isBestseller": false,
      "isNew": false
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-product-trend.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-product-trend.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-product-trend.json)
- [Response fixture](../../examples/responses/ozon-product-trend.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_product_trend`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
