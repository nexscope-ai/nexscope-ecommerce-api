# Amazon SP-API GET /fba/inbound/v0/shipments/{shipmentId}/labels

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-labels?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-labels?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound_v0.getLabels. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getlabels

## Endpoint

`POST https://api.nexscope.ai/spapi/getLabels`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v0/shipments/{shipmentId}/labels`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: shipmentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_v0_get_labels`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-v0-get-labels?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-v0-get-labels.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-v0-get-labels.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-v0-get-labels.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-v0-get-labels.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-v0-get-labels payloads/amazon-sp-api-inbound-v0-get-labels.json --dry-run`.
