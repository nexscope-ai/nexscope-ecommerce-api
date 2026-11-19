# Amazon SP-API GET /catalog/v0/categories

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-catalog-listcatalogcategories?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-catalog-listcatalogcategories?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API catalog.listcatalogcategories. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/listcatalogcategories

## Endpoint

`POST https://api.nexscope.ai/spapi/listCatalogCategories`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `GET /catalog/v0/categories`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `queryString` | string | No | Operation query string, percent encoded, without the leading ?. |

## MCP

Tool name: `nexscope_amazon_sp_api_catalog_listcatalogcategories`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-catalog-listcatalogcategories?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-catalog-listcatalogcategories.request.json)
- [Response schema](../../schemas/amazon-sp-api-catalog-listcatalogcategories.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-catalog-listcatalogcategories.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-catalog-listcatalogcategories.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-catalog-listcatalogcategories payloads/amazon-sp-api-catalog-listcatalogcategories.json --dry-run`.
