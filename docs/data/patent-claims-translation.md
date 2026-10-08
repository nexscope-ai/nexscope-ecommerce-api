# Patent Claims Translation API

Retrieves translated patent claims from the Zhihuiya (PatSnap) patent database.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-claims-translation?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieves translated patent claims from the Zhihuiya (PatSnap) patent database.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-claims-translation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | Patent ID. Only a single value is supported; multiple values separated by commas are not allowed. When both patentNumber and this are present, the patent ID takes precedence. Max length: 60000 characters | {} |
| `patentNumber` | string | No | Publication (announcement) number. Only a single value is supported; multiple values separated by commas are not allowed. Max length: 60000 characters | {} |
| `lang` | string | No | Translation language. Supports en (English, default), cn (Chinese), jp (Japanese). Max length: 1000 characters | {} |
| `replaceByRelated` | integer | No | Whether to substitute with a family patent when claims are unavailable: 1 yes, 0 no (default) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-claims-translation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-claims-translation request.json
# Or: node examples/javascript/run.mjs patent-claims-translation request.json
# Or: python3 examples/python/run.py patent-claims-translation request.json
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

- [Request definition](../../schemas/patent-claims-translation.request.json) — field-descriptors
- [Response definition](../../schemas/patent-claims-translation.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-claims-translation.json)
- [Response fixture](../../examples/responses/patent-claims-translation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_claims_translation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
