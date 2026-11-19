# Amazon SP-API GET /aplus/2020-11-01/contentDocuments

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-searchcontentdocuments?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-searchcontentdocuments?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API aplus.searchcontentdocuments. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/searchcontentdocuments

## Endpoint

`POST https://api.nexscope.ai/spapi/searchContentDocuments`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /aplus/2020-11-01/contentDocuments`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_aplus_searchcontentdocuments`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-aplus-searchcontentdocuments?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-aplus-searchcontentdocuments.request.json)
- [Response schema](../../schemas/amazon-sp-api-aplus-searchcontentdocuments.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-aplus-searchcontentdocuments.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-aplus-searchcontentdocuments.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-aplus-searchcontentdocuments payloads/amazon-sp-api-aplus-searchcontentdocuments.json --dry-run`.
