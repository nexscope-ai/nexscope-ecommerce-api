# Amazon Product History API

Retrieve Amazon product details by ASIN, including price, title, main image, listing date, material, weight, variant monthly sales, and up to 12 months of monthly sales history.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-history?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Retrieve Amazon product details by ASIN, including price, title, main image, listing date, material, weight, variant monthly sales, and up to 12 months of monthly sales history.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-history/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon Standard Identification Number (ASIN), multiple ASINs separated by English commas, up to 5, max length 300 characters. Example: B0088PUEPK or B0088PUEPK,B00U26V4VQ,B07M68S376 | {} |
| `domain` | string | Yes | Amazon domain ID. Options: 1 (United States), 2 (United Kingdom), 3 (Germany), 4 (France), 5 (Japan), 6 (Canada), 8 (Italy), 9 (Spain), 10 (India), 11 (Mexico), 12 (Brazil) | {} |
| `history` | integer | No | Whether to include historical data and historical sales in the response. 1 = include price history, sales rank, historical sales and other time-series data (sales for previous months), 0 = return only basic product information. Default: 0 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-history.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-history request.json
# Or: node examples/javascript/run.mjs amazon-product-history request.json
# Or: python3 examples/python/run.py amazon-product-history request.json
```

### Published request example

```json
{
  "asin": "B072MQ5BRX",
  "history": 1,
  "domain": "1"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "perPage": 1,
  "columns": [],
  "costToken": 1,
  "totalCount": 1,
  "currentPage": 1,
  "products": [
    {
      "asin": "B072MQ5BRX",
      "price": 1,
      "primePrice": 1,
      "rating": 1,
      "ratings": 1,
      "reviewCount": 1,
      "salesRank": 1,
      "salesRank30": 1,
      "salesRank90": 1,
      "salesRank180": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "monthlySalesUnits1MonthAgo": 1,
      "monthlySalesUnits2MonthsAgo": 1,
      "monthlySalesUnits3MonthsAgo": 1,
      "monthlySalesUnits4MonthsAgo": 1,
      "monthlySalesUnits5MonthsAgo": 1,
      "monthlySalesUnits6MonthsAgo": 1,
      "monthlySalesUnits7MonthsAgo": 1,
      "monthlySalesUnits8MonthsAgo": 1,
      "monthlySalesUnits9MonthsAgo": 1,
      "monthlySalesUnits10MonthsAgo": 1,
      "monthlySalesUnits11MonthsAgo": 1,
      "monthlySalesUnits12MonthsAgo": 1,
      "availableDate": "2026-01-01",
      "lastUpdate": "2026-01-01",
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "asinUrl": "B072MQ5BRX",
      "urlSlug": "https://example.com/image.jpg",
      "itemLength": 1,
      "itemWidth": 1,
      "itemHeight": 1,
      "packageLength": 1,
      "packageWidth": 1,
      "packageHeight": 1,
      "packageQuantity": 1,
      "fbaFees": 1,
      "referralFeePercentage": 1,
      "profit": 1,
      "buyBoxSellerId": "example-id",
      "sellerNum": 1,
      "variationNum": 1,
      "parentAsin": "B072MQ5BRX",
      "rootCategory": 1,
      "categoryTreeId": "example-id",
      "subcategories": [],
      "isAdultProduct": false,
      "isHazmat": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-history.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-history.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-history.json)
- [Response fixture](../../examples/responses/amazon-product-history.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_history`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
