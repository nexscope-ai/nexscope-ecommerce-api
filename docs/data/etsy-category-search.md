# Etsy Category Search API

Search Etsy category data by name, ID, or parent IDs to find category identifiers for product/store filtering.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/etsy-category-search?view=api&co-from=github-ecommerce-api)

Category: Etsy Marketplace · Data API

Search Etsy category data by name, ID, or parent IDs to find category identifiers for product/store filtering.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/etsy-category-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Keyword: matches category name, category id, or parentIds fields (substring) | {} |
| `page` | integer | No | Page number (starting from 1) | {} |
| `pageSize` | integer | No | Items per page, max 200 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/etsy-category-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh etsy-category-search request.json
# Or: node examples/javascript/run.mjs etsy-category-search request.json
# Or: python3 examples/python/run.py etsy-category-search request.json
```

### Published request example

```json
{
  "page": 1,
  "pageSize": 1,
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "costToken": 1,
  "categories": [
    {
      "categoryLevel": 1,
      "id": "example-id",
      "parentId": "example-id"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/etsy-category-search.request.json) — field-descriptors
- [Response definition](../../schemas/etsy-category-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/etsy-category-search.json)
- [Response fixture](../../examples/responses/etsy-category-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_etsy_category_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
