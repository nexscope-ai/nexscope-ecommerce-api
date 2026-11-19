# Amazon SP-API GET /fba/inbound/v0/prepInstructions

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-prep-instructions?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-v0-get-prep-instructions?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound_v0.getPrepInstructions. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getprepinstructions

## Endpoint

`POST https://api.nexscope.ai/spapi/getPrepInstructions`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v0/prepInstructions`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_v0_get_prep_instructions`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-v0-get-prep-instructions?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-v0-get-prep-instructions.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-v0-get-prep-instructions.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-v0-get-prep-instructions.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-v0-get-prep-instructions.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-v0-get-prep-instructions payloads/amazon-sp-api-inbound-v0-get-prep-instructions.json --dry-run`.
