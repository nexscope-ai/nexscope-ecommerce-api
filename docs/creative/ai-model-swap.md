# AI Model Swap API

Swap an ecommerce product image onto a target model.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-model-swap?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Generate model images by combining a source product image with a model head image, optional masks, scene references, and prompt guidance.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-model-swap/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-model-swap/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of the source product or outfit image. The image must be up to 20 MB and between 385 and 8192 pixels in both width and height. | {} |
| `modelHeadImageUrl` | string | Yes | Public URL of the target model head image. The image must be up to 5 MB and between 512 and 2048 pixels in both width and height. | {} |
| `imageSegUrl` | string | No | Optional segmentation mask URL for the source image. | {} |
| `sceneImgUrl` | string | No | Optional scene reference image URL. The image must be up to 10 MB and between 768 and 4096 pixels in both width and height. | {} |
| `sceneStrength` | number | No | Scene reference strength from 0 to 1. Defaults to 0.7. | {} |
| `modelPrompt` | string | No | Comma-separated model appearance terms, such as smile, laugh, sitting, lying, fat, plump, slim, sideways, profile, back, or bald. | {} |
| `customPrompt` | string | No | Positive generation prompt, up to 600 characters. | {} |
| `customNegPrompt` | string | No | Negative prompt to avoid unwanted artifacts. | {} |
| `genOriRes` | boolean | No | Whether to generate the original resolution. Defaults to false. | {} |
| `realModel` | boolean | No | Whether to prefer a realistic model style. | {} |
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
    "minWidthPixels": 385,
    "maxWidthPixels": 8192,
    "minHeightPixels": 385,
    "maxHeightPixels": 8192,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "modelHeadImageUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "5242880",
    "maxFiles": 1,
    "minWidthPixels": 512,
    "maxWidthPixels": 2048,
    "minHeightPixels": 512,
    "maxHeightPixels": 2048,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "imageSegUrl",
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
    "fieldName": "sceneImgUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "10485760",
    "maxFiles": 1,
    "minWidthPixels": 768,
    "maxWidthPixels": 4096,
    "minHeightPixels": 768,
    "maxHeightPixels": 4096,
    "minAspectRatio": null,
    "maxAspectRatio": null
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ai-model-swap.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-model-swap request.json
# Or: node examples/javascript/run.mjs ai-model-swap request.json
# Or: python3 examples/python/run.py ai-model-swap request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/source-image.jpg",
  "modelHeadImageUrl": "https://example.com/model-reference.jpg",
  "imageSegUrl": "https://example.com/mask.png",
  "sceneImgUrl": "https://example.com/scene.jpg",
  "sceneStrength": 0.7,
  "modelPrompt": "smile, slim",
  "customPrompt": "clean ecommerce catalog photo",
  "customNegPrompt": "blur, distorted hands",
  "genOriRes": false,
  "realModel": true,
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

- [Request definition](../../schemas/ai-model-swap.request.json) — field-descriptors
- [Response definition](../../schemas/ai-model-swap.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-model-swap.json)
- [Response fixture](../../examples/responses/ai-model-swap.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_model_swap`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
