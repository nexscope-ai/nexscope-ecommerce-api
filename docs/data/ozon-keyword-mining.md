# Ozon Keyword Mining API

Seerfar Ozon keyword mining: mines Ozon (and Wildberries) related keywords around a seed keyword with multi-dimensional filtering by search volume, growth, product count, seller count, competitor count, price, relevancy, title density, cart-add conversion, etc. Each mined keyword carries a full market profile (monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products). Use for Ozon keyword expansion, long-tail keyword mining, and seed keyword opportunity analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-keyword-mining?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Seerfar Ozon keyword mining: mines Ozon (and Wildberries) related keywords around a seed keyword with multi-dimensional filtering by search volume, growth, product count, seller count, competitor count, price, relevancy, title density, cart-add conversion, etc. Each mined keyword carries a full market profile (monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products). Use for Ozon keyword expansion, long-tail keyword mining, and seed keyword opportunity analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-keyword-mining/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Seed keyword, mining expands around this term (maxLength 1000) | {} |
| `page` | object | Yes | Pagination & sorting: {page, pageSize, orders[]} | {} |
| `page.page` | integer | No | Page number, starting from 1, default 1 | {} |
| `page.pageSize` | integer | No | Items per page, default 20 | {} |
| `page.orders` | array | No | Sort rules, elements {field, direction}; direction takes DESC (descending) / ASC (ascending) | {} |
| `matchType` | integer | No | Keyword match mode: 0 exact, 1 fuzzy | {} |
| `includeKeywords` | array | No | Include keyword array (max 1000), used to further narrow down / specify required words on top of the seed term | {} |
| `excludeKeywords` | array | No | Exclude keyword array (max 1000), used to remove irrelevant terms | {} |
| `wordCount` | string | No | Keyword word count range | {} |
| `searchVolume` | string | No | Search volume range | {} |
| `searchChange30` | string | No | 30-day search change range | {} |
| `productViews` | string | No | Product views range | {} |
| `products` | string | No | Product count range | {} |
| `sellers` | string | No | Seller count range | {} |
| `price` | string | No | Price range | {} |
| `marketSpace` | string | No | Market space range | {} |
| `conversionSharing` | string | No | Conversion concentration range | {} |
| `relevancy` | string | No | Relevance range (degree of relevance to the seed keyword) | {} |
| `uniqQueriesWCa` | string | No | Add-to-cart count range | {} |
| `ca` | string | No | Add-to-cart conversion rate range | {} |
| `titleDensity` | string | No | Title density range | {} |
| `adRivalCount` | string | No | Ad competitor count range | {} |
| `uId` | string | No | User ID | {} |
| `memberId` | string | No | Member ID (a unique member identifier; data is attributed to memberId) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-keyword-mining.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-keyword-mining request.json
# Or: node examples/javascript/run.mjs ozon-keyword-mining request.json
# Or: python3 examples/python/run.py ozon-keyword-mining request.json
```

### Published request example

```json
{
  "includeKeywords": [],
  "page": {
    "pageSize": 10,
    "page": 1
  },
  "uId": "example-id",
  "matchType": 1,
  "excludeKeywords": [],
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "total": 1,
  "data": [
    {
      "query": "phone case",
      "queryCn": "phone case",
      "platform": 1,
      "searchVolume": 1,
      "count30GrowthRate": 1,
      "productCount": 1,
      "competingProducts": 1,
      "sellers": 1,
      "avgPrice": 1,
      "itemsViews": 1,
      "viewSharing": 1,
      "conversionSharing": 1,
      "marketSpace": 1,
      "returnCancellationRate": 1,
      "uniqQueriesWCa": 1,
      "ca": 1,
      "relevancy": 1,
      "titleDensity": 1,
      "wordCount": 1,
      "categories": [],
      "categoryInfos": [],
      "products": [],
      "id": "example-id"
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1,
  "products": [
    {
      "ozonId": 1,
      "sku": 1,
      "imageUrl": "https://example.com/image.jpg",
      "advert": 1
    }
  ],
  "categoryinfos": [
    {
      "id": "example-id",
      "crossBorderSellable": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/ozon-keyword-mining.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-keyword-mining.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-keyword-mining.json)
- [Response fixture](../../examples/responses/ozon-keyword-mining.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_keyword_mining`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
