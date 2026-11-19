# Amazon SP-API GET /listings/2021-08-01/restrictions

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-getlistingsrestrictions?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-listings-getlistingsrestrictions?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API listings.getlistingsrestrictions. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getlistingsrestrictions

## Endpoint

`POST https://api.nexscope.ai/spapi/getListingsRestrictions`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /listings/2021-08-01/restrictions`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_listings_getlistingsrestrictions`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-listings-getlistingsrestrictions?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-listings-getlistingsrestrictions.request.json)
- [Response schema](../../schemas/amazon-sp-api-listings-getlistingsrestrictions.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-listings-getlistingsrestrictions.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-listings-getlistingsrestrictions.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-listings-getlistingsrestrictions payloads/amazon-sp-api-listings-getlistingsrestrictions.json --dry-run`.
