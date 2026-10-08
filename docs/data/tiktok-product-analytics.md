# TikTok Product Analytics API

Query TikTok e-commerce product leaderboards via Kalodata and query detailed data for specific products. Supports viewing high-ranking/hot-selling products by region, currency, language, and date range, and using productId to retrieve price range, sales, revenue, commission rate, listing/delisting time, and owning shop.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-product-analytics?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Query TikTok e-commerce product leaderboards via Kalodata and query detailed data for specific products. Supports viewing high-ranking/hot-selling products by region, currency, language, and date range, and using productId to retrieve price range, sales, revenue, commission rate, listing/delisting time, and owning shop.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-product-analytics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | No | TikTok Shop market region code, e.g., US. If not specified, defaults to the server default (usually US) | {} |
| `dateRange` | string | No | Relative date range, e.g., last7Day, last30Day | {} |
| `currency` | string | No | Currency code, e.g., USD | {} |
| `language` | string | No | Return language, e.g., zh-CN, en-US | {} |
| `sortField` | object | No | Sort specification object; omitted to use default ranking | {} |
| `pageNumber` | integer | No | Page number, range 1-5 | {} |
| `pageSize` | integer | No | Items per page, range 5-100 | {} |
| `productId` | string | No | TikTok product ID, e.g., 1729508370969629931 (string format, to avoid large integer precision loss), obtainable from the product_id in the product rank response | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-product-analytics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-product-analytics request.json
# Or: node examples/javascript/run.mjs tiktok-product-analytics request.json
# Or: python3 examples/python/run.py tiktok-product-analytics request.json
```

### Published request example

```json
{
  "dateRange": "last30Day",
  "sortField": {},
  "region": "US",
  "pageNumber": 1,
  "productId": "1732505564636812173",
  "pageSize": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "data": [
    {
      "product_id": "example-id",
      "unit_price": 1,
      "sales_volumn": 1,
      "revenue": 1,
      "video_revenue": 1,
      "live_revenue": 1,
      "showcase_revenue": 1,
      "revenue_growth_rate": 1,
      "commission_rate": 1,
      "launch_date": "2026-01-01",
      "product_shop_id": "example-id",
      "pri_cate_id": "example-id",
      "sec_cate_id": "example-id",
      "ter_cate_id": "example-id",
      "min_price": 1,
      "max_price": 1,
      "product_review_count": 1,
      "video_number": 1,
      "live_number": 1,
      "shopping_mall_revenue": 1,
      "creator_number": 1
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-product-analytics.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-product-analytics.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-product-analytics.json)
- [Response fixture](../../examples/responses/tiktok-product-analytics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_product_analytics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
