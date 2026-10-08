# White Background Product Image API

Generate a square white-background product image from reference photos.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/whitebg-image?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Generate one square white-background product image from one or two references of the same product using GPT Image 2. Submit one approved target per request. Review product identity and listing suitability before use; this endpoint does not perform reference inspection, image-set planning, or marketplace compliance certification. Generation consumes Nexscope credits.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/whitebg-image/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/whitebg-image/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageList` | array | Yes | Public reference image URLs of the same product. Provide up to 2 JPG, JPEG, PNG, or WEBP images; each image must be at most 10 MB and between 800 and 4096 pixels. | {"maxItems": 2, "minItems": 1} |
| `prompt` | string | Yes | Describe one target supported by the references, up to 350 characters. Output is fixed to one 1:1 image. | {"maxLength": 350} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageList",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "10485760",
    "maxFiles": 2,
    "minWidthPixels": 800,
    "maxWidthPixels": 4096,
    "minHeightPixels": 800,
    "maxHeightPixels": 4096,
    "minAspectRatio": null,
    "maxAspectRatio": null
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/whitebg-image.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh whitebg-image request.json
# Or: node examples/javascript/run.mjs whitebg-image request.json
# Or: python3 examples/python/run.py whitebg-image request.json
```

### Published request example

```json
{
  "imageList": [
    "https://example.com/product.jpg"
  ],
  "prompt": "Show the complete product from the supplied front view."
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

- [Request definition](../../schemas/whitebg-image.request.json) — field-descriptors
- [Response definition](../../schemas/whitebg-image.response.json) — field-descriptors
- [Editable request sample](../../payloads/whitebg-image.json)
- [Response fixture](../../examples/responses/whitebg-image.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_whitebg_image`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
