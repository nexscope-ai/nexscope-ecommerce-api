# WooCommerce Product Detail API

Read public products from a specified WooCommerce store.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/woocommerce-product-detail?view=api&co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/woocommerce-product-detail?view=api&co-from=github-ecommerce-api#data-example)

Category: WooCommerce Public Store Data · Data API

Read public store data through the official WooCommerce Store API. No merchant secret or merchant OAuth connection is required. Authenticate to Nexscope with your own API key. Store configuration and WooCommerce version determine which public resources are available.

## Endpoint

`POST https://api.nexscope.ai/woocommerce/productDetail`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Each request costs **10 credits**. Failed requests are automatically refunded.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `storeUrl` | string | Yes | Public HTTPS store root or WordPress installation path, without query or fragment. | {} |
| `productId` | string | Yes | Store-scoped positive product ID, at most 19 decimal digits. | {} |

The full request schema below is authoritative for nested items, ranges and required fields.

## Call this API

Run from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the editable payload and adjust the public store URL and resource IDs before executing. Each client invocation sends a separate request.

```bash
cp payloads/woocommerce-product-detail.json request.json
# Edit request.json for the public store and resources you want to inspect.
python3 examples/python/run.py woocommerce-product-detail request.json --dry-run
# Submit only after reviewing the inputs and credits:
bash examples/curl/run.sh woocommerce-product-detail request.json
# Alternatively: node examples/javascript/run.mjs woocommerce-product-detail request.json
# Alternatively: python3 examples/python/run.py woocommerce-product-detail request.json
```

### Editable request sample

```json
{
  "storeUrl": "https://cipherskincare.com",
  "productId": "20183"
}
```

The editable request uses the published Data Example inputs. The HTTP fixture below is the current Catalog's illustrative response; open Data Example above for a paired, redacted sample. This synchronization did not execute a paid request.

## Response

Check `code === 0` before reading `data`; HTTP 200 alone does not mean business success. `cost` is elapsed milliseconds, not credits. IDs and millisecond timestamps are strings; optional fields can be null. The full response schema lists the platform envelope and public business fields.

### Published HTTP response fixture

```json
{
  "data": {
    "storeUrl": "https://example.com",
    "fetchedAt": "1792972800000",
    "cacheHit": false,
    "product": {
      "id": "34",
      "type": "simple",
      "name": "Cotton Shirt",
      "sku": "SHIRT-34",
      "url": "https://example.com/product/shirt",
      "description": "Cotton shirt.",
      "shortDescription": "Cotton shirt.",
      "variation": "",
      "isInStock": true,
      "isPasswordProtected": false,
      "prices": {
        "currency": "USD",
        "minorUnit": 2,
        "price": "11.05"
      },
      "images": [
        {
          "url": "https://example.com/image.jpg",
          "alt": "Shirt"
        }
      ]
    }
  },
  "code": 0,
  "msg": null,
  "ts": "0",
  "time": "2026-01-01 00:00:00",
  "cost": "-1",
  "traceId": null
}
```

## Full definitions

- [Request definition](../../schemas/woocommerce-product-detail.request.json) — JSON Schema
- [Response definition](../../schemas/woocommerce-product-detail.response.json) — JSON Schema
- [Editable request sample](../../payloads/woocommerce-product-detail.json)
- [HTTP response fixture](../../examples/responses/woocommerce-product-detail.json)

## MCP

Tool name: `nexscope_woocommerce_product_detail`. See [MCP integration](../calling-apis.md#mcp).

WooCommerce contracts retrieved from production: 2026-10-29. See [source notes](../source-notes.md).
