# Amazon SP-API GET /definitions/2020-09-01/productTypes/{productType}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-product-types-getdefinitionsproducttype?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-product-types-getdefinitionsproducttype?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API product-types.getdefinitionsproducttype. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getdefinitionsproducttype

## Endpoint

`POST https://api.nexscope.ai/spapi/getDefinitionsProductType`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /definitions/2020-09-01/productTypes/{productType}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: productType. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_product_types_getdefinitionsproducttype`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-product-types-getdefinitionsproducttype?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-product-types-getdefinitionsproducttype.request.json)
- [Response schema](../../schemas/amazon-sp-api-product-types-getdefinitionsproducttype.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-product-types-getdefinitionsproducttype.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-product-types-getdefinitionsproducttype.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-product-types-getdefinitionsproducttype payloads/amazon-sp-api-product-types-getdefinitionsproducttype.json --dry-run`.
