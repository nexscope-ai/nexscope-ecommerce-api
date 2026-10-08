# Zhihuiya Utility Patent Image Search API

Perform visual similarity search for utility model patents using an image URL, with filtering by country, legal status, date ranges, and assignee. Supports utility model patents only (type U) with shape-only or shape+pattern+color matching models.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/zhihuiya-utility-patent-image-search?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Perform visual similarity search for utility model patents using an image URL, with filtering by country, legal status, date ranges, and assignee. Supports utility model patents only (type U) with shape-only or shape+pattern+color matching models.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/zhihuiya-utility-patent-image-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `url` | string | Yes | Image URL (maximum 1,000 characters) | {} |
| `patentType` | string | Yes | Patent type: U for a utility model patent. Default: U | {} |
| `model` | integer | Yes | Image-search model. Design patents: 1 (smart association, recommended) or 2 (search this image). Utility model patents: 3 (match shape) or 4 (match shape, pattern, and color; recommended) | {} |
| `country` | string | No | Patent authority codes for countries, organizations, or regions, separated by commas, for example CN,US,JP. Omit to search all patent authorities | {} |
| `loc` | string | No | LOC classifications (Locarno classification numbers). Join multiple classifications with AND, OR, or NOT | {} |
| `legalStatus` | string | No | Comma-separated patent legal-status codes. Values: 1 (published), 2 (substantive examination), 3 (granted), 8 (duplicate-grant avoidance), 11 (withdrawn), 12 (withdrawn-unspecified), 17 (deemed withdrawn), 18 (voluntarily withdrawn), 13 (rejected), 14 (fully revoked), 15 (expired), 16 (annual fee unpaid), 21 (rights restored), 22 (rights terminated), 23 (partially invalid), 24 (application terminated), 30 (abandoned), 19 (deemed abandoned), 20 (voluntarily abandoned), 25 (abandoned-unspecified), 222 (PCT did not enter designated state within designation period), 223 (PCT entered designated state within designation period), 224 (PCT entered designated state after designation period), and 225 (PCT did not enter designated state after designation period) | {} |
| `simpleLegalStatus` | string | No | Comma-separated simplified patent legal-status codes. Values: 0 (inactive), 1 (active), 2 (pending), 220 (PCT designation period expired), 221 (within PCT designation period), and 999 (unconfirmed) | {} |
| `assignees` | string | No | Applicant or patent owner (maximum 1,000 characters) | {} |
| `applyStartTime` | string | No | Patent application start date in yyyyMMdd format | {} |
| `applyEndTime` | string | No | Patent application end date in yyyyMMdd format | {} |
| `publicStartTime` | string | No | Patent publication start date in yyyyMMdd format | {} |
| `publicEndTime` | string | No | Patent publication end date in yyyyMMdd format | {} |
| `limit` | integer | No | Number of patents to return, from 1 to 100. Default: 10 | {} |
| `offset` | integer | No | Result offset, from 0 to 1,000. Default: 0 | {} |
| `field` | string | No | Result sort field: SCORE (relevance), APD (application date), PBD (publication date), or ISD (grant date). Default: SCORE | {} |
| `order` | string | No | Available when field is APD, PBD, or ISD: desc (descending) or asc (ascending). Default: desc | {} |
| `lang` | string | No | Preferred title language: original (original patent title), cn (Chinese-translated title), or en (English-translated title). Default: original | {} |
| `preFilter` | integer | No | Whether to enable country/LOC pre-filtering: 1 for enabled and 0 for disabled. Default: 1 | {} |
| `stemming` | integer | No | Whether to enable stemming: 1 for enabled and 0 for disabled. Default: 0 | {} |
| `mainField` | string | No | Primary patent fields, including title, abstract, claims, specification, publication number, application number, applicant, inventor, and IPC/UPC/LOC classifications (maximum 1,000 characters) | {} |
| `includeMachineTranslation` | boolean | No | Include machine-translated data in the search | {} |
| `scoreExpansion` | boolean | No | Score expansion | {} |
| `isHttps` | integer | No | Whether to return images over HTTPS: 1 for HTTPS and 0 for HTTP. Default: 0 | {} |
| `returnImgId` | boolean | No | Whether to return img_id. Default: false | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/zhihuiya-utility-patent-image-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh zhihuiya-utility-patent-image-search request.json
# Or: node examples/javascript/run.mjs zhihuiya-utility-patent-image-search request.json
# Or: python3 examples/python/run.py zhihuiya-utility-patent-image-search request.json
```

### Published request example

```json
{
  "url": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg",
  "country": "US",
  "offset": 0,
  "stemming": 0,
  "limit": 5,
  "isHttps": 1,
  "preFilter": 1,
  "model": 4,
  "patentType": "U"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "allRecordsCount": 1,
  "data": [
    {
      "patentId": "example-id",
      "url": "https://example.com/image.jpg",
      "score": 1,
      "loc": [],
      "locMatch": 1,
      "apdt": 1,
      "pbdt": 1,
      "imgId": "example-id"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/zhihuiya-utility-patent-image-search.request.json) — field-descriptors
- [Response definition](../../schemas/zhihuiya-utility-patent-image-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/zhihuiya-utility-patent-image-search.json)
- [Response fixture](../../examples/responses/zhihuiya-utility-patent-image-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_zhihuiya_utility_patent_image_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
