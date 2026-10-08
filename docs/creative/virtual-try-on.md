# Virtual Try-On API

Place a product naturally onto a person or model image.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/virtual-try-on?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Generate wearable-product imagery from a source person image and target product image.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/virtual-try-on/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/virtual-try-on/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the wearable product image. The image must be between 300 and 4096 pixels in both width and height. The width-to-height ratio must be between 0.4 and 2.5. | {} |
| `targetOriginUrl` | string | Yes | Public URL of the person or model image. | {} |
| `targetMaskUrl` | string | Yes | Public URL of the black-and-white target wear-area mask. Required because this API accepts custom target images rather than saved upstream materials. | {} |
| `productCategory` | string | No | Product category. Supported values: footwear (shoes), luggage (bags), eyewear (glasses), necklace, hat, earring, ring, wristband, watch, headwear, belt, other. | {} |
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
    "minWidthPixels": 300,
    "maxWidthPixels": 4096,
    "minHeightPixels": 300,
    "maxHeightPixels": 4096,
    "minAspectRatio": 0.4,
    "maxAspectRatio": 2.5
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
    "fieldName": "targetMaskUrl",
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
cp payloads/virtual-try-on.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh virtual-try-on request.json
# Or: node examples/javascript/run.mjs virtual-try-on request.json
# Or: python3 examples/python/run.py virtual-try-on request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "targetOriginUrl": "https://example.com/model-reference.jpg",
  "targetMaskUrl": "https://example.com/mask.png",
  "productCategory": "hat",
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

- [Request definition](../../schemas/virtual-try-on.request.json) — field-descriptors
- [Response definition](../../schemas/virtual-try-on.response.json) — field-descriptors
- [Editable request sample](../../payloads/virtual-try-on.json)
- [Response fixture](../../examples/responses/virtual-try-on.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_virtual_try_on`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
