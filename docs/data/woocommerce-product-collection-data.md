# WooCommerce Product Collection Data API

Read public collection from a specified WooCommerce store.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/woocommerce-product-collection-data?view=api&co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/woocommerce-product-collection-data?view=api&co-from=github-ecommerce-api#data-example)

Category: WooCommerce Public Store Data · Data API

Read public store data through the official WooCommerce Store API. No merchant secret or merchant OAuth connection is required. Authenticate to Nexscope with your own API key. Store configuration and WooCommerce version determine which public resources are available.

## Endpoint

`POST https://api.nexscope.ai/woocommerce/productCollectionData`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Each request costs **10 credits**. Failed requests are automatically refunded.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `storeUrl` | string | Yes | Public HTTPS store root or WordPress installation path. | {"maxLength": 2048} |
| `keyword` | string | No | Search within this store; at most 200 characters. | {"maxLength": 200} |
| `categoryId` | string | No | Restrict to a public product category. | {"pattern": "^[1-9][0-9]{0,18}$"} |
| `calculatePriceRange` | boolean | No | Calculate this aggregate; default true. Unsupported store fields may be null. | {} |
| `calculateRatingCounts` | boolean | No | Calculate this aggregate; default true. Unsupported store fields may be null. | {} |
| `calculateStockStatusCounts` | boolean | No | Calculate this aggregate; default true. Unsupported store fields may be null. | {} |
| `attributeTaxonomies` | array | No | Attribute taxonomies to count, using OR semantics, for example pa_color. Default empty. | {"maxItems": 20, "items": {"pattern": "^pa_[a-z0-9_-]{1,28}$", "type": "string"}} |
| `taxonomies` | array | No | Public taxonomies to count; default empty. Store support varies. | {"maxItems": 20, "items": {"type": "string", "enum": ["product_cat", "product_tag", "product_brand"]}} |

The full request schema below is authoritative for nested items, ranges and required fields.

## Call this API

Run from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the editable payload and adjust the public store URL and resource IDs before executing. Each client invocation sends a separate request.

```bash
cp payloads/woocommerce-product-collection-data.json request.json
# Edit request.json for the public store and resources you want to inspect.
python3 examples/python/run.py woocommerce-product-collection-data request.json --dry-run
# Submit only after reviewing the inputs and credits:
bash examples/curl/run.sh woocommerce-product-collection-data request.json
# Alternatively: node examples/javascript/run.mjs woocommerce-product-collection-data request.json
# Alternatively: python3 examples/python/run.py woocommerce-product-collection-data request.json
```

### Editable request sample

```json
{
  "storeUrl": "https://cipherskincare.com"
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
    "collection": {
      "priceRange": {
        "currency": "USD",
        "minorUnit": 2,
        "minPrice": "10.00",
        "maxPrice": "10.00",
        "minPriceMinor": "1000",
        "maxPriceMinor": "1000"
      },
      "attributeCounts": [
        {
          "termId": "16",
          "count": 1
        }
      ],
      "ratingCounts": [
        {
          "rating": 5,
          "count": 1
        }
      ],
      "stockStatusCounts": [
        {
          "status": "instock",
          "count": 1
        }
      ],
      "taxonomyCounts": [
        {
          "termId": "16",
          "count": 1
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

- [Request definition](../../schemas/woocommerce-product-collection-data.request.json) — JSON Schema
- [Response definition](../../schemas/woocommerce-product-collection-data.response.json) — JSON Schema
- [Editable request sample](../../payloads/woocommerce-product-collection-data.json)
- [HTTP response fixture](../../examples/responses/woocommerce-product-collection-data.json)

## MCP

Tool name: `nexscope_woocommerce_product_collection_data`. See [MCP integration](../calling-apis.md#mcp).

WooCommerce contracts retrieved from production: 2026-10-29. See [source notes](../source-notes.md).
