# Amazon Market Research API

Use Nexscope market list capability to filter Amazon niche markets by category dimensions, supporting market size, competition, top concentration, seller structure, new product share, price/rating/margin ranges, and many other criteria for discovering viable markets and evaluating product selection directions.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-market-research?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use Nexscope market list capability to filter Amazon niche markets by category dimensions, supporting market size, competition, top concentration, seller structure, new product share, price/rating/margin ranges, and many other criteria for discovering viable markets and evaluating product selection directions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-market-research/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Site code, see [marketplace](#marketplace-options) | {} |
| `nodeIdPath` | string | No | Category node ID path, e.g. 172282:281407 | {} |
| `departmentKeyword` | string | No | Category keyword path, e.g. Electronics:Accessories & Supplies | {} |
| `sellerLocation` | string | No | Seller location, multiple values comma-separated; see Nexscope table 1.3 for values | {} |
| `newProduct` | integer | No | New product definition (months) | {} |
| `topNum` | integer | No | Top Listing count | {} |
| `month` | string | No | Filter date: nearly or yyyyMM | {} |
| `page` | integer | No | Page number, starting from 1 | {} |
| `size` | integer | No | Results per page | {} |
| `orderField` | string | No | Sort field, see [orderField](#orderfield-options) | {} |
| `orderDesc` | boolean | No | true descending, false ascending | {} |
| `minAvgRevenue/maxAvgRevenue` | number | No | Minimum / maximum average monthly sales revenue | {} |
| `minAvgUnits/maxAvgUnits` | integer | No | Minimum / maximum average monthly sales volume | {} |
| `minGoodsCount/maxGoodsCount` | integer | No | Minimum / maximum product count | {} |
| `minSellers/maxSellers` | integer | No | Minimum / maximum seller count | {} |
| `minBrands/maxBrands` | integer | No | Minimum / maximum brand count | {} |
| `minAvgSellers/maxAvgSellers` | number | No | Minimum / maximum average seller count | {} |
| `minGoodsCrn/maxGoodsCrn` | number | No | Minimum / maximum product concentration (decimal 0-1) | {} |
| `minSellerCrn/maxSellerCrn` | number | No | Minimum / maximum seller concentration (decimal 0-1) | {} |
| `minBrandCrn/maxBrandCrn` | number | No | Minimum / maximum brand concentration (decimal 0-1) | {} |
| `minAmazonSelfProportion/maxAmazonSelfProportion` | number | No | Minimum / maximum Amazon self-operated share (decimal 0-1) | {} |
| `minFbaProportion/maxFbaProportion` | number | No | Minimum / maximum FBA share (decimal 0-1) | {} |
| `minFbmProportion/maxFbmProportion` | number | No | Minimum / maximum FBM share (decimal 0-1) | {} |
| `minEbcProportion/maxEbcProportion` | number | No | Minimum / maximum A+ share (decimal 0-1) | {} |
| `minNewProportion/maxNewProportion` | number | No | Minimum / maximum new product share (scale may differ from other ratio fields; refer to tool schema / actual network behavior) | {} |
| `minAvgPrice/maxAvgPrice` | number | No | Minimum / maximum average price | {} |
| `minAvgRating/maxAvgRating` | number | No | Minimum / maximum average rating value | {} |
| `minAvgRatings/maxAvgRatings` | integer | No | Minimum / maximum average review count | {} |
| `minAvgProfit/maxAvgProfit` | number | No | Minimum / maximum average gross margin (input N means N%, 0-100) | {} |
| `minAvgBsr/maxAvgBsr` | integer | No | Minimum / maximum average BSR rank | {} |
| `minNewCount/maxNewCount` | integer | No | Minimum / maximum new product count | {} |
| `minNewAvgPrice/maxNewAvgPrice` | number | No | Minimum / maximum new product average price | {} |
| `minNewAvgRating/maxNewAvgRating` | number | No | Minimum / maximum new product average star rating | {} |
| `minNewAvgRatings/maxNewAvgRatings` | integer | No | Minimum / maximum new product average review count | {} |
| `minNewAvgUnits/maxNewAvgUnits` | number | No | Minimum / maximum new product average monthly sales | {} |
| `minNewAvgRevenue/maxNewAvgRevenue` | number | No | Minimum / maximum new product average monthly revenue | {} |
| `minTopAvgUnits/maxTopAvgUnits` | integer | No | Minimum / maximum top listing average monthly sales | {} |
| `minTopAvgRevenue/maxTopAvgRevenue` | number | No | Minimum / maximum top listing average monthly revenue | {} |
| `minTopAvgBsr/maxTopAvgBsr` | integer | No | Minimum / maximum top listing average BSR | {} |
| `minWeight/maxWeight` | number | No | Minimum / maximum weight | {} |
| `minVolume/maxVolume` | number | No | Minimum / maximum volume | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-market-research.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-market-research request.json
# Or: node examples/javascript/run.mjs amazon-market-research request.json
# Or: python3 examples/python/run.py amazon-market-research request.json
```

### Published request example

```json
{
  "page": 1,
  "departmentKeyword": "phone case",
  "newProduct": 1,
  "size": 1,
  "marketplace": "US",
  "topNum": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "marketplace": "US",
  "data": [
    {
      "nodeId": "example-id",
      "marketplace": "US",
      "ranking": 1,
      "totalProducts": 1,
      "topProducts": 1,
      "sellers": 1,
      "brands": 1,
      "avgSellers": 1,
      "avgUnits": 1,
      "totalUnits": 1,
      "avgRevenue": 1,
      "totalRevenue": 1,
      "avgPrice": 1,
      "avgRating": 1,
      "avgRatings": 1,
      "avgBsr": 1,
      "avgProfit": 1,
      "fbaProportion": 1,
      "fbmProportion": 1,
      "amazonSelfProportion": 1,
      "ebcProportion": 1,
      "returnRatio": 1,
      "avgReturnRatio": 1,
      "searchToPurchaseRatio": 1,
      "sellerProportion": 1,
      "avgWeight": 1,
      "baseAvgWeight": 1,
      "avgVolume": 1,
      "baseAvgVolume": 1,
      "top10Images": []
    }
  ],
  "columns": [],
  "costToken": 1,
  "top10images": [
    {
      "image": "https://example.com/image.jpg",
      "asin": "B072MQ5BRX"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-market-research.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-market-research.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-market-research.json)
- [Response fixture](../../examples/responses/amazon-market-research.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_market_research`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
