# TikTok Shop Analytics API

Search TikTok e-commerce store leaderboards via Kalodata and query detailed information for specific stores. Supports viewing high-ranking, high-sales TikTok Shop stores by region, currency, language, and date range, and using shopId to retrieve revenue, sales volume, on-sale product count, self-operated/affiliate/shopping mall channel revenue, and creator collaboration count.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-shop-analytics?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search TikTok e-commerce store leaderboards via Kalodata and query detailed information for specific stores. Supports viewing high-ranking, high-sales TikTok Shop stores by region, currency, language, and date range, and using shopId to retrieve revenue, sales volume, on-sale product count, self-operated/affiliate/shopping mall channel revenue, and creator collaboration count.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-shop-analytics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `region` | string | No | Region/market code, e.g., US. Max length 1000 | {} |
| `dateRange` | string | No | Time range, e.g., last7Day (last 7 days), last30Day (last 30 days). Max length 1000 | {} |
| `pageNumber` | integer | No | Page number, value range 1-5 (out of range returns errcode 501) | {} |
| `pageSize` | integer | No | Items per page, value range 5-100 | {} |
| `language` | string | No | Return language, e.g., zh-CN, en-US. Max length 1000 | {} |
| `currency` | string | No | Currency unit, e.g., USD. Max length 1000 | {} |
| `sortField` | object | No | Sort criteria; pass an empty object {} for default rank order when not sorting | {} |
| `shopId` | string | No | TikTok shop unique ID (string, to avoid large integer precision loss), e.g., 7495514739648989419. Obtainable from the shop_id field in the shop rank response | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-shop-analytics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-shop-analytics request.json
# Or: node examples/javascript/run.mjs tiktok-shop-analytics request.json
# Or: python3 examples/python/run.py tiktok-shop-analytics request.json
```

### Published request example

```json
{
  "dateRange": "last30Day",
  "sortField": {},
  "region": "US",
  "pageNumber": 1,
  "shopId": "7496162162184128712",
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
      "rank": 1,
      "shop_id": "example-id",
      "revenue": 1,
      "sales_volumn": 1,
      "on_sell_product_count": 1,
      "unit_price": 1,
      "revenue_growth_rate": 1,
      "self_promotion_revenue": 1,
      "affiliate_revenue": 1,
      "shopping_mall_revenue": 1,
      "region": "US",
      "product_number": 1,
      "self_account_revenue": 1,
      "shoppingmall_revenue": 1,
      "creator_number": 1,
      "video_number": 1,
      "live_number": 1
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-shop-analytics.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-shop-analytics.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-shop-analytics.json)
- [Response fixture](../../examples/responses/tiktok-shop-analytics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_shop_analytics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
