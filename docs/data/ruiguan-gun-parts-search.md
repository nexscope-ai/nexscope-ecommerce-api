# Ruiguan Gun Parts Search API

Check product images against a database of policy-violating items using visual similarity matching.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ruiguan-gun-parts-search?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Check product images against a database of policy-violating items using visual similarity matching.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ruiguan-gun-parts-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | URL of the product image to inspect (maximum 1,000 characters) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ruiguan-gun-parts-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ruiguan-gun-parts-search request.json
# Or: node examples/javascript/run.mjs ruiguan-gun-parts-search request.json
# Or: python3 examples/python/run.py ruiguan-gun-parts-search request.json
```

### Published request example

```json
{
  "imageUrl": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "data": [
    {
      "pdImgOssUrl": "https://example.com/image.jpg",
      "cosine": 1
    }
  ],
  "detectId": "example-id",
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ruiguan-gun-parts-search.request.json) — field-descriptors
- [Response definition](../../schemas/ruiguan-gun-parts-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ruiguan-gun-parts-search.json)
- [Response fixture](../../examples/responses/ruiguan-gun-parts-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ruiguan_gun_parts_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
