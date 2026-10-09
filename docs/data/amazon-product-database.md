# Amazon Product Database API

Nexscope Product Database multi-condition filtering. Filter Amazon products by category, price, sales volume, revenue, reviews, rating, weight, BSR rank, LQS, seller type, and more across 10 marketplaces.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-database?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Nexscope Product Database multi-condition filtering. Filter Amazon products by category, price, sales volume, revenue, reviews, rating, weight, BSR rank, LQS, seller type, and more across 10 marketplaces.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-database/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Target marketplace code. Options: us, uk, de, in, ca, fr, it, es, mx, jp | {} |
| `includeKeywords` | string | No | Keywords to include in title/ASIN, comma-separated, up to 100 items, max 50 chars each | {} |
| `excludeKeywords` | string | No | Keywords to exclude from title/ASIN, comma-separated, up to 100 items, max 50 chars each | {} |
| `categories` | string | No | Primary category names, comma-separated, must match the standard category names for the corresponding site. US site examples: Appliances, Arts Crafts & Sewing, Automotive, Baby, Beauty & Personal Care, Books, CDs & Vinyl, Cell Phones & Accessories, Clothing Shoes & Jewelry, Collectibles & Fine Art, Computers, Digital Music, Electronics, Garden & Outdoor, Grocery & Gourmet Food, Handmade, Health Household & Baby Care, Home & Kitchen, Industrial & Scientific, Kindle Store, Kitchen & Dining, Movies & TV, Musical Instruments, Office Products, Pet Supplies, Sports & Outdoors, Tools & Home Improvement, Toys & Games, Video Games, etc. Other sites (uk, de, fr, it, es, mx, jp, ca, in) have their own localized category names | {} |
| `minPrice` | number | No | Minimum price | {} |
| `maxPrice` | number | No | Maximum price | {} |
| `minSales` | integer | No | Minimum monthly sales | {} |
| `maxSales` | integer | No | Maximum monthly sales | {} |
| `minRevenue` | number | No | Minimum monthly revenue | {} |
| `maxRevenue` | number | No | Maximum monthly revenue | {} |
| `minReviews` | integer | No | Minimum number of reviews | {} |
| `maxReviews` | integer | No | Maximum number of reviews | {} |
| `minRating` | number | No | Minimum rating (1.0-5.0) | {} |
| `maxRating` | number | No | Maximum rating (1.0-5.0) | {} |
| `minWeight` | number | No | Minimum weight (lbs) | {} |
| `maxWeight` | number | No | Maximum weight (lbs) | {} |
| `minRank` | integer | No | Minimum BSR ranking | {} |
| `maxRank` | integer | No | Maximum BSR ranking | {} |
| `minLqs` | integer | No | Minimum LQS score (1-10) | {} |
| `maxLqs` | integer | No | Maximum LQS score (1-10) | {} |
| `minSellers` | integer | No | Minimum number of sellers | {} |
| `maxSellers` | integer | No | Maximum number of sellers | {} |
| `minNet` | number | No | Minimum net profit | {} |
| `maxNet` | number | No | Maximum net profit | {} |
| `sellerTypes` | string | No | Seller types, comma-separated. Options: amz (Amazon self-operated), fba, fbm | {} |
| `productTiers` | string | No | Product size tiers, comma-separated. Options: oversize, standard | {} |
| `excludeTopBrands` | boolean | No | Whether to exclude top brands | {} |
| `excludeUnavailableProducts` | boolean | No | Whether to exclude unavailable products | {} |
| `minUpdatedAt` | string | No | Data update start date (YYYY-MM-DD) | {} |
| `maxUpdatedAt` | string | No | Data update end date (YYYY-MM-DD) | {} |
| `needCount` | integer | No | Total number of results to return, API auto-paginates internally | {} |
| `sort` | string | No | Sort field. Options: name, -name, category, -category, revenue, -revenue, sales, -sales, price, -price, rank, -rank, reviews, -reviews, lqs, -lqs, sellers, -sellers. Prefix - indicates descending. Default: name | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-database.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-database request.json
# Or: node examples/javascript/run.mjs amazon-product-database request.json
# Or: python3 examples/python/run.py amazon-product-database request.json
```

### Published request example

```json
{
  "needCount": 10,
  "includeKeywords": "phone case",
  "marketplace": "us",
  "sort": "-sales"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costToken": 1,
  "productDatabaseList": [
    {
      "id": "example-id",
      "price": 1,
      "approximate30DayUnitsSold": 1,
      "approximate30DayRevenue": 1,
      "productRank": 1,
      "reviews": 1,
      "rating": 1,
      "listingQualityScore": 1,
      "numberOfSellers": 1,
      "imageUrl": "https://example.com/image.jpg",
      "dateFirstAvailable": "2026-01-01",
      "weightValue": 1,
      "lengthValue": 1,
      "widthValue": 1,
      "heightValue": 1,
      "parentAsin": "B072MQ5BRX",
      "isParent": false,
      "isVariant": false,
      "isStandalone": false,
      "isAvailable": false,
      "buyBoxOwnerSellerId": "example-id",
      "updatedAt": "2026-01-01",
      "feeBreakdown": {},
      "subcategoryRanks": [],
      "variants": [],
      "upcList": [],
      "eanList": [],
      "isbnList": [],
      "gtinList": [],
      "dateFirstAvailableIsEstimated": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-database.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-database.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-database.json)
- [Response fixture](../../examples/responses/amazon-product-database.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_database`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
