# Amazon Ads API Access

Authorize Amazon Ads and inspect owned connections and profiles.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-ads-api-access?view=api&co-from=github-ecommerce-api)

Category: Amazon Advertising · Data API

Starts Amazon Ads OAuth authorization or returns safe connection and profile metadata. Access and refresh tokens are never accepted or returned.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-ads-api-access/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operation` | string | Yes | Operation: authorize, connections, or profiles. | {} |
| `region` | string | Yes | Required when operation=authorize. Amazon Ads region: NA, EU, or FE. | {} |
| `marketplaceId` | string | Yes | Required when operation=authorize. Amazon marketplace identifier. | {} |
| `accountName` | string | No | Optional display name for the authorization request. | {} |
| `connectionId` | integer | No | Required when operation=profiles. Owned Amazon Ads connection ID. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-ads-api-access.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-ads-api-access request.json
# Or: node examples/javascript/run.mjs amazon-ads-api-access request.json
# Or: python3 examples/python/run.py amazon-ads-api-access request.json
```

### Published request example

```json
{
  "operation": "authorize",
  "accountName": "US Ads account",
  "region": "NA",
  "marketplaceId": "ATVPDKIKX0DER"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "authorizationUrl": "https://example.com/authorize",
  "state": "opaque-state",
  "expiresAt": "1760000000000",
  "connections": [],
  "profiles": [
    {
      "profileId": "123456789",
      "countryCode": "US",
      "currencyCode": "USD"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-ads-api-access.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-ads-api-access.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-ads-api-access.json)
- [Response fixture](../../examples/responses/amazon-ads-api-access.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_ads_api_access`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
