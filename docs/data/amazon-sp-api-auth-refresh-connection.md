# Amazon Seller: refresh connection

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-refresh-connection?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-refresh-connection?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Ensure a usable Amazon credential, refreshing it when needed.

## Endpoint

`POST https://api.nexscope.ai/spapi/refreshConnection`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Seller connection ID. |

## MCP

Tool name: `nexscope_amazon_sp_api_auth_refresh_connection`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-auth-refresh-connection?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-auth-refresh-connection.request.json)
- [Response schema](../../schemas/amazon-sp-api-auth-refresh-connection.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-auth-refresh-connection.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-auth-refresh-connection.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-auth-refresh-connection payloads/amazon-sp-api-auth-refresh-connection.json --dry-run`.
