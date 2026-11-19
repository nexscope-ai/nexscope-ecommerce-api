# Amazon SP-API GET /products/pricing/v0/listings/{SellerSKU}/offers

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getlistingoffers?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getlistingoffers?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API pricing.getlistingoffers. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getlistingoffers

## Endpoint

`POST https://api.nexscope.ai/spapi/getListingOffers`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /products/pricing/v0/listings/{SellerSKU}/offers`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: SellerSKU. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_pricing_getlistingoffers`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-pricing-getlistingoffers?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-pricing-getlistingoffers.request.json)
- [Response schema](../../schemas/amazon-sp-api-pricing-getlistingoffers.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-pricing-getlistingoffers.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-pricing-getlistingoffers.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-pricing-getlistingoffers payloads/amazon-sp-api-pricing-getlistingoffers.json --dry-run`.
