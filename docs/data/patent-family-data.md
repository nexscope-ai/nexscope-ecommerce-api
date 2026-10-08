# Patent Family Data API

Retrieve simple, INPADOC, and PatSnap patent family records.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-family-data?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Returns patent family identifiers and members for up to 100 patents.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-family-data/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | One or up to 100 comma-separated PatSnap patent IDs. Takes precedence when both identifiers are provided. | {} |
| `patentNumber` | string | No | One or up to 100 comma-separated publication or grant numbers. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Provide patentId or patentNumber. Fields: `patentId`, `patentNumber`.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-family-data.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-family-data request.json
# Or: node examples/javascript/run.mjs patent-family-data request.json
# Or: python3 examples/python/run.py patent-family-data request.json
```

### Published request example

```json
{
  "patentNumber": "US10123456B2"
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
      "patentId": "patent-id",
      "pn": "US10123456B2",
      "simpleFamilyId": 1,
      "simpleFamily": [],
      "inpadocFamilyId": 1,
      "inpadocFamily": [],
      "patsnapFamilyId": 1,
      "patsnapFamily": []
    }
  ],
  "columns": [],
  "costToken": 6000
}
```

## Full definitions

- [Request definition](../../schemas/patent-family-data.request.json) — field-descriptors
- [Response definition](../../schemas/patent-family-data.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-family-data.json)
- [Response fixture](../../examples/responses/patent-family-data.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_family_data`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
