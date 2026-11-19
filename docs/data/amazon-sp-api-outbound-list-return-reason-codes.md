# Amazon SP-API GET /fba/outbound/2020-07-01/returnReasonCodes

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-list-return-reason-codes?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-list-return-reason-codes?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.listReturnReasonCodes. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listreturnreasoncodes

## Endpoint

`POST https://api.nexscope.ai/spapi/listReturnReasonCodes`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/outbound/2020-07-01/returnReasonCodes`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_list_return_reason_codes`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-list-return-reason-codes?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-list-return-reason-codes.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-list-return-reason-codes.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-list-return-reason-codes.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-list-return-reason-codes.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-list-return-reason-codes payloads/amazon-sp-api-outbound-list-return-reason-codes.json --dry-run`.
