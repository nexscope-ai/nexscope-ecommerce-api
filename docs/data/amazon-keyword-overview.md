# Amazon Keyword Overview API

SIF overview analysis of Amazon keyword market competition.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-overview?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

SIF overview analysis of Amazon keyword market competition.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-overview/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword, translate to the corresponding country's language whenever possible. Max length: 1000 characters | {} |
| `country` | string | No | Country site, default US. Options (13 total): US, UK, DE, CA, JP, FR, ES, IT, MX, AU, AE, BR, SA | {} |
| `last7d` | boolean | No | Whether to get last 7 days data, default true. When false, use startDate/endDate range | {} |
| `startDate` | string | No | Start date yyyy-MM-dd (effective when last7d=false) | {} |
| `endDate` | string | No | End date yyyy-MM-dd (paired with startDate) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-overview.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-overview request.json
# Or: node examples/javascript/run.mjs amazon-keyword-overview request.json
# Or: python3 examples/python/run.py amazon-keyword-overview request.json
```

### Published request example

```json
{
  "last7d": true,
  "country": "US",
  "keyword": "phone case"
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
      "keywordPopularityRank": 1,
      "estimatedWeeklySearchVolume": 1,
      "supplyDemandRatio": 1,
      "totalSearchResultProductCount": 1,
      "naturalSearchProductCount": 1,
      "sponsoredProductsCount": 1,
      "brandAdProductCount": 1,
      "videoAdProductCount": 1,
      "paidAdvertisingProductCount": 1,
      "amazonChoiceProductCount": 1,
      "topRatedProductCount": 1,
      "searchRecommendationProductCount": 1,
      "editorialRecommendationsProductCount": 1,
      "recNonadProductCount": 1,
      "recAdProductCount": 1,
      "trackedAsinTotalCount": 1,
      "totalMarketplaceKeywordCount": 1,
      "dataPeriodStartDate": "2026-01-01",
      "dataPeriodEndDate": "2026-01-01",
      "keywordDataUpdateTime": "phone case"
    }
  ],
  "costTime": 1,
  "costToken": 1,
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-overview.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-overview.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-overview.json)
- [Response fixture](../../examples/responses/amazon-keyword-overview.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_overview`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
