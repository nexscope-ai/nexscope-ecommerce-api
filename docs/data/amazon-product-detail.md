# Amazon Product Detail API

Retrieve detailed Amazon product information by ASIN, including title, Item Highlights when extractable from raw HTML, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more. Trigger when users mention Amazon product details, ASIN lookup, Item Highlights, product page data, listing analysis, bullet point extraction, product image retrieval, variant inspection, competitor listing research, price lookup, review breakdown, product specification query, or similar terms. Even if the user does not explicitly say "product details," trigger this skill whenever the request involves retrieving structured data from Amazon product pages via ASIN.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-detail?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asins` | string | Yes | ASIN list, supports batch query, up to 40 ASINs. Format: ^[A-Z0-9]+(,[A-Z0-9]+){0,39}$. Example: B072MQ5BRX,B08N5WRWNW | {} |
| `amazonDomain` | string | No | Amazon country site, default amazon.com. Options: amazon.com, amazon.co.uk, amazon.de, amazon.fr, amazon.it, amazon.es, amazon.co.jp, amazon.ca, amazon.com.au, amazon.com.br, amazon.in, amazon.nl, amazon.se, amazon.pl, amazon.sg, amazon.sa, amazon.ae, amazon.com.tr, amazon.com.mx, amazon.eg, amazon.cn, amazon.com.be | {} |
| `language` | string | No | Language. Examples: en_US, de_DE, fr_FR, ja_JP, it_IT, es_ES, pt_BR, en_GB, zh_CN | {} |
| `deliveryZip` | string | No | Delivery zip code, used to get delivery-related pricing. Examples: 10001 (New York, US), 10115 (Berlin, Germany), EC1A 1BB (London, UK) | {} |
| `device` | string | No | Device type: desktop (default), mobile, tablet | {} |
| `returnBoughtTogether` | boolean | No | Whether to return frequently bought together items (boughtTogether), default false | {} |
| `returnRelatedProducts` | boolean | No | Whether to return related product list (relatedProducts), default false | {} |
| `returnAuthorsReviews` | boolean | No | Whether to return author review list (authorsReviews), default false | {} |

The [complete request definition](../../schemas/amazon-product-detail.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/amazon-product-detail.json request.json
python3 examples/python/run.py amazon-product-detail request.json --dry-run
# Alternatively: node examples/javascript/run.mjs amazon-product-detail request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "returnAuthorsReviews": false,
  "asins": "B072MQ5BRX",
  "returnBoughtTogether": false,
  "returnRelatedProducts": false
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/amazon-product-detail.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "total": 1,
    "columns": [],
    "costToken": 1,
    "products": [
      {
        "asin": "B072MQ5BRX",
        "price": 1,
        "extractedPrice": 1,
        "oldPrice": 1,
        "extractedOldPrice": 1,
        "rating": 1,
        "ratings": 1,
        "prime": false,
        "asinUrl": "https://www.amazon.com/dp/B072MQ5BRX",
        "imageUrl": "https://example.com/image.jpg",
        "productImageUrls": [],
        "aboutItem": [],
        "climatePledgeFriendly": false,
        "snapEbtEligible": false,
        "boughtLastMonthCount": 1,
        "reviewsImages": [],
        "pageFileUrl": "https://example.com/product.json",
        "rawHtmlFile": "https://example.com/product.html"
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
