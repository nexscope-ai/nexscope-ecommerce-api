# AI Video Reclone API

Recreate a product marketing video from references.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-video-reclone?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Generate a product marketing video using a reference video, reference images, and model-specific generation settings.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-video-reclone/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-video-reclone/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `refVideoUrl` | string | Yes | Public URL of the reference video. | {} |
| `refImageList` | array | Yes | Public image URLs for product or visual references. | {} |
| `videoType` | string | Yes | Video model. Supported values: seedance-2-0, seedance-2-0-fast, seedance-2-0-mini, seedance-2-5, or happyhorse-v2. | {} |
| `videoTime` | integer | No | Optional target video duration in seconds. Seedance 2.0, Fast, Mini, and HappyHorse V2 support any integer from 5 through 15; Seedance 2.5 supports 5, 10, 15, 20, 25, or 30. | {"allowedValuesBy": {"videoType": {"seedance-2-0": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seedance-2-0-mini": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seedance-2-0-fast": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "happyhorse-v2": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seedance-2-5": [5, 10, 15, 20, 25, 30]}}, "allowedValues": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 25, 30]} |
| `resolution` | string | Yes | Target video resolution supported by the selected model, such as 720p or 1080p. | {} |
| `aspectRatio` | string | No | Target video aspect ratio supported by the selected model. | {} |
| `saleCountry` | string | Yes | Target market country code used to localize the recreated video. | {} |
| `targetLanguage` | string | Yes | Target spoken and on-screen language for the recreated video. | {} |
| `productInfo` | string | No | Concise product information used to guide the recreation. Maximum 2500 characters. | {} |
| `prompt` | string | No | Optional creative direction prompt. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "refVideoUrl",
    "mediaKind": "video",
    "acceptedContentTypes": [
      "video/mp4",
      "video/quicktime"
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
    "fieldName": "refImageList",
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
cp payloads/ai-video-reclone.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-video-reclone request.json
# Or: node examples/javascript/run.mjs ai-video-reclone request.json
# Or: python3 examples/python/run.py ai-video-reclone request.json
```

### Published request example

```json
{
  "refVideoUrl": "https://example.com/reference-video.mp4",
  "refImageList": [
    "https://example.com/product.jpg"
  ],
  "videoType": "seedance-2-0-fast",
  "videoTime": 10,
  "resolution": "720p",
  "aspectRatio": "9:16",
  "saleCountry": "US",
  "targetLanguage": "English",
  "productInfo": "Slim shockproof phone case with a clear finish.",
  "prompt": "highlight the slim protective design"
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

- [Request definition](../../schemas/ai-video-reclone.request.json) — field-descriptors
- [Response definition](../../schemas/ai-video-reclone.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-video-reclone.json)
- [Response fixture](../../examples/responses/ai-video-reclone.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_video_reclone`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
