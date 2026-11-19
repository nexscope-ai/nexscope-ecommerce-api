# Amazon SP-API GET /fba/inventory/v1/summaries

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-inventory-get-inventory-summaries?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-inventory-get-inventory-summaries?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API inventory.getInventorySummaries. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getinventorysummaries

## Endpoint

`POST https://api.nexscope.ai/spapi/getInventorySummaries`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/inventory/v1/summaries`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_inventory_get_inventory_summaries`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-inventory-get-inventory-summaries?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-inventory-get-inventory-summaries.request.json)
- [Response schema](../../schemas/amazon-sp-api-inventory-get-inventory-summaries.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-inventory-get-inventory-summaries.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-inventory-get-inventory-summaries.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-inventory-get-inventory-summaries payloads/amazon-sp-api-inventory-get-inventory-summaries.json --dry-run`.
