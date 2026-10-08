# Jewelry Text Design API

Generate linked text for jewelry or accessory designs.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/jewelry-text-design?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create decorative linked-word imagery using font, size, and prompt controls.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/jewelry-text-design/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/jewelry-text-design/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `fontname` | string | Yes | Font name. Allowed values: Caitlyn, ItaliannoRob, Alison, ALSScript, WhiteAngelica, Milkshake, ScriptMTBold, PassionsConflictROB, Sacramento, Cervanttis, Notera 2 PERSONAL USE ONLY, UyghurMerdane, OldEnglishText, Halimun, AlexBrush, Scriptina, CounselorScript, EliannaBoldItalic, AutumnChant, MagnoliaScript. | {} |
| `fontSize` | integer | Yes | Output font size. | {} |
| `left` | boolean | No | Whether to add a ring on the left side. Defaults to false. | {} |
| `right` | boolean | No | Whether to add a ring on the right side. Defaults to false. | {} |
| `prompt` | string | Yes | Jewelry text content. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/jewelry-text-design.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh jewelry-text-design request.json
# Or: node examples/javascript/run.mjs jewelry-text-design request.json
# Or: python3 examples/python/run.py jewelry-text-design request.json
```

### Published request example

```json
{
  "fontname": "UyghurMerdane",
  "fontSize": 10,
  "left": false,
  "right": false,
  "prompt": "hello"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "taskId": "6b3f1c61-1b7d-4a59-8a7d-3b23e4b0c9e2",
  "status": "PENDING",
  "message": "The task has been created. Use taskId to query the result."
}
```

## Full definitions

- [Request definition](../../schemas/jewelry-text-design.request.json) — field-descriptors
- [Response definition](../../schemas/jewelry-text-design.response.json) — field-descriptors
- [Editable request sample](../../payloads/jewelry-text-design.json)
- [Response fixture](../../examples/responses/jewelry-text-design.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_jewelry_text_design`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
