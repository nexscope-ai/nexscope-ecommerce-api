# Ruiguan Copyright Detection API

Detect image copyright infringement risks by comparing against a database of registered copyrighted works with similarity scoring, TRO litigation history, and radar-based infringement assessment.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ruiguan-copyright-detection?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Detect image copyright infringement risks by comparing against a database of registered copyrighted works with similarity scoring, TRO litigation history, and radar-based infringement assessment.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ruiguan-copyright-detection/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | URL of the copyrighted image to inspect (maximum 1,000 characters) | {} |
| `topNumber` | integer | Yes | Maximum number of matches to return (default 100, minimum 10, maximum 200) | {} |
| `enableRadar` | boolean | Yes | Whether to enable radar detection (default true) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ruiguan-copyright-detection.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ruiguan-copyright-detection request.json
# Or: node examples/javascript/run.mjs ruiguan-copyright-detection request.json
# Or: python3 examples/python/run.py ruiguan-copyright-detection request.json
```

### Published request example

```json
{
  "imageUrl": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg",
  "enableRadar": false,
  "topNumber": 10
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
      "subRadarResult": 1,
      "copyrightUrl": "https://example.com/image.jpg",
      "troCase": false,
      "troHolder": false
    }
  ],
  "detectId": "example-id",
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ruiguan-copyright-detection.request.json) — field-descriptors
- [Response definition](../../schemas/ruiguan-copyright-detection.response.json) — field-descriptors
- [Editable request sample](../../payloads/ruiguan-copyright-detection.json)
- [Response fixture](../../examples/responses/ruiguan-copyright-detection.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ruiguan_copyright_detection`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
