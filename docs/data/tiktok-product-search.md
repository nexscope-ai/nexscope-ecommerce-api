# TikTok Product Search API

Search and analyze TikTok product data including sales, influencer sales data, pricing, and commission rates across 16 TikTok Shop sites.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-product-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search and analyze TikTok product data including sales, influencer sales data, pricing, and commission rates across 16 TikTok Shop sites.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Product keyword (please translate to the local language). Max length 1000 | {} |
| `region` | string | No | Region, default US. Options: US (United States), ID (Indonesia), TH (Thailand), PH (Philippines), MY (Malaysia), VN (Vietnam), GB (United Kingdom), MX (Mexico), SG (Singapore), SA (Saudi Arabia), BR (Brazil), ES (Spain), JP (Japan), DE (Germany), IT (Italy), FR (France) | {} |
| `categoryKeywordCN` | string | No | Product category (please enter in Chinese). Max length 1000 | {} |
| `minTotalSaleCnt` | integer | No | Total sales (minimum) | {} |
| `maxTotalSaleCnt` | integer | No | Total sales (maximum) | {} |
| `minTotalSale30dCnt` | integer | No | 30-day sales (minimum) | {} |
| `maxTotalSale30dCnt` | integer | No | 30-day sales (maximum) | {} |
| `minTotalSaleGmvAmt` | string | No | Product total GMV (minimum). Max length 1000 | {} |
| `maxTotalSaleGmvAmt` | string | No | Product total GMV (maximum). Max length 1000 | {} |
| `minTotalSaleGmv30dAmt` | string | No | Product total GMV (30-day) (minimum). Max length 1000 | {} |
| `maxTotalSaleGmv30dAmt` | string | No | Product total GMV (30-day) (maximum). Max length 1000 | {} |
| `minSpuAvgPrice` | number | No | SPU average price (minimum) | {} |
| `maxSpuAvgPrice` | number | No | SPU average price (maximum) | {} |
| `minProductRating` | number | No | Product rating (minimum) | {} |
| `maxProductRating` | number | No | Product rating (maximum) | {} |
| `minReviewCount` | integer | No | Review count (minimum) | {} |
| `maxReviewCount` | integer | No | Review count (maximum) | {} |
| `minProductCommissionRate` | number | No | Product commission rate (minimum). Input as percentage will be automatically converted to decimal, e.g., 5%->0.05 | {} |
| `maxProductCommissionRate` | number | No | Product commission rate (maximum). Input as percentage will be automatically converted to decimal, e.g., 5%->0.05 | {} |
| `minTotalIflCnt` | integer | No | Promoting creator count (minimum) | {} |
| `maxTotalIflCnt` | integer | No | Promoting creator count (maximum) | {} |
| `minTotalVideoCnt` | integer | No | Promotional video count (minimum) | {} |
| `maxTotalVideoCnt` | integer | No | Promotional video count (maximum) | {} |
| `minTotalViewsCnt` | integer | No | Promotional view count (minimum) | {} |
| `maxTotalViewsCnt` | integer | No | Promotional view count (maximum) | {} |
| `minFirstCrawlDt` | integer | No | Product listing time (minimum), format YYYYMMDD (e.g., 20200101 represents 2020-01-01) | {} |
| `maxFirstCrawlDt` | integer | No | Product listing time (maximum), format YYYYMMDD | {} |
| `saleDays` | integer | No | Days the product has been on sale, unit is days | {} |
| `productSortField` | integer | No | Sort field: 1=total sales, 2=total GMV, 3=SPU average price, 4=7-day sales, 5=30-day sales, 6=7-day GMV, 7=30-day GMV. Default 1 | {} |
| `sortType` | integer | No | Sort direction: 0=ascending, 1=descending. Default 1 | {} |
| `pageNum` | integer | No | Page number. Default 1 | {} |
| `pageSize` | integer | No | Items per page. Default 50 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-product-search request.json
# Or: node examples/javascript/run.mjs tiktok-product-search request.json
# Or: python3 examples/python/run.py tiktok-product-search request.json
```

### Published request example

```json
{
  "pageNumber": 1,
  "keyword": "phone case",
  "pageSize": 10,
  "region": "US"
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
      "productId": "example-id",
      "imageUrl": "https://example.com/image.jpg",
      "coverUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "categoryIds": [],
      "region": "US",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "spuAvgPrice": 1,
      "productRating": 1,
      "reviewCount": 1,
      "ratings": 1,
      "productCommissionRate": 1,
      "totalSaleCnt": 1,
      "totalSale1dCnt": 1,
      "totalSale7dCnt": 1,
      "totalSale15dCnt": 1,
      "totalSale30dCnt": 1,
      "totalSale60dCnt": 1,
      "totalSale90dCnt": 1,
      "monthlySalesUnits": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv1dAmt": 1,
      "totalSaleGmv7dAmt": 1,
      "totalSaleGmv15dAmt": 1,
      "totalSaleGmv30dAmt": 1,
      "totalSaleGmv60dAmt": 1,
      "totalSaleGmv90dAmt": 1,
      "firstCrawlDt": 1,
      "availableDate": "2026-01-01",
      "salePropsInfo": [],
      "asin": "B072MQ5BRX"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-product-search.json)
- [Response fixture](../../examples/responses/tiktok-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
