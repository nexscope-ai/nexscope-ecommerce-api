# Amazon SP-API POST /batches/products/pricing/2022-05-01/items/competitiveSummary

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getcompetitivesummary?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getcompetitivesummary?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API pricing.getcompetitivesummary. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getcompetitivesummary

## Endpoint

`POST https://api.nexscope.ai/spapi/getCompetitiveSummary`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /batches/products/pricing/2022-05-01/items/competitiveSummary`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_pricing_getcompetitivesummary`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-pricing-getcompetitivesummary?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-pricing-getcompetitivesummary.request.json)
- [Response schema](../../schemas/amazon-sp-api-pricing-getcompetitivesummary.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-pricing-getcompetitivesummary.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-pricing-getcompetitivesummary.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-pricing-getcompetitivesummary payloads/amazon-sp-api-pricing-getcompetitivesummary.json --dry-run`.
