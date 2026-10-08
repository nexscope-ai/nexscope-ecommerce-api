# Object Eraser & Image Object Removal API

Erase masked objects from an image.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/object-eraser-image-object-removal?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Remove selected objects or regions using a mask image.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/object-eraser-image-object-removal/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/object-eraser-image-object-removal/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the base image. The image must be between 300 and 4096 pixels in both width and height, and its width-to-height ratio must be between 0.4 and 2.5. | {} |
| `maskImageUrl` | string | Yes | Public URL of the mask image for the area to erase. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 1,
    "minWidthPixels": 300,
    "maxWidthPixels": 4096,
    "minHeightPixels": 300,
    "maxHeightPixels": 4096,
    "minAspectRatio": 0.4,
    "maxAspectRatio": 2.5
  },
  {
    "fieldName": "maskImageUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 1,
    "minWidthPixels": null,
    "maxWidthPixels": null,
    "minHeightPixels": null,
    "maxHeightPixels": null,
    "minAspectRatio": null,
    "maxAspectRatio": null
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/object-eraser-image-object-removal.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh object-eraser-image-object-removal request.json
# Or: node examples/javascript/run.mjs object-eraser-image-object-removal request.json
# Or: python3 examples/python/run.py object-eraser-image-object-removal request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "maskImageUrl": "https://example.com/mask.png"
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

- [Request definition](../../schemas/object-eraser-image-object-removal.request.json) — field-descriptors
- [Response definition](../../schemas/object-eraser-image-object-removal.response.json) — field-descriptors
- [Editable request sample](../../payloads/object-eraser-image-object-removal.json)
- [Response fixture](../../examples/responses/object-eraser-image-object-removal.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_object_eraser_image_object_removal`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
