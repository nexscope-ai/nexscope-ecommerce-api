# Amazon SP-API GET /fba/inbound/v0/shipments/{shipmentId}/items

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound_v0.getShipmentItemsByShipmentId. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getshipmentitemsbyshipmentid

## Endpoint

`POST https://api.nexscope.ai/spapi/getShipmentItemsByShipmentId`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v0/shipments/{shipmentId}/items`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: shipmentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_v0_get_shipment_item_5db3eda79e03`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id payloads/amazon-sp-api-inbound-v0-get-shipment-items-by-shipment-id.json --dry-run`.
