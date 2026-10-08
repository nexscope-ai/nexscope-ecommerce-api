# GeekBI Temu Category List API

List Temu category records.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/geekbi-temu-category-list?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Return provider category records without inventing search pagination fields.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-category-list/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `parentCatId` | integer | No | Known nonnegative category ID; omit for top-level categories | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/geekbi-temu-category-list.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh geekbi-temu-category-list request.json
# Or: node examples/javascript/run.mjs geekbi-temu-category-list request.json
# Or: python3 examples/python/run.py geekbi-temu-category-list request.json
```

### Published request example

```json
{}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 0,
  "errmsg": "ok",
  "columns": [],
  "categories": [],
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/geekbi-temu-category-list.request.json) — json-schema
- [Response definition](../../schemas/geekbi-temu-category-list.response.json) — json-schema
- [Editable request sample](../../payloads/geekbi-temu-category-list.json)
- [Response fixture](../../examples/responses/geekbi-temu-category-list.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_geekbi_temu_category_list`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
