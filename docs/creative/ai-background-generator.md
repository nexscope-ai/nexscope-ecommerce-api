# AI Background Generator API

Generate an ecommerce scene image from a prompt.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ai-background-generator?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Create product or lifestyle scene images from text prompts and optional reference images.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ai-background-generator/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/ai-background-generator/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `prompt` | string | Yes | Text prompt describing the desired scene. | {} |
| `imageUrl` | string | No | Optional reference image URL. | {} |
| `style` | string | No | Style preset. Supported values: scene-material, portrait-material, ancient-chinese, expressive-sketch, cyberpunk, pixel-illustration, tranquil-ink, anime-line-art, makoto-shinkai, hayao-miyazaki, cg, monochrome-illustration, retro-anime, chibi-character, realistic-oil-painting, c4d-paper-cut, expressive-watercolor, fresh-anime. | {} |
| `scale` | string | No | Output aspect ratio. Supported values: 1:1, 16:9, 9:16. Defaults to 1:1. | {} |
| `outputNum` | integer | No | Number of images to generate, from 1 to 4. Defaults to 4. | {} |

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
cp payloads/ai-background-generator.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ai-background-generator request.json
# Or: node examples/javascript/run.mjs ai-background-generator request.json
# Or: python3 examples/python/run.py ai-background-generator request.json
```

### Published request example

```json
{
  "prompt": "a premium phone case on a clean marble desk",
  "imageUrl": "https://example.com/product.jpg",
  "style": "scene-material",
  "scale": "1:1",
  "outputNum": 4
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

- [Request definition](../../schemas/ai-background-generator.request.json) — field-descriptors
- [Response definition](../../schemas/ai-background-generator.response.json) — field-descriptors
- [Editable request sample](../../payloads/ai-background-generator.json)
- [Response fixture](../../examples/responses/ai-background-generator.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ai_background_generator`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
