# Amazon SP-API GET /externalFulfillment/2024-09-11/returns

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-list-returns?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-list-returns?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API external-fulfillment.listReturns. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listreturns

## Endpoint

`POST https://api.nexscope.ai/spapi/listReturns`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /externalFulfillment/2024-09-11/returns`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_external_fulfillment_list_returns`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-external-fulfillment-list-returns?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-external-fulfillment-list-returns.request.json)
- [Response schema](../../schemas/amazon-sp-api-external-fulfillment-list-returns.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-external-fulfillment-list-returns.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-external-fulfillment-list-returns.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-external-fulfillment-list-returns payloads/amazon-sp-api-external-fulfillment-list-returns.json --dry-run`.
