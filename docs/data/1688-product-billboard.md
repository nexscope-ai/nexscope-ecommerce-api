# 1688 Product Billboard API

Query 1688 product bestseller billboard data for sourcing discovery and wholesale product research.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-billboard?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API

Query 1688 product bestseller billboard data for sourcing discovery and wholesale product research.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-billboard/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyWord` | string | No | Product search keyword (must be written in Simplified Chinese; translate it before calling this API). Maximum 50 characters | {} |
| `date` | string | No | Query time. Weekly chart: pass the Sunday date of that week, e.g. 2025-06-15 (up to 90 days); Monthly chart: pass the first day of the month, e.g. 2025-06-01 (up to one year) | {} |
| `pageType` | integer | No | Billboard type: 2 = weekly, 3 = monthly. Default 3 | {} |
| `pageIndex` | integer | No | Page number (starting from 1), default 1 | {} |
| `pageSize` | integer | No | Number of results per page (10-100), default 20 | {} |
| `sortField` | string | No | Sort field, default orderCount. Options: orderCount (order count), saleCount (units sold), saleVolume (estimated sales amount), offerCreateTime (listing time), price (wholesale price), consignPrice (dropship price) | {} |
| `sortType` | string | No | Sort order: desc (descending), asc (ascending), default desc | {} |
| `searchType` | integer | No | Product keyword search type: 1 = fuzzy match, 3 = exact match. Default 1 | {} |
| `offerType` | integer | No | Product tag: 0 = no limit, 2 = new product, 3 = 1688 Select, 4 = cross-border, 5 = customization supported, 6 = store highlight. Default 0 | {} |
| `companyType` | integer | No | Company type: 0 = no limit, 1 = store, 2 = factory | {} |
| `shiLiType` | string | No | Seller membership type (multi-select), comma-separated. Options: superFactory (Super Factory), Power (Power Seller), TrustPass (TrustPass member only) | {} |
| `beginTpYear` | integer | No | Start TrustPass years | {} |
| `endTpYear` | integer | No | End TrustPass years | {} |
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
| `beginStartQuantity` | integer | No | Minimum order quantity (start) | {} |
| `endStartQuantity` | integer | No | Minimum order quantity (end) | {} |
| `beginOfferCreateTime` | string | No | Listing time (start), format: YYYY-MM-DD | {} |
| `endOfferCreateTime` | string | No | Listing time (end), format: YYYY-MM-DD | {} |
| `sendTime` | string | No | Delivery time (multi-select), comma-separated. Options: 24 (24 hours), 48 (48 hours), 72 (72 hours) | {} |
| `proxyRights` | string | No | Dropship rights (multi-select), comma-separated. Options: 4360897 (one-piece dropship with free shipping), 449154 (procure now, pay later) | {} |
| `shopService` | string | No | Seller services (multi-select), comma-separated. Options: 4057409 (Safe Buy), 888777 (Deep Verification Report) | {} |
| `buyerProtections` | string | No | Buyer protections, comma-separated: free shipping, 7-day free return, or shipping insurance | {} |
| `faceToFaceSupport` | string | No | Waybill support (multi-select), comma-separated. Options: 441218 (Taobao), 386434 (Douyin), 422914 (Pinduoduo), 422978 (Xiaohongshu), 386370 (Kuaishou) | {} |
| `productIds` | string | No | Product IDs, separated by Chinese comma for multiple, max 20 | {} |
| `goodsUrl` | string | No | Product link URL | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/1688-product-billboard.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh 1688-product-billboard request.json
# Or: node examples/javascript/run.mjs 1688-product-billboard request.json
# Or: python3 examples/python/run.py 1688-product-billboard request.json
```

### Published request example

```json
{
  "searchType": 1,
  "pageIndex": 1,
  "keyWord": "iPhone 15",
  "date": "2026-07-01",
  "pageSize": 10,
  "pageType": 3
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
      "price": 1,
      "consignPrice": 1,
      "quantityBegin": 1,
      "salesOrderCount": 1,
      "salesQuantity": 1,
      "estimatedSalesAmount": 1,
      "availableDate": "2026-01-01",
      "shopId": "example-id",
      "shopUrl": "https://example.com/image.jpg",
      "asinUrl": "B072MQ5BRX",
      "imageUrl": "https://example.com/image.jpg"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/1688-product-billboard.request.json) — field-descriptors
- [Response definition](../../schemas/1688-product-billboard.response.json) — field-descriptors
- [Editable request sample](../../payloads/1688-product-billboard.json)
- [Response fixture](../../examples/responses/1688-product-billboard.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_1688_product_billboard`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
