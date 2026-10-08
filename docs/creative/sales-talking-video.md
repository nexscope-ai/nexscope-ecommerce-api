# Sales Talking Video API

Generate a talking sales video.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/sales-talking-video?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create a product-selling video from prompt and product image references.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/sales-talking-video/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/sales-talking-video/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `prompt` | string | Yes | Sales script or creative prompt. | {} |
| `imageList` | array | Yes | Public product image URLs. Provide up to 30 images for Seedance 2.5 or up to 9 images for the other supported models. | {"maxItemsBy": {"videoType": {"seedance-2-0": 9, "seedance-2-0-mini": 9, "seedance-2-0-fast": 9, "happyhorse-v2": 9, "seedance-2-5": 30}}, "minItems": 1, "maxItems": 30} |
| `videoType` | string | Yes | Video model. Supported values: seedance-2-0, seedance-2-0-fast, seedance-2-0-mini, seedance-2-5, or happyhorse-v2. | {"allowedValues": ["seedance-2-0", "seedance-2-0-fast", "seedance-2-0-mini", "seedance-2-5", "happyhorse-v2"]} |
| `videoTime` | integer | No | Target duration in seconds. Seedance 2.0, Fast, Mini, and HappyHorse V2 support 5, 10, or 15; Seedance 2.5 also supports 30. | {"allowedValuesBy": {"videoType": {"seedance-2-0": [5, 10, 15], "seedance-2-0-mini": [5, 10, 15], "seedance-2-0-fast": [5, 10, 15], "happyhorse-v2": [5, 10, 15], "seedance-2-5": [5, 10, 15, 30]}}, "allowedValues": [5, 10, 15, 30]} |
| `aspectRatio` | string | No | Target aspect ratio: 16:9, 9:16, 1:1, 4:3, 3:4, or 21:9. | {"allowedValues": ["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"]} |
| `isPro` | boolean | No | Enable Pro mode for any Seedance model. HappyHorse V2 does not support Pro mode. When enabled without resolution, the default is 720p. | {"forbiddenWhen": {"videoType": ["happyhorse-v2"]}} |
| `resolution` | string | No | Target resolution. Seedance 2.0 and 2.5 support 480p, 720p, or 1080p; Seedance Fast and Mini support 480p or 720p; HappyHorse V2 supports 720p or 1080p. | {"allowedValuesBy": {"videoType": {"seedance-2-0": ["480p", "720p", "1080p"], "seedance-2-0-mini": ["480p", "720p"], "seedance-2-0-fast": ["480p", "720p"], "happyhorse-v2": ["720p", "1080p"], "seedance-2-5": ["480p", "720p", "1080p"]}}, "allowedValues": ["480p", "720p", "1080p"]} |

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
    "maxFileSizeBytes": "20971520",
    "maxFiles": 30,
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
cp payloads/sales-talking-video.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh sales-talking-video request.json
# Or: node examples/javascript/run.mjs sales-talking-video request.json
# Or: python3 examples/python/run.py sales-talking-video request.json
```

### Published request example

```json
{
  "prompt": "Introduce this shockproof phone case in an upbeat tone.",
  "imageList": [
    "https://example.com/product.jpg"
  ],
  "videoType": "seedance-2-0-fast",
  "videoTime": 10,
  "aspectRatio": "9:16",
  "isPro": false,
  "resolution": "720p"
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

- [Request definition](../../schemas/sales-talking-video.request.json) — field-descriptors
- [Response definition](../../schemas/sales-talking-video.response.json) — field-descriptors
- [Editable request sample](../../payloads/sales-talking-video.json)
- [Response fixture](../../examples/responses/sales-talking-video.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_sales_talking_video`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
