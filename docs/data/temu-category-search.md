# Temu Category Search API

Search synced Temu category data in the local database by keyword to find category Chinese names, English names, and category IDs for use in product/store filtering.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/temu-category-search?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Search synced Temu category data in the local database by keyword to find category Chinese names, English names, and category IDs for use in product/store filtering.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/temu-category-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword: matches against category Chinese name, English name, category ID (substring) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Results per page, max 200 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/temu-category-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh temu-category-search request.json
# Or: node examples/javascript/run.mjs temu-category-search request.json
# Or: python3 examples/python/run.py temu-category-search request.json
```

### Published request example

```json
{
  "page": 1,
  "pageSize": 10,
  "keyword": "home"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "categories": [
    {
      "id": "example-id",
      "categoryId": "example-id",
      "parentId": "example-id",
      "level": 1,
      "isDeleted": 1,
      "hasChildren": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/temu-category-search.request.json) — field-descriptors
- [Response definition](../../schemas/temu-category-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/temu-category-search.json)
- [Response fixture](../../examples/responses/temu-category-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_temu_category_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
