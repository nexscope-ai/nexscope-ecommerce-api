# Patent Title Abstract Translation API

Retrieve translated patent titles and abstracts from the Nexscope (Nexscope) patent database.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-title-abstract-translation?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieve translated patent titles and abstracts from the Nexscope (Nexscope) patent database.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-title-abstract-translation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | Nexscope internal patent ID. Only a single value is supported; multiple values separated by commas are not allowed. Max length: 60,000 characters | {} |
| `patentNumber` | string | No | Publication (grant) number. Only a single value is supported; multiple values separated by commas are not allowed. Max length: 60,000 characters | {} |
| `replaceByRelated` | integer | No | Whether to substitute with a family patent's abstract when the abstract is unavailable: 1 Yes, 0 No. Default 0 | {} |
| `lang` | string | No | Target translation language. Options: en (English, default), cn (Chinese), jp (Japanese). Max length: 1,000 characters | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-title-abstract-translation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-title-abstract-translation request.json
# Or: node examples/javascript/run.mjs patent-title-abstract-translation request.json
# Or: python3 examples/python/run.py patent-title-abstract-translation request.json
```

### Published request example

```json
{
  "patentNumber": "CN115000000A",
  "replaceByRelated": 1,
  "lang": "en"
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
      "patentId": "example-id"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-title-abstract-translation.request.json) — field-descriptors
- [Response definition](../../schemas/patent-title-abstract-translation.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-title-abstract-translation.json)
- [Response fixture](../../examples/responses/patent-title-abstract-translation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_title_abstract_translation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
