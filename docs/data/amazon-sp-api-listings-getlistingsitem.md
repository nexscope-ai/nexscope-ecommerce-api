# Amazon SP-API GET /listings/2021-08-01/items/{sellerId}/{sku}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-getlistingsitem?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-getlistingsitem?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API listings.getlistingsitem. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getlistingsitem

## Endpoint

`POST https://api.nexscope.ai/spapi/getListingsItem`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /listings/2021-08-01/items/{sellerId}/{sku}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: sellerId, sku. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_listings_getlistingsitem`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-listings-getlistingsitem?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-listings-getlistingsitem.request.json)
- [Response schema](../../schemas/amazon-sp-api-listings-getlistingsitem.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-listings-getlistingsitem.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-listings-getlistingsitem.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-listings-getlistingsitem payloads/amazon-sp-api-listings-getlistingsitem.json --dry-run`.
