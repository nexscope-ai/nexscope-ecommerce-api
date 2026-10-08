# Mercado Market Intelligence API

Mercado Market Intelligence public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/mercado-market-intelligence?view=api&co-from=github-ecommerce-api)

Category: Product & Market Research · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/mercado-market-intelligence/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `toolName` | string | Yes | Mercado research operation | {} |
| `arguments` | object | Yes | Arguments for the selected operation | {} |
| `arguments.market_code` | string | No | Mercado market code: MLM, MLB, MLA, MLC, or MCO | {} |
| `arguments.query` | string | No | Category search query | {} |
| `arguments.category_id` | string | No | Mercado category ID | {} |
| `arguments.keyword` | string | No | Product search keyword | {} |
| `arguments.sku_id` | string | No | Mercado product SKU ID | {} |
| `arguments.product_url` | string | No | Mercado product URL | {} |
| `arguments.shop_id` | string | No | Mercado shop ID | {} |
| `arguments.shop_query` | string | No | Shop search query | {} |
| `arguments.image_url` | string | No | Public image URL for image search | {} |
| `arguments.image_base64` | string | No | Base64 image input for image search | {} |
| `arguments.days` | integer | No | Sales-trend lookback days | {} |
| `arguments.page` | integer | No | Page number, starting at 1 | {} |
| `arguments.limit` | integer | No | Maximum number of records | {} |
| `arguments.sort_by` | string | No | Snapshot result sort field | {} |
| `arguments.sort_order` | string | No | Sort direction: asc or desc | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/mercado-market-intelligence.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh mercado-market-intelligence request.json
# Or: node examples/javascript/run.mjs mercado-market-intelligence request.json
# Or: python3 examples/python/run.py mercado-market-intelligence request.json
```

### Published request example

```json
{
  "arguments": {
    "market_code": "MLM",
    "query": "celulares",
    "limit": 10
  },
  "toolName": "search_categories"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": {
    "record_count": 1,
    "records": [
      {
        "taxonomy_name": "Cell Phones",
        "taxonomy_code": "MLM1055"
      }
    ]
  },
  "operation": "search_categories",
  "total": 1
}
```

## Full definitions

- [Request definition](../../schemas/mercado-market-intelligence.request.json) — json-schema
- [Response definition](../../schemas/mercado-market-intelligence.response.json) — json-schema
- [Editable request sample](../../payloads/mercado-market-intelligence.json)
- [Response fixture](../../examples/responses/mercado-market-intelligence.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_mercado_market_intelligence`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
