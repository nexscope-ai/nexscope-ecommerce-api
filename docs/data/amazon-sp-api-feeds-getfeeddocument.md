# Amazon SP-API GET /feeds/2021-06-30/documents/{feedDocumentId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-getfeeddocument?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-getfeeddocument?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API feeds.getfeeddocument. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfeeddocument

## Endpoint

`POST https://api.nexscope.ai/spapi/getFeedDocument`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /feeds/2021-06-30/documents/{feedDocumentId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: feedDocumentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_feeds_getfeeddocument`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-feeds-getfeeddocument?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-feeds-getfeeddocument.request.json)
- [Response schema](../../schemas/amazon-sp-api-feeds-getfeeddocument.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-feeds-getfeeddocument.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-feeds-getfeeddocument.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-feeds-getfeeddocument payloads/amazon-sp-api-feeds-getfeeddocument.json --dry-run`.
