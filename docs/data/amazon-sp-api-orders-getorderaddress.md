# Amazon SP-API GET /orders/v0/orders/{orderId}/address

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-getorderaddress?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-getorderaddress?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API orders.getorderaddress. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getorderaddress

## Endpoint

`POST https://api.nexscope.ai/spapi/getOrderAddress`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /orders/v0/orders/{orderId}/address`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: orderId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_orders_getorderaddress`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-orders-getorderaddress?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-orders-getorderaddress.request.json)
- [Response schema](../../schemas/amazon-sp-api-orders-getorderaddress.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-orders-getorderaddress.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-orders-getorderaddress.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-orders-getorderaddress payloads/amazon-sp-api-orders-getorderaddress.json --dry-run`.
