# Nexscope Temu Product Search API

Product Search using Nexscope Temu data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/geekbi-temu-goods-search?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Execute the selected product search operation and preserve provider business fields and extensions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-goods-search/run`

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
| `catIds` | array | No | Category identifiers obtained from category lookup. | {"type": "array", "description": "Category identifiers obtained from category lookup.", "items": {"type": "integer", "minimum": 0}} |
| `matchMode` | integer | No | 1 strict matching, 2 fuzzy matching. | {"enum": [1, 2], "type": "integer", "default": 2, "description": "1 strict matching, 2 fuzzy matching."} |
| `status` | array | No | 1 normal, 2 out of stock, 3 delisted. | {"type": "array", "description": "1 normal, 2 out of stock, 3 delisted.", "items": {"type": "integer", "enum": [1, 2, 3]}} |
| `hostingMode` | integer | No | 1 fully managed, 2 semi-managed. | {"enum": [1, 2], "type": "integer", "description": "1 fully managed, 2 semi-managed."} |
| `soldMin` | integer | No | Lower bound for sold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for sold; minimum must not exceed maximum.", "minimum": 0} |
| `soldMax` | integer | No | Upper bound for sold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for sold; minimum must not exceed maximum.", "minimum": 0} |
| `daySoldMin` | integer | No | Lower bound for daySold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for daySold; minimum must not exceed maximum.", "minimum": 0} |
| `daySoldMax` | integer | No | Upper bound for daySold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for daySold; minimum must not exceed maximum.", "minimum": 0} |
| `weekSoldMin` | integer | No | Lower bound for weekSold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for weekSold; minimum must not exceed maximum.", "minimum": 0} |
| `weekSoldMax` | integer | No | Upper bound for weekSold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for weekSold; minimum must not exceed maximum.", "minimum": 0} |
| `monthSoldMin` | integer | No | Lower bound for monthSold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for monthSold; minimum must not exceed maximum.", "minimum": 0} |
| `monthSoldMax` | integer | No | Upper bound for monthSold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for monthSold; minimum must not exceed maximum.", "minimum": 0} |
| `quantityMin` | integer | No | Lower bound for quantity; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for quantity; minimum must not exceed maximum.", "minimum": 0} |
| `quantityMax` | integer | No | Upper bound for quantity; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for quantity; minimum must not exceed maximum.", "minimum": 0} |
| `mallSoldMin` | integer | No | Lower bound for mallSold; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for mallSold; minimum must not exceed maximum.", "minimum": 0} |
| `mallSoldMax` | integer | No | Upper bound for mallSold; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for mallSold; minimum must not exceed maximum.", "minimum": 0} |
| `reviewNumMin` | integer | No | Lower bound for reviewNum; minimum must not exceed maximum. | {"type": "integer", "description": "Lower bound for reviewNum; minimum must not exceed maximum.", "minimum": 0} |
| `reviewNumMax` | integer | No | Upper bound for reviewNum; minimum must not exceed maximum. | {"type": "integer", "description": "Upper bound for reviewNum; minimum must not exceed maximum.", "minimum": 0} |
| `salesMin` | number | No | Lower bound for sales; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for sales; minimum must not exceed maximum.", "minimum": 0} |
| `salesMax` | number | No | Upper bound for sales; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for sales; minimum must not exceed maximum.", "minimum": 0} |
| `daySalesMin` | number | No | Lower bound for daySales; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for daySales; minimum must not exceed maximum.", "minimum": 0} |
| `daySalesMax` | number | No | Upper bound for daySales; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for daySales; minimum must not exceed maximum.", "minimum": 0} |
| `weekSalesMin` | number | No | Lower bound for weekSales; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for weekSales; minimum must not exceed maximum.", "minimum": 0} |
| `weekSalesMax` | number | No | Upper bound for weekSales; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for weekSales; minimum must not exceed maximum.", "minimum": 0} |
| `monthSalesMin` | number | No | Lower bound for monthSales; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for monthSales; minimum must not exceed maximum.", "minimum": 0} |
| `monthSalesMax` | number | No | Upper bound for monthSales; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for monthSales; minimum must not exceed maximum.", "minimum": 0} |
| `priceMin` | number | No | Lower bound for price; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for price; minimum must not exceed maximum.", "minimum": 0} |
| `priceMax` | number | No | Upper bound for price; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for price; minimum must not exceed maximum.", "minimum": 0} |
| `supplyPriceMin` | number | No | Lower bound for supplyPrice; minimum must not exceed maximum. | {"type": "number", "description": "Lower bound for supplyPrice; minimum must not exceed maximum.", "minimum": 0} |
| `supplyPriceMax` | number | No | Upper bound for supplyPrice; minimum must not exceed maximum. | {"type": "number", "description": "Upper bound for supplyPrice; minimum must not exceed maximum.", "minimum": 0} |
| `daySoldRateMin` | number | No | Lower bound for daySoldRate; minimum must not exceed maximum. | {"description": "Lower bound for daySoldRate; minimum must not exceed maximum.", "type": "number"} |
| `daySoldRateMax` | number | No | Upper bound for daySoldRate; minimum must not exceed maximum. | {"description": "Upper bound for daySoldRate; minimum must not exceed maximum.", "type": "number"} |
| `weekSoldRateMin` | number | No | Lower bound for weekSoldRate; minimum must not exceed maximum. | {"description": "Lower bound for weekSoldRate; minimum must not exceed maximum.", "type": "number"} |
| `weekSoldRateMax` | number | No | Upper bound for weekSoldRate; minimum must not exceed maximum. | {"description": "Upper bound for weekSoldRate; minimum must not exceed maximum.", "type": "number"} |
| `monthSoldRateMin` | number | No | Lower bound for monthSoldRate; minimum must not exceed maximum. | {"description": "Lower bound for monthSoldRate; minimum must not exceed maximum.", "type": "number"} |
| `monthSoldRateMax` | number | No | Upper bound for monthSoldRate; minimum must not exceed maximum. | {"description": "Upper bound for monthSoldRate; minimum must not exceed maximum.", "type": "number"} |
| `daySalesRateMin` | number | No | Lower bound for daySalesRate; minimum must not exceed maximum. | {"description": "Lower bound for daySalesRate; minimum must not exceed maximum.", "type": "number"} |
| `daySalesRateMax` | number | No | Upper bound for daySalesRate; minimum must not exceed maximum. | {"description": "Upper bound for daySalesRate; minimum must not exceed maximum.", "type": "number"} |
| `weekSalesRateMin` | number | No | Lower bound for weekSalesRate; minimum must not exceed maximum. | {"description": "Lower bound for weekSalesRate; minimum must not exceed maximum.", "type": "number"} |
| `weekSalesRateMax` | number | No | Upper bound for weekSalesRate; minimum must not exceed maximum. | {"description": "Upper bound for weekSalesRate; minimum must not exceed maximum.", "type": "number"} |
| `monthSalesRateMin` | number | No | Lower bound for monthSalesRate; minimum must not exceed maximum. | {"description": "Lower bound for monthSalesRate; minimum must not exceed maximum.", "type": "number"} |
| `monthSalesRateMax` | number | No | Upper bound for monthSalesRate; minimum must not exceed maximum. | {"description": "Upper bound for monthSalesRate; minimum must not exceed maximum.", "type": "number"} |
| `goodsScoreMin` | number | No | Lower bound for goodsScore; minimum must not exceed maximum. | {"maximum": 5, "type": "number", "description": "Lower bound for goodsScore; minimum must not exceed maximum.", "minimum": 0} |
| `goodsScoreMax` | number | No | Upper bound for goodsScore; minimum must not exceed maximum. | {"maximum": 5, "type": "number", "description": "Upper bound for goodsScore; minimum must not exceed maximum.", "minimum": 0} |
| `onSaleTimeMin` | string | No | Earliest onSaleTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Earliest onSaleTime in ISO-8601 date-time; minimum must not exceed maximum."} |
| `onSaleTimeMax` | string | No | Latest onSaleTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Latest onSaleTime in ISO-8601 date-time; minimum must not exceed maximum."} |
| `mallOpenTimeMin` | string | No | Earliest mallOpenTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Earliest mallOpenTime in ISO-8601 date-time; minimum must not exceed maximum."} |
| `mallOpenTimeMax` | string | No | Latest mallOpenTime in ISO-8601 date-time; minimum must not exceed maximum. | {"format": "date-time", "type": "string", "maxLength": 40, "description": "Latest mallOpenTime in ISO-8601 date-time; minimum must not exceed maximum."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/geekbi-temu-goods-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh geekbi-temu-goods-search request.json
# Or: node examples/javascript/run.mjs geekbi-temu-goods-search request.json
# Or: python3 examples/python/run.py geekbi-temu-goods-search request.json
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

- [Request definition](../../schemas/geekbi-temu-goods-search.request.json) — json-schema
- [Response definition](../../schemas/geekbi-temu-goods-search.response.json) — json-schema
- [Editable request sample](../../payloads/geekbi-temu-goods-search.json)
- [Response fixture](../../examples/responses/geekbi-temu-goods-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_geekbi_temu_goods_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
