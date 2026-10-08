# Wan 3 Video Generation

Generate ecommerce videos with the wan3 model.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/wan-3-video-generation?view=api&co-from=github-ecommerce-api)

Category: Video Generation Models · Creative API

Generate a Wan 3 video from up to 10 image references, first and final frames, or a reference video. The model is fixed by this API, so videoType must not be supplied in the request.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/wan-3-video-generation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/wan-3-video-generation/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `videoTime` | integer | Yes | Video duration in seconds. Supported values: 5, 10, 15, 20, 25, 30. | {"allowedValues": [5, 10, 15, 20, 25, 30]} |
| `prompt` | string | Yes | Video generation prompt describing motion, subject consistency, camera movement, and the ecommerce scene. Maximum 2000 characters. | {"maxLength": 2000} |
| `promptOptimizer` | boolean | No | Whether Nexscope should optimize the video prompt before generation. Defaults to false. | {} |
| `isPro` | boolean | No | Whether to use the model's professional generation mode when supported. Defaults to false. | {} |
| `resolution` | string | Yes | Output resolution. Supported values: 480p, 720p, 1080p. | {"allowedValues": ["480p", "720p", "1080p"]} |
| `imageUrl` | string | No | Public URL of a first-frame or primary reference image. | {} |
| `imageList` | array | No | Public reference image URLs. Provide 1 to 10 images. | {"maxItems": 10, "minItems": 1} |
| `video` | array | No | Optional public reference-video URL list. Reference-video mode cannot be combined with image references or a final-frame image. | {"minItems": 1, "conflictsWith": ["imageUrl", "imageList", "lastFrameImageUrl"]} |
| `aspectRatio` | string | No | Target video aspect ratio supported by this model. Supported values: 16:9, 4:3, 1:1, 3:4, 9:16. | {"allowedValues": ["16:9", "4:3", "1:1", "3:4", "9:16"]} |
| `lastFrameImageUrl` | string | No | Optional public URL of the final-frame image. Use imageUrl for the first frame; do not combine first-and-last-frame mode with imageList or video. | {"conflictsWith": ["imageList", "video"]} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Add at least one reference using imageUrl, imageList, or video. Fields: `imageUrl`, `imageList`, `video`.

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
  },
  {
    "fieldName": "imageList",
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
  },
  {
    "fieldName": "video",
    "mediaKind": "video",
    "acceptedContentTypes": [
      "video/mp4",
      "video/quicktime"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 5,
    "minWidthPixels": null,
    "maxWidthPixels": null,
    "minHeightPixels": null,
    "maxHeightPixels": null,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
  {
    "fieldName": "lastFrameImageUrl",
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
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/wan-3-video-generation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh wan-3-video-generation request.json
# Or: node examples/javascript/run.mjs wan-3-video-generation request.json
# Or: python3 examples/python/run.py wan-3-video-generation request.json
```

### Published request example

```json
{
  "videoTime": 5,
  "prompt": "Keep the product consistent while the camera slowly orbits and highlights material details.",
  "imageUrl": "https://example.com/source-image.jpg",
  "resolution": "480p"
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

- [Request definition](../../schemas/wan-3-video-generation.request.json) — field-descriptors
- [Response definition](../../schemas/wan-3-video-generation.response.json) — field-descriptors
- [Editable request sample](../../payloads/wan-3-video-generation.json)
- [Response fixture](../../examples/responses/wan-3-video-generation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_wan_3_video_generation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
