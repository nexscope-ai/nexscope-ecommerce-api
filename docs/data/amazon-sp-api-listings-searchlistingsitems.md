# Amazon SP-API GET /listings/2021-08-01/items/{sellerId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-searchlistingsitems?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-searchlistingsitems?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API listings.searchlistingsitems. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/searchlistingsitems

## Endpoint

`POST https://api.nexscope.ai/spapi/searchListingsItems`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /listings/2021-08-01/items/{sellerId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: sellerId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_listings_searchlistingsitems`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-listings-searchlistingsitems?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-listings-searchlistingsitems.request.json)
- [Response schema](../../schemas/amazon-sp-api-listings-searchlistingsitems.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-listings-searchlistingsitems.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-listings-searchlistingsitems.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-listings-searchlistingsitems payloads/amazon-sp-api-listings-searchlistingsitems.json --dry-run`.
