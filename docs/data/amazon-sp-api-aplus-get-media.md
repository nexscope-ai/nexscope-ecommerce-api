# Amazon SP-API GET /aplus/2020-11-01/media/{mediaId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-get-media?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-get-media?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API aplus.getMedia. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getmedia

## Endpoint

`POST https://api.nexscope.ai/spapi/getMedia`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /aplus/2020-11-01/media/{mediaId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: mediaId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_aplus_get_media`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-aplus-get-media?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-aplus-get-media.request.json)
- [Response schema](../../schemas/amazon-sp-api-aplus-get-media.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-aplus-get-media.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-aplus-get-media.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-aplus-get-media payloads/amazon-sp-api-aplus-get-media.json --dry-run`.
