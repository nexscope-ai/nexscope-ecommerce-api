# Similar Image Variations API

Create similar image variations.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/similar-image-variations?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Generate similar ecommerce images from a reference image with optional prompt and strength controls.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/similar-image-variations/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/similar-image-variations/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of a JPG, PNG, or WEBP reference image up to 10 MB and at most 4096 pixels in both width and height. | {} |
| `prompt` | string | No | Optional prompt for the desired variation, up to 600 characters. | {} |
| `weight` | integer | No | Reference image weight from 0 to 2. Defaults to 2. | {} |
| `width` | integer | No | Desired output width in pixels, from 384 to 4096. | {"minimum": 384, "maximum": 4096, "requiredWhenPresent": ["height"]} |
| `height` | integer | No | Desired output height in pixels, from 384 to 4096. | {"minimum": 384, "maximum": 4096, "requiredWhenPresent": ["width"]} |
| `scale` | string | No | Optional aspect ratio. Provide scale or both width and height. | {} |
| `outputNum` | integer | No | Number of images to generate, from 1 to 4. Defaults to 4. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Provide scale or both width and height to define the output shape. Fields: `scale`, `width`.

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
    "maxFileSizeBytes": "10485760",
    "maxFiles": 1,
    "minWidthPixels": null,
    "maxWidthPixels": 4096,
    "minHeightPixels": null,
    "maxHeightPixels": 4096,
    "minAspectRatio": null,
    "maxAspectRatio": null
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/similar-image-variations.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh similar-image-variations request.json
# Or: node examples/javascript/run.mjs similar-image-variations request.json
# Or: python3 examples/python/run.py similar-image-variations request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "prompt": "same product, brighter background",
  "weight": 2,
  "width": 1024,
  "height": 1024,
  "outputNum": 4
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

- [Request definition](../../schemas/similar-image-variations.request.json) — field-descriptors
- [Response definition](../../schemas/similar-image-variations.response.json) — field-descriptors
- [Editable request sample](../../payloads/similar-image-variations.json)
- [Response fixture](../../examples/responses/similar-image-variations.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_similar_image_variations`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
