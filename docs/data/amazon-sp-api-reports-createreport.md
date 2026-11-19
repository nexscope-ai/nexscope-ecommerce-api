# Amazon SP-API POST /reports/2021-06-30/reports

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-createreport?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-createreport?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API reports.createreport. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/createreport Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/createReport`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /reports/2021-06-30/reports`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_reports_createreport`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-reports-createreport?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-reports-createreport.request.json)
- [Response schema](../../schemas/amazon-sp-api-reports-createreport.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-reports-createreport.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-reports-createreport.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-reports-createreport payloads/amazon-sp-api-reports-createreport.json --dry-run`.
