# 1688 Product Billboard API

Query 1688 product bestseller billboard data for sourcing discovery and wholesale product research. Trigger when the user mentions 1688 product rankings, 1688 bestseller lists, wholesale hot products, domestic sourcing rankings, dropshipping product selection, 1688 trending products, bulk purchase popular items, supplier product rankings, 1688 billboard, 1688 bestsellers, sourcing rankings, wholesale hot products, trending product rankings, supplier rankings, 1688 trends. Even if the user does not explicitly mention "1688 billboard", if their need involves discovering hot-selling wholesale products or sourcing opportunities on the 1688 platform, this skill should also be triggered.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-billboard?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-billboard/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

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

The [complete request definition](../../schemas/1688-product-billboard.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/1688-product-billboard.json request.json
python3 examples/python/run.py 1688-product-billboard request.json --dry-run
# Alternatively: node examples/javascript/run.mjs 1688-product-billboard request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "keyWord": "\u624b\u673a\u58f3",
  "date": "2026-07-01",
  "pageSize": 20,
  "pageType": 3,
  "searchType": 1,
  "pageIndex": 1
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/1688-product-billboard.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
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
        "asinUrl": "https://detail.1688.com/offer/1040473674152.html",
        "imageUrl": "https://example.com/image.jpg"
      }
    ]
  },
  "code": 0,
  "msg": null,
  "ts": "0",
  "time": "2026-01-01 00:00:00",
  "cost": "-1",
  "traceId": null
}
```

Keep the request trace when reporting errors. Do not infer authorization, order creation or payment success from a redirect, process exit or missing identifier alone.
