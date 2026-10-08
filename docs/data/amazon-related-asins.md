# Amazon Related ASINs API

Find Amazon same-niche competitors by ASIN, with multi-dimensional filtering by click conversion rate, composite conversion rate, click volume, sales volume, reviews, ratings, price, and gross margin to identify potential competitors.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-related-asins?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Find Amazon same-niche competitors by ASIN, with multi-dimensional filtering by click conversion rate, composite conversion rate, click volume, sales volume, reviews, ratings, price, and gross margin to identify potential competitors.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-related-asins/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Reference ASIN, used to query competitor listings that belong to the same niche as this ASIN, max length 1000 characters | {} |
| `countryCode` | string | No | Country code, options: US (United States), JP (Japan), DE (Germany) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Items returned per page (10-100) | {} |
| `sortField` | string | No | Sort field (see sort options below) | {} |
| `sortType` | string | No | Sort direction: desc (descending) or asc (ascending) | {} |
| `priceMin` | number | No | Minimum product price | {} |
| `priceMax` | number | No | Maximum product price | {} |
| `fbaFeeMin` | number | No | Minimum FBA fee | {} |
| `fbaFeeMax` | number | No | Maximum FBA fee | {} |
| `grossProfitMarginMin` | number | No | Minimum gross profit margin | {} |
| `grossProfitMarginMax` | number | No | Maximum gross profit margin | {} |
| `totalReviewsMin` | integer | No | Minimum review count | {} |
| `totalReviewsMax` | integer | No | Maximum review count | {} |
| `customerRatingMin` | number | No | Minimum rating, range 0.0-5.0 | {} |
| `customerRatingMax` | number | No | Maximum rating, range 0.0-5.0 | {} |
| `clickCountT7Min` | integer | No | Minimum weekly click count | {} |
| `clickCountT7Max` | integer | No | Maximum weekly click count | {} |
| `clickCountGrowthT7Min` | number | No | Minimum weekly click growth rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickCountGrowthT7Max` | number | No | Maximum weekly click growth rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickConversionRateMin` | number | No | Minimum click conversion rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickConversionRateMax` | number | No | Maximum click conversion rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickCountT30Min` | integer | No | Minimum monthly click count | {} |
| `clickCountT30Max` | integer | No | Maximum monthly click count | {} |
| `clickCountGrowthT30Min` | number | No | Minimum monthly click growth rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickCountGrowthT30Max` | number | No | Maximum monthly click growth rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickConversionRateCompositeMin` | number | No | Minimum composite click conversion rate, range 0-1, e.g., 0.1 means 10% | {} |
| `clickConversionRateCompositeMax` | number | No | Maximum composite click conversion rate, range 0-1, e.g., 0.1 means 10% | {} |
| `salesVolumeT360Min` | integer | No | Minimum annual sales volume | {} |
| `salesVolumeT360Max` | integer | No | Maximum annual sales volume | {} |
| `launchDateMin` | string | No | Earliest listing time, format yyyyMMdd000000 | {} |
| `launchDateMax` | string | No | Latest listing time, format yyyyMMdd000000 | {} |
| `nicheCountMin` | integer | No | Minimum number of niche markets | {} |
| `nicheCountMax` | integer | No | Maximum number of niche markets | {} |
| `sellerCountry` | string | No | Seller country code, comma-separated for multiple countries, e.g.: CN,US | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-related-asins.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-related-asins request.json
# Or: node examples/javascript/run.mjs amazon-related-asins request.json
# Or: python3 examples/python/run.py amazon-related-asins request.json
```

### Published request example

```json
{
  "asin": "B072MQ5BRX",
  "page": 1,
  "pageSize": 10,
  "countryCode": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "pages": 1,
  "page": 1,
  "pageSize": 10,
  "data": [
    {
      "asin": "B072MQ5BRX",
      "parentAsin": "B072MQ5BRX",
      "price": 1,
      "currentPrice": 1,
      "customerRating": 1,
      "totalReviews": 1,
      "launchDate": "2026-01-01",
      "imagesUrl": "https://example.com/image.jpg",
      "sellerId": "example-id",
      "fbaFee": 1,
      "shippingFee": 1,
      "gpm": 1,
      "clickConversionRate": 1,
      "clickConversionRateComposite": 1,
      "clickCountT7": 1,
      "clickCountT30": 1,
      "clickCountT90": 1,
      "clickCountGrowthT7": 1,
      "clickCountGrowthT30": 1,
      "purchasedClicksT360": 1,
      "salesVolumeT360": 1,
      "nicheCount": 1,
      "involvedNum": 1,
      "involvedFrequency": 1,
      "categoryNames": [],
      "hasMetric": false,
      "niches": [],
      "bestSellersRanking": [],
      "trends": [],
      "lastUpdateTime": "2026-01-01"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-related-asins.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-related-asins.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-related-asins.json)
- [Response fixture](../../examples/responses/amazon-related-asins.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_related_asins`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
