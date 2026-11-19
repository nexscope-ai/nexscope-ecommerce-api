# Amazon SP-API GET /orders/2026-01-01/orders

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-searchorders?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-orders-searchorders?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API orders.searchorders. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/searchorders

## Endpoint

`POST https://api.nexscope.ai/spapi/searchOrders`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /orders/2026-01-01/orders`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_orders_searchorders`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-orders-searchorders?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-orders-searchorders.request.json)
- [Response schema](../../schemas/amazon-sp-api-orders-searchorders.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-orders-searchorders.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-orders-searchorders.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-orders-searchorders payloads/amazon-sp-api-orders-searchorders.json --dry-run`.
