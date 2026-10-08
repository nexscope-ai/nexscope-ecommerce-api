# Amazon Keyword Share Of Voice API

Jungle Scout keyword Share of Voice analysis, returning brand visibility share across the first 3 pages of Amazon search results (organic/ad/combined), 30-day exact search volume, median PPC bid, and TOP3 ASIN click and conversion data, covering 10 marketplaces.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-keyword-share-of-voice?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Jungle Scout keyword Share of Voice analysis, returning brand visibility share across the first 3 pages of Amazon search results (organic/ad/combined), 30-day exact search volume, median PPC bid, and TOP3 ASIN click and conversion data, covering 10 marketplaces.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-keyword-share-of-voice/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Target marketplace code. Options: us, uk, de, in, ca, fr, it, es, mx, jp | {} |
| `keyword` | string | Yes | Keyword to query | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-keyword-share-of-voice.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-keyword-share-of-voice request.json
# Or: node examples/javascript/run.mjs amazon-keyword-share-of-voice request.json
# Or: python3 examples/python/run.py amazon-keyword-share-of-voice request.json
```

### Published request example

```json
{
  "keyword": "phone case",
  "marketplace": "us"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costToken": 1,
  "shareOfVoice": {},
  "id": "example-id",
  "estimated30DaySearchVolume": 1,
  "exactSuggestedBidMedian": 1,
  "productCount": 1,
  "updatedAt": "2026-01-01",
  "topAsinsModelStartDate": "B072MQ5BRX",
  "topAsinsModelEndDate": "B072MQ5BRX",
  "brands": [
    {
      "organicProducts": 1,
      "sponsoredProducts": 1,
      "combinedProducts": 1,
      "organicBasicSov": 1,
      "organicWeightedSov": 1,
      "sponsoredBasicSov": 1,
      "sponsoredWeightedSov": 1,
      "combinedBasicSov": 1,
      "combinedWeightedSov": 1,
      "organicAveragePosition": 1,
      "sponsoredAveragePosition": 1,
      "combinedAveragePosition": 1,
      "organicAveragePrice": 1,
      "sponsoredAveragePrice": 1,
      "combinedAveragePrice": 1
    }
  ],
  "topAsins": [
    {
      "asin": "B072MQ5BRX",
      "clicks": 1,
      "conversions": 1,
      "conversionRate": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-keyword-share-of-voice.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-keyword-share-of-voice.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-keyword-share-of-voice.json)
- [Response fixture](../../examples/responses/amazon-keyword-share-of-voice.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_keyword_share_of_voice`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
