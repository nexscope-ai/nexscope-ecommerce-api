# Patent Core Bibliography API

Retrieve core bibliographic records for one or more patents.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-core-bibliography?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Returns titles, abstracts, identifiers, dates, applicants, inventors, assignees, and classifications.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-core-bibliography/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | One or up to 100 comma-separated Nexscope patent IDs. Takes precedence when both identifiers are provided. | {} |
| `patentNumber` | string | No | One or up to 100 comma-separated publication or grant numbers. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Provide patentId or patentNumber. Fields: `patentId`, `patentNumber`.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-core-bibliography.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-core-bibliography request.json
# Or: node examples/javascript/run.mjs patent-core-bibliography request.json
# Or: python3 examples/python/run.py patent-core-bibliography request.json
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
  "allRecordsCount": 1,
  "data": [
    {
      "patentId": "patent-id",
      "title": "Wireless speaker system",
      "abstractContent": "A wireless speaker system...",
      "publicationNumber": "US10123456B2",
      "applicationNo": "US15/123456",
      "applicants": [],
      "inventors": [],
      "assignees": [],
      "ipcFurther": []
    }
  ],
  "columns": [],
  "costToken": 6000
}
```

## Full definitions

- [Request definition](../../schemas/patent-core-bibliography.request.json) — field-descriptors
- [Response definition](../../schemas/patent-core-bibliography.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-core-bibliography.json)
- [Response fixture](../../examples/responses/patent-core-bibliography.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_core_bibliography`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
