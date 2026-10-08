# Mercado Product Selection API

Run one of 24 documented Mercado Libre product, category, trend, seller, review, rate, or usage tools.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/mercado-product-selection?view=api&co-from=github-ecommerce-api)

Category: Product & Market Research · Data API

Validates the selected tool and its required arguments before calling the governed Lingdong gateway.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/mercado-product-selection/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `toolName` | string | Yes | Exact Mercado tool name. | {"allowedValues": ["catalogHistory", "catalogInfo", "catalogSearch", "categorySearch", "categorySmallSearch", "itemHistory", "itemInfo", "itemSearch", "keywordDateSearch", "keywordMonthSearch", "keywordReverse", "myUsage", "rateInfo", "reviewSearch", "sellerSearch", "trendBrandTopBrand", "trendBrandTopItem", "trendBrandTopSeller", "trendNewItems", "trendPrice", "trendSale", "trendSoldHis", "trendStatistical", "trendStoreInventoryType"]} |
| `arguments` | object | Yes | Arguments for the selected tool. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/mercado-product-selection.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh mercado-product-selection request.json
# Or: node examples/javascript/run.mjs mercado-product-selection request.json
# Or: python3 examples/python/run.py mercado-product-selection request.json
```

### Published request example

```json
{
  "arguments": {
    "searchText": "Auriculares",
    "siteId": "MLM"
  },
  "toolName": "categorySearch"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "code": "200",
  "msg": "ok",
  "errcode": 200,
  "errmsg": "ok",
  "type": "rawMcpToolResult",
  "toolName": "categorySearch",
  "charged": false,
  "data": {},
  "contentText": "Category results...",
  "textParsedAsJson": true,
  "total": 1,
  "costToken": 0,
  "costTime": 308
}
```

## Full definitions

- [Request definition](../../schemas/mercado-product-selection.request.json) — field-descriptors
- [Response definition](../../schemas/mercado-product-selection.response.json) — field-descriptors
- [Editable request sample](../../payloads/mercado-product-selection.json)
- [Response fixture](../../examples/responses/mercado-product-selection.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_mercado_product_selection`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
