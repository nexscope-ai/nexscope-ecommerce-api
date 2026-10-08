# Amazon Advertising API

Run a catalogued Amazon Ads entity operation.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-advertising?view=api&co-from=github-ecommerce-api)

Category: Amazon Advertising · Data API

Accepts only documented ads_manager.sb/sd/sp operation IDs. Provider methods and paths are derived server-side; mutations require preview followed by confirmation.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-advertising/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operationId` | string | Yes | Exact catalog operation ID, for example ads_manager.sp.list_campaigns. | {} |
| `connectionId` | integer | Yes | Owned Amazon Ads connection ID. | {} |
| `payload` | object | No | Documented fields for the selected operation; required by create/update operations. | {} |
| `queryString` | string | No | Optional operation-specific query string without a leading ?. | {} |
| `adType` | string | No | Required only by ads_manager.sb.create_ads. | {} |
| `action` | string | No | preview (default) or confirm for mutations; ignored for reads. | {} |
| `confirmationToken` | string | No | Single-use token required when action is confirm. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-advertising.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-advertising request.json
# Or: node examples/javascript/run.mjs amazon-advertising request.json
# Or: python3 examples/python/run.py amazon-advertising request.json
```

### Published request example

```json
{
  "connectionId": 123,
  "operationId": "ads_manager.sp.list_campaigns",
  "payload": {}
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": {},
  "confirmationToken": "opaque-token",
  "expiresAt": "1760000000000"
}
```

## Full definitions

- [Request definition](../../schemas/amazon-advertising.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-advertising.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-advertising.json)
- [Response fixture](../../examples/responses/amazon-advertising.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_advertising`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
