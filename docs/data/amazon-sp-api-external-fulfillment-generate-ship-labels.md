# Amazon SP-API PUT /externalFulfillment/2024-09-11/shipments/{shipmentId}/shipLabels

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-generate-ship-labels?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-generate-ship-labels?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API external-fulfillment.generateShipLabels. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/generateshiplabels Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/generateShipLabels`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `PUT /externalFulfillment/2024-09-11/shipments/{shipmentId}/shipLabels`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: shipmentId. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_external_fulfillment_generate_ship_labels`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-external-fulfillment-generate-ship-labels?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-external-fulfillment-generate-ship-labels.request.json)
- [Response schema](../../schemas/amazon-sp-api-external-fulfillment-generate-ship-labels.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-external-fulfillment-generate-ship-labels.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-external-fulfillment-generate-ship-labels.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-external-fulfillment-generate-ship-labels payloads/amazon-sp-api-external-fulfillment-generate-ship-labels.json --dry-run`.
