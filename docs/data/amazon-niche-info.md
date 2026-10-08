# Amazon Niche Info API

Query and analyze Jiimore data for Amazon niche market insights, including market metrics, buyer reviews, competitive landscape, price trends, and growth trends.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-niche-info?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Query and analyze Jiimore data for Amazon niche market insights, including market metrics, buyer reviews, competitive landscape, price trends, and growth trends.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-niche-info/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `nicheId` | string | Yes | Niche market ID, max length 1000 characters, only supports single ID query | {} |
| `countryCode` | string | No | Country code, only supports US, JP, DE, default US | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-niche-info.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-niche-info request.json
# Or: node examples/javascript/run.mjs amazon-niche-info request.json
# Or: python3 examples/python/run.py amazon-niche-info request.json
```

### Published request example

```json
{
  "nicheId": "dfecfecfa9701de73a08867d7bcd3bc0",
  "countryCode": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "data": [],
  "columns": [],
  "costToken": 1,
  "nicheId": "dfecfecfa9701de73a08867d7bcd3bc0",
  "referenceAsinImageUrl": "B072MQ5BRX",
  "marketplaceId": "US",
  "demand": 1,
  "categorieList": [],
  "productCount": 1,
  "productCountNow": 1,
  "productCountT90Before": 1,
  "productCountT360Before": 1,
  "brandCount": 1,
  "brandCountNow": 1,
  "brandCountT90Before": 1,
  "brandCountT360Before": 1,
  "brandCountT360Now": 1,
  "brandCountT360T90Before": 1,
  "brandCountT360T360Before": 1,
  "sellingPartnerCountNow": 1,
  "sellingPartnerCountT90Before": 1,
  "sellingPartnerCountT360Before": 1,
  "sellingPartnerCountT360Now": 1,
  "sellingPartnerCountT360T90Before": 1,
  "sellingPartnerCountT360T360Before": 1,
  "avgPrice": 1,
  "avgProductPriceNow": 1,
  "avgProductPriceT90Before": 1,
  "avgProductPriceT360Before": 1,
  "minimumPrice": 1,
  "maximumPrice": 1,
  "searchVolumeWeekly": 1,
  "searchVolumeQuarterly": 1,
  "searchVolumeGrowthWeekly": 1,
  "searchVolumeGrowthQuarterly": 1,
  "searchConversionRateWeekly": 1,
  "searchConversionRateQuarterly": 1,
  "clickCountWeekly": 1,
  "clickCountQuarterly": 1,
  "clickConversionRateQuarterly": 1,
  "clickToSaleConversionWeekly": 1,
  "unitsSoldWeekly": 1,
  "unitsSoldQuarterly": 1,
  "top5ProductsClickShare": 1,
  "top5ProductsClickShareNow": 1,
  "top5ProductsClickShareT90Before": 1,
  "top5ProductsClickShareT360Before": 1,
  "top5ProductsClickShareT360Now": 1,
  "top5ProductsClickShareT360T90Before": 1,
  "top5ProductsClickShareT360T360Before": 1,
  "top20ProductsClickShareNow": 1,
  "top20ProductsClickShareT90Before": 1,
  "top20ProductsClickShareT360Before": 1,
  "top20ProductsClickShareT360Now": 1,
  "top20ProductsClickShareT360T90Before": 1,
  "top20ProductsClickShareT360T360Before": 1,
  "top5BrandsClickShare": 1,
  "top5BrandsClickShareNow": 1,
  "top5BrandsClickShareT90Before": 1,
  "top5BrandsClickShareT360Before": 1,
  "top5BrandsClickShareT360Now": 1,
  "top5BrandsClickShareT360T90Before": 1,
  "top5BrandsClickShareT360T360Before": 1,
  "top20BrandsClickShareNow": 1,
  "top20BrandsClickShareT90Before": 1,
  "top20BrandsClickShareT360Before": 1,
  "top20BrandsClickShareT360Now": 1,
  "top20BrandsClickShareT360T90Before": 1,
  "top20BrandsClickShareT360T360Before": 1,
  "newProductsLaunchedSemiannual": 1,
  "newProductsLaunchedT180Now": 1,
  "newProductsLaunchedT180T90Before": 1,
  "newProductsLaunchedT180T360Before": 1,
  "newProductsLaunchedT360Now": 1,
  "newProductsLaunchedT360T90Before": 1,
  "newProductsLaunchedT360T360Before": 1,
  "successfulLaunchedSemiannual": 1,
  "launchRateSemiannual": 1,
  "successfulLaunchesT90Now": 1,
  "successfulLaunchesT90T90Before": 1,
  "successfulLaunchesT90T360Before": 1,
  "successfulLaunchesT180Now": 1,
  "successfulLaunchesT180T90Before": 1,
  "successfulLaunchesT180T360Before": 1,
  "successfulLaunchesT360Now": 1,
  "successfulLaunchesT360T90Before": 1,
  "successfulLaunchesT360T360Before": 1,
  "avgOOSRateNow": 1,
  "avgOOSRateT90Before": 1,
  "avgOOSRateT360Before": 1,
  "avgOOSRateT360Now": 1,
  "avgOOSRateT360T90Before": 1,
  "avgOOSRateT360T360Before": 1,
  "primeProductsPercentageNow": 1,
  "primeProductsPercentageT90Before": 1,
  "primeProductsPercentageT360Before": 1,
  "primeProductsPercentageT360Now": 1,
  "primeProductsPercentageT360T90Before": 1,
  "primeProductsPercentageT360T360Before": 1,
  "avgReviewRatingNow": 1,
  "avgReviewRatingT90Before": 1,
  "avgReviewRatingT360Before": 1,
  "avgReviewCountNow": 1,
  "avgReviewCountT90Before": 1,
  "avgReviewCountT360Before": 1,
  "positiveCustomerReviewInsights": [],
  "negativeCustomerReviewInsights": [],
  "productStarRatingImpact": [],
  "avgBrandAgeNow": 1,
  "avgBrandAgeT90Before": 1,
  "avgBrandAgeT360Before": 1,
  "avgBrandAgeQuarterly": 1,
  "avgBrandAgeT360Now": 1,
  "avgBrandAgeT360T90Before": 1,
  "avgBrandAgeT360T360Before": 1,
  "avgSellingPartnerAgeNow": 1,
  "avgSellingPartnerAgeT90Before": 1,
  "avgSellingPartnerAgeT360Before": 1,
  "avgBestSellerRankNow": 1,
  "avgBestSellerRankT90Before": 1,
  "avgBestSellerRankT360Before": 1,
  "acos": 1,
  "sponsoredProductsPercentageNow": 1,
  "sponsoredProductsPercentageT90Before": 1,
  "sponsoredProductsPercentageT360Before": 1,
  "sponsoredProductsPercentageT360Now": 1,
  "sponsoredProductsPercentageT360T90Before": 1,
  "sponsoredProductsPercentageT360T360Before": 1,
  "profitMarginGt50PctSkuRatio": 1,
  "breakEvenRatio": 1,
  "returnRateAnnual": 1,
  "cpc": {}
}
```

## Full definitions

- [Request definition](../../schemas/amazon-niche-info.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-niche-info.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-niche-info.json)
- [Response fixture](../../examples/responses/amazon-niche-info.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_niche_info`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
