# Amazon Market Statistics API

Use SellerSprite market statistics capability to output a market statistics dashboard by category node, including top listing average rating, average price, BSR, sales, seller count, and new product related metrics, suitable for quickly assessing the market quality and competitive landscape of a category.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-market-statistics?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use SellerSprite market statistics capability to output a market statistics dashboard by category node, including top listing average rating, average price, BSR, sales, seller count, and new product related metrics, suitable for quickly assessing the market quality and competitive landscape of a category.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-statistics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Site code, see [marketplace](#marketplace-options) | {} |
| `nodeIdPath` | string | Yes | Node ID path string, e.g. 1064954:1069242:1069784:1069820:1069838:1069828 | {} |
| `month` | string | No | Filter date: nearly or yyyyMM | {} |
| `topN` | integer | No | Top Listing count (used for top-related metric definitions) | {} |
| `newProduct` | integer | No | New product definition (months) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-market-statistics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-market-statistics request.json
# Or: node examples/javascript/run.mjs amazon-market-statistics request.json
# Or: python3 examples/python/run.py amazon-market-statistics request.json
```

### Published request example

```json
{
  "newProduct": 1,
  "topN": 1,
  "nodeIdPath": "1064954:1069242",
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
  "data": [],
  "columns": [],
  "costToken": 1,
  "totalProducts": 1,
  "products": 1,
  "sellers": 1,
  "brands": 1,
  "avgSellers": 1,
  "hlProducts": 1,
  "avgUnits": 1,
  "avgRevenue": 1,
  "avgPrice": 1,
  "avgRating": 1,
  "avgRatings": 1,
  "avgRatingsCv": 1,
  "avgBsr": 1,
  "avgProfit": 1,
  "avgWeight": 1,
  "baseAvgWeight": 1,
  "avgVolume": 1,
  "baseAvgVolume": 1,
  "hlAvgUnits": 1,
  "hlAvgRevenue": 1,
  "hlAvgPrice": 1,
  "hlAvgRating": 1,
  "hlAvgRatings": 1,
  "hlAvgRatingsCv": 1,
  "hlAvgBsr": 1,
  "newProducts": 1,
  "newProductProportion": 1,
  "newAvgUnits": 1,
  "newAvgRevenue": 1,
  "newAvgPrice": 1,
  "newAvgRating": 1,
  "newAvgRatings": 1,
  "minNewRatings": 1,
  "maxNewRatings": 1,
  "firstShelfDate": "2026-01-01",
  "lastShelfDate": "2026-01-01"
}
```

## Full definitions

- [Request definition](../../schemas/amazon-market-statistics.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-market-statistics.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-market-statistics.json)
- [Response fixture](../../examples/responses/amazon-market-statistics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_market_statistics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
