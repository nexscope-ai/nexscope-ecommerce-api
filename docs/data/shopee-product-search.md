# Shopee Product Search API

YouYing Shopee product selection tool supporting product query and filtering across all Shopee marketplaces, covering Malaysia, Taiwan (China), Indonesia, Thailand, Philippines, Singapore, Vietnam, Brazil, Mexico, Chile, and Colombia.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/shopee-product-search?view=api&co-from=github-ecommerce-api)

Category: Shopee Marketplace · Data API

YouYing Shopee product selection tool supporting product query and filtering across all Shopee marketplaces, covering Malaysia, Taiwan (China), Indonesia, Thailand, Philippines, Singapore, Vietnam, Brazil, Mexico, Chile, and Colombia.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/shopee-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `station` | string | Yes | Required. Shopee site, accepts name or code. See site mapping table below | {} |
| `keyword` | string | No | Product title keyword | {} |
| `keywordType` | integer | No | Match mode: 1=Exact phrase (default), 2=Multi-word AND, 3=Multi-word OR | {} |
| `notExistKeyword` | string | No | Exclude products containing this keyword | {} |
| `notExistKeywordType` | integer | No | Exclusion match mode: 1=Exact phrase (default), 2=Multi-word AND, 3=Multi-word OR | {} |
| `priceMin` | number | No | Minimum total product price (local currency) | {} |
| `priceMax` | number | No | Maximum total product price | {} |
| `soldMin` | integer | No | Minimum units sold in last 30 days | {} |
| `soldMax` | integer | No | Maximum units sold in last 30 days | {} |
| `estimateSoldStart` | integer | No | Minimum estimated units sold in last 30 days | {} |
| `estimateSoldEnd` | integer | No | Maximum estimated units sold in last 30 days | {} |
| `historicalSoldStart` | integer | No | Minimum total historical units sold | {} |
| `historicalSoldEnd` | integer | No | Maximum total historical units sold | {} |
| `paymentStart` | number | No | Minimum sales revenue in last 30 days | {} |
| `paymentEnd` | number | No | Maximum sales revenue in last 30 days | {} |
| `ratingMin` | number | No | Minimum product rating (0-5) | {} |
| `ratingMax` | number | No | Maximum product rating | {} |
| `ratingsMin` | integer | No | Minimum number of ratings | {} |
| `ratingsMax` | integer | No | Maximum number of ratings | {} |
| `favoriteMin` | integer | No | Minimum number of favorites | {} |
| `favoriteMax` | integer | No | Maximum number of favorites | {} |
| `skuNumberStart` | integer | No | Minimum total SKU count | {} |
| `skuNumberEnd` | integer | No | Maximum total SKU count | {} |
| `listingDateFrom` | string | No | Product listing date range start (format: yyyy-MM-dd) | {} |
| `listingDateTo` | string | No | Product listing date range end (format: yyyy-MM-dd) | {} |
| `statTimeStart` | string | No | Statistics time range start (format: yyyy-MM-dd HH:mm:ss) | {} |
| `statTimeEnd` | string | No | Statistics time range end (format: yyyy-MM-dd HH:mm:ss) | {} |
| `lastModiTimeStart` | string | No | Latest crawl time range start (format: yyyy-MM-dd) | {} |
| `lastModiTimeEnd` | string | No | Latest crawl time range end (format: yyyy-MM-dd) | {} |
| `approvedDateStart` | string | No | Store opening time range start (format: yyyy-MM-dd) | {} |
| `approvedDateEnd` | string | No | Store opening time range end (format: yyyy-MM-dd) | {} |
| `pL1Id` | string | No | Level 1 category ID | {} |
| `pL2Id` | string | No | Level 2 category ID | {} |
| `pL3Id` | string | No | Level 3 category ID | {} |
| `cidList` | string | No | Category ID list, full path, multiple groups separated by | {} |
| `shopIdList` | string | No | Specific store ID list, comma-separated | {} |
| `notExistShopIdList` | string | No | Excluded store ID list, comma-separated | {} |
| `merchant` | string | No | Store name or username | {} |
| `shopLocation` | string | No | Store location | {} |
| `shippingIconType` | integer | No | Store location type: 0=Local, 1=Overseas | {} |
| `cbOption` | integer | No | Shipping origin: 0=Local, 1=Cross-border | {} |
| `isShopeeVerified` | integer | No | Shopee Preferred: 0=Not preferred, 1=Preferred | {} |
| `isOfficialShop` | integer | No | Official store: 0=No, 1=Yes | {} |
| `isHotSales` | integer | No | Hot selling: 0=Not hot, 1=Hot | {} |
| `pids` | string | No | Product ID list (max 500), comma-separated | {} |
| `orderBy` | string | No | Sort field: rating, price, historical_sold (total sales), sold (30-day sales), payment (30-day revenue), favorite, ratings, gen_time (listing time), estimate_sold (estimated sales) | {} |
| `orderByType` | string | No | Sort direction: ASC (ascending), DESC (descending) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Products per page (range 1-1000) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/shopee-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh shopee-product-search request.json
# Or: node examples/javascript/run.mjs shopee-product-search request.json
# Or: python3 examples/python/run.py shopee-product-search request.json
```

### Published request example

```json
{
  "station": "SG",
  "page": 1,
  "keyword": "phone case",
  "keywordType": 1,
  "pageSize": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "totalSize": 1,
  "columns": [],
  "costToken": 1,
  "products": [
    {
      "pid": "example-id",
      "imageUrl": "https://example.com/image.jpg",
      "productUrl": "https://example.com/image.jpg",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "sold": 1,
      "estimateSold": 1,
      "historicalSold": 1,
      "payment": 1,
      "rating": 1,
      "ratings": 1,
      "favorite": 1,
      "viewCount": 1,
      "stock": 1,
      "skuNumber": 1,
      "cid": "example-id",
      "shopId": "example-id",
      "shopUrl": "https://example.com/image.jpg",
      "shopProductsCount": 1,
      "approvedDate": "2026-01-01",
      "isOfficialShop": 1,
      "isShopeeVerified": 1,
      "isHotSales": 1,
      "shippingIconType": 1,
      "cbOption": 1,
      "estimatedDays": 1,
      "status": 1,
      "notExist": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/shopee-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/shopee-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/shopee-product-search.json)
- [Response fixture](../../examples/responses/shopee-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_shopee_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
