# Temu Store Source Query API

Filter Temu stores by multiple dimensions (store name/ID, country site, backend category, fully-managed/semi-managed, total/weekly/monthly sales and revenue, rating, reviews, followers, product count, store opening time, etc.).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/temu-store-source-query?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Filter Temu stores by multiple dimensions (store name/ID, country site, backend category, fully-managed/semi-managed, total/weekly/monthly sales and revenue, rating, reviews, followers, product count, store opening time, etc.).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/temu-store-source-query/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `searchKey` | string | No | Store name or ID keyword | {} |
| `siteId` | string | No | Country site ID, multiple separated by commas (e.g., 211=US, 76=UK) | {} |
| `category` | string | No | Backend category ID, multiple separated by commas | {} |
| `isLocal` | string | No | Whether semi-managed: 0=fully managed, 1=semi-managed | {} |
| `orderTotalMin` | integer | No | Total sales range (start) | {} |
| `orderTotalMax` | integer | No | Total sales range (end) | {} |
| `orderWeekMin` | integer | No | Weekly sales range (start) | {} |
| `orderWeekMax` | integer | No | Weekly sales range (end) | {} |
| `orderMonthMin` | integer | No | Monthly sales range (start) | {} |
| `orderMonthMax` | integer | No | Monthly sales range (end) | {} |
| `totalRevenueMin` | number | No | Total revenue range (USD, start) | {} |
| `totalRevenueMax` | number | No | Total revenue range (USD, end) | {} |
| `weekRevenueMin` | number | No | Weekly revenue range (USD, start) | {} |
| `weekRevenueMax` | number | No | Weekly revenue range (USD, end) | {} |
| `monthRevenueMin` | number | No | Monthly revenue range (USD, start) | {} |
| `monthRevenueMax` | number | No | Monthly revenue range (USD, end) | {} |
| `ratingMin` | number | No | Rating range (start) | {} |
| `ratingMax` | number | No | Rating range (end) | {} |
| `reviewNumMin` | integer | No | Review count range (start) | {} |
| `reviewNumMax` | integer | No | Review count range (end) | {} |
| `followerNumMin` | integer | No | Follower count range (start) | {} |
| `followerNumMax` | integer | No | Follower count range (end) | {} |
| `productNumMin` | integer | No | Product count range (start) | {} |
| `productNumMax` | integer | No | Product count range (end) | {} |
| `listedTimeBegin` | string | No | Store opening date range (start) | {} |
| `listedTimeEnd` | string | No | Store opening date range (end) | {} |
| `sortBy` | string | No | Sort field+direction: order_week_count-0 (weekly sales descending, default), order_count-0, total_revenue-0, rating-0 | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Items per page, max 100 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/temu-store-source-query.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh temu-store-source-query request.json
# Or: node examples/javascript/run.mjs temu-store-source-query request.json
# Or: python3 examples/python/run.py temu-store-source-query request.json
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
      "siteId": "example-id",
      "logoUrl": "https://example.com/image.jpg"
    }
  ],
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/temu-store-source-query.request.json) — field-descriptors
- [Response definition](../../schemas/temu-store-source-query.response.json) — field-descriptors
- [Editable request sample](../../payloads/temu-store-source-query.json)
- [Response fixture](../../examples/responses/temu-store-source-query.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_temu_store_source_query`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
