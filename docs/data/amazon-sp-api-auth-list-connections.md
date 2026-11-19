# Amazon Seller: list connections

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-list-connections?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-list-connections?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

List owned Amazon Seller connections.

## Endpoint

`POST https://api.nexscope.ai/spapi/listConnections`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|

## MCP

Tool name: `nexscope_amazon_sp_api_auth_list_connections`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-auth-list-connections?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-auth-list-connections.request.json)
- [Response schema](../../schemas/amazon-sp-api-auth-list-connections.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-auth-list-connections.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-auth-list-connections.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-auth-list-connections payloads/amazon-sp-api-auth-list-connections.json --dry-run`.
