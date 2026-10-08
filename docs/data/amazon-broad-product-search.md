# Amazon Broad Product Search API

Use SellerSprite data to search and filter Amazon products, supporting multi-dimensional criteria including price, monthly sales, BSR ranking, gross margin, ratings, fulfillment method, badges, seller origin, and more across multiple Amazon marketplaces.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-broad-product-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use SellerSprite data to search and filter Amazon products, supporting multi-dimensional criteria including price, monthly sales, BSR ranking, gross margin, ratings, fulfillment method, badges, seller origin, and more across multiple Amazon marketplaces.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-broad-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `chatId` | string | No | Chat ID, maxLength 1000 | {} |
| `uid` | string | No | User ID, maxLength 1000 | {} |
| `requestId` | string | No | Push ID, maxLength 1000 | {} |
| `teamId` | string | No | Team ID, maxLength 1000 | {} |
| `keyword` | string | No | Search keyword; translate to the corresponding country's language whenever possible, e.g. use English keywords for the US, German keywords for Germany, etc.; maxLength 10240 | {} |
| `matchType` | integer | No | Match type: 1 = phrase match (default), 2 = fuzzy match, 3 = exact match | {} |
| `excludeKeywords` | string | No | Exclude keywords; maxLength 10240 | {} |
| `marketplace` | string | No | Marketplace site code, default US. Only US, UK, DE, FR, JP, CA, IT, ES, MX, IN are allowed (must match this enum; AU, TR, and other unlisted sites are not supported) | {} |
| `nodeLabel` | string | No | Amazon category name; maxLength 1000 | {} |
| `nodeIdPath` | string | No | Amazon category node ID; maxLength 1000 | {} |
| `filterSubNode` | boolean | No | Whether to filter subcategory nodes; only effective when nodeLabel or nodeIdPath has a value; pass JSON boolean true / false | {} |
| `dataSnapshotMonth` | string | No | Product data snapshot month, format yyyyMM (e.g. 202412 for December 2024 data snapshot), or nearly for last 30 days real-time data. Default: nearly. Used for historical analysis and period comparison; only supports existing historical snapshots, future dates are not supported; maxLength 1000 | {} |
| `minPrice` | number | No | Minimum price (>= 0) | {} |
| `maxPrice` | number | No | Maximum price (>= 0) | {} |
| `minProfit` | number | No | Minimum gross margin, unit % (1-100) | {} |
| `maxProfit` | number | No | Maximum gross margin, unit % (1-100) | {} |
| `minRevenue` | number | No | Minimum monthly sales revenue (>= 0) | {} |
| `maxRevenue` | number | No | Maximum monthly sales revenue (>= 0) | {} |
| `minFba` | number | No | Minimum FBA shipping fee (>= 0) | {} |
| `maxFba` | number | No | Maximum FBA shipping fee (>= 0) | {} |
| `minUnits` | integer | No | Minimum monthly sales volume (>= 0) | {} |
| `maxUnits` | integer | No | Maximum monthly sales volume (>= 0) | {} |
| `minAmzUnit` | integer | No | Minimum variant last-30-day sales volume (only supported when dataSnapshotMonth is a "last 30 days" type query); minimum 0 | {} |
| `maxAmzUnit` | integer | No | Maximum variant last-30-day sales volume (only supported for last 30 days queries); minimum 0 | {} |
| `minUnitsGrowthRate` | number | No | Minimum monthly sales volume growth rate, unit % | {} |
| `maxUnitsGrowthRate` | number | No | Maximum monthly sales volume growth rate, unit % | {} |
| `minBsr` | integer | No | Lowest main category BSR rank | {} |
| `maxBsr` | integer | No | Highest main category BSR rank | {} |
| `minBsrGrowthRate` | number | No | Minimum BSR growth rate, unit % | {} |
| `maxBsrGrowthRate` | number | No | Maximum BSR growth rate, unit % | {} |
| `minBsrGrowthCount` | integer | No | Minimum BSR growth count | {} |
| `maxBsrGrowthCount` | integer | No | Maximum main category BSR growth count | {} |
| `minSubNodeBsrRank` | integer | No | Lowest subcategory BSR rank (requires filterSubNode = true) | {} |
| `maxSubNodeBsrRank` | integer | No | Highest subcategory BSR rank (requires filterSubNode = true) | {} |
| `minRating` | number | No | Minimum rating value (0-5) | {} |
| `maxRating` | number | No | Maximum rating value (0-5), 3.8-4.3 is the product improvement opportunity range | {} |
| `minRatings` | integer | No | Minimum review count (0-10000) | {} |
| `maxRatings` | integer | No | Maximum review count (0-10000) | {} |
| `minRatingsGrowthCount` | integer | No | Minimum monthly new review count (>= 0) | {} |
| `maxRatingsGrowthCount` | integer | No | Maximum monthly new review count (>= 0) | {} |
| `minListingQualityScore` | number | No | Minimum Listing page quality score (>= 0) | {} |
| `maxListingQualityScore` | number | No | Maximum Listing page quality score (>= 0) | {} |
| `minVariations` | integer | No | Minimum number of variations | {} |
| `maxVariations` | integer | No | Maximum number of variations | {} |
| `minWeights` | number | No | Minimum weight (>= 0) | {} |
| `maxWeights` | number | No | Maximum weight (>= 0) | {} |
| `weightUnit` | string | No | Weight unit: g, kg, oz, lb. This field must be specified if the parameters include weight filtering | {} |
| `dimensionType` | string | No | Package dimension type (codes vary by site, see below) | {} |
| `minSellers` | integer | No | Minimum number of sellers | {} |
| `maxSellers` | integer | No | Maximum number of sellers | {} |
| `badgeBestSeller` | string | No | Best Seller badge filter: Y, N, or empty (all) | {} |
| `badgeAmazonsChoice` | string | No | Amazon's Choice badge filter: Y, N, or empty (all) | {} |
| `badgeNewRelease` | string | No | New Release badge filter: Y, N, or empty (all) | {} |
| `fulfillment` | string | No | Fulfillment method: single select AMZ / FBA / FBM, or multi-select such as AMZ,FBA, FBA,FBM, AMZ,FBA,FBM, etc.; multiple conditions use comma separation; empty means no limit | {} |
| `showVariation` | string | No | Whether to query variants: Y or N, default N | {} |
| `hideUnlistedProduct` | boolean | No | Whether to hide delisted products, default true | {} |
| `listedWithinLastMonths` | integer | No | Time since listing (months), only allowed: 1, 3, 6, 12, 24 (must match these enum values; do not pass other integers) | {} |
| `sellerNation` | string | No | Seller location code (e.g. US, CN, HK), multiple conditions comma-separated, default no limit | {} |
| `includeSellers` | string | No | Include sellers; maxLength 10240 | {} |
| `excludeSellers` | string | No | Exclude sellers; maxLength 10240 | {} |
| `includeBrands` | string | No | Include brands; maxLength 10240 | {} |
| `excludeBrands` | string | No | Exclude brands; maxLength 10240 | {} |
| `order` | object | No | Sort configuration; if passed, it is recommended to provide both field and desc (both are required in the sub-schema) | {} |
| `order.field` | string | No | Sort field: total_units (monthly sales), total_amount (monthly revenue), bsr_rank, price, rating, reviews, profit, reviews_rate, available_date, questions, total_units_growth, total_amount_growth, reviews_increasement, bsr_rank_cv, bsr_rank_cr, amz_unit (variant sales). Default total_units. Pass an empty string "" to not sort by the above business fields (full query sort semantics are handled by the server) | {} |
| `order.desc` | string | No | "true" descending, "false" ascending; default "true"; maxLength 1000 | {} |
| `page` | integer | No | Page number, starting from 1, default 1 | {} |
| `size` | integer | No | Results per page (10-100), default 20 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-broad-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-broad-product-search request.json
# Or: node examples/javascript/run.mjs amazon-broad-product-search request.json
# Or: python3 examples/python/run.py amazon-broad-product-search request.json
```

### Published request example

```json
{
  "marketplace": "US",
  "page": 1,
  "size": 20,
  "keyword": "phone case",
  "matchType": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "products": [
    {
      "asin": "B072MQ5BRX",
      "asinUrl": "B072MQ5BRX",
      "imageUrl": "https://example.com/image.jpg",
      "price": 1,
      "averagePrice": 1,
      "primePrice": 1,
      "monthlySalesUnits": 1,
      "monthlySalesRevenue": 1,
      "monthlySalesUnitsGrowthRate": 1,
      "bsr": 1,
      "bsrGrowthRate": 1,
      "rating": 1,
      "ratings": 1,
      "ratingsRate": 1,
      "profit": 1,
      "fba": 1,
      "sellerNum": 1,
      "sellerId": "example-id",
      "brandUrl": "https://example.com/image.jpg",
      "availableDate": "2026-01-01",
      "availableDateString": "2026-01-01",
      "variationNum": 1,
      "variant30DayUnits": 1,
      "variant30DayRevenue": 1,
      "variant30DayUpdatedAt": "2026-01-01",
      "listingQualityScore": 1,
      "deliveryPrice": 1,
      "nodeId": 1,
      "badge": {},
      "subcategories": [],
      "keyword": "phone case"
    }
  ],
  "columns": [],
  "keyword": "phone case",
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-broad-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-broad-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-broad-product-search.json)
- [Response fixture](../../examples/responses/amazon-broad-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_broad_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
