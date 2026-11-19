# Amazon SP-API GET /feeds/2021-06-30/feeds

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-getfeeds?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-feeds-getfeeds?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API feeds.getfeeds. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfeeds

## Endpoint

`POST https://api.nexscope.ai/spapi/getFeeds`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /feeds/2021-06-30/feeds`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_feeds_getfeeds`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-feeds-getfeeds?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-feeds-getfeeds.request.json)
- [Response schema](../../schemas/amazon-sp-api-feeds-getfeeds.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-feeds-getfeeds.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-feeds-getfeeds.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-feeds-getfeeds payloads/amazon-sp-api-feeds-getfeeds.json --dry-run`.
