# Amazon Product Price Series API

Query Amazon product historical time-series data, including price trends, BSR (Best Sellers Rank) trends, rating changes, seller counts, and monthly sales, supporting any ASIN across multiple Amazon marketplaces.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-price-series?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Query Amazon product historical time-series data, including price trends, BSR (Best Sellers Rank) trends, rating changes, seller counts, and monthly sales, supporting any ASIN across multiple Amazon marketplaces.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-price-series/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon Standard Identification Number (ASIN), single ASIN only, max length 1000 | {} |
| `domain` | string | Yes | Amazon domain ID. Options: 1 (United States), 2 (United Kingdom), 3 (Germany), 4 (France), 5 (Japan), 6 (Canada), 8 (Italy), 9 (Spain), 10 (India), 11 (Mexico), 12 (Brazil) | {} |
| `days` | integer | No | Limit historical data to this many days, default 90, max 365 | {} |
| `showPrice` | integer | No | Set to 1 to return the lowest new price curve in the market | {} |
| `showPriceList` | integer | No | Set to 1 to return the list/strikethrough price curve | {} |
| `showPriceDeal` | integer | No | Set to 1 to return the deal/flash sale price curve | {} |
| `showPricePrime` | integer | No | Set to 1 to return the Prime-exclusive new price curve | {} |
| `showPriceFba` | integer | No | Set to 1 to return the third-party FBA new price curve | {} |
| `showPriceFbm` | integer | No | Set to 1 to return the third-party FBM new price curve | {} |
| `showPriceCoupon` | integer | No | Set to 1 to return the coupon-applied Buy Box price curve | {} |
| `showBsrMain` | integer | No | Set to 1 to return the main category BSR curve | {} |
| `showSellerCount` | integer | No | Set to 1 to return the seller count curve | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-price-series.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-price-series request.json
# Or: node examples/javascript/run.mjs amazon-product-price-series request.json
# Or: python3 examples/python/run.py amazon-product-price-series request.json
```

### Published request example

```json
{
  "showPrice": 1,
  "asin": "B072MQ5BRX",
  "days": 30,
  "showPriceDeal": 1,
  "domain": "1",
  "showPriceList": 1,
  "showPricePrime": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "asin": "B072MQ5BRX",
  "buyboxPrice": [],
  "price": [],
  "priceList": [],
  "priceDeal": [],
  "pricePrime": [],
  "priceFba": [],
  "priceFbm": [],
  "priceCoupon": [],
  "bsrMain": [],
  "bsrSub": [],
  "sellerCount": [],
  "rating": [],
  "ratingCount": [],
  "monthlySold": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-price-series.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-price-series.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-price-series.json)
- [Response fixture](../../examples/responses/amazon-product-price-series.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_price_series`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
