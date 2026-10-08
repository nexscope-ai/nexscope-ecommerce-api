# TikTok Seller Detail API

Query TikTok Shop store (seller) details, retrieving a complete store profile by sellerId with total sales, multi-period (1d/7d/30d/90d) sales and GMV, followers, rating, review count, positive feedback rate, delivery rate, response rate, in-store product count, promoting creator count, promotional video count, livestream count, price range, product categories, and estimated listing time.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-seller-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Query TikTok Shop store (seller) details, retrieving a complete store profile by sellerId with total sales, multi-period (1d/7d/30d/90d) sales and GMV, followers, rating, review count, positive feedback rate, delivery rate, response rate, in-store product count, promoting creator count, promotional video count, livestream count, price range, product categories, and estimated listing time.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-seller-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `sellerId` | string | Yes | TikTok Shop seller ID. Obtainable from the "EchoTik TikTok Seller Search" API (nexscope-echotik-list-seller) results, or from the ID in a known store link. Max length 1000 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-seller-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-seller-detail request.json
# Or: node examples/javascript/run.mjs tiktok-seller-detail request.json
# Or: python3 examples/python/run.py tiktok-seller-detail request.json
```

### Published request example

```json
{
  "sellerId": "7496162162184128712"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 1,
  "costToken": 1,
  "columns": [
    {
      "sellerId": "example-id",
      "coverUrl": "https://example.com/image.jpg",
      "region": "US",
      "categoryId": "example-id",
      "categoryL2Id": "example-id",
      "categoryL3Id": "example-id",
      "totalSaleCnt": 1,
      "totalSale1dCnt": 1,
      "totalSale7dCnt": 1,
      "totalSale30dCnt": 1,
      "totalSale90dCnt": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv1dAmt": 1,
      "totalSaleGmv7dAmt": 1,
      "totalSaleGmv30dAmt": 1,
      "totalSaleGmv90dAmt": 1,
      "followersCount": 1,
      "rating": 1,
      "reviewCount": 1,
      "positiveFeedbackRate": 1,
      "responseRate": 1,
      "deliveryRate": 1,
      "totalProductCnt": 1,
      "totalCrawlProductCnt": 1,
      "spuAvgPrice": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "totalIflCnt": 1,
      "totalVideoCnt": 1,
      "totalLiveCnt": 1,
      "firstCrawlDt": 1,
      "userId": "example-id"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-seller-detail.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-seller-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-seller-detail.json)
- [Response fixture](../../examples/responses/tiktok-seller-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_seller_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
