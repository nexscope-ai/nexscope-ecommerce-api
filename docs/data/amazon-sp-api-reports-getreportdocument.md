# Amazon SP-API GET /reports/2021-06-30/documents/{reportDocumentId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreportdocument?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreportdocument?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API reports.getreportdocument. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getreportdocument

## Endpoint

`POST https://api.nexscope.ai/spapi/getReportDocument`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /reports/2021-06-30/documents/{reportDocumentId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: reportDocumentId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_reports_getreportdocument`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-reports-getreportdocument?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-reports-getreportdocument.request.json)
- [Response schema](../../schemas/amazon-sp-api-reports-getreportdocument.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-reports-getreportdocument.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-reports-getreportdocument.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-reports-getreportdocument payloads/amazon-sp-api-reports-getreportdocument.json --dry-run`.
