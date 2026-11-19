# Amazon SP-API GET /fba/inbound/v0/shipments

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-shipments-v0?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-shipments-v0?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound_v0.getShipmentsV0. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getshipments

## Endpoint

`POST https://api.nexscope.ai/spapi/getShipmentsV0`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v0/shipments`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_v0_get_shipments_v0`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-v0-get-shipments-v0?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-v0-get-shipments-v0.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-v0-get-shipments-v0.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-v0-get-shipments-v0.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-v0-get-shipments-v0.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-v0-get-shipments-v0 payloads/amazon-sp-api-inbound-v0-get-shipments-v0.json --dry-run`.
