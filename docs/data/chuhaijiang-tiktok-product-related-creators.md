# Nexscope TikTok Product Related Creators API

Nexscope TikTok Product Related Creators with public market data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-product-related-creators?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Provider business records for Nexscope TikTok Product Related Creators. Known row fields: user_id, uid, unique_id, nickname. Missing and null fields remain unchanged; monetary values retain their original unit and runtime type.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-product-related-creators/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase TikTok market code. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"], "type": "string", "example": "us", "description": "Lowercase TikTok market code."} |
| `page` | integer | No | Page number, starting at 1. | {"type": "integer", "example": 1, "description": "Page number, starting at 1.", "minimum": 1} |
| `pageSize` | integer | No | Maximum records per page. | {"maximum": 10, "type": "integer", "minimum": 1, "example": 5, "description": "Maximum records per page."} |
| `id` | string | Yes | Product ID, preserved as a string. | {"minLength": 1, "type": "string", "example": "1732052189676081387", "description": "Product ID, preserved as a string."} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-product-related-creators.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-product-related-creators request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-product-related-creators request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-product-related-creators request.json
```

### Published request example

```json
{
  "country": "us",
  "id": "1732052189676081387",
  "page": 1,
  "pageSize": 5
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
        "user_id": null,
        "uid": null,
        "unique_id": null
      }
    ]
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-product-related-creators.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-product-related-creators.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-product-related-creators.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-product-related-creators.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_product_related_creators`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
