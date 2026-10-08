# Amazon Traffic Keywords API

Query traffic keyword lists for an Amazon ASIN via SellerSprite, including traffic source type, conversion type, organic rank, and ad rank with historical month and multi-dimensional sorting.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-traffic-keywords?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Query traffic keyword lists for an Amazon ASIN via SellerSprite, including traffic source type, conversion type, organic rank, and ad rank with historical month and multi-dimensional sorting.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-traffic-keywords/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Marketplace site, default US | {} |
| `asin` | string | Yes | Product ASIN to reverse lookup | {} |
| `month` | string | No | 20)\d{2}(0[1-9] | {} |
| `page` | integer | No | Current page | {} |
| `size` | integer | No | Items per page | {} |
| `keyword` | string | No | Keyword filter | {} |
| `badges` | string | No | Traffic keyword type (impression position), see [Badges Enum](#badges-enum) | {} |
| `trafficKeywordTypes` | string | No | Traffic share type, see [trafficKeywordTypes Enum](#traffickeywordtypes-enum) | {} |
| `conversionKeywordTypes` | string | No | Traffic conversion type, see [conversionKeywordTypes Enum](#conversionkeywordtypes-enum) | {} |
| `orderField` | string | No | Sort field, see [orderField Options](#orderfield-options) | {} |
| `orderDesc` | boolean | No | Whether to sort in descending order | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-traffic-keywords.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-traffic-keywords request.json
# Or: node examples/javascript/run.mjs amazon-traffic-keywords request.json
# Or: python3 examples/python/run.py amazon-traffic-keywords request.json
```

### Published request example

```json
{
  "asin": "B072MQ5BRX",
  "page": 1,
  "size": 10,
  "marketplace": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "marketplace": "US",
  "asin": "B072MQ5BRX",
  "data": [
    {
      "keyword": "phone case",
      "keywordCn": "phone case",
      "trafficKeywordType": "phone case",
      "conversionKeywordType": "phone case",
      "badges": [],
      "rankPosition": {},
      "adPosition": {},
      "searches": 1,
      "searchesRank": 1,
      "searchesRankTimeFrom": 1,
      "searchesRankTimeTo": 1,
      "purchases": 1,
      "purchaseRate": 1,
      "products": 1,
      "supplyDemandRatio": 1,
      "trafficPercentage": 1,
      "naturalRatio": 1,
      "adRatio": 1,
      "calculatedWeeklySearches": 1,
      "impressions": 1,
      "clicks": 1,
      "bid": 1,
      "bidMin": 1,
      "bidMax": 1,
      "latest1daysAds": 1,
      "latest7daysAds": 1,
      "latest30daysAds": 1,
      "sprt": 1,
      "monopolyClickRate": 1,
      "top3ClickingRate": 1,
      "top3ConversionRate": 1,
      "titleDensity": 1,
      "stats": [],
      "updatedTime": 1
    }
  ],
  "summaryList": [
    {
      "total": 1,
      "keywords": "phone case"
    }
  ],
  "columns": [
    {
      "updatedTime": 1,
      "pageSize": 1,
      "index": 1,
      "page": 1,
      "position": 1
    }
  ],
  "costToken": 1,
  "stats": [
    {
      "keywords": "phone case",
      "total": 1,
      "rankPosition": {},
      "adPosition": {}
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-traffic-keywords.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-traffic-keywords.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-traffic-keywords.json)
- [Response fixture](../../examples/responses/amazon-traffic-keywords.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_traffic_keywords`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
