# Ruiguan Detection Patent Design API

Detect design patent infringement risks by comparing a product image against a global design patent database across 25+ jurisdictions.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ruiguan-detection-patent-design?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Detect design patent infringement risks by comparing a product image against a global design patent database across 25+ jurisdictions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ruiguan-detection-patent-design/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Product image URL used for comparison with the patent database (maximum 1,000 characters) | {} |
| `queryMode` | string | Yes | Search mode: physical for product-photo search, line for line-drawing search, or hybrid for combined search. Maximum 1,000 characters | {} |
| `topNumber` | integer | Yes | Number of patents to return (maximum 100) | {} |
| `regions` | string | No | Country or region codes where the product is sold, separated by commas, for example US,EU,CN. Supported values: US, EU, CN, JP, KR, DE, GB, FR, IT, AU, CA, BR, MX, IN, TH, SE, CH, IE, IL, DK, NZ, AT, BX, FI, and WO. Maximum 1,000 characters | {} |
| `productTitle` | string | No | Product title used to provide additional search context (maximum 1,000 characters) | {} |
| `productDescription` | string | No | Product description used to provide additional search context (maximum 1,000 characters) | {} |
| `patentStatus` | string | No | Patent-validity filter: 1 for active patents, 0 for inactive patents, or 1,0 for all patents. Maximum 1,000 characters | {} |
| `enableRadar` | boolean | No | Whether to enable AI radar analysis for potential infringement | {} |
| `topLoc` | string | No | Top-level LOC classes to search, for example 06,07. Pattern: ^(0[1-9]\ | {} |
| `sourceLanguage` | string | No | Source-language code used to translate content into English, for example zh-CN. Leave empty when the text is already English. Maximum 1,000 characters | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ruiguan-detection-patent-design.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ruiguan-detection-patent-design request.json
# Or: node examples/javascript/run.mjs ruiguan-detection-patent-design request.json
# Or: python3 examples/python/run.py ruiguan-detection-patent-design request.json
```

### Published request example

```json
{
  "productDescription": "A protective smartphone case with a magnetic ring stand and shockproof corners.",
  "topNumber": 10,
  "regions": "US",
  "enableRadar": false,
  "imageUrl": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg",
  "productTitle": "Magnetic phone case",
  "patentStatus": "1,0",
  "queryMode": "physical"
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
      "patentImageUrl": "https://example.com/image.jpg",
      "images": [],
      "inventors": [],
      "applicants": [],
      "applicantAddresses": [],
      "troCase": false,
      "troHolder": false,
      "radarResult": {},
      "applicationDate": "2026-01-01",
      "publicationDate": "2026-01-01",
      "grantDate": "2026-01-01",
      "estimatedDueDate": "2026-01-01",
      "patentFamily": [],
      "globalPatentId": "example-id",
      "globalImageId": "example-id"
    }
  ],
  "columns": [],
  "costToken": 1,
  "radarResult": {
    "same": false
  }
}
```

## Full definitions

- [Request definition](../../schemas/ruiguan-detection-patent-design.request.json) — field-descriptors
- [Response definition](../../schemas/ruiguan-detection-patent-design.response.json) — field-descriptors
- [Editable request sample](../../payloads/ruiguan-detection-patent-design.json)
- [Response fixture](../../examples/responses/ruiguan-detection-patent-design.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ruiguan_detection_patent_design`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
