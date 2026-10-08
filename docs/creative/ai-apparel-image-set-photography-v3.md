# AI Apparel Image Set & Photography API v3

Generate apparel marketing image sets.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-apparel-image-set-photography-v3?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create apparel ecommerce image sets from clothing images with optional model and scene references.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-apparel-image-set-photography-v3/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-apparel-image-set-photography-v3/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageList` | array | Yes | Public apparel image URLs. Provide no more than 5 JPG, JPEG, PNG, or WEBP images; each image must be at most 10 MB and between 384 and 4096 pixels. | {"maxItems": 5, "minItems": 1} |
| `provider` | string | No | Image model. Defaults to BANANA_2. Supported values: BANANA_2, BANANA_2_LITE, BANANA_PRO, WAN2_7, SEEDREAM5_PRO, GPT_2_IMAGE. | {} |
| `sellerPoint` | string | No | Product selling points, up to 2500 characters. Required when isExtractPrePoint is false. | {"requiredWhen": {"isExtractPrePoint": [false]}, "maxLength": 2500} |
| `isExtractPrePoint` | boolean | No | Whether to automatically extract selling points. Defaults to false. When false, sellerPoint is required. | {} |
| `resolution` | string | No | Target resolution supported by the selected provider. | {} |
| `aspectRatio` | string | No | Target aspect ratio. | {} |
| `noText` | boolean | No | Whether generated images should avoid text. | {} |
| `brandKey` | string | No | Optional brand information serialized as a JSON string. Supported keys: brandColor, fontStyle, salesRegion, language, platform, customSettings. | {} |
| `quality` | string | No | GPT Image quality only. Supported values: low, medium, or high. | {} |
| `sensitiveLibraryId` | integer | No | Optional sensitive-word library ID used to screen generated copy. | {} |
| `replaceLibraryId` | integer | No | Optional replacement-word library ID used to rewrite generated copy. | {} |
| `modelImageUrl` | string | No | Optional model reference image URL. | {} |
| `sceneImageUrl` | string | No | Optional scene reference image URL. | {} |
| `isExactScene` | boolean | No | Whether to match the provided scene closely. Defaults to true. | {} |
| `modelAndSceneInfo` | string | No | Model and scene information serialized as a JSON string or concise structured text. | {} |
| `aPlusNum` | integer | No | Number of standard A+ images, from 0 to 12. Defaults to 0. | {} |
| `aPlusProNum` | integer | No | Number of premium A+ images, from 0 to 12. Defaults to 0. | {} |
| `aPlusHasPhone` | boolean | No | Whether A+ output includes phone display layouts. | {} |
| `aPlusAspectRatio` | string | No | A+ output aspect ratio. Supported values: 16:9, 9:16, 1:1, 1:3.7. | {} |
| `modelTypeNum` | integer | No | Number of model images, from 0 to 12. Defaults to 0. | {} |
| `insTypeNum` | integer | No | Number of social-style images, from 0 to 12. Defaults to 0. | {} |
| `sellerTypeNum` | integer | No | Number of selling-point images, from 0 to 12. Defaults to 0. | {} |
| `sizeTypeNum` | integer | No | Number of size-information images, from 0 to 12. Defaults to 0. | {} |
| `whiteTypeNum` | integer | No | Number of white-background images, from 0 to 12. Defaults to 0. | {} |
| `aPlusStyles` | array | No | Optional A+ style entries. Each item may contain a saved style id or a custom prompt. | {} |
| `pointStyles` | array | No | Optional selling-point style entries. Each item may contain a saved style id or a custom prompt. | {} |

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
    "maxFiles": 5,
    "minWidthPixels": 384,
    "maxWidthPixels": 4096,
    "minHeightPixels": 384,
    "maxHeightPixels": 4096,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "modelImageUrl",
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
    "fieldName": "sceneImageUrl",
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
cp payloads/ai-apparel-image-set-photography-v3.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-apparel-image-set-photography-v3 request.json
# Or: node examples/javascript/run.mjs ai-apparel-image-set-photography-v3 request.json
# Or: python3 examples/python/run.py ai-apparel-image-set-photography-v3 request.json
```

### Published request example

```json
{
  "imageList": [
    "https://example.com/product.jpg"
  ],
  "provider": "BANANA_2",
  "sellerPoint": "Lightweight breathable summer dress",
  "isExtractPrePoint": false,
  "resolution": "2K",
  "aspectRatio": "1:1",
  "noText": false,
  "brandKey": "{\"brandColor\":\"#0775FA\",\"fontStyle\":\"sans serif\",\"salesRegion\":\"North America\",\"language\":\"English\",\"platform\":\"Amazon\"}",
  "quality": "medium",
  "sensitiveLibraryId": 1001,
  "replaceLibraryId": 1002,
  "modelImageUrl": "https://example.com/model-reference.jpg",
  "sceneImageUrl": "https://example.com/scene.jpg",
  "isExactScene": true,
  "modelAndSceneInfo": "{\"model\":\"female adult\",\"scene\":\"studio\"}",
  "aPlusNum": 0,
  "aPlusProNum": 0,
  "aPlusHasPhone": false,
  "aPlusAspectRatio": "1:1",
  "modelTypeNum": 0,
  "insTypeNum": 0,
  "sellerTypeNum": 0,
  "sizeTypeNum": 0,
  "whiteTypeNum": 0,
  "aPlusStyles": [
    {
      "id": 1
    },
    {
      "prompt": "clean editorial layout"
    }
  ],
  "pointStyles": [
    {
      "id": 2
    },
    {
      "prompt": "minimal feature callouts"
    }
  ]
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

- [Request definition](../../schemas/ai-apparel-image-set-photography-v3.request.json) — field-descriptors
- [Response definition](../../schemas/ai-apparel-image-set-photography-v3.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-apparel-image-set-photography-v3.json)
- [Response fixture](../../examples/responses/ai-apparel-image-set-photography-v3.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_apparel_image_set_photography_v3`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
