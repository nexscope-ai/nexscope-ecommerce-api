# Walmart Product Detail API

Query Walmart product details via Nexscope, including pricing history and sales trends.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/walmart-product-detail?view=api&co-from=github-ecommerce-api)

Category: Walmart Marketplace Intelligence · Data API

Query Walmart product details via Nexscope, including pricing history and sales trends.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/walmart-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productId` | integer | Yes | Product ID (ItemId), the numeric ID contained in the product detail link. For example: the 5169493923 in https://www.walmart.com/ip/5169493923 | {} |
| `includeStats` | boolean | No | Whether to include historical price/historical sales, default true | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/walmart-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh walmart-product-detail request.json
# Or: node examples/javascript/run.mjs walmart-product-detail request.json
# Or: python3 examples/python/run.py walmart-product-detail request.json
```

### Published request example

```json
{
  "productId": "5169493923",
  "includeStats": false
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "products": [
    {
      "usItemId": 1,
      "productId": "example-id",
      "price": 1,
      "wasPrice": 1,
      "minPrice": 1,
      "rating": 1,
      "reviews": 1,
      "salesEstimate": 1,
      "revenue": 1,
      "productPageUrl": "https://example.com/image.jpg",
      "imageUrl": "https://example.com/image.jpg",
      "departmentId": 1,
      "listingScore": 1,
      "contentScore": 1,
      "outOfStock": 1,
      "sponsored": 1,
      "isBranded": 1,
      "multipleOptionsAvailable": 1,
      "updatedAt": "2026-01-01",
      "stats": {}
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1,
  "stats": {
    "price": [],
    "sales": []
  }
}
```

## Full definitions

- [Request definition](../../schemas/walmart-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/walmart-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/walmart-product-detail.json)
- [Response fixture](../../examples/responses/walmart-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_walmart_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
