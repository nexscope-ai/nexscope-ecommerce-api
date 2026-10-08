# Amazon Product Detail API

Retrieve detailed Amazon product information by ASIN, including title, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-detail?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Retrieve detailed Amazon product information by ASIN, including title, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; check the platform response `code`, then read the business result from `data`.

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

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-detail request.json
# Or: node examples/javascript/run.mjs amazon-product-detail request.json
# Or: python3 examples/python/run.py amazon-product-detail request.json
```

### Published request example

```json
{
  "returnRelatedProducts": false,
  "returnAuthorsReviews": false,
  "asins": "B072MQ5BRX",
  "returnBoughtTogether": false
}
```

## Response

The run endpoint returns a platform response envelope, as documented in the [official API reference](https://www.nexscope.ai/api-docs/amazon-product-detail?co-from=github-ecommerce-api). HTTP 200 alone does not indicate business success: check `code === 0` before reading `data`. A nonzero `code` is a platform error; inspect `msg` and `traceId` for diagnostics. `data` may be null, so check it before accessing `data.products` or `data.total`.

| Field | Type | Meaning |
|---|---|---|
| `data` | object or null | Business result, including `products` and `total` when present. |
| `code` | integer | `0` indicates success or acceptance; nonzero indicates a platform error. |
| `msg` | string or null | Platform message. |
| `ts` | string | Epoch milliseconds. |
| `time` | string | Server local time in `yyyy-MM-dd HH:mm:ss` format. |
| `cost` | string | Elapsed milliseconds, never credits; `-1` outside web requests. |
| `traceId` | string or null | Trace identifier. |

### Parse the response (JavaScript)

```javascript
const response = await fetch(endpoint, options);
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const result = await response.json();
if (result.code !== 0) {
  throw new Error(`Nexscope error ${result.code}: ${result.msg ?? 'Unknown error'}`);
}
const products = result.data?.products ?? [];
const total = result.data?.total ?? 0;
```

Here, `endpoint` is the URL above and `options` contains the POST method, authentication headers, and JSON request body. The repository CLI helpers print the full response envelope; application code should apply the checks above.

### Published response example

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

## Full definitions

- [Request definition](../../schemas/amazon-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-detail.json)
- [Response fixture](../../examples/responses/amazon-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. Response envelope and example reconciled with the official API page: 2026-10-08. See [source and validation notes](../source-notes.md).
