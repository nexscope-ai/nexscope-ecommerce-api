# Amazon SP-API POST /feeds/2021-06-30/documents

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-createfeeddocument?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-createfeeddocument?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API feeds.createfeeddocument. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/createfeeddocument Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/createFeedDocument`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /feeds/2021-06-30/documents`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `contentBase64` | string | Yes | Base64 content to upload through the backend; maximum 20 MiB decoded. |
| `contentType` | string | No | Uploaded content MIME type. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_feeds_createfeeddocument`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-feeds-createfeeddocument?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-feeds-createfeeddocument.request.json)
- [Response schema](../../schemas/amazon-sp-api-feeds-createfeeddocument.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-feeds-createfeeddocument.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-feeds-createfeeddocument.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-feeds-createfeeddocument payloads/amazon-sp-api-feeds-createfeeddocument.json --dry-run`.
