# 1688 Search By Image API

Perform image-based product search on the 1688 platform. Use an image URL to find visually similar supplier products, returning title, price, minimum order quantity, monthly sales, repurchase rate, trade score, and seller identity.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-search-by-image?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API

Perform image-based product search on the 1688 platform. Use an image URL to find visually similar supplier products, returning title, price, minimum order quantity, monthly sales, repurchase rate, trade score, and seller identity.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-search-by-image/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | No | Valid, publicly accessible image URL (maximum 1,000 characters). Supported formats: PNG, JPG, and JPEG; WEBP and GIF are not supported. Provide exactly one of imageUrl, imageBase64, or imageId | {} |
| `imageBase64` | string | No | Raw Base64-encoded image content without a data:image/jpeg;base64, prefix. Supported formats: PNG, JPG, and JPEG. | {} |
| `imageId` | string | No | 1688 image ID. Image-search results also return this value; include it when page is greater than 1 to improve response time | {} |
| `page` | integer | No | Page number starting from 1 | {} |
| `pageSize` | integer | No | Number of products per page, maximum 50 | {} |
| `priceStart` | string | No | Minimum price in CNY, for example 10 | {} |
| `priceEnd` | string | No | Maximum price in CNY, for example 100 | {} |
| `filter` | string | No | Comma-separated filter conditions. Use the supported filter values documented for this endpoint | {} |
| `sort` | string | No | Sort condition as JSON in the form {field: direction}. Fields: price, rePurchaseRate, or monthSold. Directions: asc or desc | {} |
| `keyword` | string | No | Keyword used to search within the results | {} |
| `productCollectionId` | string | No | Single product-collection ID. Use a supported collection ID documented for this endpoint | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/1688-search-by-image.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh 1688-search-by-image request.json
# Or: node examples/javascript/run.mjs 1688-search-by-image request.json
# Or: python3 examples/python/run.py 1688-search-by-image request.json
```

### Published request example

```json
{
  "page": 1,
  "imageUrl": "https://m.media-amazon.com/images/I/61v6nYvQ7+L._AC_SL1500_.jpg",
  "pageSize": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "imageId": "example-id",
  "total": 1,
  "totalPage": 1,
  "columns": [],
  "costToken": 1,
  "products": [],
  "offerId": "example-id",
  "asin": "B072MQ5BRX",
  "imageUrl": "https://example.com/image.jpg",
  "price": 1,
  "consignPrice": 1,
  "salesQuantity": 1,
  "estimatedSalesAmount": 1,
  "asinUrl": "B072MQ5BRX",
  "quantityBegin": 1
}
```

## Full definitions

- [Request definition](../../schemas/1688-search-by-image.request.json) — field-descriptors
- [Response definition](../../schemas/1688-search-by-image.response.json) — field-descriptors
- [Editable request sample](../../payloads/1688-search-by-image.json)
- [Response fixture](../../examples/responses/1688-search-by-image.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_1688_search_by_image`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
