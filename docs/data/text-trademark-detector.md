# Text Trademark Detector API

Text trademark detection and infringement risk analysis for e-commerce product listings.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/text-trademark-detector?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Text trademark detection and infringement risk analysis for e-commerce product listings.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/text-trademark-detector/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productTitle` | string | Yes | Product title, used for trademark detection (max 1000 characters) | {} |
| `regions` | string | No | Country/region codes, multiple separated by commas. Supported values: US, EM, GB, DE, FR, IT, ES, AU, CA, MX, JP, CN, WO, TR, BX | {} |
| `limit` | integer | Yes | Limit on the number of returned results (default 100, max 500) | {} |
| `productText` | string | No | Other product text information, such as bullet points or product description (max 1000 characters) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/text-trademark-detector.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh text-trademark-detector request.json
# Or: node examples/javascript/run.mjs text-trademark-detector request.json
# Or: python3 examples/python/run.py text-trademark-detector request.json
```

### Published request example

```json
{
  "regions": "US",
  "productTitle": "MagSafe Phone Case for iPhone",
  "limit": 10,
  "productText": "Protective magnetic phone case with shockproof corners."
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "data": [
    {
      "region": "US",
      "score": 1,
      "highestModeScore": 1,
      "isFamous": false,
      "isAmazonBrand": false,
      "isActiveHolder": false,
      "isCompatibility": false,
      "isCommonSense": false,
      "niceClass": [],
      "originalTextMatches": []
    }
  ],
  "detectId": "example-id",
  "columns": [],
  "blacklistTrademarks": [],
  "whitelistTrademarks": [],
  "costToken": 1,
  "blacklisttrademarks": [
    {
      "region": "US"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/text-trademark-detector.request.json) — field-descriptors
- [Response definition](../../schemas/text-trademark-detector.response.json) — field-descriptors
- [Editable request sample](../../payloads/text-trademark-detector.json)
- [Response fixture](../../examples/responses/text-trademark-detector.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_text_trademark_detector`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
