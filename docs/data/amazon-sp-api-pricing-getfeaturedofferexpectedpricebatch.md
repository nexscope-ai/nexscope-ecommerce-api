# Amazon SP-API POST /batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API pricing.getfeaturedofferexpectedpricebatch. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfeaturedofferexpectedpricebatch

## Endpoint

`POST https://api.nexscope.ai/spapi/getFeaturedOfferExpectedPriceBatch`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `body` | object | No | Official operation request body. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_pricing_getfeaturedofferexpe_954a6e2e73a2`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch.request.json)
- [Response schema](../../schemas/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch payloads/amazon-sp-api-pricing-getfeaturedofferexpectedpricebatch.json --dry-run`.
