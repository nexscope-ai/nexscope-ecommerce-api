# 1688 Search By Image API

Perform image-based product search on the 1688 platform. Use an image URL to find visually similar supplier products, returning title, price, minimum order quantity, monthly sales, repurchase rate, trade score, and seller identity. Triggered when users mention 1688 image search, 1688 visual search, find supplier by image, reverse image search 1688, 1688 product sourcing by image, or Alibaba 1688 image search. Even if the user does not explicitly mention "image search," this skill should be triggered whenever a user provides an image URL and wants to find matching or similar products on the 1688 wholesale platform.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-search-by-image?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-search-by-image/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | No | Public HTTP/80 or HTTPS/443 URL, maximum 1,000 characters, without redirects. A sole direct source is checked for PNG/JPEG headers, at most 14.3 MiB, each dimension at most 20,000 and at most 40,000,000 pixels. This is not full pixel-integrity validation. Provide exactly one of imageUrl, imageBase64, or imageId. | {} |
| `imageBase64` | string | No | Raw standard Base64 for PNG/JPEG; optional padding and outer whitespace allowed, embedded whitespace and data URI prefixes rejected for a sole direct source. Byte/header limits match imageUrl; at most 19,992,848 Base64 characters after outer whitespace trimming. Provide this as the only image source. | {} |
| `imageId` | string | No | 1688 image ID. Image-search results also return this value; include it when page is greater than 1 to improve response time | {} |
| `page` | integer | No | Page number starting from 1 | {} |
| `pageSize` | integer | No | Number of products per page; default 20, maximum 50 | {} |
| `priceStart` | string | No | Minimum price in CNY, for example 10 | {} |
| `priceEnd` | string | No | Maximum price in CNY, for example 100 | {} |
| `filter` | string | No | Comma-separated filter conditions. Use the supported filter values documented for this endpoint | {} |
| `sort` | string | No | Sort condition as JSON in the form {field: direction}. Fields: price, rePurchaseRate, or monthSold. Directions: asc or desc | {} |
| `keyword` | string | No | Keyword used to search within the results | {} |
| `productCollectionId` | string | No | Single product-collection ID. Use a supported collection ID documented for this endpoint | {} |

The [complete request definition](../../schemas/1688-search-by-image.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/1688-search-by-image.json request.json
python3 examples/python/run.py 1688-search-by-image request.json --dry-run
# Alternatively: node examples/javascript/run.mjs 1688-search-by-image request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "pageSize": 20,
  "page": 1,
  "imageUrl": "https://m.media-amazon.com/images/I/61v6nYvQ7+L._AC_SL1500_.jpg"
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/1688-search-by-image.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "imageId": "example-id",
    "total": 1,
    "totalPage": 1,
    "columns": [],
    "costToken": 1,
    "products": [
      {
        "offerId": "example-id",
        "asin": "example-id",
        "imageUrl": "https://example.com/image.jpg",
        "price": 1,
        "consignPrice": 1,
        "salesQuantity": 1,
        "estimatedSalesAmount": 1,
        "asinUrl": "https://detail.1688.com/offer/1040473674152.html",
        "quantityBegin": 1
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
