# AI Product Marketing Image Set API v4

Generate product marketing image sets.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-product-marketing-image-set-v4?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create ecommerce product marketing materials such as selling-point images and A+ style visuals from product images and brief inputs.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-product-marketing-image-set-v4/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-product-marketing-image-set-v4/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageList` | array | Yes | Public product image URLs. Provide no more than 5 JPG, JPEG, PNG, or WEBP images; each image must be at most 10 MB and between 800 and 4096 pixels. | {"maxItems": 5, "minItems": 1} |
| `provider` | string | No | Image model. Defaults to BANANA_2. Supported values: BANANA_2, BANANA_2_LITE, BANANA_PRO, WAN2_7, SEEDREAM5_PRO, GPT_2_IMAGE. | {} |
| `sellerPoint` | string | No | Product selling points, up to 2500 characters. Required when isExtractPrePoint is false. | {"requiredWhen": {"isExtractPrePoint": [false]}, "maxLength": 2500} |
| `isExtractPrePoint` | boolean | No | Whether to automatically extract selling points. Defaults to false. When false, sellerPoint is required. | {} |
| `resolution` | string | No | Target resolution supported by the selected provider. | {} |
| `aspectRatio` | string | No | Target aspect ratio supported by the selected provider. | {} |
| `noText` | boolean | No | Whether generated images should avoid text. | {} |
| `brandKey` | string | No | Optional brand information serialized as a JSON string. Supported keys: brandColor, fontStyle, salesRegion, language, platform, customSettings. | {} |
| `quality` | string | No | GPT Image quality only. Supported values: low, medium, or high. | {} |
| `sensitiveLibraryId` | integer | No | Optional sensitive-word library ID used to screen generated copy. | {} |
| `replaceLibraryId` | integer | No | Optional replacement-word library ID used to rewrite generated copy. | {} |
| `aPlusNum` | integer | No | Number of standard A+ images, from 0 to 12. Defaults to 0. | {} |
| `aPlusProNum` | integer | No | Number of premium A+ images, from 0 to 12. Defaults to 0. | {} |
| `aPlusHasPhone` | boolean | No | Whether A+ output includes phone display layouts. | {} |
| `aPlusAspectRatio` | string | No | Premium A+ aspect ratio. Supported values: 16:9, 9:16, 1:1, 1:3.7. | {} |
| `sellerTypeNum` | integer | No | Number of selling-point images, from 0 to 12. Defaults to 0. | {} |
| `sceneTypeNum` | integer | No | Number of scene images, from 0 to 12. Defaults to 0. | {} |
| `closeUpTypeNum` | integer | No | Number of close-up images, from 0 to 12. Defaults to 0. | {} |
| `closeUpWhiteTypeNum` | integer | No | Number of white-background close-up images, from 0 to 12. Defaults to 0. | {} |
| `whiteBgTypeNum` | integer | No | Number of white-background images, from 0 to 12. Defaults to 0. | {} |
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
cp payloads/ai-product-marketing-image-set-v4.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-product-marketing-image-set-v4 request.json
# Or: node examples/javascript/run.mjs ai-product-marketing-image-set-v4 request.json
# Or: python3 examples/python/run.py ai-product-marketing-image-set-v4 request.json
```

### Published request example

```json
{
  "imageList": [
    "https://example.com/product.jpg"
  ],
  "provider": "BANANA_2",
  "sellerPoint": "Shockproof, slim, clear phone case",
  "isExtractPrePoint": false,
  "resolution": "2K",
  "aspectRatio": "1:1",
  "noText": false,
  "brandKey": "{\"brandColor\":\"#0775FA\",\"fontStyle\":\"sans serif\",\"salesRegion\":\"North America\",\"language\":\"English\",\"platform\":\"Amazon\"}",
  "quality": "medium",
  "sensitiveLibraryId": 1001,
  "replaceLibraryId": 1002,
  "aPlusNum": 0,
  "aPlusProNum": 0,
  "aPlusHasPhone": false,
  "aPlusAspectRatio": "1:1",
  "sellerTypeNum": 0,
  "sceneTypeNum": 0,
  "closeUpTypeNum": 0,
  "closeUpWhiteTypeNum": 0,
  "whiteBgTypeNum": 0,
  "aPlusStyles": [
    {
      "id": 1
    },
    {
      "prompt": "clean premium layout"
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

- [Request definition](../../schemas/ai-product-marketing-image-set-v4.request.json) — field-descriptors
- [Response definition](../../schemas/ai-product-marketing-image-set-v4.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-product-marketing-image-set-v4.json)
- [Response fixture](../../examples/responses/ai-product-marketing-image-set-v4.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_product_marketing_image_set_v4`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
