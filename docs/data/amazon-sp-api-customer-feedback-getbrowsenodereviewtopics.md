# Amazon SP-API GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/topics

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API customer-feedback.getbrowsenodereviewtopics. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getbrowsenodereviewtopics

## Endpoint

`POST https://api.nexscope.ai/spapi/getBrowseNodeReviewTopics`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/topics`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: browseNodeId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_customer_feedback_getbrowsen_b326f4966468`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics.request.json)
- [Response schema](../../schemas/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-customer-feedback-getbrowsenodereviewtopics payloads/amazon-sp-api-customer-feedback-getbrowsenodereviewtopics.json --dry-run`.
