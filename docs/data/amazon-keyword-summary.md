# Amazon Keyword Summary API

Break down all competitor ASIN traffic sources under a given keyword -- organic search, SP ads, SB brand ads, SBV video ads, SP recommendations, AC/ER/TR recommendation slots, with support for ASIN filtering, custom date ranges, and new traffic keyword filters.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-summary?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Break down all competitor ASIN traffic sources under a given keyword -- organic search, SP ads, SB brand ads, SBV video ads, SP recommendations, AC/ER/TR recommendation slots, with support for ASIN filtering, custom date ranges, and new traffic keyword filters.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-summary/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKeyword` | string | Yes | Search keyword, translate to the corresponding country's language whenever possible. Max length 1000 characters | {} |
| `country` | string | No | Country site, default US. Options (13 total): US, UK, DE, CA, JP, FR, ES, IT, MX, AU, AE, BR, SA | {} |
| `asins` | string | No | ASIN filter list, comma-separated; if not provided, returns all ASINs for this keyword. Max length 1000 characters | {} |
| `condition` | string | No | Condition filter, only one at a time.<br>Flag type: nfPosition (natural traffic keyword), isSpAd (SP ad keyword), isVedioAd (video ad keyword), isBrandAd (brand ad keyword), isPPCAd (PPC ad keyword), isSearchRecommend (search recommendation keyword), acAd (SP recommendation)<br>Period count type: totalPeriod.in (new incoming traffic keywords), nfKeywordCnt.total / .in, adKeywordCnt.total / .in, allSpKeywordCnt.total / .in, spKeywordCnt.total / .in, recSpKeywordCnt.total / .in, allSbKeywordCnt.total / .in, sbKeywordCnt.total / .in, sbvKeywordCnt.total / .in | {} |
| `last7d` | boolean | No | Whether to get last 7 days data, default true. When false, use startDate/endDate range | {} |
| `startDate` | string | No | Start date yyyy-MM-dd (effective when last7d=false; if omitted, the latest system full week is used) | {} |
| `endDate` | string | No | End date yyyy-MM-dd (paired with startDate) | {} |
| `sortBy` | string | No | Sort field. Options: totalKeywordNum (all traffic keywords), naturalKeywordNum (natural traffic keywords), brandKeywordNum (brand ad keywords), vedioKeywordNum (video ad keywords), acKeywordNum (AC recommended keywords), erKeywordNum (ER recommended keywords), trKeywordNum (TR recommended keywords), sumScore (total keyword exposure score), totalNfScore, totalSpSocre (note spelling), totalBrandScore, totalVedioScore, totalAcScore, totalTrScore, totalErScore | {} |
| `pageNum` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Results per page, min 10, max 100, default 100 | {} |
| `desc` | boolean | No | Whether to sort descending, default true | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-summary.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-summary request.json
# Or: node examples/javascript/run.mjs amazon-keyword-summary request.json
# Or: python3 examples/python/run.py amazon-keyword-summary request.json
```

### Published request example

```json
{
  "searchKeyword": "phone case",
  "country": "US",
  "pageNum": 1,
  "last7d": true,
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
      "productImageUrl": "https://example.com/image.jpg",
      "productPrice": 1,
      "customerRatingCount": 1,
      "productStarRating": 1,
      "productRatingScore": 1,
      "productUpdateTime": "2026-01-01",
      "dataPeriodStartDate": "2026-01-01",
      "totalExposureScore": 1,
      "totalExposureRatio": 1,
      "naturalSearchExposureScore": 1,
      "naturalSearchExposureRatio": 1,
      "sponsoredProductsExposureScore": 1,
      "sponsoredProductsExposureRatio": 1,
      "brandAdExposureScore": 1,
      "brandAdExposureRatio": 1,
      "videoAdExposureScore": 1,
      "videoAdExposureRatio": 1,
      "amazonsChoiceExposureScore": 1,
      "amazonsChoiceExposureRatio": 1,
      "editorialRecommendationsExposureScore": 1,
      "editorialRecommendationsExposureRatio": 1,
      "topRatedExposureScore": 1,
      "topRatedExposureRatio": 1,
      "recommendPositionExposureScore": 1,
      "recommendAdExposureScore": 1,
      "recommendAdExposureRatio": 1,
      "recommendNonadExposureScore": 1,
      "recommendNonadExposureRatio": 1,
      "comprehensiveNaturalExposureScore": 1,
      "comprehensiveNaturalExposureRatio": 1,
      "keywordTotalExposureScore": 1,
      "keywordNaturalExposureScore": 1,
      "keywordSponsoredProductsExposureScore": 1,
      "keywordBrandAdExposureScore": 1,
      "keywordVideoAdExposureScore": 1,
      "keywordAmazonsChoiceExposureScore": 1,
      "keywordRecommendExposureScore": 1,
      "keywordRecommendAdExposureScore": 1,
      "keywordRecommendNonadExposureScore": 1,
      "keywordComprehensiveNaturalExposureScore": 1,
      "ppcTrafficSources": [],
      "naturalSearchTrafficSources": [],
      "amazonRecommendationSources": [],
      "promotionalDealSources": []
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-summary.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-summary.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-summary.json)
- [Response fixture](../../examples/responses/amazon-keyword-summary.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_summary`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
