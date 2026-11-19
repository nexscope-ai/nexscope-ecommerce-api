# Amazon SP-API GET /fba/outbound/2020-07-01/features

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-features?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-features?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.getFeatures. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfeatures

## Endpoint

`POST https://api.nexscope.ai/spapi/getFeatures`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/outbound/2020-07-01/features`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_get_features`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-get-features?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-get-features.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-get-features.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-get-features.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-get-features.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-get-features payloads/amazon-sp-api-outbound-get-features.json --dry-run`.
