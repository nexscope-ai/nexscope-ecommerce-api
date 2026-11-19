# Amazon SP-API GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-get-shipment-content-update-preview?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-get-shipment-content-update-preview?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound.getShipmentContentUpdatePreview. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getshipmentcontentupdatepreview

## Endpoint

`POST https://api.nexscope.ai/spapi/getShipmentContentUpdatePreview`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: inboundPlanId, shipmentId, contentUpdatePreviewId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_get_shipment_content_a2c8f3191c68`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-get-shipment-content-update-preview?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-get-shipment-content-update-preview.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-get-shipment-content-update-preview.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-get-shipment-content-update-preview.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-get-shipment-content-update-preview.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-get-shipment-content-update-preview payloads/amazon-sp-api-inbound-get-shipment-content-update-preview.json --dry-run`.
