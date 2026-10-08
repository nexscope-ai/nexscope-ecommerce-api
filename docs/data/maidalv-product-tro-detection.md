# Product TRO Detection API

Assess product imagery for TRO, trademark, patent, and copyright infringement risk.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/maidalv-product-tro-detection?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Analyzes a main product image with optional evidence images, text, keywords, and language.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/maidalv-product-tro-detection/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `mainProductImage` | string | Yes | Public HTTPS URL of the main product image. | {} |
| `referenceImages` | array | No | Public reference image URLs. | {} |
| `otherProductImages` | array | No | Additional product image URLs. | {} |
| `ipImages` | array | No | Known intellectual-property evidence image URLs. | {} |
| `referenceText` | string | No | Reference text associated with the product. | {} |
| `description` | string | No | Product description used as additional evidence. | {} |
| `ipKeywords` | array | No | Intellectual-property keywords. | {} |
| `language` | string | No | Requested response language. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "mainProductImage",
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
    "fieldName": "referenceImages",
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
    "fieldName": "otherProductImages",
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
    "fieldName": "ipImages",
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
cp payloads/maidalv-product-tro-detection.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh maidalv-product-tro-detection request.json
# Or: node examples/javascript/run.mjs maidalv-product-tro-detection request.json
# Or: python3 examples/python/run.py maidalv-product-tro-detection request.json
```

### Published request example

```json
{
  "language": "en",
  "mainProductImage": "https://example.com/product.jpg"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "checkId": "check-id",
  "status": "success",
  "total": 2,
  "riskLevel": "medium",
  "data": [],
  "costToken": 225000
}
```

## Full definitions

- [Request definition](../../schemas/maidalv-product-tro-detection.request.json) — field-descriptors
- [Response definition](../../schemas/maidalv-product-tro-detection.response.json) — field-descriptors
- [Editable request sample](../../payloads/maidalv-product-tro-detection.json)
- [Response fixture](../../examples/responses/maidalv-product-tro-detection.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_maidalv_product_tro_detection`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
