# Amazon SP-API GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/boxes

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-list-inbound-plan-boxes?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inbound-list-inbound-plan-boxes?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inbound.listInboundPlanBoxes. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listinboundplanboxes

## Endpoint

`POST https://api.nexscope.ai/spapi/listInboundPlanBoxes`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /inbound/fba/2024-03-20/inboundPlans/{inboundPlanId}/boxes`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: inboundPlanId. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inbound_list_inbound_plan_boxes`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inbound-list-inbound-plan-boxes?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inbound-list-inbound-plan-boxes.request.json)
- [Response schema](../../schemas/amazon-sp-api-inbound-list-inbound-plan-boxes.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inbound-list-inbound-plan-boxes.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inbound-list-inbound-plan-boxes.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inbound-list-inbound-plan-boxes payloads/amazon-sp-api-inbound-list-inbound-plan-boxes.json --dry-run`.
