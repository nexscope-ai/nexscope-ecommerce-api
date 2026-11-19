# Amazon SP-API GET /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-fulfillment-order?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-fulfillment-order?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.getFulfillmentOrder. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfulfillmentorder

## Endpoint

`POST https://api.nexscope.ai/spapi/getFulfillmentOrder`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: sellerFulfillmentOrderId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_get_fulfillment_order`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-get-fulfillment-order?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-get-fulfillment-order.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-get-fulfillment-order.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-get-fulfillment-order.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-get-fulfillment-order.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-get-fulfillment-order payloads/amazon-sp-api-outbound-get-fulfillment-order.json --dry-run`.
