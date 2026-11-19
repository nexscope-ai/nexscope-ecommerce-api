# Amazon SP-API POST /fulfillment/outbound/2026-07-04/offers

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-get-offers?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-2026-get-offers?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound-2026.getOffers. Uses an owned seller connection. Official reference: https://developer-docs.amazon/sp-api/reference/getoffers

## Endpoint

`POST https://api.nexscope.ai/spapi/getOffers`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /fulfillment/outbound/2026-07-04/offers`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_2026_get_offers`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-2026-get-offers?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-2026-get-offers.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-2026-get-offers.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-2026-get-offers.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-2026-get-offers.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-2026-get-offers payloads/amazon-sp-api-outbound-2026-get-offers.json --dry-run`.
