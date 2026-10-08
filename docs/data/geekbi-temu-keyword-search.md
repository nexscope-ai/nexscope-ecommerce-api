# GeekBI Temu Keyword Research API

Keyword Research using GeekBI Temu data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/geekbi-temu-keyword-search?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Execute the selected keyword research operation and preserve provider business fields and extensions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-keyword-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `regionId` | integer | No | Temu region from sites[].regionId; never siteId. | {"default": 211, "type": "integer", "description": "Temu region from sites[].regionId; never siteId.", "minimum": 1} |
| `page` | integer | No | Page number. | {"default": 1, "type": "integer", "description": "Page number.", "minimum": 1} |
| `size` | integer | No | Items per page; page times size must not exceed 10000. | {"maximum": 200, "type": "integer", "default": 20, "minimum": 1, "description": "Items per page; page times size must not exceed 10000."} |
| `keyword` | string | No | User keyword; preserve the supplied language. | {"type": "string", "description": "User keyword; preserve the supplied language.", "maxLength": 300} |
| `sort` | string | No | Confirmed provider sort field; omit when unnecessary. | {"type": "string", "description": "Confirmed provider sort field; omit when unnecessary.", "maxLength": 100} |
| `order` | string | No | Sort direction, case-insensitive. | {"type": "string", "description": "Sort direction, case-insensitive.", "pattern": "^([aA][sS][cC]\|[dD][eE][sS][cC])$"} |
| `dsrMin` | number | No | Lower bound for dsr; minimum must not exceed maximum. | {"description": "Lower bound for dsr; minimum must not exceed maximum.", "type": "number"} |
| `dsrMax` | number | No | Upper bound for dsr; minimum must not exceed maximum. | {"description": "Upper bound for dsr; minimum must not exceed maximum.", "type": "number"} |
| `totalSoldMin` | integer | No | Lower bound for totalSold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for totalSold; minimum must not exceed maximum.", "minimum": 0} |
| `totalSoldMax` | integer | No | Upper bound for totalSold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for totalSold; minimum must not exceed maximum.", "minimum": 0} |
| `itemCountMin` | integer | No | Lower bound for itemCount; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for itemCount; minimum must not exceed maximum.", "minimum": 0} |
| `itemCountMax` | integer | No | Upper bound for itemCount; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for itemCount; minimum must not exceed maximum.", "minimum": 0} |
| `mallCountMin` | integer | No | Lower bound for mallCount; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for mallCount; minimum must not exceed maximum.", "minimum": 0} |
| `mallCountMax` | integer | No | Upper bound for mallCount; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for mallCount; minimum must not exceed maximum.", "minimum": 0} |
| `avgPriceMin` | number | No | Lower bound for avgPrice; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for avgPrice; minimum must not exceed maximum.", "minimum": 0} |
| `avgPriceMax` | number | No | Upper bound for avgPrice; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for avgPrice; minimum must not exceed maximum.", "minimum": 0} |
| `totalSalesMin` | number | No | Lower bound for totalSales; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for totalSales; minimum must not exceed maximum.", "minimum": 0} |
| `totalSalesMax` | number | No | Upper bound for totalSales; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for totalSales; minimum must not exceed maximum.", "minimum": 0} |
| `catIds` | array | No | Category identifiers obtained from category lookup. | {"type": "array", "description": "Category identifiers obtained from category lookup.", "items": {"type": "integer", "minimum": 0}} |
| `firstOnSaleTimeMin` | string | No | Earliest firstOnSaleTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Earliest firstOnSaleTime in ISO-8601 date-time; minimum must not exceed maximum."} |
| `firstOnSaleTimeMax` | string | No | Latest firstOnSaleTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Latest firstOnSaleTime in ISO-8601 date-time; minimum must not exceed maximum."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/geekbi-temu-keyword-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh geekbi-temu-keyword-search request.json
# Or: node examples/javascript/run.mjs geekbi-temu-keyword-search request.json
# Or: python3 examples/python/run.py geekbi-temu-keyword-search request.json
```

### Published request example

```json
{
  "regionId": 211,
  "page": 1,
  "size": 3,
  "keyword": "dress"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errmsg": "ok",
  "columns": [],
  "errcode": 200,
  "items": [],
  "total": 0,
  "regionId": 211,
  "page": 1,
  "size": 3
}
```

## Full definitions

- [Request definition](../../schemas/geekbi-temu-keyword-search.request.json) — json-schema
- [Response definition](../../schemas/geekbi-temu-keyword-search.response.json) — json-schema
- [Editable request sample](../../payloads/geekbi-temu-keyword-search.json)
- [Response fixture](../../examples/responses/geekbi-temu-keyword-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_geekbi_temu_keyword_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
