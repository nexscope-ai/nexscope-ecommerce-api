# Wan 2.7 Image Generation

Generate ecommerce images with the WAN2_7 model.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/wan-2-7-image-generation?view=api&co-from=github-ecommerce-api)

Category: Image Generation Models · Creative API

Generate ecommerce images with the Wan 2.7 image model. The model is fixed by this API, so provider must not be supplied in the request.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/wan-2-7-image-generation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/wan-2-7-image-generation/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrls` | array | Yes | Public reference image URLs required by this image generation API. When supplied, provide 1 to 10 JPG, PNG, or WEBP images; each image must not exceed 20 MB. | {"maxItems": 10, "minItems": 1} |
| `prompt` | string | Yes | Generation prompt describing the target image, scene, composition, style, and constraints. Maximum 5000 characters. | {"maxLength": 5000} |
| `outputNum` | integer | No | Number of images to generate. Valid range: 1 to 10; defaults to 1. | {"maximum": 10, "minimum": 1} |
| `resolution` | string | No | Output resolution. Supported values: 1K or 2K; defaults to 1K. | {"allowedValues": ["1K", "2K"]} |
| `aspectRatio` | string | No | Output aspect ratio. Supported values: 1:1, 1:4, 4:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 16:9, 9:16, 21:9. | {"allowedValues": ["1:1", "1:4", "4:1", "3:2", "2:3", "3:4", "4:3", "4:5", "5:4", "16:9", "9:16", "21:9"]} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageUrls",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 10,
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
cp payloads/wan-2-7-image-generation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh wan-2-7-image-generation request.json
# Or: node examples/javascript/run.mjs wan-2-7-image-generation request.json
# Or: python3 examples/python/run.py wan-2-7-image-generation request.json
```

### Published request example

```json
{
  "imageUrls": [
    "https://example.com/product.jpg"
  ],
  "prompt": "Keep the product consistent and generate a clean white-background ecommerce hero image.",
  "outputNum": 1,
  "resolution": "1K",
  "aspectRatio": "1:1"
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

- [Request definition](../../schemas/wan-2-7-image-generation.request.json) — field-descriptors
- [Response definition](../../schemas/wan-2-7-image-generation.response.json) — field-descriptors
- [Editable request sample](../../payloads/wan-2-7-image-generation.json)
- [Response fixture](../../examples/responses/wan-2-7-image-generation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_wan_2_7_image_generation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
