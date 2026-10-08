# One-Click Image Recoloring API v2

Change product colors in an image.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/one-click-image-recoloring-v2?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Recolor the requested subject using one or more target colors.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/one-click-image-recoloring-v2/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/one-click-image-recoloring-v2/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the product image. The image must be between 300 and 4096 pixels in both width and height. | {} |
| `colors` | array | No | Target colors, from 1 to 25 entries. Each value must use full HEX (#RRGGBB), HSB (hsb(H, S%, B%)), or RGB (rgb(R, G, B)) format. Provide colors or refImageUrls, but not both. | {"conflictsWith": ["refImageUrls"], "minItems": 1, "maxItems": 25} |
| `refImageUrls` | array | No | Reference image URLs for reference-image recoloring, from 1 to 25 entries. Provide refImageUrls or colors, but not both. | {"conflictsWith": ["colors"], "minItems": 1, "maxItems": 25} |
| `colorSubject` | string | Yes | Subject to recolor. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Provide either colors or refImageUrls to define the target color. Fields: `colors`, `refImageUrls`.

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
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "colors",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 25,
    "minWidthPixels": null,
    "maxWidthPixels": null,
    "minHeightPixels": null,
    "maxHeightPixels": null,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "refImageUrls",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 25,
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
cp payloads/one-click-image-recoloring-v2.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh one-click-image-recoloring-v2 request.json
# Or: node examples/javascript/run.mjs one-click-image-recoloring-v2 request.json
# Or: python3 examples/python/run.py one-click-image-recoloring-v2 request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "colors": [
    "#000000",
    "#FFFFFF"
  ],
  "colorSubject": "phone case"
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

- [Request definition](../../schemas/one-click-image-recoloring-v2.request.json) — field-descriptors
- [Response definition](../../schemas/one-click-image-recoloring-v2.response.json) — field-descriptors
- [Editable request sample](../../payloads/one-click-image-recoloring-v2.json)
- [Response fixture](../../examples/responses/one-click-image-recoloring-v2.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_one_click_image_recoloring_v2`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
