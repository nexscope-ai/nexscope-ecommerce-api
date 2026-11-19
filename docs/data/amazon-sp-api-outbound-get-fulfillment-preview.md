# Amazon SP-API POST /fba/outbound/2020-07-01/fulfillmentOrders/preview

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-fulfillment-preview?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-fulfillment-preview?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.getFulfillmentPreview. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfulfillmentpreview

## Endpoint

`POST https://api.nexscope.ai/spapi/getFulfillmentPreview`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /fba/outbound/2020-07-01/fulfillmentOrders/preview`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_get_fulfillment_preview`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-get-fulfillment-preview?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-get-fulfillment-preview.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-get-fulfillment-preview.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-get-fulfillment-preview.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-get-fulfillment-preview.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-get-fulfillment-preview payloads/amazon-sp-api-outbound-get-fulfillment-preview.json --dry-run`.
