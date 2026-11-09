# Amazon Product History API

Retrieve Amazon product details by ASIN, including price, title, Item Highlights when available, main image, listing date, material, weight, variant monthly sales, and up to 12 months of monthly sales history. Triggered when users query Amazon product details, ASIN lookup, product pricing, sales rank history, monthly sales trends, product dimensions, FBA fees, product specifications, batch ASIN query, Nexscope product details, ASIN detail lookup, monthly sales data, pricing info, product specifications, FBA fees, batch ASIN query. Even if users do not explicitly mention "Nexscope", this skill should be triggered whenever the task involves obtaining structured product data for one or more Amazon ASINs.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-history?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-history/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon Standard Identification Number (ASIN), multiple ASINs separated by English commas, up to 5, max length 300 characters. Example: B0088PUEPK or B0088PUEPK,B00U26V4VQ,B07M68S376 | {} |
| `domain` | string | Yes | Amazon domain ID. Options: 1 (United States), 2 (United Kingdom), 3 (Germany), 4 (France), 5 (Japan), 6 (Canada), 8 (Italy), 9 (Spain), 10 (India), 11 (Mexico), 12 (Brazil) | {} |
| `history` | integer | No | Whether to include historical data and historical sales in the response. 1 = include price history, sales rank, historical sales and other time-series data (sales for previous months), 0 = return only basic product information. Default: 0 | {} |

The [complete request definition](../../schemas/amazon-product-history.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/amazon-product-history.json request.json
python3 examples/python/run.py amazon-product-history request.json --dry-run
# Alternatively: node examples/javascript/run.mjs amazon-product-history request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "asin": "B072MQ5BRX",
  "history": 1,
  "domain": "1"
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/amazon-product-history.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "total": 1,
    "perPage": 1,
    "columns": [],
    "costToken": 1,
    "totalCount": 1,
    "currentPage": 1,
    "products": [
      {
        "asin": "B072MQ5BRX",
        "price": 1,
        "primePrice": 1,
        "rating": 1,
        "ratings": 1,
        "reviewCount": 1,
        "salesRank": 1,
        "salesRank30": 1,
        "salesRank90": 1,
        "salesRank180": 1,
        "monthlySalesUnits": 1,
        "monthlySalesRevenue": 1,
        "monthlySalesUnits1MonthAgo": 1,
        "monthlySalesUnits2MonthsAgo": 1,
        "monthlySalesUnits3MonthsAgo": 1,
        "monthlySalesUnits4MonthsAgo": 1,
        "monthlySalesUnits5MonthsAgo": 1,
        "monthlySalesUnits6MonthsAgo": 1,
        "monthlySalesUnits7MonthsAgo": 1,
        "monthlySalesUnits8MonthsAgo": 1,
        "monthlySalesUnits9MonthsAgo": 1,
        "monthlySalesUnits10MonthsAgo": 1,
        "monthlySalesUnits11MonthsAgo": 1,
        "monthlySalesUnits12MonthsAgo": 1,
        "availableDate": "2026-01-01 00:00:00",
        "lastUpdate": "2026-01-01 00:00:00",
        "imageUrl": "https://example.com/image.jpg",
        "productImageUrls": [],
        "asinUrl": "https://www.amazon.com/dp/B072MQ5BRX",
        "urlSlug": "example-product",
        "itemLength": 1,
        "itemWidth": 1,
        "itemHeight": 1,
        "packageLength": 1,
        "packageWidth": 1,
        "packageHeight": 1,
        "packageQuantity": 1,
        "fbaFees": 1,
        "referralFeePercentage": 1,
        "profit": 1,
        "buyBoxSellerId": "example-id",
        "sellerNum": 1,
        "variationNum": 1,
        "parentAsin": "B072MQ5BRX",
        "rootCategory": 1,
        "categoryTreeId": "example-id",
        "subcategories": [],
        "isAdultProduct": false,
        "isHazmat": false
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
