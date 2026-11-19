# Amazon SP-API POST /fulfillment/outbound/2026-07-04/orders

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-create-order?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-create-order?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound-2026.createOrder. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/createorder Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/createOrder`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /fulfillment/outbound/2026-07-04/orders`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_2026_create_order`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-2026-create-order?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-2026-create-order.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-2026-create-order.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-2026-create-order.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-2026-create-order.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-2026-create-order payloads/amazon-sp-api-outbound-2026-create-order.json --dry-run`.
