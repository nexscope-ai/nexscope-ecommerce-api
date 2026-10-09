# Amazon Product Discovery API

Amazon product discovery and potential bestseller mining via Nexscope data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-discovery?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Amazon product discovery and potential bestseller mining via Nexscope data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-discovery/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword (required; translate the keyword to the language of the selected country) | {} |
| `countryCode` | string | No | Country, use country abbreviation. Default US. Options: US, JP, DE | {} |
| `priceMin` | number | No | Minimum product price | {} |
| `priceMax` | number | No | Maximum product price | {} |
| `totalReviewsMin` | integer | No | Minimum number of reviews | {} |
| `totalReviewsMax` | integer | No | Maximum number of reviews | {} |
| `customerRatingMin` | number | No | Minimum rating | {} |
| `customerRatingMax` | number | No | Maximum rating | {} |
| `clickConversionRateMin` | number | No | Minimum click-to-purchase conversion rate, value range 0-1, 0.1 means 10% | {} |
| `clickConversionRateMax` | number | No | Maximum click-to-purchase conversion rate, value range 0-1, 0.1 means 10% | {} |
| `clickConversionRateCompositeMin` | number | No | Minimum composite conversion rate, value range 0-1, 0.1 means 10% | {} |
| `clickConversionRateCompositeMax` | number | No | Maximum composite conversion rate, value range 0-1, 0.1 means 10% | {} |
| `clickCountT7Min` | integer | No | Minimum weekly click count | {} |
| `clickCountT7Max` | integer | No | Maximum weekly click count | {} |
| `clickCountT30Min` | integer | No | Minimum monthly click count | {} |
| `clickCountT30Max` | integer | No | Maximum monthly click count | {} |
| `clickCountGrowthT7Min` | number | No | Minimum weekly click growth rate, value range 0-1, 0.1 means 10% | {} |
| `clickCountGrowthT7Max` | number | No | Maximum weekly click growth rate, value range 0-1, 0.1 means 10% | {} |
| `clickCountGrowthT30Min` | number | No | Minimum monthly click growth rate, value range 0-1, 0.1 means 10% | {} |
| `clickCountGrowthT30Max` | number | No | Maximum monthly click growth rate, value range 0-1, 0.1 means 10% | {} |
| `salesVolumeT360Min` | integer | No | Minimum annual sales volume | {} |
| `salesVolumeT360Max` | integer | No | Maximum annual sales volume | {} |
| `grossProfitMarginMin` | number | No | Minimum gross profit margin | {} |
| `grossProfitMarginMax` | number | No | Maximum gross profit margin | {} |
| `fbaFeeMin` | number | No | Minimum FBA fee | {} |
| `fbaFeeMax` | number | No | Maximum FBA fee | {} |
| `launchDateMin` | string | No | Earliest listing time, format: yyyyMMdd000000 | {} |
| `launchDateMax` | string | No | Latest listing time, format: yyyyMMdd000000 | {} |
| `nicheCountMin` | integer | No | Minimum niche market count | {} |
| `nicheCountMax` | integer | No | Maximum niche market count | {} |
| `sellerCountry` | string | No | Seller country/region code, comma-separated for multiple selections, e.g.: CN,US | {} |
| `sortField` | string | No | Sort field. Default purchasedClicksT360. Options: totalReviews (total reviews), price (price), launchDate (listing time), clickCountT7 (7-day click count), clickCountT30 (30-day click count), clickCountT90 (90-day click count), clickConversionRate (click-to-purchase conversion rate), clickConversionRateComposite (composite click-to-purchase conversion rate), customerRating (rating), purchasedClicksT360 (360-day purchase clicks), clickCountGrowthT7 (weekly click growth rate), clickCountGrowthT30 (monthly click growth rate), currentPrice (current price), fbaFee (FBA fee), shippingFee (FBA shipping), gpm (gross profit margin) | {} |
| `sortType` | string | No | Sort direction. Default desc. Options: desc (descending), asc (ascending) | {} |
| `page` | integer | No | Page number. Default 1 | {} |
| `pageSize` | integer | No | Items per page (10-100). Default 50 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-discovery.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-discovery request.json
# Or: node examples/javascript/run.mjs amazon-product-discovery request.json
# Or: python3 examples/python/run.py amazon-product-discovery request.json
```

### Published request example

```json
{
  "page": 1,
  "pageSize": 10,
  "keyword": "phone case",
  "countryCode": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "costToken": 1,
  "columns": [],
  "products": [
    {
      "asin": "B072MQ5BRX",
      "parentAsin": "B072MQ5BRX",
      "price": 1,
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "asinUrl": "B072MQ5BRX",
      "ratings": 1,
      "availableDate": "2026-01-01",
      "availableDateString": "2026-01-01",
      "categoryNames": [],
      "marketplaceId": "US",
      "clickCountT7": 1,
      "clickCountT30": 1,
      "clickCountT90": 1,
      "clickConversionRate": 1,
      "clickConversionRateComposite": 1,
      "grossProfitMargin": 1,
      "fbaFee": 1,
      "shippingFee": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-discovery.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-discovery.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-discovery.json)
- [Response fixture](../../examples/responses/amazon-product-discovery.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_discovery`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
