# Patent Claims API

Retrieves patent claims data from Zhihuiya (PatSnap).

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-claims?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieves patent claims data from Zhihuiya (PatSnap).

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-claims/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | PatSnap internal patent ID. Only a single value is supported; multiple values separated by commas are not allowed. Max length 60000 characters | {} |
| `patentNumber` | string | No | Publication/announcement number. Only a single value is supported; multiple values separated by commas are not allowed. Max length 60000 characters | {} |
| `replaceByRelated` | string | No | Whether to substitute with a family patent's claims when the current patent's claims are unavailable: 1 yes, 0 no. Max length 1000 characters | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-claims.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-claims request.json
# Or: node examples/javascript/run.mjs patent-claims request.json
# Or: python3 examples/python/run.py patent-claims request.json
```

### Published request example

```json
{
  "patentNumber": "US11299876B2"
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
      "patentId": "example-id",
      "claims": [],
      "claimCount": 1
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-claims.request.json) — field-descriptors
- [Response definition](../../schemas/patent-claims.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-claims.json)
- [Response fixture](../../examples/responses/patent-claims.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_claims`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
