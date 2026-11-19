# Amazon SP-API GET /fba/inbound/v1/eligibility/itemPreview

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-eligibility-get-item-eligibility-preview?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-eligibility-get-item-eligibility-preview?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API eligibility.getItemEligibilityPreview. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getitemeligibilitypreview

## Endpoint

`POST https://api.nexscope.ai/spapi/getItemEligibilityPreview`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inbound/v1/eligibility/itemPreview`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_eligibility_get_item_eligibility_preview`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-eligibility-get-item-eligibility-preview?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-eligibility-get-item-eligibility-preview.request.json)
- [Response schema](../../schemas/amazon-sp-api-eligibility-get-item-eligibility-preview.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-eligibility-get-item-eligibility-preview.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-eligibility-get-item-eligibility-preview.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-eligibility-get-item-eligibility-preview payloads/amazon-sp-api-eligibility-get-item-eligibility-preview.json --dry-run`.
