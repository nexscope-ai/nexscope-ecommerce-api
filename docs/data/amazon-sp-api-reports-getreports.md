# Amazon SP-API GET /reports/2021-06-30/reports

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreports?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-reports-getreports?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API reports.getreports. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getreports

## Endpoint

`POST https://api.nexscope.ai/spapi/getReports`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /reports/2021-06-30/reports`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_reports_getreports`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-reports-getreports?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-reports-getreports.request.json)
- [Response schema](../../schemas/amazon-sp-api-reports-getreports.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-reports-getreports.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-reports-getreports.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-reports-getreports payloads/amazon-sp-api-reports-getreports.json --dry-run`.
