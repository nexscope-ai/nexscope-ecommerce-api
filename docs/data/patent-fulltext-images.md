# Patent Fulltext Images API

Retrieve fulltext images (drawings, diagrams, charts) from patent documents by patent ID or publication number.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-fulltext-images?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieve fulltext images (drawings, diagrams, charts) from patent documents by patent ID or publication number.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-fulltext-images/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | Patent ID | {} |
| `patentNumber` | string | No | Publication (grant) number | {} |
| `limit` | string | No | Total number of images to return, max 100, default "100" | {} |
| `offset` | string | No | Offset | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-fulltext-images.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-fulltext-images request.json
# Or: node examples/javascript/run.mjs patent-fulltext-images request.json
# Or: python3 examples/python/run.py patent-fulltext-images request.json
```

### Published request example

```json
{
  "patentNumber": "US11299876B2",
  "offset": "0",
  "limit": "10"
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
      "fulltextImagePath": "https://example.com/image.jpg",
      "imageType": "https://example.com/image.jpg"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-fulltext-images.request.json) — field-descriptors
- [Response definition](../../schemas/patent-fulltext-images.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-fulltext-images.json)
- [Response fixture](../../examples/responses/patent-fulltext-images.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_fulltext_images`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
