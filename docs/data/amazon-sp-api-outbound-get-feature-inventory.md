# Amazon SP-API GET /fba/outbound/2020-07-01/features/inventory/{featureName}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-feature-inventory?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-outbound-get-feature-inventory?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API outbound.getFeatureInventory. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getfeatureinventory

## Endpoint

`POST https://api.nexscope.ai/spapi/getFeatureInventory`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /fba/outbound/2020-07-01/features/inventory/{featureName}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: featureName. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_outbound_get_feature_inventory`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-outbound-get-feature-inventory?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-outbound-get-feature-inventory.request.json)
- [Response schema](../../schemas/amazon-sp-api-outbound-get-feature-inventory.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-outbound-get-feature-inventory.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-outbound-get-feature-inventory.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-outbound-get-feature-inventory payloads/amazon-sp-api-outbound-get-feature-inventory.json --dry-run`.
