# Amazon Search By Image API

Perform image-based visual product search on Amazon across 8 marketplaces. Use an image URL to find visually similar products, with optional Keepa enrichment for sales data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-search-by-image?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Perform image-based visual product search on Amazon across 8 marketplaces. Use an image URL to find visually similar products, with optional Keepa enrichment for sales data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-search-by-image/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Valid, publicly accessible image URL (maximum 1,000 characters) | {} |
| `amazonDomain` | string | Yes | Amazon marketplace. Supported domains: United States (amazon.com), United Kingdom (amazon.co.uk), Germany (amazon.de), France (amazon.fr), Italy (amazon.it), Spain (amazon.es), Japan (amazon.co.jp), and India (amazon.in). Default: amazon.com | {} |
| `sort` | string | No | Sort by price, rating, or rating count. Values: default, price-asc-rank, price-desc-rank, rating-asc-rank, rating-desc-rank, ratings-asc-rank, and ratings-desc-rank | {} |
| `deliveryZip` | string | No | Delivery postal code or city within the selected marketplace. If omitted, the marketplace default is used. Maximum 1,000 characters. Defaults: United States=10001, United Kingdom=EC1A 1BB, Germany=10115, France=75001, Italy=00100, Spain=28001, Japan=100-0001, and India=110034 | {} |
| `countryOrAreaCode` | string | No | Destination country or region code for cross-border delivery, such as CN, JP, KR, TW, HK, MO, SG, TH, VN, PH, or MY. Do not provide this together with deliveryZip. Amazon India does not support cross-border destination settings. Maximum 1,000 characters | {} |
| `aggregateByKeepaData` | boolean | No | Whether to enrich results with Keepa data such as sales rank, monthly sales, FBA fees, and dimensions | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-search-by-image.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-search-by-image request.json
# Or: node examples/javascript/run.mjs amazon-search-by-image request.json
# Or: python3 examples/python/run.py amazon-search-by-image request.json
```

### Published request example

```json
{
  "imageUrl": "https://m.media-amazon.com/images/I/31SkgVLWSuL._SL75_.jpg",
  "amazonDomain": "amazon.com",
  "aggregateByKeepaData": false
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "totalCount": 1,
  "perPage": 1,
  "currentPage": 1,
  "columns": [],
  "costToken": 1,
  "products": [],
  "asin": "B072MQ5BRX",
  "imageUrl": "https://example.com/image.jpg",
  "asinUrl": "B072MQ5BRX",
  "price": 1,
  "oldPrice": 1,
  "rating": 1,
  "ratings": 1,
  "salesRank": 1,
  "salesRank30": 1,
  "salesRank90": 1,
  "salesRank180": 1,
  "monthlySalesUnits": 1,
  "monthlySalesRevenue": 1,
  "monthlySalesUnits1MonthAgo~monthlySalesUnits12MonthsAgo": 1,
  "reviewCount": 1,
  "fbaFees": 1,
  "profit": 1,
  "referralFeePercentage": 1,
  "primePrice": 1,
  "buyBoxSellerId": "example-id",
  "sellerNum": 1,
  "variationNum": 1,
  "parentAsin": "B072MQ5BRX",
  "availableDate": "2026-01-01",
  "lastUpdate": "2026-01-01",
  "itemLength": 1,
  "itemWidth": 1,
  "itemHeight": 1,
  "packageLength": 1,
  "packageWidth": 1,
  "packageHeight": 1,
  "packageQuantity": 1,
  "categoryTreeId": "example-id",
  "rootCategory": 1,
  "isAdultProduct": false,
  "isHazmat": false,
  "urlSlug": "https://example.com/image.jpg",
  "productImageUrls": []
}
```

## Full definitions

- [Request definition](../../schemas/amazon-search-by-image.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-search-by-image.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-search-by-image.json)
- [Response fixture](../../examples/responses/amazon-search-by-image.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_search_by_image`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
