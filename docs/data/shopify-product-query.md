# Shopify Product Query API

Filter Shopify standalone store products by multiple dimensions (keyword/URL, price, weekly sales, listing date, Facebook ads, competitiveness, supplier availability, shipping country, etc.).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/shopify-product-query?view=api&co-from=github-ecommerce-api)

Category: Shopify Commerce · Data API

Filter Shopify standalone store products by multiple dimensions (keyword/URL, price, weekly sales, listing date, Facebook ads, competitiveness, supplier availability, shipping country, etc.).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/shopify-product-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKey` | string | No | Keyword or Shopify product/store URL | {} |
| `priceMin` | number | No | Price range start (USD), combined with priceMax to form upstream price | {} |
| `priceMax` | number | No | Price range end (USD) | {} |
| `salesWeeklyMin` | integer | No | Weekly sales range start | {} |
| `salesWeeklyMax` | integer | No | Weekly sales range end | {} |
| `publishedTimeBegin` | string | No | Listing date range start | {} |
| `publishedTimeEnd` | string | No | Listing date range end | {} |
| `facebookAd` | integer | No | Has Facebook ad: 1=Yes | {} |
| `competitionMin` | integer | No | Competition (number of stores selling) range start | {} |
| `competitionMax` | integer | No | Competition (number of stores selling) range end | {} |
| `hasSupplier` | integer | No | Has supplier: 1=Yes, 0=No | {} |
| `showDeleted` | integer | No | Show delisted products: 1=Yes, 0=No | {} |
| `country` | string | No | Shipping country (two-letter country code, e.g., US) | {} |
| `sortBy` | integer | No | Sort field (default 14=Weekly sales descending; also includes price/ad count/competition/revenue etc. values, see enumeration below) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page, max 100, recommended not to exceed 50 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/shopify-product-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh shopify-product-query request.json
# Or: node examples/javascript/run.mjs shopify-product-query request.json
# Or: python3 examples/python/run.py shopify-product-query request.json
```

### Published request example

```json
{
  "page": 1,
  "pageSize": 10,
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "productNum": 1,
  "products": [
    {
      "productId": "example-id",
      "previewImageUrl": "https://example.com/image.jpg",
      "storeId": "example-id",
      "shopId": "example-id"
    }
  ],
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/shopify-product-query.request.json) — field-descriptors
- [Response definition](../../schemas/shopify-product-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/shopify-product-query.json)
- [Response fixture](../../examples/responses/shopify-product-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_shopify_product_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
