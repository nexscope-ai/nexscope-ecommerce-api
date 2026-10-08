# Reverse Product Image Search API

Find visually similar Amazon products from a public image URL.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/reverse-product-image-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Runs the server-side image-search and enrichment workflow without exposing local file paths or intermediate artifacts.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/reverse-product-image-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Publicly accessible product image URL. | {} |
| `amazonDomain` | string | Yes | Amazon marketplace domain. | {} |
| `topN` | integer | No | Maximum number of ranked matches to return after enrichment. | {} |
| `sort` | string | No | Optional provider sort mode. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/reverse-product-image-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh reverse-product-image-search request.json
# Or: node examples/javascript/run.mjs reverse-product-image-search request.json
# Or: python3 examples/python/run.py reverse-product-image-search request.json
```

### Published request example

```json
{
  "imageUrl": "https://m.media-amazon.com/images/I/31SkgVLWSuL._SL75_.jpg",
  "amazonDomain": "amazon.com",
  "topN": 20
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "query": {},
  "matches": [
    {
      "rank": 1,
      "asin": "B072MQ5BRX",
      "title": "Example product",
      "imageUrl": "https://example.com/image.jpg",
      "price": 29.99,
      "rating": 4.5,
      "estimatedMonthlySales": 1200
    }
  ],
  "caveats": []
}
```

## Full definitions

- [Request definition](../../schemas/reverse-product-image-search.request.json) — field-descriptors
- [Response definition](../../schemas/reverse-product-image-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/reverse-product-image-search.json)
- [Response fixture](../../examples/responses/reverse-product-image-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_reverse_product_image_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
