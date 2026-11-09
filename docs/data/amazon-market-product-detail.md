# Amazon Market Product Detail API

Query Amazon product detail and historical trends by ASIN using Nexscope data, covering 14 marketplaces. Trigger when the user mentions Nexscope product detail, ASIN detail query, sales trends, price curves, price history, BSR ranking history, BSR trends, profit analysis, FBA fee analysis, gross margin, product trend analysis, daily/monthly sales, revenue trends, Deal promotion history, product detail, sales trend, price history, BSR ranking, profit analysis, FBA fees. Even if the user does not explicitly mention "Nexscope", if their need involves querying Amazon product detail or historical trend data by ASIN, this skill should also be triggered.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-market-product-detail?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon Standard Identification Number (ASIN), supports multiple (max 10), comma-separated. Example: B0088PUEPK or B0088PUEPK,B00U26V4VQ | {} |
| `marketplace` | string | Yes | Amazon site code: us, gb, de, fr, in, ca, jp, es, it, mx, ae, au, br, sa | {} |
| `includeTrend` | integer | No | Whether to include trend data. 1: include (default); 2: exclude | {} |
| `queryTrendStartDate` | string | No | Trend start date, format yyyy-MM-dd. Default returns only the last 15 days; querying more than 15 days doubles the cost | {} |
| `queryTrendEndDate` | string | No | Trend end date, format yyyy-MM-dd | {} |

The [complete request definition](../../schemas/amazon-market-product-detail.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/amazon-market-product-detail.json request.json
python3 examples/python/run.py amazon-market-product-detail request.json --dry-run
# Alternatively: node examples/javascript/run.mjs amazon-market-product-detail request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "queryTrendStartDate": "2026-01-01",
  "includeTrend": 1,
  "asin": "B072MQ5BRX",
  "marketplace": "us",
  "queryTrendEndDate": "2026-01-15"
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/amazon-market-product-detail.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
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
  },
  "code": 0,
  "msg": null,
  "ts": "0",
  "time": "2026-01-01 00:00:00",
  "cost": "-1",
  "traceId": null
}
```

Keep the request trace when reporting errors. Do not infer authorization, order creation or payment success from a redirect, process exit or missing identifier alone.
