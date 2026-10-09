# TikTok New Product Rank API

Discover trending new products across 16 TikTok Shop regional markets via Nexscope new product ranking data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-new-product-rank?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Discover trending new products across 16 TikTok Shop regional markets via Nexscope new product ranking data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-new-product-rank/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `date` | string | Yes | Date in YYYY-MM-DD format | {} |
| `region` | string | No | Region, default US. Options: US (United States), ID (Indonesia), TH (Thailand), PH (Philippines), MY (Malaysia), VN (Vietnam), GB (United Kingdom), MX (Mexico), SG (Singapore), SA (Saudi Arabia), BR (Brazil), ES (Spain), JP (Japan), DE (Germany), IT (Italy), FR (France) | {} |
| `pageNum` | integer | No | Page number, default 1 | {} |
| `pageSize` | integer | No | Items per page, default 50 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-new-product-rank.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-new-product-rank request.json
# Or: node examples/javascript/run.mjs tiktok-new-product-rank request.json
# Or: python3 examples/python/run.py tiktok-new-product-rank request.json
```

### Published request example

```json
{
  "pageNum": 1,
  "pageSize": 10,
  "region": "US",
  "date": "2026-08-01"
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
      "region": "US",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "totalSaleCnt": 1,
      "totalSale30dCnt": 1,
      "totalSaleGmvAmt": 1,
      "totalSaleGmv30dAmt": 1,
      "totalVideoCnt": 1,
      "totalLiveCnt": 1,
      "totalIflCnt": 1,
      "productCommissionRate": 1,
      "productRating": 1,
      "reviewCount": 1,
      "availableDate": "2026-01-01",
      "categoryId": "example-id",
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": []
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-new-product-rank.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-new-product-rank.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-new-product-rank.json)
- [Response fixture](../../examples/responses/tiktok-new-product-rank.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_new_product_rank`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
