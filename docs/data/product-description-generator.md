# Product Description Generator API

Create or query asynchronous product-description generation tasks.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/product-description-generator?view=api&co-from=github-ecommerce-api)

Category: AI Content Generation · Data API

Creates a text-generation task from product copy instructions and image URLs, or queries a known task ID.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/product-description-generator/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operation` | string | No | create (default) or query. | {"allowedValues": ["create", "query"]} |
| `prompt` | string | No | Product-copy generation instruction; required by create. | {"requiredWhen": {"operation": ["create"]}, "maxLength": 100000} |
| `imageUrls` | array | No | Media URLs used as context. Pass an empty array for text-only generation; use up to 10 images or typically one video. | {"maxItems": 10} |
| `thinkingLevel` | string | No | Reasoning level required by create. GEM_3_1_PRO does not support minimal. | {"requiredWhen": {"operation": ["create"]}, "allowedValuesBy": {"model": {"GEM_3_FLASH": ["minimal", "low", "medium", "high"], "GEM_3_1_PRO": ["low", "medium", "high"]}}, "allowedValues": ["minimal", "low", "medium", "high"]} |
| `model` | string | No | Text-generation model. GEM_3_FLASH is the default. | {"allowedValues": ["GEM_3_FLASH", "GEM_3_1_PRO"]} |
| `memberId` | string | No | Optional provider member identifier used by create and query. | {} |
| `taskId` | string | No | Provider task ID returned by create; required by operation=query. | {"requiredWhen": {"operation": ["query"]}} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageUrls",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp",
      "video/mp4",
      "video/quicktime"
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
cp payloads/product-description-generator.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh product-description-generator request.json
# Or: node examples/javascript/run.mjs product-description-generator request.json
# Or: python3 examples/python/run.py product-description-generator request.json
```

### Published request example

```json
{
  "model": "GEM_3_FLASH",
  "thinkingLevel": "minimal",
  "operation": "create",
  "imageUrls": [],
  "prompt": "Write a product description for a wireless speaker."
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "taskId": "123456789",
  "status": "PROCESSING",
  "content": "Example product description.",
  "promptTokens": 120,
  "completionTokens": 350,
  "totalTokens": 470,
  "errorMsg": "Generation failed.",
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/product-description-generator.request.json) — field-descriptors
- [Response definition](../../schemas/product-description-generator.response.json) — field-descriptors
- [Editable request sample](../../payloads/product-description-generator.json)
- [Response fixture](../../examples/responses/product-description-generator.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_product_description_generator`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
