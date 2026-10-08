# Amazon ASIN Traffic Summary API

Use SIF (Search Intelligence Framework) data to analyze ASIN traffic source composition and exposure distribution, covering current period/previous period/newly entered/exited period comparisons.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-asin-traffic-summary?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use SIF (Search Intelligence Framework) data to analyze ASIN traffic source composition and exposure distribution, covering current period/previous period/newly entered/exited period comparisons.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-asin-traffic-summary/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchValue` | string | Yes | Search value, ASIN codes, comma-separated, max 10 ASINs, max length 1000 characters | {} |
| `country` | string | No | Country site, default US. Options (13 total): US, UK, DE, CA, JP, FR, ES, IT, MX, AU, AE, BR, SA | {} |
| `last7d` | boolean | No | Whether to get last 7 days data, default true. When false, use startDate/endDate range | {} |
| `startDate` | string | No | Start date yyyy-MM-dd (effective when last7d=false; if omitted, the latest system week is used) | {} |
| `endDate` | string | No | End date yyyy-MM-dd (paired with startDate) | {} |
| `conditions` | string | No | Condition filters, comma-separated. Options: nf (natural traffic), sp (SP ads), sb (SB regular), sbv (video ads), ad (ad traffic), acAd (SP recommendation), totalPeriod.in (new incoming traffic keywords) | {} |
| `sortBy` | string | No | Sort field. Options: totalKeywordNum (all traffic keywords), naturalKeywordNum (natural traffic keywords), brandKeywordNum (brand ad keywords), vedioKeywordNum (video ad keywords), acKeywordNum (AC recommended keywords), erKeywordNum (ER recommended keywords), trKeywordNum (TR recommended keywords), sumScore (total keyword exposure score), totalNfScore (total natural rank exposure score), totalSpSocre (total SP ad exposure score, note spelling), totalBrandScore (total brand ad exposure score), totalVedioScore (total video ad exposure score), totalAcScore (total AC recommendation exposure score), totalTrScore (total TR recommendation exposure score), totalErScore (total ER recommendation exposure score) | {} |
| `pageNum` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Results per page, min 10, max 10000, default 10000 | {} |
| `desc` | boolean | No | Whether to sort descending, default true | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-asin-traffic-summary.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-asin-traffic-summary request.json
# Or: node examples/javascript/run.mjs amazon-asin-traffic-summary request.json
# Or: python3 examples/python/run.py amazon-asin-traffic-summary request.json
```

### Published request example

```json
{
  "last7d": true,
  "searchValue": "B072MQ5BRX",
  "country": "US",
  "pageNum": 1,
  "desc": true,
  "pageSize": 10
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
      "asin": "B072MQ5BRX",
      "productPrice": 1,
      "productImageUrl": "https://example.com/image.jpg",
      "productFeatures": [],
      "customerRatingCount": 1,
      "productStarRating": 1,
      "productRatingScore": 1,
      "isVariantProduct": false,
      "isMonitored": false,
      "dataPeriodStartDate": "2026-01-01",
      "totalExposureScore": 1,
      "totalExposureScorePrev": 1,
      "totalTrafficKeywordCount": 1,
      "totalTrafficKeywordCountIn": 1,
      "totalTrafficKeywordCountOut": 1,
      "totalTrafficKeywordCountPrev": 1,
      "naturalSearchExposureScore": 1,
      "naturalSearchExposureRatio": 1,
      "naturalSearchExposureScorePrev": 1,
      "naturalSearchKeywordCount": 1,
      "naturalSearchKeywordCountIn": 1,
      "naturalSearchKeywordCountOut": 1,
      "naturalSearchKeywordCountPrev": 1,
      "sponsoredProductsExposureScore": 1,
      "sponsoredProductsExposureRatio": 1,
      "sponsoredProductsExposureScorePrev": 1,
      "sponsoredProductsKeywordCount": 1,
      "brandAdExposureScore": 1,
      "brandAdExposureRatio": 1,
      "brandAdExposureScorePrev": 1,
      "brandAdKeywordCount": 1,
      "topBrandAdKeywordCount": 1,
      "bottomBrandAdKeywordCount": 1,
      "videoAdExposureScore": 1,
      "videoAdExposureRatio": 1,
      "videoAdExposureScorePrev": 1,
      "videoAdKeywordCount": 1,
      "amazonsChoiceExposureScore": 1,
      "amazonsChoiceExposureRatio": 1,
      "amazonsChoiceExposureScorePrev": 1,
      "amazonsChoiceKeywordCount": 1,
      "amazonsChoiceKeywordCountIn": 1,
      "amazonsChoiceKeywordCountOut": 1,
      "editorialRecommendationsExposureScore": 1,
      "editorialRecommendationsExposureRatio": 1,
      "editorialRecommendationsKeywordCount": 1,
      "topRatedExposureScore": 1,
      "topRatedExposureRatio": 1,
      "topRatedKeywordCount": 1,
      "frequentlyBoughtKeywordCount": 1,
      "recommendPositionExposureScore": 1,
      "recommendAdExposureScore": 1,
      "recommendNonadExposureScore": 1,
      "nonAcRecommendExposureScore": 1,
      "recommendKeywordCount": 1,
      "recommendAdKeywordCount": 1,
      "recommendNonadKeywordCount": 1,
      "ppcTrafficSources": [],
      "naturalSearchTrafficSources": [],
      "amazonRecommendationSources": [],
      "promotionalDealSources": []
    }
  ],
  "columns": [],
  "isParentAsin": false,
  "variantsNum": 1,
  "noKeywordVariantsNum": 1,
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-asin-traffic-summary.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-asin-traffic-summary.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-asin-traffic-summary.json)
- [Response fixture](../../examples/responses/amazon-asin-traffic-summary.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_asin_traffic_summary`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
