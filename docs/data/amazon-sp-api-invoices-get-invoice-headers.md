# Amazon SP-API GET /finances/invoices/2026-06-25/invoices

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-invoices-get-invoice-headers?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-invoices-get-invoice-headers?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API invoices.getInvoiceHeaders. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getinvoiceheaders

## Endpoint

`POST https://api.nexscope.ai/spapi/getInvoiceHeaders`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /finances/invoices/2026-06-25/invoices`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_invoices_get_invoice_headers`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-invoices-get-invoice-headers?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-invoices-get-invoice-headers.request.json)
- [Response schema](../../schemas/amazon-sp-api-invoices-get-invoice-headers.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-invoices-get-invoice-headers.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-invoices-get-invoice-headers.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-invoices-get-invoice-headers payloads/amazon-sp-api-invoices-get-invoice-headers.json --dry-run`.
