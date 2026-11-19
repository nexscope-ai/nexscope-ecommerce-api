# Amazon SP-API GET /customerFeedback/2024-06-01/items/{asin}/browseNode

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getitembrowsenode?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getitembrowsenode?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API customer-feedback.getitembrowsenode. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getitembrowsenode

## Endpoint

`POST https://api.nexscope.ai/spapi/getItemBrowseNode`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /customerFeedback/2024-06-01/items/{asin}/browseNode`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: asin. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_customer_feedback_getitembrowsenode`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-customer-feedback-getitembrowsenode?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-customer-feedback-getitembrowsenode.request.json)
- [Response schema](../../schemas/amazon-sp-api-customer-feedback-getitembrowsenode.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-customer-feedback-getitembrowsenode.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-customer-feedback-getitembrowsenode.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-customer-feedback-getitembrowsenode payloads/amazon-sp-api-customer-feedback-getitembrowsenode.json --dry-run`.
