# Product Logo Detection & Removal API

Detect and remove product logos.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/product-logo-detection-removal?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Detect and optionally remove a specified brand logo from a product image.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/product-logo-detection-removal/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/product-logo-detection-removal/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the product image. The image must be up to 20 MB. | {} |
| `brandName` | string | Yes | Brand name to detect or remove. | {} |
| `isDetect` | boolean | No | Whether to only detect instead of removing. | {} |

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
cp payloads/product-logo-detection-removal.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh product-logo-detection-removal request.json
# Or: node examples/javascript/run.mjs product-logo-detection-removal request.json
# Or: python3 examples/python/run.py product-logo-detection-removal request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "brandName": "SampleBrand",
  "isDetect": false
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

- [Request definition](../../schemas/product-logo-detection-removal.request.json) — field-descriptors
- [Response definition](../../schemas/product-logo-detection-removal.response.json) — field-descriptors
- [Editable request sample](../../payloads/product-logo-detection-removal.json)
- [Response fixture](../../examples/responses/product-logo-detection-removal.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_product_logo_detection_removal`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
