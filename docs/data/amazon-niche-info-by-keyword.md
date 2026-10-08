# Amazon Niche Info By Keyword API

Deep analysis of Amazon niche markets by keyword, covering monopoly level, brand concentration, new product success rate, and market opportunity score.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-niche-info-by-keyword?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Deep analysis of Amazon niche markets by keyword, covering monopoly level, brand concentration, new product success rate, and market opportunity score.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-niche-info-by-keyword/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword (required, translate the keyword to the corresponding country's language based on the selected country), max length 1000 characters | {} |
| `countryCode` | string | No | Country code, options: US (United States), JP (Japan), DE (Germany) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page (10-100) | {} |
| `sortField` | string | No | Sort field (see sort options below) | {} |
| `sortType` | string | No | Sort direction: desc (descending) or asc (ascending) | {} |
| `productCountMin` | integer | No | Minimum product count (current) | {} |
| `productCountMax` | integer | No | Maximum product count (current) | {} |
| `avgPriceMin` | number | No | Minimum average price (current) | {} |
| `avgPriceMax` | number | No | Maximum average price (current) | {} |
| `searchVolumeT7Min` | integer | No | Minimum search volume (7-day stats) | {} |
| `searchVolumeT7Max` | integer | No | Maximum search volume (7-day stats) | {} |
| `unitsSoldT7Min` | integer | No | Minimum sales volume (7-day stats) | {} |
| `unitsSoldT7Max` | integer | No | Maximum sales volume (7-day stats) | {} |
| `clickCountT7Min` | integer | No | Minimum click volume (7-day stats) | {} |
| `clickCountT7Max` | integer | No | Maximum click volume (7-day stats) | {} |
| `clickConversionRateT7Min` | number | No | Minimum click conversion rate (7-day stats), range 0-1, representing 0%-100% | {} |
| `clickConversionRateT7Max` | number | No | Maximum click conversion rate (7-day stats), range 0-1, representing 0%-100% | {} |
| `brandCountMin` | integer | No | Minimum brand count | {} |
| `brandCountMax` | integer | No | Maximum brand count | {} |
| `top5BrandsClickShareMin` | number | No | Minimum top 5 brands' click share in the niche market, range 0-1, representing 0%-100% | {} |
| `top5BrandsClickShareMax` | number | No | Maximum top 5 brands' click share in the niche market, range 0-1, representing 0%-100% | {} |
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
| `top5ProductsClickShareMin` | number | No | Minimum top 5 products click share (current), range 0-1, representing 0%-100% | {} |
| `top5ProductsClickShareMax` | number | No | Maximum top 5 products click share (current), range 0-1, representing 0%-100% | {} |
| `sponsoredProductsPercentageMin` | number | No | Minimum SP ad share, range 0-1, representing 0%-100% | {} |
| `sponsoredProductsPercentageMax` | number | No | Maximum SP ad share, range 0-1, representing 0%-100% | {} |
| `cpcMediumMin` | number | No | Minimum CPC (current) | {} |
| `cpcMediumMax` | number | No | Maximum CPC (current) | {} |
| `launchRateT180Min` | number | No | Minimum product launch success rate (180-day stats), range 0-1, representing 0%-100% | {} |
| `launchRateT180Max` | number | No | Maximum product launch success rate (180-day stats), range 0-1, representing 0%-100% | {} |
| `newProductRateT180` | number | No | Minimum new product share (180-day stats), range 0-1, representing 0%-100% | {} |
| `returnRateT360Min` | number | No | Minimum return rate (360-day stats), range 0-1, representing 0%-100% | {} |
| `returnRateT360Max` | number | No | Maximum return rate (360-day stats), range 0-1, representing 0%-100% | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-niche-info-by-keyword.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-niche-info-by-keyword request.json
# Or: node examples/javascript/run.mjs amazon-niche-info-by-keyword request.json
# Or: python3 examples/python/run.py amazon-niche-info-by-keyword request.json
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
      "demand": 1,
      "productCount": 1,
      "avgPrice": 1,
      "minimumPrice": 1,
      "maximumPrice": 1,
      "searchVolumeWeekly": 1,
      "searchVolumeQuarterly": 1,
      "searchVolumeGrowthWeekly": 1,
      "searchVolumeGrowthQuarterly": 1,
      "unitsSoldWeekly": 1,
      "unitsSoldQuarterly": 1,
      "clickCountWeekly": 1,
      "clickCountQuarterly": 1,
      "clickToSaleConversionWeekly": 1,
      "clickConversionRateQuarterly": 1,
      "searchConversionRateWeekly": 1,
      "searchConversionRateQuarterly": 1,
      "brandCount": 1,
      "top5BrandsClickShare": 1,
      "top5ProductsClickShare": 1,
      "avgBrandAgeNow": 1,
      "avgBrandAgeQuarterly": 1,
      "newProductsLaunchedSemiannual": 1,
      "successfulLaunchedSemiannual": 1,
      "launchRateSemiannual": 1,
      "returnRateAnnual": 1,
      "acos": 1,
      "profitMarginGt50PctSkuRatio": 1,
      "breakEvenRatio": 1,
      "cpc": {},
      "categorieList": [],
      "referenceAsinImageUrl": "B072MQ5BRX"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-niche-info-by-keyword.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-niche-info-by-keyword.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-niche-info-by-keyword.json)
- [Response fixture](../../examples/responses/amazon-niche-info-by-keyword.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_niche_info_by_keyword`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
