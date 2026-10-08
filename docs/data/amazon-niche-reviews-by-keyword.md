# Amazon Niche Reviews By Keyword API

Amazon niche market review analysis and consumer sentiment insights.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-niche-reviews-by-keyword?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Amazon niche market review analysis and consumer sentiment insights.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-niche-reviews-by-keyword/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword (required, use the language of the corresponding site, e.g. English for the US site, German for the Germany site), max length 1000 characters | {} |
| `countryCode` | string | No | Country code, options: US (United States), JP (Japan), DE (Germany) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page (10-100) | {} |
| `sortField` | string | No | Sort field, options: clickConversionRateT7 (7-day click conversion rate), demand (demand score), avgPrice (average product price), maximumPrice (highest product price), minimumPrice (lowest product price), productCount (product count), searchConversionRateT7 (7-day search conversion rate), searchVolumeT7 (7-day search volume), unitsSoldT7 (7-day sales volume), searchVolumeGrowthT7 (search growth rate), clickCountT90 (90-day click volume), clickCountT7 (weekly click volume), brandCount (brand count), top5BrandsClickShare (TOP5 brand share), newProductsLaunchedT180 (180-day new product success rate - launch count), successfulLaunchesT180 (180-day new product success rate - new product count), launchRateT180 (180-day new product success rate - launch rate), top5ProductsClickShare (top 5 product click share), returnRateT360 (return rate), clickConversionRateT90 (90-day click conversion rate), searchConversionRateT90 (90-day search conversion rate), searchVolumeT90 (90-day search volume), unitsSoldT90 (90-day sales volume), unitsSoldGrowthT90 (90-day sales growth rate), searchVolumeGrowthT90 (90-day search growth rate), acos, profitRate50 (profit rate for 50% natural orders) | {} |
| `sortType` | string | No | Sort direction, options: desc (descending), asc (ascending) | {} |
| `productCountMin` | integer | No | Minimum product count (current) | {} |
| `productCountMax` | integer | No | Maximum product count (current) | {} |
| `brandCountMin` | integer | No | Minimum brand count | {} |
| `brandCountMax` | integer | No | Maximum brand count | {} |
| `avgPriceMin` | number | No | Minimum average price (current) | {} |
| `avgPriceMax` | number | No | Maximum average price (current) | {} |
| `unitsSoldT7Min` | integer | No | Minimum sales volume (7-day stats) | {} |
| `unitsSoldT7Max` | integer | No | Maximum sales volume (7-day stats) | {} |
| `searchVolumeT7Min` | integer | No | Minimum search volume (7-day stats) | {} |
| `searchVolumeT7Max` | integer | No | Maximum search volume (7-day stats) | {} |
| `clickCountT7Min` | integer | No | Minimum click volume (7-day stats) | {} |
| `clickCountT7Max` | integer | No | Maximum click volume (7-day stats) | {} |
| `clickConversionRateT7Min` | number | No | Minimum click conversion rate (7-day stats) | {} |
| `clickConversionRateT7Max` | number | No | Maximum click conversion rate (7-day stats) | {} |
| `top5BrandsClickShareMin` | number | No | Minimum top 5 brands' click share in the niche market | {} |
| `top5BrandsClickShareMax` | number | No | Maximum top 5 brands' click share in the niche market | {} |
| `top5ProductsClickShareMin` | number | No | Minimum top 5 products click share (current) | {} |
| `top5ProductsClickShareMax` | number | No | Maximum top 5 products click share (current) | {} |
| `sponsoredProductsPercentageMin` | number | No | Minimum SP ad share | {} |
| `sponsoredProductsPercentageMax` | number | No | Maximum SP ad share | {} |
| `avgBrandAgeMin` | number | No | Minimum average brand age (current) | {} |
| `avgBrandAgeMax` | number | No | Maximum average brand age (current) | {} |
| `avgBrandAgeQoqMin` | number | No | Minimum average brand age (90-day stats) | {} |
| `avgBrandAgeQoqMax` | number | No | Maximum average brand age (90-day stats) | {} |
| `avgBrandAgeYoyMin` | number | No | Minimum average brand age (360-day stats) | {} |
| `avgBrandAgeYoyMax` | number | No | Maximum average brand age (360-day stats) | {} |
| `avgSellingPartnerAgeMin` | number | No | Minimum average selling partner age | {} |
| `avgSellingPartnerAgeMax` | number | No | Maximum average selling partner age | {} |
| `avgSellingPartnerAgeQoqMin` | number | No | Minimum average selling partner age (90-day stats) | {} |
| `avgSellingPartnerAgeQoqMax` | number | No | Maximum average selling partner age (90-day stats) | {} |
| `avgSellingPartnerAgeYoyMin` | number | No | Minimum average selling partner age (360-day stats) | {} |
| `avgSellingPartnerAgeYoyMax` | number | No | Maximum average selling partner age (360-day stats) | {} |
| `launchRateT180Min` | number | No | Minimum product launch success rate (180-day stats) | {} |
| `launchRateT180Max` | number | No | Maximum product launch success rate (180-day stats) | {} |
| `newProductRateT180` | number | No | Minimum new product share (180-day stats) | {} |
| `returnRateT360Min` | number | No | Minimum return rate (360-day stats) | {} |
| `returnRateT360Max` | number | No | Maximum return rate (360-day stats) | {} |
| `cpcMediumMin` | number | No | Minimum CPC (current) | {} |
| `cpcMediumMax` | number | No | Maximum CPC (current) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-niche-reviews-by-keyword.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-niche-reviews-by-keyword request.json
# Or: node examples/javascript/run.mjs amazon-niche-reviews-by-keyword request.json
# Or: python3 examples/python/run.py amazon-niche-reviews-by-keyword request.json
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
  "data": [
    {
      "nicheId": "example-id",
      "keyword": "phone case",
      "percentOfMentions": 1
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-niche-reviews-by-keyword.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-niche-reviews-by-keyword.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-niche-reviews-by-keyword.json)
- [Response fixture](../../examples/responses/amazon-niche-reviews-by-keyword.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_niche_reviews_by_keyword`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
