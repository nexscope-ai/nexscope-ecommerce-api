# Amazon SP-API GET /definitions/2020-09-01/productTypes

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-product-types-searchdefinitionsproducttypes?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-product-types-searchdefinitionsproducttypes?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API product-types.searchdefinitionsproducttypes. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/searchdefinitionsproducttypes

## Endpoint

`POST https://api.nexscope.ai/spapi/searchDefinitionsProductTypes`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /definitions/2020-09-01/productTypes`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_product_types_searchdefiniti_bcca1638e413`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-product-types-searchdefinitionsproducttypes?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-product-types-searchdefinitionsproducttypes.request.json)
- [Response schema](../../schemas/amazon-sp-api-product-types-searchdefinitionsproducttypes.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-product-types-searchdefinitionsproducttypes.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-product-types-searchdefinitionsproducttypes.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-product-types-searchdefinitionsproducttypes payloads/amazon-sp-api-product-types-searchdefinitionsproducttypes.json --dry-run`.
