# Amazon ASIN Keywords API

Use Nexscope data to reverse-lookup traffic keywords for any Amazon ASIN, including organic ranking, ad ranking, search volume, traffic share, organic/paid scores, ABA TOP3 click concentration, click conversion rate, year-over-year search volume changes, and weekly/monthly time windows.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-asin-keywords?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Use Nexscope data to reverse-lookup traffic keywords for any Amazon ASIN, including organic ranking, ad ranking, search volume, traffic share, organic/paid scores, ABA TOP3 click concentration, click conversion rate, year-over-year search volume changes, and weekly/monthly time windows.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-asin-keywords/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | ASIN code, max length 1000 characters. This tool can only query one ASIN at a time | {} |
| `country` | string | No | Country site, default US. Options (13 total): US, UK, DE, CA, JP, FR, ES, IT, MX, AU, AE, BR, SA | {} |
| `keyword` | string | No | Keyword, max length 1000. Translate to the corresponding country's language whenever possible | {} |
| `timePieceType` | string | No | Time slice type, default latelyDay. Options: latelyDay (last N days), month (a specific month), week (a specific week) | {} |
| `timePieceValue` | string | No | Time slice value, default 7, max length 1000. For latelyDay only 7 or 30; for month format YYYY-MM (e.g. 2026-04); for week format week start date YYYY-MM-DD (e.g. 2026-04-13) | {} |
| `conditions` | string | No | Condition filters, comma-separated. Options:<br>Flag type: nfPosition (natural traffic keyword), isSpAd (SP ad keyword), isBrandAd (brand ad keyword), isVedioAd (video ad keyword), isAC (AC recommended keyword), isAccurateKw (precise traffic keyword), isAccurateTailKw (precise long-tail keyword), isPurchaseKw (converting keyword), isQualityKw (high-quality conversion keyword), isStableKw (stable conversion keyword), isLossKw (lost conversion keyword), isInvalidKw (invalid impression keyword), isMultiVariantKw (multi-variant natural rank keyword), isSearchVolUpKw (search volume YoY growth keyword), isSearchVolDownKw (search volume YoY decline keyword)<br>Period count type (.total all / .in new): totalPeriod.in, nfKeywordCnt.total, nfKeywordCnt.in, adKeywordCnt.total, adKeywordCnt.in, allSpKeywordCnt.total, allSpKeywordCnt.in, spKeywordCnt.total, spKeywordCnt.in, recSpKeywordCnt.total, recSpKeywordCnt.in, allSbKeywordCnt.total, allSbKeywordCnt.in, sbKeywordCnt.total, sbKeywordCnt.in, sbvKeywordCnt.total, sbvKeywordCnt.in | {} |
| `sortBy` | string | No | Sort field. Options: lastRank (natural rank), adLastRank (ad rank), updateTime (keyword crawl time), searchesRank (search rank), estSearchesNum (monthly search volume). Empty string means default system sort | {} |
| `desc` | boolean | No | Whether to sort descending, default true | {} |
| `pageNum` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Results per page, min 10, max 100, default 100 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-asin-keywords.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-asin-keywords request.json
# Or: node examples/javascript/run.mjs amazon-asin-keywords request.json
# Or: python3 examples/python/run.py amazon-asin-keywords request.json
```

### Published request example

```json
{
  "country": "US",
  "pageNum": 1,
  "desc": true,
  "pageSize": 10,
  "asin": "B072MQ5BRX"
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
      "keyword": "phone case",
      "translateKeyword": "phone case",
      "asin": "B072MQ5BRX",
      "productNaturalRank": 1,
      "productAdRank": 1,
      "weeklySearchVolume": 1,
      "keywordPopularityRank": 1,
      "totalSearchResultProductCount": 1,
      "trafficShare": 1,
      "naturalTrafficShare": 1,
      "paidTrafficShare": 1,
      "naturalTrafficScore": 1,
      "sponsoredProductsScore": 1,
      "brandAdScore": 1,
      "videoAdScore": 1,
      "sponsoredRecommendationScore": 1,
      "sponsoredRecommendationBreakdown": [],
      "clickConcentrationShare": 1,
      "clickToPurchaseConversionRate": 1,
      "displayPositionTypes": [],
      "trafficCharacteristicMarkers": [],
      "conversionPerformanceMarkers": [],
      "periodEndDate": "2026-01-01",
      "updateTime": "2026-01-01"
    }
  ],
  "columns": [],
  "isParentAsin": false,
  "hasVaiants": false,
  "abaCreateDateWeek": "2026-01-01",
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-asin-keywords.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-asin-keywords.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-asin-keywords.json)
- [Response fixture](../../examples/responses/amazon-asin-keywords.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_asin_keywords`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
