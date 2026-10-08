# Temu Product Source Query API

Filter Temu products by multiple dimensions (keyword/product ID/store ID, front/backend categories, price, rating, reviews, total/weekly/daily sales, listing date, fully-managed/semi-managed, semi-managed regions, tags, etc.).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/temu-product-source-query?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Filter Temu products by multiple dimensions (keyword/product ID/store ID, front/backend categories, price, rating, reviews, total/weekly/daily sales, listing date, fully-managed/semi-managed, semi-managed regions, tags, etc.).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/temu-product-source-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKey` | string | No | Keyword or product ID / store ID | {} |
| `categoryHome` | string | No | Front-end category ID | {} |
| `categoryBackend` | string | No | Back-end category ID | {} |
| `priceBegin` | number | No | Price range start (USD), combined to form upstream price | {} |
| `priceEnd` | number | No | Price range end (USD) | {} |
| `ratingBegin` | number | No | Rating range start, combined to form upstream rating | {} |
| `ratingEnd` | number | No | Rating range end | {} |
| `reviewsBegin` | integer | No | Review count range start, combined to form reviews | {} |
| `reviewsEnd` | integer | No | Review count range end | {} |
| `salesTotalBegin` | integer | No | Total sales range start, combined to form sales_total | {} |
| `salesTotalEnd` | integer | No | Total sales range end | {} |
| `salesWeeklyBegin` | integer | No | Weekly sales range start, combined to form sales_weekly | {} |
| `salesWeeklyEnd` | integer | No | Weekly sales range end | {} |
| `salesDailyBegin` | integer | No | Daily sales range start, combined to form sales_daily | {} |
| `salesDailyEnd` | integer | No | Daily sales range end | {} |
| `publishTimeBegin` | string | No | Listing date range start, combined to form publish_time | {} |
| `publishTimeEnd` | string | No | Listing date range end | {} |
| `soldOut` | integer | No | Whether delisted: 0=Listed, 1=Delisted | {} |
| `isLocal` | integer | No | Whether semi-managed: 0=Fully managed, 1=Semi-managed | {} |
| `region` | string | No | Semi-managed regions, comma-separated | {} |
| `tags` | string | No | Product tags, comma-separated | {} |
| `customTags` | string | No | Custom tags, comma-separated | {} |
| `sortBy` | string | No | Sort field+direction: order_week-0 (weekly sales descending, default), price-0, order_total-0, rating-0, etc. | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page, max 100, recommended not to exceed 50 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/temu-product-source-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh temu-product-source-query request.json
# Or: node examples/javascript/run.mjs temu-product-source-query request.json
# Or: python3 examples/python/run.py temu-product-source-query request.json
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
      "logoUrl": "https://example.com/image.jpg",
      "storeId": "example-id"
    }
  ],
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/temu-product-source-query.request.json) — field-descriptors
- [Response definition](../../schemas/temu-product-source-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/temu-product-source-query.json)
- [Response fixture](../../examples/responses/temu-product-source-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_temu_product_source_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
