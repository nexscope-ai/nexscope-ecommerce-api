# Image Captioning API

Create an image prompt extraction task and return the completed result.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/image-captioning?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Extract descriptive prompts or selling-point text from one or more images.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/image-captioning/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/image-captioning/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `type` | integer | Yes | Analysis type. Supported values: 5 (similar-image prompt), 13 (scene prompt), 30 (image-to-video analysis), 69 (apparel selling points), 71 (product selling points), 73 (sales-video script), 89 (video-reclone prompt). | {} |
| `imageUrlList` | array | Yes | Public image URLs used for analysis. Provide no more than 6 images for modes that accept multiple images. | {"maxItems": 6, "minItems": 1} |
| `keyword` | string | No | Optional keyword context. | {} |
| `provider` | string | No | Analysis provider. Supported values: API_PRE_POINT (default), API_LAYOUT_DESC. | {} |
| `refVideoUrl` | string | No | Reference video URL. Required when type is 89. | {"requiredWhen": {"type": [89]}} |
| `saleCountry` | string | No | Target sale country code. | {} |
| `targetLanguage` | string | No | Target language for generated text. Used by video-reclone analysis. | {} |
| `duration` | integer | No | Target duration in seconds. Used by video-reclone analysis. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageUrlList",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 6,
    "minWidthPixels": null,
    "maxWidthPixels": null,
    "minHeightPixels": null,
    "maxHeightPixels": null,
    "minAspectRatio": null,
    "maxAspectRatio": null
  },
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
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/image-captioning.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh image-captioning request.json
# Or: node examples/javascript/run.mjs image-captioning request.json
# Or: python3 examples/python/run.py image-captioning request.json
```

### Published request example

```json
{
  "type": 71,
  "imageUrlList": [
    "https://example.com/product.jpg"
  ],
  "keyword": "phone case",
  "provider": "API_PRE_POINT"
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

- [Request definition](../../schemas/image-captioning.request.json) — field-descriptors
- [Response definition](../../schemas/image-captioning.response.json) — field-descriptors
- [Editable request sample](../../payloads/image-captioning.json)
- [Response fixture](../../examples/responses/image-captioning.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_image_captioning`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
