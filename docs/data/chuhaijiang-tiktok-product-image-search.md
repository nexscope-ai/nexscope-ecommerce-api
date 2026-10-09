# Nexscope TikTok Product Image Search API

Nexscope TikTok Product Image Search with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-product-image-search?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Product Image Search. Known row fields: id, product_name, product_images, floor_price, ceiling_price, product_gmv. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-product-image-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `osKey` | string | Yes | ossKey from a completed NexScope API Asset upload and confirmation; obtain this value before calling. | {"minLength": 1, "type": "string", "example": "returned-key", "description": "ossKey from a completed NexScope API Asset upload and confirmation; obtain this value before calling."} |
| `country` | string | No | Uppercase two-letter market code. | {"type": "string", "pattern": "^[A-Z]{2}$", "default": "US", "example": "US", "description": "Uppercase two-letter market code."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "osKey",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png"
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
cp payloads/chuhaijiang-tiktok-product-image-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-product-image-search request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-product-image-search request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-product-image-search request.json
```

### Published request example

```json
{
  "osKey": "returned-key",
  "country": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errmsg": "ok",
  "data": {
    "items": [
      {
        "id": null,
        "product_name": null,
        "product_images": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-product-image-search.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-product-image-search.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-product-image-search.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-product-image-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_product_image_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
