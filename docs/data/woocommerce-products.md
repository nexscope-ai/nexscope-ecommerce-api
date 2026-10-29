# WooCommerce Products API

Read public products from a specified WooCommerce store.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/woocommerce-products?view=api&co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/woocommerce-products?view=api&co-from=github-ecommerce-api#data-example)

Category: WooCommerce Public Store Data · Data API

Read public store data through the official WooCommerce Store API. No merchant secret or merchant OAuth connection is required. Authenticate to Nexscope with your own API key. Store configuration and WooCommerce version determine which public resources are available.

## Endpoint

`POST https://api.nexscope.ai/woocommerce/products`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Each request costs **10 credits**. Failed requests are automatically refunded.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `storeUrl` | string | Yes | Public HTTPS store root or WordPress installation path, without query or fragment. | {} |
| `keyword` | string | No | Search only within this store; at most 200 characters. | {} |
| `pageNum` | integer | No | Page number, default 1. | {"maximum": 10000, "minimum": 1} |
| `pageSize` | integer | No | Page size, default 20, maximum 100. | {"maximum": 100, "minimum": 1} |

The full request schema below is authoritative for nested items, ranges and required fields.

## Call this API

Run from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the editable payload and adjust the public store URL and resource IDs before executing. Each client invocation sends a separate request.

```bash
cp payloads/woocommerce-products.json request.json
# Edit request.json for the public store and resources you want to inspect.
python3 examples/python/run.py woocommerce-products request.json --dry-run
# Submit only after reviewing the inputs and credits:
bash examples/curl/run.sh woocommerce-products request.json
# Alternatively: node examples/javascript/run.mjs woocommerce-products request.json
# Alternatively: python3 examples/python/run.py woocommerce-products request.json
```

### Editable request sample

```json
{
  "storeUrl": "https://cipherskincare.com",
  "pageSize": 2
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
    "products": [
      {
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
    ],
    "pageNum": 1,
    "pageSize": 20,
    "total": 1,
    "totalPages": 1,
    "hasMore": false
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

- [Request definition](../../schemas/woocommerce-products.request.json) — JSON Schema
- [Response definition](../../schemas/woocommerce-products.response.json) — JSON Schema
- [Editable request sample](../../payloads/woocommerce-products.json)
- [HTTP response fixture](../../examples/responses/woocommerce-products.json)

## MCP

Tool name: `nexscope_woocommerce_products`. See [MCP integration](../calling-apis.md#mcp).

WooCommerce contracts retrieved from production: 2026-10-29. See [source notes](../source-notes.md).
