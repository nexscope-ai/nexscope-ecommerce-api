# Amazon SP-API POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API aplus.postcontentdocumentapprovalsubmission. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentapprovalsubmission Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/postContentDocumentApprovalSubmission`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: contentReferenceKey. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_aplus_postcontentdocumentapp_4ee55e29cc56`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission.request.json)
- [Response schema](../../schemas/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-aplus-postcontentdocumentapprovalsubmission payloads/amazon-sp-api-aplus-postcontentdocumentapprovalsubmission.json --dry-run`.
