# Ozon Market Keyword Search API

Nexscope Ozon market hot keyword search: filters Ozon (and Wildberries) market keywords by multi-dimensional metrics including search volume, growth, product count, seller count, competitor count, price, sales, conversion concentration, etc. Each keyword carries monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products, and market profile. Use for Ozon keyword selection, blue-ocean keyword mining, and market opportunity analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-market-keyword-search?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Nexscope Ozon market hot keyword search: filters Ozon (and Wildberries) market keywords by multi-dimensional metrics including search volume, growth, product count, seller count, competitor count, price, sales, conversion concentration, etc. Each keyword carries monthly search volume, growth, market space, competitor/seller counts, average price, cart-add conversion, top products, and market profile. Use for Ozon keyword selection, blue-ocean keyword mining, and market opportunity analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-market-keyword-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `page` | object | Yes | Pagination & sorting: {page, pageSize, orders[]} | {} |
| `page.page` | integer | No | Page number, starting from 1, default 1 | {} |
| `page.pageSize` | integer | No | Items per page, default 20 | {} |
| `page.orders` | array | No | Sort rules, elements {field, direction}; direction takes DESC (descending) / ASC (ascending) | {} |
| `keywords` | array | No | Keyword array (max 1000), used with matchType | {} |
| `matchType` | integer | No | Keyword match mode: 0 exact, 1 fuzzy | {} |
| `searchDate` | string | No | Query date yyyy-MM-dd (e.g., 2026-04-01); defaults to last 30 days if omitted; passing 2026-04-01 queries March 2026 data | {} |
| `categories` | array | No | Category ID array (max 1000) | {} |
| `searchVolume` | object | No | Search volume range {min,max} | {} |
| `searchChange30` | object | No | 30-day search change range {min,max} | {} |
| `monthlySales` | object | No | Monthly sales range {min,max} | {} |
| `monthlyRevenue` | object | No | Monthly revenue range {min,max} | {} |
| `price` | object | No | Price range {min,max} | {} |
| `productViews` | object | No | Product views range {min,max} | {} |
| `products` | object | No | Product count range {min,max} | {} |
| `volume` | object | No | Volume range {min,max} | {} |
| `marketSpace` | object | No | Market space range {min,max} | {} |
| `conversionSharing` | object | No | Conversion concentration range {min,max} | {} |
| `reviews` | object | No | Review count range {min,max} | {} |
| `ratings` | object | No | Rating range {min,max} | {} |
| `sellers` | object | No | Seller count range {min,max} | {} |
| `weight` | object | No | Weight range {min,max} | {} |
| `uId` | string | No | User ID | {} |
| `memberId` | string | No | Member ID (a unique member identifier; data is attributed to memberId) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-market-keyword-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-market-keyword-search request.json
# Or: node examples/javascript/run.mjs ozon-market-keyword-search request.json
# Or: python3 examples/python/run.py ozon-market-keyword-search request.json
```

### Published request example

```json
{
  "page": {
    "page": 1,
    "pageSize": 10,
    "orders": [
      {
        "field": "searchVolume",
        "direction": "DESC"
      }
    ]
  }
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
      "categories": [],
      "categoryInfos": [
        {
          "id": "example-id",
          "crossBorderSellable": false
        }
      ],
      "products": [
        {
          "ozonId": 1,
          "sku": 1,
          "imageUrl": "https://example.com/image.jpg",
          "advert": 1
        }
      ],
      "id": "example-id"
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-market-keyword-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-market-keyword-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-market-keyword-search.json)
- [Response fixture](../../examples/responses/ozon-market-keyword-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_market_keyword_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
