# Amazon Product Database Search API

Advanced Amazon product search and filtering powered by Keepa data, supporting multi-dimensional criteria including category, price, monthly sales, keywords, BSR rank, review count, rating, package dimensions, weight, fulfillment type, and more.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-database-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Advanced Amazon product search and filtering powered by Keepa data, supporting multi-dimensional criteria including category, price, monthly sales, keywords, BSR rank, review count, rating, package dimensions, weight, fulfillment type, and more.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-database-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `domain` | string | Yes | Amazon domain ID: 1=United States, 2=United Kingdom, 3=Germany, 4=France, 5=Japan, 6=Canada, 8=Italy, 9=Spain, 10=India, 11=Mexico | {} |
| `keyword` | string | No | Title keyword (case-insensitive; spaces mean AND tokenization; wrap keywords containing spaces in double quotes; prefix - for exclusion; & symbol is replaced with space; up to 50 keywords, max 1000 characters) | {} |
| `rootCategory` | array | No | Root category IDs (up to 50), only include products in these root categories | {} |
| `rootCategoryNames` | array | No | Root category names (up to 50), used when rootCategory is empty; the system automatically looks up corresponding category IDs | {} |
| `categoriesInclude` | array | No | Subcategory IDs to include only (up to 50), only include products directly listed in these subcategories | {} |
| `categoriesIncludeNames` | array | No | Subcategory names to include (up to 50), used when categoriesInclude is empty; the system automatically looks up corresponding category IDs. Supports full category paths (separated by : or >) for more accurate results | {} |
| `categoriesExclude` | array | No | Subcategory IDs to exclude (up to 50) | {} |
| `categoriesExcludeNames` | array | No | Subcategory names to exclude (up to 50), used when categoriesExclude is empty; the system automatically looks up corresponding category IDs. Supports full category paths for more accurate results | {} |
| `currentSalesGte/currentSalesLte` | integer | No | Current sales rank range (lower value = better ranking) | {} |
| `avg90SalesGte/avg90SalesLte` | integer | No | 90-day average sales rank range | {} |
| `deltaPercent90SalesGte/deltaPercent90SalesLte` | integer | No | 90-day sales rank change percentage range | {} |
| `monthlySoldGte/monthlySoldLte` | integer | No | Units sold / monthly sales range | {} |
| `srAvgGte/srAvgLte` | integer | No | Historical sales rank range (positive integer, lower value = better ranking, used for the month specified by srAvgMonth) | {} |
| `srAvgMonth` | string | No | Historical sales rank - selected month (format: YYYYMM, e.g., 202511 for November 2025, within the last 36 months) | {} |
| `currentNewGte/currentNewLte` | integer | No | Current new price range (in minor currency unit) | {} |
| `currentBuyBoxShippingGte/currentBuyBoxShippingLte` | integer | No | Current Buy Box price with shipping range (in minor currency unit) | {} |
| `currentCountReviewsGte/currentCountReviewsLte` | integer | No | Current review count range | {} |
| `currentRatingGte/currentRatingLte` | number | No | Current rating range (0.0-5.0) | {} |
| `packageLengthGte/packageLengthLte` | integer | No | Package length range (mm) | {} |
| `packageWidthGte/packageWidthLte` | integer | No | Package width range (mm) | {} |
| `packageHeightGte/packageHeightLte` | integer | No | Package height range (mm) | {} |
| `packageWeightGte/packageWeightLte` | integer | No | Package weight range (grams) | {} |
| `brand` | array | No | Brand (OR match) | {} |
| `color` | array | No | Color (OR match), filter products with specified colors | {} |
| `size` | array | No | Size (OR match), filter products with specified sizes | {} |
| `availableDateGte/availableDateLte` | string | No | Product listing time range (date format: yyyy-MM-dd) | {} |
| `buyBoxIsAmazon` | boolean | No | Whether the Buy Box seller is Amazon | {} |
| `buyBoxIsFBA` | boolean | No | Whether the Buy Box is FBA | {} |
| `isHazMat` | boolean | No | Whether it is hazardous material | {} |
| `variationCountGte/variationCountLte` | integer | No | Variation count range | {} |
| `currentCountNewGte/currentCountNewLte` | integer | No | Current new offer count range | {} |
| `outOfStockPercentage90Gte/outOfStockPercentage90Lte` | integer | No | 90-day out-of-stock percentage range | {} |
| `singleVariation` | boolean | No | Return only one variation; when set to true, multi-variation products will only return one variation | {} |
| `productType` | array | No | Product type filter (default [0,1,2]): 0=standard product, 1=downloadable product, 2=eBook, 5=variant parent ASIN | {} |
| `history` | integer | No | Whether to include historical data / historical sales in the response (1=include, 0=exclude, default 0) | {} |
| `rating` | integer | No | Whether to fetch rating info (1=fetch, 0=do not fetch, default 1) | {} |
| `page` | integer | No | Page number (starting from 1, default 1) | {} |
| `perPage` | integer | No | Maximum results per page (min 50, max 100, default 50) | {} |
| `sort` | array | No | Sort (up to 3): array of objects, each containing {"fieldName": "...", "sortDirection": "asc\ | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-database-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-database-search request.json
# Or: node examples/javascript/run.mjs amazon-product-database-search request.json
# Or: python3 examples/python/run.py amazon-product-database-search request.json
```

### Published request example

```json
{
  "page": 1,
  "keyword": "phone case",
  "domain": "1",
  "perPage": 50
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "perPage": 1,
  "currentPage": 1,
  "totalCount": 1,
  "columns": [],
  "costToken": 1,
  "products": [
    {
      "asin": "B072MQ5BRX",
      "price": 1,
      "primePrice": 1,
      "salesRank": 1,
      "salesRank30": 1,
      "salesRank90": 1,
      "salesRank180": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "rating": 1,
      "ratings": 1,
      "reviewCount": 1,
      "availableDate": "2026-01-01",
      "lastUpdate": "2026-01-01",
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "asinUrl": "B072MQ5BRX",
      "categoryTreeId": "example-id",
      "rootCategory": 1,
      "subcategories": [],
      "buyBoxSellerId": "example-id",
      "sellerNum": 1,
      "parentAsin": "B072MQ5BRX",
      "variationNum": 1,
      "packageLength": 1,
      "packageWidth": 1,
      "packageHeight": 1,
      "packageQuantity": 1,
      "itemLength": 1,
      "itemWidth": 1,
      "itemHeight": 1,
      "isAdultProduct": false,
      "isHazmat": false,
      "referralFeePercentage": 1,
      "fbaFees": 1,
      "profit": 1,
      "urlSlug": "https://example.com/image.jpg"
    }
  ],
  "monthlySalesUnits1MonthAgo": {
    "": {
      "monthlySalesUnits12MonthsAgo": 1
    }
  }
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-database-search.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-database-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-database-search.json)
- [Response fixture](../../examples/responses/amazon-product-database-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_database_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
