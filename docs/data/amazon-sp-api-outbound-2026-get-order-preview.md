# Amazon SP-API POST /fulfillment/outbound/2026-07-04/previews

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-get-order-preview?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-get-order-preview?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound-2026.getOrderPreview. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getorderpreview

## Endpoint

`POST https://api.nexscope.ai/spapi/getOrderPreview`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /fulfillment/outbound/2026-07-04/previews`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_2026_get_order_preview`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-2026-get-order-preview?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-2026-get-order-preview.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-2026-get-order-preview.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-2026-get-order-preview.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-2026-get-order-preview.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-2026-get-order-preview payloads/amazon-sp-api-outbound-2026-get-order-preview.json --dry-run`.
