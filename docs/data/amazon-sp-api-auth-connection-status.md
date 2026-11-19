# Amazon Seller: connection status

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-connection-status?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-connection-status?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Read the stored status of an owned Seller connection.

## Endpoint

`POST https://api.nexscope.ai/spapi/connectionStatus`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Seller connection ID. |

## MCP

Tool name: `nexscope_amazon_sp_api_auth_connection_status`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-auth-connection-status?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-auth-connection-status.request.json)
- [Response schema](../../schemas/amazon-sp-api-auth-connection-status.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-auth-connection-status.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-auth-connection-status.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-auth-connection-status payloads/amazon-sp-api-auth-connection-status.json --dry-run`.
