# Amazon SP-API GET /catalog/2022-04-01/items/{asin}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-catalog-getcatalogitem-2022-04-01?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-catalog-getcatalogitem-2022-04-01?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API catalog.getcatalogitem-2022-04-01. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/getcatalogitem

## Endpoint

`POST https://api.nexscope.ai/spapi/getCatalogItemV20220401`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /catalog/2022-04-01/items/{asin}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: asin. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_catalog_getcatalogitem_2022_04_01`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-catalog-getcatalogitem-2022-04-01?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-catalog-getcatalogitem-2022-04-01.request.json)
- [Response schema](../../schemas/amazon-sp-api-catalog-getcatalogitem-2022-04-01.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-catalog-getcatalogitem-2022-04-01.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-catalog-getcatalogitem-2022-04-01.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-catalog-getcatalogitem-2022-04-01 payloads/amazon-sp-api-catalog-getcatalogitem-2022-04-01.json --dry-run`.
