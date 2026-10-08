# Amazon Market Product Detail API

Query Amazon product detail and historical trends by ASIN using Sorftime data, covering 14 marketplaces.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-market-product-detail?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Query Amazon product detail and historical trends by ASIN using Sorftime data, covering 14 marketplaces.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon Standard Identification Number (ASIN), supports multiple (max 10), comma-separated. Example: B0088PUEPK or B0088PUEPK,B00U26V4VQ | {} |
| `marketplace` | string | Yes | Amazon site code: us, gb, de, fr, in, ca, jp, es, it, mx, ae, au, br, sa | {} |
| `includeTrend` | integer | No | Whether to include trend data. 1: include (default); 2: exclude | {} |
| `queryTrendStartDate` | string | No | Trend start date, format yyyy-MM-dd. Default returns only the last 15 days; querying more than 15 days doubles the cost | {} |
| `queryTrendEndDate` | string | No | Trend end date, format yyyy-MM-dd | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-market-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-market-product-detail request.json
# Or: node examples/javascript/run.mjs amazon-market-product-detail request.json
# Or: python3 examples/python/run.py amazon-market-product-detail request.json
```

### Published request example

```json
{
  "marketplace": "us",
  "queryTrendEndDate": "2026-01-15",
  "queryTrendStartDate": "2026-01-01",
  "includeTrend": 1,
  "asin": "B072MQ5BRX"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "code": 1,
  "total": 1,
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
      "ebcPhoto": [],
      "productBadge": [],
      "lastUpdate": "2026-01-01",
      "offSale": false,
      "size": [],
      "parentAsin": "B072MQ5BRX",
      "variationNum": 1,
      "variationASIN": [],
      "attribute": [],
      "price": 1,
      "coupon": 1,
      "platformFee": 1,
      "fbaFees": 1,
      "fbaDetail": [],
      "shipCost": 1,
      "profitAmount": 1,
      "profitRate": 1,
      "monthlySalesUnits": 1,
      "salesRank": 1,
      "category": [],
      "bsrCategory": [],
      "availableDate": "2026-01-01",
      "onlineDays": 1,
      "rating": 1,
      "ratings": 1,
      "fiveStarRatings": 1,
      "fourStarRatings": 1,
      "threeStarRatings": 1,
      "twoStarRatings": 1,
      "oneStarRatings": 1,
      "buyBoxSellerId": "example-id",
      "isFBA": false,
      "sellerNum": 1,
      "aPlus": false,
      "hasVideo": false,
      "hasBrandStore": false,
      "feature": {},
      "productInfo": {},
      "property": {},
      "extraSavings": [],
      "rankTrend": [],
      "bsrRankTrend": [],
      "listingSalesVolumeOfDailyTrend": [],
      "listingSalesOfDailyTrend": [],
      "listingSalesVolumeOfMonthTrend": [],
      "listingSalesOfMonthTrend": [],
      "priceTrend": [],
      "listPriceTrend": [],
      "dealTrend": []
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-market-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-market-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-market-product-detail.json)
- [Response fixture](../../examples/responses/amazon-market-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_market_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
