# AI Suit Virtual Try-On API

Generate try-on images for one-piece outfits.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-suit-virtual-try-on?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Dress a model image with a one-piece outfit or suit image, supporting optional garment and model masks.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-suit-virtual-try-on/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-suit-virtual-try-on/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `suitOriginUrl` | string | Yes | Public URL of the original one-piece garment image. The image must be up to 20 MB and between 385 and 4096 pixels in both width and height. | {} |
| `modelImageUrl` | string | Yes | Public URL of the model image. | {} |
| `suitImageUrl` | string | No | Optional processed suit mask or crop URL. | {} |
| `modelMaskImageUrl` | string | No | Optional mask URL for the model body area. | {} |
| `outputNum` | integer | No | Number of images to generate, from 1 to 4. Defaults to 1. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "suitOriginUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "20971520",
    "maxFiles": 1,
    "minWidthPixels": 385,
    "maxWidthPixels": 4096,
    "minHeightPixels": 385,
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
    "fieldName": "suitImageUrl",
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
    "fieldName": "modelMaskImageUrl",
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
cp payloads/ai-suit-virtual-try-on.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-suit-virtual-try-on request.json
# Or: node examples/javascript/run.mjs ai-suit-virtual-try-on request.json
# Or: python3 examples/python/run.py ai-suit-virtual-try-on request.json
```

### Published request example

```json
{
  "suitOriginUrl": "https://example.com/suit.jpg",
  "modelImageUrl": "https://example.com/model-reference.jpg",
  "suitImageUrl": "https://example.com/suit-mask.png",
  "modelMaskImageUrl": "https://example.com/mask.png",
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

- [Request definition](../../schemas/ai-suit-virtual-try-on.request.json) — field-descriptors
- [Response definition](../../schemas/ai-suit-virtual-try-on.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-suit-virtual-try-on.json)
- [Response fixture](../../examples/responses/ai-suit-virtual-try-on.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_suit_virtual_try_on`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
