# Amazon Ads Reporting API

Create, poll, and download governed Amazon Ads reports.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-ads-reporting?view=api&co-from=github-ecommerce-api)

Category: Amazon Advertising · Data API

Uses the source get_report contract: omit reportId to create, supply reportId to poll, or supply a backend documentToken to download.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-ads-reporting/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `connectionId` | integer | Yes | Owned Amazon Ads connection ID. | {} |
| `reportId` | string | No | Existing report ID; when present the API polls that report. | {} |
| `reportTypeId` | string | No | Report type required by a new report unless configuration supplies it. | {} |
| `adProduct` | string | No | Ad product required by a new report unless configuration supplies it. | {} |
| `groupBy` | array | No | Report grouping fields. | {} |
| `columns` | array | No | Requested report columns. | {} |
| `name` | string | No | Optional report name. | {} |
| `startDate` | string | No | Inclusive report start date for a new report. | {} |
| `endDate` | string | No | Inclusive report end date for a new report. | {} |
| `timeUnit` | string | No | Optional report time unit. | {} |
| `format` | string | No | Optional report format. | {} |
| `filters` | array | No | Optional report filters. | {} |
| `configuration` | object | No | Complete Amazon Ads reporting configuration; may replace reportTypeId/adProduct/groupBy/columns. | {} |
| `documentToken` | string | No | Backend-issued token for downloading a completed report. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-ads-reporting.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-ads-reporting request.json
# Or: node examples/javascript/run.mjs amazon-ads-reporting request.json
# Or: python3 examples/python/run.py amazon-ads-reporting request.json
```

### Published request example

```json
{
  "reportTypeId": "spCampaigns",
  "startDate": "2026-07-01",
  "columns": [
    "campaignId",
    "impressions"
  ],
  "endDate": "2026-07-31",
  "groupBy": [
    "campaign"
  ],
  "connectionId": 123,
  "adProduct": "SPONSORED_PRODUCTS"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "status": "PENDING",
  "reportId": "report-id",
  "documentToken": "opaque-document-token",
  "content": {},
  "contentType": "application/json"
}
```

## Full definitions

- [Request definition](../../schemas/amazon-ads-reporting.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-ads-reporting.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-ads-reporting.json)
- [Response fixture](../../examples/responses/amazon-ads-reporting.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_ads_reporting`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
