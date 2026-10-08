# TikTok Product Discovery API

Search and filter TikTok global e-commerce products based on FastMoss data, supporting keyword search, multi-dimensional filtering (category, shop type, commission rate, sales, creator count, etc.) and sorting.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-product-discovery?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Search and filter TikTok global e-commerce products based on FastMoss data, supporting keyword search, multi-dimensional filtering (category, shop type, commission rate, sales, creator count, etc.) and sorting.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-product-discovery/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Search keyword (fuzzy match on product title) | {} |
| `region` | string | No | Market region code. Options: US (United States), GB (United Kingdom), MX (Mexico), ES (Spain), DE (Germany), IT (Italy), FR (France), ID (Indonesia), VN (Vietnam), MY (Malaysia), TH (Thailand), PH (Philippines), BR (Brazil), JP (Japan), SG (Singapore) | {} |
| `category` | string | No | English category name, automatically matched to TikTok category ID. Non-English input must be translated to English first | {} |
| `shopType` | integer | No | Store type: 1=local store, 2=cross-border store | {} |
| `isTopSelling` | boolean | No | Filter hot-selling products only | {} |
| `isNewListed` | boolean | No | Filter newly listed products only | {} |
| `isSshop` | boolean | No | Filter TikTok fully managed (S-shop) products only | {} |
| `isFreeShipping` | boolean | No | Filter free shipping products only | {} |
| `isLocalWarehouse` | boolean | No | Filter local warehouse shipping products only | {} |
| `unitsSoldRange` | object | No | Sales volume range filter, format: {"min": 100, "max": 5000} | {} |
| `commissionRateRange` | object | No | Commission rate range filter, format: {"min": 0.05, "max": 0.20} (decimal, 0.10=10%) | {} |
| `creatorCountRange` | object | No | Creator count range filter, format: {"min": 10, "max": 500} | {} |
| `orderField` | string | No | Sort field: day7_units_sold (7-day sales), day7_gmv (7-day GMV), commission_rate (commission rate), total_units_sold (total sales), total_gmv (total GMV), creator_count (creator count). Default descending order | {} |
| `page` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Items per page, max 10, default 10 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-product-discovery.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-product-discovery request.json
# Or: node examples/javascript/run.mjs tiktok-product-discovery request.json
# Or: python3 examples/python/run.py tiktok-product-discovery request.json
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
      "region": "US",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "totalSaleCnt": 1,
      "totalSale1dCnt": 1,
      "totalSale7dCnt": 1,
      "totalSale28dCnt": 1,
      "totalSale90dCnt": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv7dAmt": 1,
      "totalSaleGmv28dAmt": 1,
      "totalVideoCnt": 1,
      "totalLiveCnt": 1,
      "totalIflCnt": 1,
      "productCommissionRate": 1,
      "productRating": 1,
      "reviewCount": 1,
      "skuCount": 1,
      "shopSellerId": "example-id",
      "shopTotalUnitsSold": 1,
      "isCrossBorder": 1,
      "availableDate": "2026-01-01",
      "tiktokUrl": "https://example.com/image.jpg",
      "fastmossUrl": "https://example.com/image.jpg",
      "imageUrl": "https://example.com/image.jpg"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-product-discovery.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-product-discovery.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-product-discovery.json)
- [Response fixture](../../examples/responses/tiktok-product-discovery.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_product_discovery`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
