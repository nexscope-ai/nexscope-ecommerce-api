# Amazon SP-API GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-get-self-ship-appointment-slots?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-get-self-ship-appointment-slots?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound.getSelfShipAppointmentSlots. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getselfshipappointmentslots

## Endpoint

`POST https://api.nexscope.ai/spapi/getSelfShipAppointmentSlots`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: inboundPlanId, shipmentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_get_self_ship_appointment_slots`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-get-self-ship-appointment-slots?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-get-self-ship-appointment-slots.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-get-self-ship-appointment-slots.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-get-self-ship-appointment-slots.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-get-self-ship-appointment-slots.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-get-self-ship-appointment-slots payloads/amazon-sp-api-inbound-get-self-ship-appointment-slots.json --dry-run`.
