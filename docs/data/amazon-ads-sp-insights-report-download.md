# Amazon Ads SP Insights Report Download API

Amazon Ads SP Insights Report Download using an owned Amazon Ads connection.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-ads-sp-insights-report-download?view=api&co-from=github-ecommerce-api)

Category: Amazon Advertising · Data API

Uses existing Amazon Ads authorization and tokenized download handling. Create once, poll by reportId, then download using a documentToken.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-ads-sp-insights-report-download/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Ads connection ID; profile and region are resolved by the backend. | {} |
| `documentToken` | string | Yes | Backend-issued token from a completed report part, consumed by the existing download workflow. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-ads-sp-insights-report-download.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-ads-sp-insights-report-download request.json
# Or: node examples/javascript/run.mjs amazon-ads-sp-insights-report-download request.json
# Or: python3 examples/python/run.py amazon-ads-sp-insights-report-download request.json
```

### Published request example

```json
{
  "connectionId": 123,
  "documentToken": "opaque-document-token"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "content": "date.value,metric.impressions\n2026-08-01,10\n",
  "contentType": "text/csv"
}
```

## Full definitions

- [Request definition](../../schemas/amazon-ads-sp-insights-report-download.request.json) — json-schema
- [Response definition](../../schemas/amazon-ads-sp-insights-report-download.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-ads-sp-insights-report-download.json)
- [Response fixture](../../examples/responses/amazon-ads-sp-insights-report-download.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_ads_sp_insights_report_download`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
