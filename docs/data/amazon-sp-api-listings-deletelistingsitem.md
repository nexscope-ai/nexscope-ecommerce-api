# Amazon SP-API DELETE /listings/2021-08-01/items/{sellerId}/{sku}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-deletelistingsitem?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-deletelistingsitem?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API listings.deletelistingsitem. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/deletelistingsitem Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/deleteListingsItem`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `DELETE /listings/2021-08-01/items/{sellerId}/{sku}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: sellerId, sku. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_listings_deletelistingsitem`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-listings-deletelistingsitem?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-listings-deletelistingsitem.request.json)
- [Response schema](../../schemas/amazon-sp-api-listings-deletelistingsitem.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-listings-deletelistingsitem.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-listings-deletelistingsitem.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-listings-deletelistingsitem payloads/amazon-sp-api-listings-deletelistingsitem.json --dry-run`.
