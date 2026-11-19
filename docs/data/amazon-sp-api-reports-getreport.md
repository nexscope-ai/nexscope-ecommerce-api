# Amazon SP-API GET /reports/2021-06-30/reports/{reportId}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreport?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreport?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API reports.getreport. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getreport

## Endpoint

`POST https://api.nexscope.ai/spapi/getReport`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /reports/2021-06-30/reports/{reportId}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: reportId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_reports_getreport`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-reports-getreport?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-reports-getreport.request.json)
- [Response schema](../../schemas/amazon-sp-api-reports-getreport.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-reports-getreport.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-reports-getreport.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-reports-getreport payloads/amazon-sp-api-reports-getreport.json --dry-run`.
