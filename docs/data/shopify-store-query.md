# Shopify Store Query API

Filter Shopify standalone stores by multiple dimensions (store name/domain, country, years since creation, product count, ad count, monthly visits, monthly orders, social media followers, etc.).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/shopify-store-query?view=api&co-from=github-ecommerce-api)

Category: Shopify Commerce · Data API

Filter Shopify standalone stores by multiple dimensions (store name/domain, country, years since creation, product count, ad count, monthly visits, monthly orders, social media followers, etc.).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/shopify-store-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKey` | string | No | Store name or domain keyword | {} |
| `country` | string | No | Country code (e.g., US, CN) | {} |
| `year` | integer | No | Store creation year: 1=Last 1 year, 2=1~2 years, 3=2~3 years, 4=3+ years | {} |
| `productNumMin` | integer | No | Product count range start | {} |
| `productNumMax` | integer | No | Product count range end | {} |
| `advertiseCountMin` | integer | No | Ad count range start | {} |
| `advertiseCountMax` | integer | No | Ad count range end | {} |
| `monthlyVisitMin` | integer | No | Monthly visits range start | {} |
| `monthlyVisitMax` | integer | No | Monthly visits range end | {} |
| `monthOrderMin` | integer | No | Monthly orders range start | {} |
| `monthOrderMax` | integer | No | Monthly orders range end | {} |
| `sortBy` | integer | No | Sort field: 0=Product count, 1=Category count, 2=Monthly visits, 3=FB followers, 4=Ins followers, 5=Ad count, 6=Relevance, 7=Monthly orders (default) | {} |
| `orderBy` | string | No | Sort direction: desc (default) / asc | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page, max 100 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/shopify-store-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh shopify-store-query request.json
# Or: node examples/javascript/run.mjs shopify-store-query request.json
# Or: python3 examples/python/run.py shopify-store-query request.json
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
  "storeNum": 1,
  "stores": [
    {
      "storeId": "example-id",
      "shopId": "example-id",
      "facebookUrl": "https://example.com/image.jpg",
      "instagramUrl": "https://example.com/image.jpg"
    }
  ],
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/shopify-store-query.request.json) — field-descriptors
- [Response definition](../../schemas/shopify-store-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/shopify-store-query.json)
- [Response fixture](../../examples/responses/shopify-store-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_shopify_store_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
