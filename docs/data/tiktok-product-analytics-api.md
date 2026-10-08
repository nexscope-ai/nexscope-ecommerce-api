# TikTok Product Analytics Detail API

Retrieve detailed performance data for a TikTok product.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-product-analytics-api?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Queries Kalodata product details, including price, sales, revenue, commission, lifecycle, and shop data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-product-analytics-api/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productId` | string | Yes | TikTok product ID. | {} |
| `region` | string | No | TikTok Shop market region. | {} |
| `currency` | string | No | Currency code. | {} |
| `language` | string | No | Response language. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-product-analytics-api.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-product-analytics-api request.json
# Or: node examples/javascript/run.mjs tiktok-product-analytics-api request.json
# Or: python3 examples/python/run.py tiktok-product-analytics-api request.json
```

### Published request example

```json
{
  "region": "US",
  "productId": "1732505564636812173"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": [
    {
      "product_id": "1732505564636812173",
      "product_name": "Example product",
      "unit_price": 12.99,
      "sales_volumn": 100,
      "revenue": 1000,
      "video_revenue": 600,
      "live_revenue": 300,
      "showcase_revenue": 100,
      "revenue_growth_rate": 12.5,
      "commission_rate": 20,
      "launch_date": "2026-01-01",
      "product_region": "US",
      "product_shop_id": "shop-id",
      "min_price": 9.99,
      "max_price": 19.99,
      "product_review_count": 200,
      "video_number": 25,
      "live_number": 5,
      "creator_number": 10
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-product-analytics-api.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-product-analytics-api.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-product-analytics-api.json)
- [Response fixture](../../examples/responses/tiktok-product-analytics-api.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_product_analytics_api`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
