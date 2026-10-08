# Web Search API

Web search, online retrieval, real-time information query, search engine search, Reddit and other community platform discussions, external site posts and trending topics.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/web-search?view=api&co-from=github-ecommerce-api)

Category: Search & Trend Intelligence · Data API

Web search, online retrieval, real-time information query, search engine search, Reddit and other community platform discussions, external site posts and trending topics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/web-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Search keyword, max length 1000 characters | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/web-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh web-search request.json
# Or: node examples/javascript/run.mjs web-search request.json
# Or: python3 examples/python/run.py web-search request.json
```

### Published request example

```json
{
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "searchList": [
    {
      "score": 1,
      "url": "https://example.com/image.jpg"
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/web-search.request.json) — field-descriptors
- [Response definition](../../schemas/web-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/web-search.json)
- [Response fixture](../../examples/responses/web-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_web_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
