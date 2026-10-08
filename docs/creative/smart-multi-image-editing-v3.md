# Smart Multi-Image Editing API v3

Fuse multiple images with an instruction prompt.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/smart-multi-image-editing-v3?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create an edited output from multiple source images using prompt, provider, resolution, and quality controls.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/smart-multi-image-editing-v3/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/smart-multi-image-editing-v3/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageList` | array | Yes | Public image URLs to combine or reference. Provide no more than 6 JPG, JPEG, PNG, or WEBP images; each image must be at most 10 MB and between 800 and 4096 pixels. | {"maxItems": 6, "minItems": 1} |
| `provider` | string | Yes | Image model. Supported values: BANANA, BANANA_2, BANANA_PRO, WAN2_7, QWEN_IMAGE_3_PRO, SEEDREAM5, GPT_2_IMAGE, or AIDRAW_EDIT. | {"allowedValues": ["BANANA", "BANANA_2", "BANANA_PRO", "WAN2_7", "QWEN_IMAGE_3_PRO", "SEEDREAM5", "GPT_2_IMAGE", "AIDRAW_EDIT"]} |
| `prompt` | string | No | Optional fusion instruction, up to 600 characters. | {} |
| `outputNum` | integer | No | Number of images to generate. Defaults to 1. | {} |
| `resolution` | string | No | Target resolution preset. | {} |
| `aspectRatio` | string | No | Target aspect ratio. | {} |
| `supplyType` | string | No | Generation route. Supported values: eco or stable. Defaults to stable. | {} |
| `needOptimize` | boolean | No | Whether the prompt should be optimized upstream. | {} |
| `template` | string | No | Optional fusion template. Supported values: outfit-fusion, outfit-try-on. | {} |
| `quality` | string | No | GPT Image quality only. Supported values: low, medium, or high. Defaults to medium. | {} |

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
    "maxFiles": 6,
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
cp payloads/smart-multi-image-editing-v3.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh smart-multi-image-editing-v3 request.json
# Or: node examples/javascript/run.mjs smart-multi-image-editing-v3 request.json
# Or: python3 examples/python/run.py smart-multi-image-editing-v3 request.json
```

### Published request example

```json
{
  "imageList": [
    "https://example.com/product.jpg",
    "https://example.com/model-reference.jpg"
  ],
  "provider": "BANANA_PRO",
  "prompt": "combine the product with the model in a clean studio scene",
  "outputNum": 1,
  "resolution": "1K",
  "aspectRatio": "1:1",
  "supplyType": "stable",
  "needOptimize": true,
  "template": "outfit-fusion",
  "quality": "medium"
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

- [Request definition](../../schemas/smart-multi-image-editing-v3.request.json) — field-descriptors
- [Response definition](../../schemas/smart-multi-image-editing-v3.response.json) — field-descriptors
- [Editable request sample](../../payloads/smart-multi-image-editing-v3.json)
- [Response fixture](../../examples/responses/smart-multi-image-editing-v3.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_smart_multi_image_editing_v3`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
