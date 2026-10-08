# Product Replacement API

Replace a product region in an ecommerce image.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/product-replacement?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Use source and target product references to replace product content while preserving scene consistency.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/product-replacement/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/product-replacement/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the base image. The image must be up to 20 MB and between 384 and 8192 pixels in both width and height. | {} |
| `targetOriginUrl` | string | Yes | Public URL of the replacement product image. | {} |
| `sourceImageUrl` | string | No | Optional source product crop URL. | {} |
| `targetImageUrl` | string | No | Optional processed replacement product URL. | {} |
| `denoiseStrength` | number | No | Generation denoise strength from 0 to 1. Defaults to 0.5. | {} |
| `imageOutputWidth` | integer | No | Desired output width in pixels, from 32 to 4096. | {} |
| `imageOutputHeight` | integer | No | Desired output height in pixels, from 32 to 4096. | {} |
| `outputNum` | integer | No | Number of images to generate, from 1 to 4. Defaults to 1. | {} |

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
    "minWidthPixels": 384,
    "maxWidthPixels": 8192,
    "minHeightPixels": 384,
    "maxHeightPixels": 8192,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "targetOriginUrl",
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
  },
  {
    "fieldName": "sourceImageUrl",
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
  },
  {
    "fieldName": "targetImageUrl",
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
cp payloads/product-replacement.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh product-replacement request.json
# Or: node examples/javascript/run.mjs product-replacement request.json
# Or: python3 examples/python/run.py product-replacement request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/source-image.jpg",
  "targetOriginUrl": "https://example.com/product.jpg",
  "sourceImageUrl": "https://example.com/source-product.jpg",
  "targetImageUrl": "https://example.com/target-product.png",
  "denoiseStrength": 0.5,
  "imageOutputWidth": 1024,
  "imageOutputHeight": 1024,
  "outputNum": 1
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

- [Request definition](../../schemas/product-replacement.request.json) — field-descriptors
- [Response definition](../../schemas/product-replacement.response.json) — field-descriptors
- [Editable request sample](../../payloads/product-replacement.json)
- [Response fixture](../../examples/responses/product-replacement.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_product_replacement`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
