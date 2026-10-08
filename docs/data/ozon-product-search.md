# Ozon Product Search API

MPSTATS Ozon Russia product search and reverse lookup. Searches Ozon products in the MPSTATS database by Russian keyword or SKU, returning product ID, title, brand, and seller information. The entry point for Ozon product discovery and competitor analysis chains.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ozon-product-search?view=api&co-from=github-ecommerce-api)

Category: Ozon Marketplace · Data API

MPSTATS Ozon Russia product search and reverse lookup. Searches Ozon products in the MPSTATS database by Russian keyword or SKU, returning product ID, title, brand, and seller information. The entry point for Ozon product discovery and competitor analysis chains.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ozon-product-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Russian search keyword, e.g., кроссовки (running shoes) | {} |
| `productIds` | array | No | List of Ozon product SKUs (integer or string) | {} |
| `startDate` | string | No | Statistics start date, format YYYY-MM-DD; defaults to one year ago if empty; latest is yesterday | {} |
| `endDate` | string | No | Statistics end date, format YYYY-MM-DD; defaults to yesterday if empty; latest is yesterday | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ozon-product-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ozon-product-search request.json
# Or: node examples/javascript/run.mjs ozon-product-search request.json
# Or: python3 examples/python/run.py ozon-product-search request.json
```

### Published request example

```json
{
  "endDate": "2026-01-31",
  "keyword": "phone case",
  "startDate": "2026-01-01"
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
      "productId": 1,
      "productPageUrl": "https://example.com/image.jpg",
      "imageUrl": "https://example.com/image.jpg",
      "brandId": 1,
      "sellerId": 1
    }
  ],
  "columns": [],
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ozon-product-search.request.json) — field-descriptors
- [Response definition](../../schemas/ozon-product-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ozon-product-search.json)
- [Response fixture](../../examples/responses/ozon-product-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ozon_product_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
