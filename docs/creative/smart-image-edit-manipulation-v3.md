# Smart Image Edit & Manipulation API v3

Edit an image using an instruction prompt.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/smart-image-edit-manipulation-v3?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Perform general image editing with provider, prompt, resolution, aspect ratio, and quality controls.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/smart-image-edit-manipulation-v3/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/smart-image-edit-manipulation-v3/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the image to edit. The image must be between 300 and 4096 pixels in both width and height, and its width-to-height ratio must be between 0.4 and 2.5. | {} |
| `prompt` | string | Yes | Editing instruction. | {} |
| `provider` | string | Yes | Image model. Supported values: BANANA, BANANA_2, BANANA_PRO, WAN2_7, QWEN_IMAGE_3_PRO, SEEDREAM5, GPT_2_IMAGE, or AIDRAW_EDIT. | {"allowedValues": ["BANANA", "BANANA_2", "BANANA_PRO", "WAN2_7", "QWEN_IMAGE_3_PRO", "SEEDREAM5", "GPT_2_IMAGE", "AIDRAW_EDIT"]} |
| `outputNum` | integer | No | Number of images to generate, from 1 to 4. | {} |
| `resolution` | string | No | Target resolution preset. | {} |
| `aspectRatio` | string | No | Target aspect ratio. | {} |
| `supplyType` | string | No | Generation route. Supported values: eco or stable. Defaults to stable. | {} |
| `needOptimize` | boolean | No | Whether the prompt should be optimized upstream. | {} |
| `template` | string | No | Optional Nexscope editing template. Supported values: white-background, product-main-image-retouching, scene-generation, poster-design, add-person-or-object, change-animal, flat-lay-apparel, 3d-apparel, mannequin-to-model, cartoon-illustration, body-reshape, change-style, remove-element, remove-text, remove-watermark, add-watermark. | {} |
| `source` | string | No | Optional traffic or product source code. | {} |
| `quality` | string | No | GPT Image quality only. Supported values: low, medium, or high. Defaults to medium. | {} |

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
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/smart-image-edit-manipulation-v3.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh smart-image-edit-manipulation-v3 request.json
# Or: node examples/javascript/run.mjs smart-image-edit-manipulation-v3 request.json
# Or: python3 examples/python/run.py smart-image-edit-manipulation-v3 request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "prompt": "make the background pure white and keep the product unchanged",
  "provider": "BANANA_PRO",
  "outputNum": 1,
  "resolution": "1K",
  "aspectRatio": "1:1",
  "supplyType": "stable",
  "needOptimize": true,
  "template": "white-background",
  "source": "api",
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

- [Request definition](../../schemas/smart-image-edit-manipulation-v3.request.json) — field-descriptors
- [Response definition](../../schemas/smart-image-edit-manipulation-v3.response.json) — field-descriptors
- [Editable request sample](../../payloads/smart-image-edit-manipulation-v3.json)
- [Response fixture](../../examples/responses/smart-image-edit-manipulation-v3.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_smart_image_edit_manipulation_v3`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
