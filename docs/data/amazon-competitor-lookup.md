# Amazon Competitor Lookup API

Use SellerSprite data to find and analyze competitors on Amazon, covering 12 marketplaces, with product metrics including sales, BSR, pricing, ratings, and growth trends.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-competitor-lookup?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use SellerSprite data to find and analyze competitors on Amazon, covering 12 marketplaces, with product metrics including sales, BSR, pricing, ratings, and growth trends.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-competitor-lookup/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | No | Amazon site code, default US. Options: US, UK, DE, FR, JP, CA, IT, ES, MX, AU, TR, IN | {} |
| `keyword` | string | No | Search keyword. Translate to the corresponding country's language whenever possible, e.g. use English keywords for the US, German keywords for Germany, etc. | {} |
| `asinList` | string | No | ASINs, multiple ASINs comma-separated, max 40. Format: ^[A-Z0-9]+(,[A-Z0-9]+){0,39}$ | {} |
| `sellerName` | string | No | Seller name filter | {} |
| `brand` | string | No | Brand name filter | {} |
| `nodeLabel` | string | No | Amazon category name, supports multi-level category names, levels separated by colon :, e.g. Electronics:Headphones | {} |
| `nodeIdPath` | string | No | Amazon category ID path | {} |
| `matchType` | integer | No | Match type. 1 = phrase match (default), 2 = fuzzy match, 3 = exact match | {} |
| `showVariation` | string | No | Whether to query variants. Y = yes, N = no (default) | {} |
| `dataSnapshotMonth` | string | No | Amazon product data snapshot month. Default nearly (queries last 30 days real-time data). Use yyyyMM format to query historical snapshots (e.g. 202412 for December 2024). Only supports existing historical snapshots, future dates are not supported. Recommended for seasonal analysis to query the same period last year's snapshot for comparison | {} |
| `page` | integer | No | Page number, starting from 1 (default 1) | {} |
| `size` | integer | No | Results per page, returns 10-100 records (default 50) | {} |
| `order` | object | No | Sort configuration (see below) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-competitor-lookup.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-competitor-lookup request.json
# Or: node examples/javascript/run.mjs amazon-competitor-lookup request.json
# Or: python3 examples/python/run.py amazon-competitor-lookup request.json
```

### Published request example

```json
{
  "page": 1,
  "asinList": "B072MQ5BRX",
  "matchType": 1,
  "size": 10,
  "marketplace": "US",
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "columns": [],
  "products": [
    {
      "asin": "B072MQ5BRX",
      "price": 1,
      "primePrice": 1,
      "averagePrice": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "monthlySalesUnitsGrowthRate": 1,
      "bsr": 1,
      "bsrGrowthRate": 1,
      "bsrGrowthCount": 1,
      "rating": 1,
      "ratings": 1,
      "ratingsGrowth": 1,
      "ratingsRate": 1,
      "brandUrl": "https://example.com/image.jpg",
      "sellerId": "example-id",
      "sellerNum": 1,
      "availableDate": "2026-01-01",
      "availableDateString": "2026-01-01",
      "profit": 1,
      "fba": 1,
      "deliveryPrice": 1,
      "imageUrl": "https://example.com/image.jpg",
      "variationNum": 1,
      "variant30DayUnits": 1,
      "variant30DayRevenue": 1,
      "variant30DayUpdatedAt": "2026-01-01",
      "amzUnitDateString": "2026-01-01",
      "listingQualityScore": 1,
      "nodeId": 1,
      "keyword": "phone case",
      "badge": {},
      "subcategories": []
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-competitor-lookup.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-competitor-lookup.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-competitor-lookup.json)
- [Response fixture](../../examples/responses/amazon-competitor-lookup.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_competitor_lookup`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
