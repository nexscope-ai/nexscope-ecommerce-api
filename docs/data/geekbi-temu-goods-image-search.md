# Nexscope Temu Image Search API

Image Search using Nexscope Temu data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/geekbi-temu-goods-image-search?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Execute the selected image search operation and preserve provider business fields and extensions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-goods-image-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Provider OSS temporary image URL, obtained through presignedPut and a successful PUT upload with the signature query removed. Replace the example.invalid placeholder before calling; external URLs are rejected upstream. Actual image must be at most 10 MB and JPEG, PNG, GIF, WebP or BMP. | {"minLength": 1, "type": "string", "format": "uri", "maxLength": 2048, "description": "Provider OSS temporary image URL, obtained through presignedPut and a successful PUT upload with the signature query removed. Replace the example.invalid placeholder before calling; external URLs are rejected upstream. Actual image must be at most 10 MB and JPEG, PNG, GIF, WebP or BMP."} |
| `contentType` | string | No | Must match OSS response and actual image bytes; omitted means server detection. | {"enum": ["image/jpeg", "image/png", "image/gif", "image/webp", "image/bmp"], "type": "string", "maxLength": 100, "description": "Must match OSS response and actual image bytes; omitted means server detection."} |

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
      "image/gif",
      "image/webp",
      "image/bmp"
    ],
    "maxFileSizeBytes": "10000000",
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
cp payloads/geekbi-temu-goods-image-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh geekbi-temu-goods-image-search request.json
# Or: node examples/javascript/run.mjs geekbi-temu-goods-image-search request.json
# Or: python3 examples/python/run.py geekbi-temu-goods-image-search request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.invalid/replace-with-provider-oss-image",
  "contentType": "image/jpeg"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errmsg": "ok",
  "columns": [],
  "errcode": 200,
  "items": [],
  "total": 0
}
```

## Full definitions

- [Request definition](../../schemas/geekbi-temu-goods-image-search.request.json) — json-schema
- [Response definition](../../schemas/geekbi-temu-goods-image-search.response.json) — json-schema
- [Editable request sample](../../payloads/geekbi-temu-goods-image-search.json)
- [Response fixture](../../examples/responses/geekbi-temu-goods-image-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_geekbi_temu_goods_image_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
