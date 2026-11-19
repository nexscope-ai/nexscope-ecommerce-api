# Amazon SP-API GET /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-listcontentdocumentasinrelations?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-listcontentdocumentasinrelations?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API aplus.listcontentdocumentasinrelations. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listcontentdocumentasinrelations

## Endpoint

`POST https://api.nexscope.ai/spapi/listContentDocumentAsinRelations`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: contentReferenceKey. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_aplus_listcontentdocumentasinrelations`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-aplus-listcontentdocumentasinrelations?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-aplus-listcontentdocumentasinrelations.request.json)
- [Response schema](../../schemas/amazon-sp-api-aplus-listcontentdocumentasinrelations.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-aplus-listcontentdocumentasinrelations.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-aplus-listcontentdocumentasinrelations.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-aplus-listcontentdocumentasinrelations payloads/amazon-sp-api-aplus-listcontentdocumentasinrelations.json --dry-run`.
