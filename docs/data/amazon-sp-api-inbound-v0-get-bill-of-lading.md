# Amazon SP-API GET /fba/inbound/v0/shipments/{shipmentId}/billOfLading

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-bill-of-lading?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-bill-of-lading?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound_v0.getBillOfLading. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getbilloflading

## Endpoint

`POST https://api.nexscope.ai/spapi/getBillOfLading`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v0/shipments/{shipmentId}/billOfLading`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: shipmentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_v0_get_bill_of_lading`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-v0-get-bill-of-lading?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-v0-get-bill-of-lading.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-v0-get-bill-of-lading.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-v0-get-bill-of-lading.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-v0-get-bill-of-lading.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-v0-get-bill-of-lading payloads/amazon-sp-api-inbound-v0-get-bill-of-lading.json --dry-run`.
