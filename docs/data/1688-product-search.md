# 1688 Product Search API

Search and analyze products on the Chinese 1688 wholesale platform (Alibaba domestic B2B market) for sourcing, supplier discovery, and product selection.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-search?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API

Search and analyze products on the Chinese 1688 wholesale platform (Alibaba domestic B2B market) for sourcing, supplier discovery, and product selection.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyWord` | string | No | Search keyword (must be written in Simplified Chinese; maximum 50 characters) | {} |
| `goodsUrl` | string | No | Product link URL (mutually exclusive with keyWord) | {} |
| `productIds` | string | No | Product IDs, comma-separated, max 20 | {} |
| `cycle` | string | No | Statistical period: 7 (last 7 days) or 30 (last 30 days) | {} |
| `searchType` | integer | No | Search type: 1 = fuzzy match, 3 = exact match | {} |
| `sortField` | string | No | Sort field: orderCount7d, saleCount7d, saleVolume7d, orderCount30d, saleCount30d, saleVolume30d, offerCreateTime, price, consignPrice | {} |
| `sortType` | string | No | Sort order: desc (descending), asc (ascending) | {} |
| `pageIndex` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page (10-100) | {} |
| `beginPrice` | number | No | Wholesale price (start) | {} |
| `endPrice` | number | No | Wholesale price (end) | {} |
| `beginConsignPrice` | number | No | Dropship price (start) | {} |
| `endConsignPrice` | number | No | Dropship price (end) | {} |
| `beginOrderCount` | integer | No | Order count (start) | {} |
| `endOrderCount` | integer | No | Order count (end) | {} |
| `beginSaleCount` | integer | No | Units sold (start) | {} |
| `endSaleCount` | integer | No | Units sold (end) | {} |
| `beginSaleVolume` | number | No | Sales amount (start) | {} |
| `endSaleVolume` | number | No | Sales amount (end) | {} |
| `beginStartQuantity` | integer | No | Minimum purchase quantity (start) | {} |
| `endStartQuantity` | integer | No | Minimum purchase quantity (end) | {} |
| `beginTpYear` | integer | No | TrustPass years (start) | {} |
| `endTpYear` | integer | No | TrustPass years (end) | {} |
| `beginOfferCreateTime` | string | No | Listing time start (format: YYYY-MM-DD) | {} |
| `endOfferCreateTime` | string | No | Listing time end (format: YYYY-MM-DD) | {} |
| `companyType` | integer | No | Company type: 0 = no limit, 1 = store, 2 = factory | {} |
| `offerType` | integer | No | Product tag: 0 = no limit, 2 = new product, 3 = 1688 Select, 4 = cross-border, 5 = customization supported, 6 = store highlight | {} |
| `shiLiType` | string | No | Seller type (multi-select, comma-separated): superFactory (Super Factory), Power (Power Seller), TrustPass (TrustPass) | {} |
| `sendTime` | string | No | Delivery time (multi-select, comma-separated): 24, 48, 72 | {} |
| `faceToFaceSupport` | string | No | Waybill support (multi-select, comma-separated): 441218 (Taobao), 386434 (Douyin), 422914 (Pinduoduo), 422978 (Xiaohongshu), 386370 (Kuaishou) | {} |
| `proxyRights` | string | No | Dropship rights (multi-select, comma-separated): 4360897 (one-piece dropship with free shipping), 449154 (procure now, pay later) | {} |
| `shopService` | string | No | Seller services (multi-select, comma-separated): 4057409 (Safe Buy), 888777 (Deep Verification Report) | {} |
| `buyerProtections` | string | No | Buyer protections, comma-separated: free shipping, 7-day free return, or shipping insurance | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/1688-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh 1688-product-search request.json
# Or: node examples/javascript/run.mjs 1688-product-search request.json
# Or: python3 examples/python/run.py 1688-product-search request.json
```

### Published request example

```json
{
  "pageSize": 10,
  "keyWord": "iPhone 15",
  "searchType": 1,
  "pageIndex": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "columns": [],
  "products": [
    {
      "offerId": "example-id",
      "asin": "B072MQ5BRX",
      "asinUrl": "B072MQ5BRX",
      "imageUrl": "https://example.com/image.jpg",
      "price": 1,
      "consignPrice": 1,
      "quantityBegin": 1,
      "salesOrderCount": 1,
      "salesQuantity": 1,
      "estimatedSalesAmount": 1,
      "availableDate": "2026-01-01",
      "shopId": "example-id",
      "shopUrl": "https://example.com/image.jpg"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/1688-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/1688-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/1688-product-search.json)
- [Response fixture](../../examples/responses/1688-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_1688_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
