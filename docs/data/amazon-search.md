# Amazon Search API

Simulates a real user searching on Amazon's storefront to get real-time keyword ranking and search results page data. Use when the user mentions Amazon product search, search result scraping, keyword ranking on search pages, ASIN ranking position check, competitor discovery, search page price comparison, sponsored product analysis, new product monitoring, or storefront search simulation. Even if the user does not explicitly mention "search simulation", trigger this skill whenever their need involves real-time Amazon search results, product ranking data, or storefront SERP analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Keyword; please translate to the language of the target country whenever possible, e.g., use English keywords for the US, German keywords for Germany, etc. (max length 1024) | {} |
| `amazonDomain` | string | No | Amazon country site, default amazon.com | {} |
| `node` | string | No | Amazon category node (max length 1000) | {} |
| `language` | string | No | Language/region code, e.g., en_US, de_DE, ja_JP, fr_FR (max length 1000) | {} |
| `sort` | string | No | Sort order: relevanceblender (Featured, default), price-asc-rank (Price low to high), price-desc-rank (Price high to low), review-rank (Avg. customer review), date-desc-rank (Newest arrivals), exact-aware-popularity-rank (Best sellers) | {} |
| `page` | integer | No | Page number (starting from 1, ~20 items per page), default 1 | {} |
| `deliveryZip` | string | No | Delivery zip code, used to simulate Amazon frontend address. It is recommended to use commonly used zip codes for major cities in the target country, e.g., New York zip code 10001 for the US site (max length 1000) | {} |
| `device` | string | No | Device type: desktop, mobile, tablet, default desktop (max length 1000) | {} |
| `includeSellerSpriteData` | boolean | No | Enable additional product-data enrichment, including availableDate when available. Default: false. Enabling enrichment incurs additional dynamic charges and does not guarantee a date for every ASIN. | {} |

The [complete request definition](../../schemas/amazon-search.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/amazon-search.json request.json
python3 examples/python/run.py amazon-search request.json --dry-run
# Alternatively: node examples/javascript/run.mjs amazon-search request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "keyword": "phone case",
  "includeSellerSpriteData": false,
  "page": 1
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/amazon-search.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "total": 1,
    "keyword": "phone case",
    "columns": [],
    "costToken": 1,
    "sellerSpriteEnriched": false,
    "products": [
      {
        "asin": "B072MQ5BRX",
        "price": 1,
        "extractedPrice": 1,
        "oldPrice": 1,
        "extractedOldPrice": 1,
        "extractedPriceUnit": 1,
        "rating": 1,
        "ratings": 1,
        "position": 1,
        "sponsored": false,
        "imageUrl": "https://example.com/image.jpg",
        "asinUrl": "https://www.amazon.com/dp/B072MQ5BRX",
        "availableDate": "2026-01-01 00:00:00",
        "monthlySalesUnits": 1,
        "snapEbtEligible": false,
        "keyword": "phone case"
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
