# Amazon Policy Feed API

Query Amazon is latest policy, regulation, and compliance feed. Supports paginated browsing by marketplace and time range (with AI-generated Chinese summaries), and fetching full article body by record ID.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-policy-feed?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Query Amazon is latest policy, regulation, and compliance feed. Supports paginated browsing by marketplace and time range (with AI-generated Chinese summaries), and fetching full article body by record ID.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-policy-feed/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `site` | string | No | Amazon site code, uppercase. Defaults to US. | {} |
| `publishedAtGte` | string | No | Publication or change time lower bound, inclusive, format yyyy-MM-dd HH:mm:ss. | {} |
| `publishedAtLte` | string | No | Publication or change time upper bound, inclusive, format yyyy-MM-dd HH:mm:ss. | {} |
| `page` | integer | No | Page number, starting from 1. | {} |
| `pageSize` | integer | No | Items per page, range 1-100. | {} |
| `id` | string | No | News record ID from data[].id. Required when calling the policy detail endpoint. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-policy-feed.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-policy-feed request.json
# Or: node examples/javascript/run.mjs amazon-policy-feed request.json
# Or: python3 examples/python/run.py amazon-policy-feed request.json
```

### Published request example

```json
{
  "site": "US",
  "page": 1,
  "pageSize": 20
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errcode": 200,
  "errmsg": "ok",
  "code": "200",
  "msg": "ok",
  "total": 1,
  "type": "tableListWorkbenches",
  "data": [
    {
      "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
      "title": "Amazon policy update",
      "summaryZh": "Policy summary",
      "originalUrl": "https://example.com/news",
      "publishedAt": "2026-01-01 00:00:00"
    }
  ],
  "stdout": "# Amazon policy update",
  "title": "Amazon policy update",
  "summaryZh": "Policy summary",
  "costTime": 1,
  "costToken": 1,
  "columns": []
}
```

## Full definitions

- [Request definition](../../schemas/amazon-policy-feed.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-policy-feed.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-policy-feed.json)
- [Response fixture](../../examples/responses/amazon-policy-feed.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_policy_feed`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
