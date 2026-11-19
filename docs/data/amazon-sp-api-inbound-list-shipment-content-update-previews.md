# Amazon SP-API GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-list-shipment-content-update-previews?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-list-shipment-content-update-previews?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound.listShipmentContentUpdatePreviews. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listshipmentcontentupdatepreviews

## Endpoint

`POST https://api.nexscope.ai/spapi/listShipmentContentUpdatePreviews`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: inboundPlanId, shipmentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_list_shipment_conten_898bb5b92c18`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-list-shipment-content-update-previews?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-list-shipment-content-update-previews.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-list-shipment-content-update-previews.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-list-shipment-content-update-previews.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-list-shipment-content-update-previews.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-list-shipment-content-update-previews payloads/amazon-sp-api-inbound-list-shipment-content-update-previews.json --dry-run`.
