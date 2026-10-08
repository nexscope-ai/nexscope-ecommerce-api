# Amazon Market Product Search API

Multi-dimensional Amazon product search and filtering based on Sorftime data, covering 14 marketplaces, with support for historical monthly snapshot lookback.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-market-product-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Multi-dimensional Amazon product search and filtering based on Sorftime data, covering 14 marketplaces, with support for historical monthly snapshot lookback.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Amazon site code: us, gb, de, fr, in, ca, jp, es, it, mx, ae, au, br, sa | {} |
| `queryMode` | integer | No | Query mode. 1: single condition query (default); 2: multi-condition combined query (AND relationship) | {} |
| `queryType` | integer | No | Query type (1-16), only effective when queryMode=1. See the complete Query Types description in API.md | {} |
| `queryValue` | string | No | Query condition value, format varies by queryMode and queryType. See the format description for each queryType in API.md | {} |
| `page` | integer | No | Page number, default 1. Max 100 products per page | {} |
| `queryMonth` | string | No | Historical month lookback, format yyyy-MM. When not specified, queries real-time data | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-market-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-market-product-search request.json
# Or: node examples/javascript/run.mjs amazon-market-product-search request.json
# Or: python3 examples/python/run.py amazon-market-product-search request.json
```

### Published request example

```json
{
  "marketplace": "us",
  "queryMode": 1,
  "page": 1,
  "queryValue": "B072MQ5BRX",
  "queryType": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "code": 1,
  "total": 1,
  "page": 1,
  "pageCount": 1,
  "costTime": 1,
  "costToken": 1,
  "requestConsumed": 1,
  "columns": [],
  "products": [
    {
      "asin": "B072MQ5BRX",
      "asinUrl": "B072MQ5BRX",
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "parentAsin": "B072MQ5BRX",
      "variationNum": 1,
      "size": [],
      "price": 1,
      "oldPrice": 1,
      "salesPrice": 1,
      "coupon": 1,
      "fbaFees": 1,
      "fbaDetail": [],
      "platformFee": 1,
      "profitAmount": 1,
      "profitRate": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "listingSalesVolumeOfDaily": 1,
      "listingSalesOfDaily": 1,
      "salesRank": 1,
      "category": [],
      "bsrCategory": [],
      "rating": 1,
      "ratings": 1,
      "availableDate": "2026-01-01",
      "onlineDays": 1,
      "buyBoxSellerId": "example-id",
      "isFBA": false,
      "sellerNum": 1,
      "aPlus": false,
      "hasVideo": false,
      "hasBrandStore": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-market-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-market-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-market-product-search.json)
- [Response fixture](../../examples/responses/amazon-market-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_market_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
