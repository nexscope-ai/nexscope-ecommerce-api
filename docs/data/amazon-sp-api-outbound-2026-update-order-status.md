# Amazon SP-API PUT /fulfillment/outbound/2026-07-04/orders/{orderId}/status

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-update-order-status?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-update-order-status?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound-2026.updateOrderStatus. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/updateorderstatus Amazon sandbox only; results are test data. Changes require preview and confirmation.

This operation uses the Amazon sandbox. Results are test data.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/updateOrderStatus`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `PUT /fulfillment/outbound/2026-07-04/orders/{orderId}/status`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: orderId. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_2026_update_order_status`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-2026-update-order-status?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-2026-update-order-status.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-2026-update-order-status.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-2026-update-order-status.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-2026-update-order-status.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-2026-update-order-status payloads/amazon-sp-api-outbound-2026-update-order-status.json --dry-run`.
