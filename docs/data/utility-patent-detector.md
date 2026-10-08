# Utility Patent Detector API

Detect and search for similar utility/invention patents based on product information.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/utility-patent-detector?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Detect and search for similar utility/invention patents based on product information.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/utility-patent-detector/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productTitle` | string | Yes | Product title, max 1000 characters | {} |
| `productDescription` | string | Yes | Product description, max 1000 characters | {} |
| `region` | string | Yes | Country/region code(s) where the product is intended for sale, multiple separated by commas. Currently supports US. Default US | {} |
| `topNumber` | integer | Yes | Number of results to recall, range: 10--200, default 100 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/utility-patent-detector.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh utility-patent-detector request.json
# Or: node examples/javascript/run.mjs utility-patent-detector request.json
# Or: python3 examples/python/run.py utility-patent-detector request.json
```

### Published request example

```json
{
  "productTitle": "Magnetic phone case with ring stand",
  "region": "US",
  "productDescription": "A protective smartphone case with a magnetic ring stand and shockproof corners.",
  "topNumber": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "detectId": "example-id",
  "costToken": 1,
  "columns": [],
  "data": [
    {
      "globalUtilityId": "example-id",
      "similarity": 1,
      "applicationDate": "2026-01-01",
      "publicationDate": "2026-01-01",
      "estimatedDueDate": "2026-01-01",
      "region": "US",
      "inventors": [],
      "inventorAddresses": [],
      "applicants": [],
      "applicantAddresses": [],
      "priorityNumber": [],
      "relatedPublicationDate": [],
      "patentImageUrl": "https://example.com/image.jpg",
      "images": [],
      "classNumList": [],
      "cpcKindRaw": [],
      "troCase": false,
      "troHolder": false
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/utility-patent-detector.request.json) — field-descriptors
- [Response definition](../../schemas/utility-patent-detector.response.json) — field-descriptors
- [Editable request sample](../../payloads/utility-patent-detector.json)
- [Response fixture](../../examples/responses/utility-patent-detector.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_utility_patent_detector`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
