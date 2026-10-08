# Google Patent Search API

Google Patent Search public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/google-patent-search?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/google-patent-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `q` | string | Yes | Patent search query, maximum 1000 characters | {} |
| `num` | integer | No | Results per page, from 10 to 100 | {} |
| `page` | integer | No | Page number, starting at 1 | {} |
| `country` | string | No | Country filter | {} |
| `language` | string | No | Language filter | {} |
| `before` | string | No | Upper date boundary such as filing:20260101 | {} |
| `after` | string | No | Lower date boundary such as filing:20200101 | {} |
| `sort` | string | No | Sort order: new or old | {} |
| `type` | string | No | Document type: PATENT or DESIGN | {} |
| `status` | string | No | Document status: GRANT or APPLICATION | {} |
| `patents` | boolean | No | Include patent results | {} |
| `scholar` | boolean | No | Include scholar results | {} |
| `litigation` | string | No | Litigation filter: YES or NO | {} |
| `inventor` | string | No | Inventor filter | {} |
| `assignee` | string | No | Assignee filter | {} |
| `clustered` | boolean | No | Enable clustered results; only true is supported | {} |
| `dups` | string | No | Duplicate grouping mode; only language is supported | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/google-patent-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh google-patent-search request.json
# Or: node examples/javascript/run.mjs google-patent-search request.json
# Or: python3 examples/python/run.py google-patent-search request.json
```

### Published request example

```json
{
  "q": "wireless earbuds",
  "num": 10,
  "page": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "results": [],
  "summary": {
    "cpc": [
      {
        "percentage": 100,
        "key": "Total"
      }
    ]
  }
}
```

## Full definitions

- [Request definition](../../schemas/google-patent-search.request.json) — json-schema
- [Response definition](../../schemas/google-patent-search.response.json) — json-schema
- [Editable request sample](../../payloads/google-patent-search.json)
- [Response fixture](../../examples/responses/google-patent-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_google_patent_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
