# Amazon Seller: authorize

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-authorize?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-auth-authorize?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Generate the Amazon Seller OAuth consent URL.

## Endpoint

`POST https://api.nexscope.ai/spapi/authorize`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `marketplaceId` | string | Yes | Amazon marketplace ID. |
| `region` | string | No | Amazon region inferred from marketplace if omitted. |
| `accountName` | string | No | Optional connection display name. |

## MCP

Tool name: `nexscope_amazon_sp_api_auth_authorize`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-auth-authorize?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-auth-authorize.request.json)
- [Response schema](../../schemas/amazon-sp-api-auth-authorize.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-auth-authorize.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-auth-authorize.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-auth-authorize payloads/amazon-sp-api-auth-authorize.json --dry-run`.
