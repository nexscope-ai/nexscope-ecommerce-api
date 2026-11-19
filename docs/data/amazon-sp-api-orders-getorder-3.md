# Amazon SP-API GET /orders/2026-01-01/orders/{orderId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-getorder-3?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-getorder-3?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API orders.getorder-3. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getorder-3

## Endpoint

`POST https://api.nexscope.ai/spapi/getorder3`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /orders/2026-01-01/orders/{orderId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: orderId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_orders_getorder_3`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-orders-getorder-3?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-orders-getorder-3.request.json)
- [Response schema](../../schemas/amazon-sp-api-orders-getorder-3.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-orders-getorder-3.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-orders-getorder-3.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-orders-getorder-3 payloads/amazon-sp-api-orders-getorder-3.json --dry-run`.
