# TikTok Batch Product Detail API

Batch query TikTok product detail data, including multi-period sales and GMV (1d/7d/15d/30d/60d/90d/cumulative), live sales and live GMV, promoting video and creator data, views, price, rating, review count, commission rate, and delisted/fully-managed status. Supports batch retrieval by product ID or TikTok Shop product URL.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-batch-product-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Batch query TikTok product detail data, including multi-period sales and GMV (1d/7d/15d/30d/60d/90d/cumulative), live sales and live GMV, promoting video and creator data, views, price, rating, review count, commission rate, and delisted/fully-managed status. Supports batch retrieval by product ID or TikTok Shop product URL.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-batch-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productIds` | array | No | List of product IDs (max 1000). Example: ["1729382310407603945", "1729382310407603946"] | {} |
| `productUrls` | array | No | List of product URLs (max 1000), in the form https://shop.tiktok.com/us/pdp/<slug>/<productId>?...; the backend will extract the trailing productId from each URL and merge into productIds, not mutually exclusive with productIds | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-batch-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-batch-product-detail request.json
# Or: node examples/javascript/run.mjs tiktok-batch-product-detail request.json
# Or: python3 examples/python/run.py tiktok-batch-product-detail request.json
```

### Published request example

```json
{
  "productIds": [
    "1732294342978343112"
  ]
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
      "productImageUrls": [],
      "region": "US",
      "sellerId": "example-id",
      "categoryId": "example-id",
      "categoryL2Id": "example-id",
      "categoryL3Id": "example-id",
      "minPrice": 1,
      "maxPrice": 1,
      "spuAvgPrice": 1,
      "productRating": 1,
      "reviewCount": 1,
      "productCommissionRate": 1,
      "totalSaleCnt": 1,
      "totalSale1dCnt": 1,
      "totalSale7dCnt": 1,
      "totalSale15dCnt": 1,
      "totalSale30dCnt": 1,
      "totalSale60dCnt": 1,
      "totalSale90dCnt": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv1dAmt": 1,
      "totalSaleGmv7dAmt": 1,
      "totalSaleGmv15dAmt": 1,
      "totalSaleGmv30dAmt": 1,
      "totalSaleGmv60dAmt": 1,
      "totalSaleGmv90dAmt": 1,
      "totalLiveCnt": 1,
      "totalLive1dCnt": 1,
      "totalLive7dCnt": 1,
      "totalLive15dCnt": 1,
      "totalLive30dCnt": 1,
      "totalLive60dCnt": 1,
      "totalLive90dCnt": 1,
      "totalLiveSale1dCnt": 1,
      "totalLiveSale7dCnt": 1,
      "totalLiveSale15dCnt": 1,
      "totalLiveSale30dCnt": 1,
      "totalLiveSale60dCnt": 1,
      "totalLiveSale90dCnt": 1,
      "totalLiveSaleGmv1dAmt": 1,
      "totalLiveSaleGmv7dAmt": 1,
      "totalLiveSaleGmv15dAmt": 1,
      "totalLiveSaleGmv30dAmt": 1,
      "totalLiveSaleGmv60dAmt": 1,
      "totalLiveSaleGmv90dAmt": 1,
      "totalVideoCnt": 1,
      "totalVideo1dCnt": 1,
      "totalVideo7dCnt": 1,
      "totalVideo15dCnt": 1,
      "totalVideo30dCnt": 1,
      "totalVideo60dCnt": 1,
      "totalVideo90dCnt": 1,
      "totalIflCnt": 1,
      "totalIflVideo1dCnt": 1,
      "totalIflVideo7dCnt": 1,
      "totalIflVideo15dCnt": 1,
      "totalIflVideo30dCnt": 1,
      "totalIflVideo60dCnt": 1,
      "totalIflVideo90dCnt": 1,
      "totalIflLive1dCnt": 1,
      "totalIflLive7dCnt": 1,
      "totalIflLive15dCnt": 1,
      "totalIflLive30dCnt": 1,
      "totalIflLive60dCnt": 1,
      "totalIflLive90dCnt": 1,
      "totalViewsCnt": 1,
      "totalViews1dCnt": 1,
      "totalViews7dCnt": 1,
      "totalViews15dCnt": 1,
      "totalViews30dCnt": 1,
      "totalViews60dCnt": 1,
      "totalViews90dCnt": 1,
      "freeShipping": 1,
      "salesFlag": 1,
      "salesTrendFlag": 1,
      "isSShop": 1,
      "offMark": 1
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-batch-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-batch-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-batch-product-detail.json)
- [Response fixture](../../examples/responses/tiktok-batch-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_batch_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
