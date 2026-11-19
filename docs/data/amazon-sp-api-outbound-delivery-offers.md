# Amazon SP-API POST /fba/outbound/2020-07-01/deliveryOffers

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-delivery-offers?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-delivery-offers?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.deliveryOffers. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/deliveryoffers

## Endpoint

`POST https://api.nexscope.ai/spapi/deliveryOffers`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /fba/outbound/2020-07-01/deliveryOffers`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_delivery_offers`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-delivery-offers?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-delivery-offers.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-delivery-offers.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-delivery-offers.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-delivery-offers.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-delivery-offers payloads/amazon-sp-api-outbound-delivery-offers.json --dry-run`.
