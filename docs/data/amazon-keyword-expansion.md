# Amazon Keyword Expansion API

Jungle Scout keyword expansion tool that expands a seed keyword into a list of related keywords with search volume, trends, PPC bids, ranking difficulty, and other metrics, covering 10 Amazon marketplaces including US, UK, DE, JP, etc.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-expansion?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Jungle Scout keyword expansion tool that expands a seed keyword into a list of related keywords with search volume, trends, PPC bids, ranking difficulty, and other metrics, covering 10 Amazon marketplaces including US, UK, DE, JP, etc.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-expansion/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Target marketplace code. Options: us, uk, de, in, ca, fr, it, es, mx, jp. Default us | {} |
| `searchTerms` | string | Yes | Seed keyword (single keyword string) | {} |
| `needCount` | integer | No | Total number of results returned | {} |
| `sort` | string | No | Sort field, default -monthly_search_volume_exact (exact search volume descending) | {} |
| `minMonthlySearchVolumeExact` | integer | No | Minimum exact search volume | {} |
| `maxMonthlySearchVolumeExact` | integer | No | Maximum exact search volume | {} |
| `minMonthlySearchVolumeBroad` | integer | No | Minimum broad search volume | {} |
| `maxMonthlySearchVolumeBroad` | integer | No | Maximum broad search volume | {} |
| `minWordCount` | integer | No | Minimum word count for keywords (for filtering long-tail keywords) | {} |
| `maxWordCount` | integer | No | Maximum word count for keywords | {} |
| `minOrganicProductCount` | integer | No | Minimum organic product count | {} |
| `maxOrganicProductCount` | integer | No | Maximum organic product count | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-expansion.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-expansion request.json
# Or: node examples/javascript/run.mjs amazon-keyword-expansion request.json
# Or: python3 examples/python/run.py amazon-keyword-expansion request.json
```

### Published request example

```json
{
  "marketplace": "us",
  "searchTerms": "phone case",
  "needCount": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costToken": 1,
  "keywordInfoList": [
    {
      "monthlySearchVolumeExact": 1,
      "monthlySearchVolumeBroad": 1,
      "monthlyTrend": 1,
      "quarterlyTrend": 1,
      "relevancyScore": 1,
      "easeOfRankingScore": 1,
      "organicProductCount": 1,
      "sponsoredProductCount": 1,
      "ppcBidExact": 1,
      "ppcBidBroad": 1,
      "spBrandAdBid": 1,
      "recommendedPromotions": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-expansion.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-expansion.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-expansion.json)
- [Response fixture](../../examples/responses/amazon-keyword-expansion.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_expansion`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
