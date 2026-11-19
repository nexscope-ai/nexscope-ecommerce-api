# Amazon SP-API GET /externalFulfillment/2024-09-11/returns/{returnId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-get-return?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-external-fulfillment-get-return?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API external-fulfillment.getReturn. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getreturn

## Endpoint

`POST https://api.nexscope.ai/spapi/getReturn`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /externalFulfillment/2024-09-11/returns/{returnId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: returnId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_external_fulfillment_get_return`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-external-fulfillment-get-return?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-external-fulfillment-get-return.request.json)
- [Response schema](../../schemas/amazon-sp-api-external-fulfillment-get-return.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-external-fulfillment-get-return.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-external-fulfillment-get-return.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-external-fulfillment-get-return payloads/amazon-sp-api-external-fulfillment-get-return.json --dry-run`.
