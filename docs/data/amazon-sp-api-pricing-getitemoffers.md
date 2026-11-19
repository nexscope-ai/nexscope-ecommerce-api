# Amazon SP-API GET /products/pricing/v0/items/{Asin}/offers

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getitemoffers?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getitemoffers?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API pricing.getitemoffers. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getitemoffers

## Endpoint

`POST https://api.nexscope.ai/spapi/getItemOffers`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /products/pricing/v0/items/{Asin}/offers`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: Asin. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_pricing_getitemoffers`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-pricing-getitemoffers?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-pricing-getitemoffers.request.json)
- [Response schema](../../schemas/amazon-sp-api-pricing-getitemoffers.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-pricing-getitemoffers.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-pricing-getitemoffers.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-pricing-getitemoffers payloads/amazon-sp-api-pricing-getitemoffers.json --dry-run`.
