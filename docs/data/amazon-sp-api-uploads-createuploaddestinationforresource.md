# Amazon SP-API POST /uploads/2020-11-01/uploadDestinations/{resource}

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sp-api-uploads-createuploaddestinationforresource?co-from=github-ecommerce-api) · [Data Example](https://www.nexscope.ai/api-docs/amazon-sp-api-uploads-createuploaddestinationforresource?co-from=github-ecommerce-api#data-example)

Category: Amazon Selling Partner API

Amazon Seller SP-API uploads.createuploaddestinationforresource. Uses an owned seller connection. Official reference: https://developer-docs.amazon.com/sp-api/reference/createuploaddestinationforresource Changes require preview and confirmation.

Review the target and obtain explicit approval before confirming any change. Supplied JSON examples use fictional values.

## Endpoint

`POST https://api.nexscope.ai/spapi/createUploadDestinationForResource`

Send your Nexscope API key as a Bearer token and use `Content-Type: application/json`. Each successful call costs **10 credits**.

Amazon upstream operation: `POST /uploads/2020-11-01/uploadDestinations/{resource}`.

## Request fields

| Name | Type | Required | Description |
|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Seller connection ID. |
| `pathParams` | object | Yes | Required path values: resource. |
| `contentBase64` | string | Yes | Base64 content to upload through the backend; maximum 20 MiB decoded. |
| `contentType` | string | No | Uploaded content MIME type. |
| `marketplaceId` | string | Yes | Amazon marketplace ID. |
| `action` | string | No | preview (default) or confirm. |
| `confirmationToken` | string | No | Single-use token returned by preview; required for confirm. |

## MCP

Tool name: `nexscope_amazon_sp_api_uploads_createuploaddestinat_fdd522c9493a`. See the [MCP reference](https://www.nexscope.ai/mcp-map/amazon-sp-api-uploads-createuploaddestinationforresource?co-from=github-ecommerce-api).

## Definitions and examples

- [Request schema](../../schemas/amazon-sp-api-uploads-createuploaddestinationforresource.request.json)
- [Response schema](../../schemas/amazon-sp-api-uploads-createuploaddestinationforresource.response.json)
- [Illustrative request](../../payloads/amazon-sp-api-uploads-createuploaddestinationforresource.json)
- [Illustrative response](../../examples/responses/amazon-sp-api-uploads-createuploaddestinationforresource.json)

From the repository root, preview the resolved request with `python3 examples/python/run.py amazon-sp-api-uploads-createuploaddestinationforresource payloads/amazon-sp-api-uploads-createuploaddestinationforresource.json --dry-run`.
