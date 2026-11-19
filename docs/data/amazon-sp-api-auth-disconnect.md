# Amazon Seller: disconnect

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-disconnect?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-disconnect?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Disconnect the owned Seller connection and linked marketplaces sharing its credential.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/disconnect`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Seller connection ID. |
| `revision` | integer | Yes | Current connection revision from status. |
| `confirm` | boolean | Yes | Explicit confirmation to disconnect. |

## MCP

Tool name: `nexscope_amazon_sp_api_auth_disconnect`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-auth-disconnect?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-auth-disconnect.request.json)
- [Response schema](../../schemas/amazon-sp-api-auth-disconnect.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-auth-disconnect.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-auth-disconnect.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-auth-disconnect payloads/amazon-sp-api-auth-disconnect.json --dry-run`.
