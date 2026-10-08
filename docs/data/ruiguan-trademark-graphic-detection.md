# Ruiguan Trademark Graphic Detection API

Detect graphic trademarks in product images by comparing against registered trademark databases across 15 major trademark offices using YOLO-based object detection and visual similarity.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ruiguan-trademark-graphic-detection?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Detect graphic trademarks in product images by comparing against registered trademark databases across 15 major trademark offices using YOLO-based object detection and visual similarity.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ruiguan-trademark-graphic-detection/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Product image URL or Base64-encoded image data (maximum 1,000 characters) | {} |
| `topNumber` | integer | Yes | Maximum number of YOLO bounding boxes to return (default 5, maximum 100). The actual result count may be lower | {} |
| `productTitle` | string | No | Product title used for context-aware detection (maximum 1,000 characters) | {} |
| `trademarkName` | string | No | Possible graphic-logo name used to narrow the search (maximum 1,000 characters) | {} |
| `regions` | string | No | Comma-separated country or region codes to inspect. Defaults to all regions. Supported values: US (United States), WO (WIPO), ES (Spain), GB (United Kingdom), DE (Germany), IT (Italy), CA (Canada), MX (Mexico), EM (European Union), AU (Australia), FR (France), JP (Japan), TR (Turkey), BX (Benelux), and CN (China) | {} |
| `enableLocalizing` | boolean | No | Whether to enable image cropping (default false) | {} |
| `enableRadar` | boolean | No | Whether to enable radar monitoring (default true) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ruiguan-trademark-graphic-detection.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ruiguan-trademark-graphic-detection request.json
# Or: node examples/javascript/run.mjs ruiguan-trademark-graphic-detection request.json
# Or: python3 examples/python/run.py ruiguan-trademark-graphic-detection request.json
```

### Published request example

```json
{
  "enableRadar": false,
  "regions": "US",
  "imageUrl": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg",
  "topNumber": 10,
  "enableLocalizing": false
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "boundingBoxCount": 1,
  "total": 1,
  "data": [
    {
      "image": "https://example.com/image.jpg",
      "niceClass": [],
      "similarity": 1,
      "registrationDate": "2026-01-01",
      "bid": "example-id",
      "applicationDate": "2026-01-01"
    }
  ],
  "detectId": "example-id",
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ruiguan-trademark-graphic-detection.request.json) — field-descriptors
- [Response definition](../../schemas/ruiguan-trademark-graphic-detection.response.json) — field-descriptors
- [Editable request sample](../../payloads/ruiguan-trademark-graphic-detection.json)
- [Response fixture](../../examples/responses/ruiguan-trademark-graphic-detection.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ruiguan_trademark_graphic_detection`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
