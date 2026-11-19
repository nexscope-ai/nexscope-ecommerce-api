# Amazon SP-API GET /customerFeedback/2024-06-01/items/{asin}/reviews/topics

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getitemreviewtopics?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-customer-feedback-getitemreviewtopics?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API customer-feedback.getitemreviewtopics. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getitemreviewtopics

## Endpoint

`POST https://api.nexscope.ai/spapi/getItemReviewTopics`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /customerFeedback/2024-06-01/items/{asin}/reviews/topics`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: asin. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_customer_feedback_getitemreviewtopics`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-customer-feedback-getitemreviewtopics?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-customer-feedback-getitemreviewtopics.request.json)
- [Response schema](../../schemas/amazon-sp-api-customer-feedback-getitemreviewtopics.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-customer-feedback-getitemreviewtopics.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-customer-feedback-getitemreviewtopics.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-customer-feedback-getitemreviewtopics payloads/amazon-sp-api-customer-feedback-getitemreviewtopics.json --dry-run`.
