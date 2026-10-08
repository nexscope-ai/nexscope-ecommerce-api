# 1688 Product Detail API

1688 Product Detail public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-detail?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `offerId` | string | Yes | Positive integer 1688 product ID. Use a string to preserve large identifiers. | {} |
| `currency` | string | No | Optional three-letter currency code. The service normalizes it to uppercase. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/1688-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh 1688-product-detail request.json
# Or: node examples/javascript/run.mjs 1688-product-detail request.json
# Or: python3 examples/python/run.py 1688-product-detail request.json
```

### Published request example

```json
{
  "offerId": "1040473674152"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "product": {
    "companyName": "Example supplier",
    "skuList": [],
    "subject": "Example 1688 product",
    "offerId": "1040473674152",
    "shippingInfo": {},
    "saleInfo": {}
  }
}
```

## Full definitions

- [Request definition](../../schemas/1688-product-detail.request.json) — json-schema
- [Response definition](../../schemas/1688-product-detail.response.json) — json-schema
- [Editable request sample](../../payloads/1688-product-detail.json)
- [Response fixture](../../examples/responses/1688-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_1688_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
