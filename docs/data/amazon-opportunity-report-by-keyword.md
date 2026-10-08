# Amazon Opportunity Report By Keyword API

Query Amazon business insight reports by keyword, covering six dimensions: market potential, product characteristics, user reviews, customer profiles, search trends, and pricing analysis with AI-powered comprehensive analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-opportunity-report-by-keyword?view=api&co-from=github-ecommerce-api)

Category: Keyword & Search Demand · Data API

Query Amazon business insight reports by keyword, covering six dimensions: market potential, product characteristics, user reviews, customer profiles, search trends, and pricing analysis with AI-powered comprehensive analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-opportunity-report-by-keyword/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `site` | string | Yes | Amazon site code, currently only supports US | {} |
| `keyword` | string | Yes | Search keyword for the insight report | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-opportunity-report-by-keyword.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-opportunity-report-by-keyword request.json
# Or: node examples/javascript/run.mjs amazon-opportunity-report-by-keyword request.json
# Or: python3 examples/python/run.py amazon-opportunity-report-by-keyword request.json
```

### Published request example

```json
{
  "keyword": "phone case",
  "site": "US"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "costTime": 1,
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-opportunity-report-by-keyword.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-opportunity-report-by-keyword.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-opportunity-report-by-keyword.json)
- [Response fixture](../../examples/responses/amazon-opportunity-report-by-keyword.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_opportunity_report_by_keyword`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
