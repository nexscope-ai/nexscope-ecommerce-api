# 1688 Product Search API

Search and analyze products on the Chinese 1688 wholesale platform (Alibaba domestic B2B market) for sourcing, supplier discovery, and product selection. Trigger when the user mentions 1688 product search, finding suppliers on 1688, wholesale product queries, factory sourcing, dropshipping supplier search, 1688 keyword product selection, wholesale price comparison, filtering by sales volume, any product research on the 1688 platform, 1688 search, 1688 product selection, find suppliers, factory lookup, wholesale pricing, supplier search, domestic sourcing, 1688 products. Even if the user does not explicitly say "1688", if their need involves searching for wholesale products, finding domestic suppliers, or sourcing from the domestic Chinese market, this skill should also be triggered.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-search?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Search language

Translate the user's English keyword into Simplified Chinese before sending `keyWord`. JSON Unicode escapes in examples decode to the actual Chinese request value; do not send the literal English translation. Multiple `productIds` use the Chinese enumeration comma U+3001. The API does not translate an English search term automatically.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyWord` | string | No | Search keyword (must be written in Simplified Chinese; maximum 50 characters) | {} |
| `goodsUrl` | string | No | Product link URL (mutually exclusive with keyWord) | {} |
| `productIds` | string | No | Product IDs, separated by the Chinese enumeration comma (U+3001), max 20 | {} |
| `cycle` | string | No | Statistical period: 7 (last 7 days) or 30 (last 30 days) | {} |
| `searchType` | integer | No | Search type: 1 = fuzzy match, 3 = exact match | {} |
| `sortField` | string | No | Sort field: orderCount7d, saleCount7d, saleVolume7d, orderCount30d, saleCount30d, saleVolume30d, offerCreateTime, price, consignPrice. Default orderCount30d | {} |
| `sortType` | string | No | Sort order: desc (descending), asc (ascending). Default desc | {} |
| `pageIndex` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page (10-100), default 20 | {} |
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
| `companyType` | integer | No | Company type: 0 = no limit, 1 = store, 2 = factory. Default 0 | {} |
| `offerType` | integer | No | Product tag: 0 = no limit, 2 = new product, 3 = 1688 Select, 4 = cross-border, 5 = customization supported, 6 = store highlight. Default 0 | {} |
| `shiLiType` | string | No | Seller type (multi-select, comma-separated): superFactory (Super Factory), Power (Power Seller), TrustPass (TrustPass) | {} |
| `sendTime` | string | No | Delivery time (multi-select, comma-separated): 24, 48, 72 | {} |
| `faceToFaceSupport` | string | No | Waybill support (multi-select, comma-separated): 441218 (Taobao), 386434 (Douyin), 422914 (Pinduoduo), 422978 (Xiaohongshu), 386370 (Kuaishou) | {} |
| `proxyRights` | string | No | Dropship rights (multi-select, comma-separated): 4360897 (one-piece dropship with free shipping), 449154 (procure now, pay later) | {} |
| `shopService` | string | No | Seller services (multi-select, comma-separated): 4057409 (Safe Buy), 888777 (Deep Verification Report) | {} |
| `buyerProtections` | string | No | Buyer protections, comma-separated: free shipping, 7-day free return, or shipping insurance | {} |

The [complete request definition](../../schemas/1688-product-search.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/1688-product-search.json request.json
python3 examples/python/run.py 1688-product-search request.json --dry-run
# Alternatively: node examples/javascript/run.mjs 1688-product-search request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "keyWord": "\u745c\u4f3d\u57ab",
  "searchType": 1,
  "pageIndex": 1,
  "pageSize": 20
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/1688-product-search.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "total": 1,
    "columns": [],
    "products": [
      {
        "offerId": "example-id",
        "asin": "B072MQ5BRX",
        "asinUrl": "https://detail.1688.com/offer/1040473674152.html",
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
