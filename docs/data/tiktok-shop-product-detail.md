# TikTok Shop Product Detail API

TikTok Shop Product Detail public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-shop-product-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-shop-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productInput` | string | Yes | 19-digit TikTok Shop product ID or supported HTTPS TikTok product URL | {} |
| `region` | string | No | TikTok Shop region: US, GB, ID, MY, TH, VN, PH, SG, DE, FR, IT, or ES | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-shop-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-shop-product-detail request.json
# Or: node examples/javascript/run.mjs tiktok-shop-product-detail request.json
# Or: python3 examples/python/run.py tiktok-shop-product-detail request.json
```

### Published request example

```json
{
  "region": "US",
  "productInput": "1729937400435937604"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "product": {
    "productId": "1729937400435937604",
    "title": "Example TikTok Shop product",
    "seller": {
      "name": "CARER SPARK"
    }
  }
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-shop-product-detail.request.json) — json-schema
- [Response definition](../../schemas/tiktok-shop-product-detail.response.json) — json-schema
- [Editable request sample](../../payloads/tiktok-shop-product-detail.json)
- [Response fixture](../../examples/responses/tiktok-shop-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_shop_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
