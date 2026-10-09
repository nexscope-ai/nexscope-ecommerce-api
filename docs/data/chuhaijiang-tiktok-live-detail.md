# Nexscope TikTok Live Detail API

Nexscope TikTok Live Detail

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/chuhaijiang-tiktok-live-detail?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Nexscope TikTok Live Detail. Execute only this operation; no automatic retries or pagination. Preserve provider fields and metric units.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/chuhaijiang-tiktok-live-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `country` | string | Yes | Lowercase request market. Returned country_code may differ; preserve both. | {"enum": ["br", "de", "es", "fr", "gb", "id", "it", "jp", "mx", "my", "ph", "sg", "th", "us", "vn"]} |
| `id` | string | Yes | Livestream ID returned by its search operation. Keep identifiers as strings to avoid precision loss. | {"minLength": 1} |
| `include` | string | No | Comma-separated expansions: core. Request only needed expansions. | {"pattern": "^(core)(,(core))*$"} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/chuhaijiang-tiktok-live-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh chuhaijiang-tiktok-live-detail request.json
# Or: node examples/javascript/run.mjs chuhaijiang-tiktok-live-detail request.json
# Or: python3 examples/python/run.py chuhaijiang-tiktok-live-detail request.json
```

### Published request example

```json
{
  "id": "7643101948819835678",
  "country": "us",
  "include": "core"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "errmsg": "ok",
  "data": {
    "items": []
  },
  "errcode": 200
}
```

## Full definitions

- [Request definition](../../schemas/chuhaijiang-tiktok-live-detail.request.json) — json-schema
- [Response definition](../../schemas/chuhaijiang-tiktok-live-detail.response.json) — json-schema
- [Editable request sample](../../payloads/chuhaijiang-tiktok-live-detail.json)
- [Response fixture](../../examples/responses/chuhaijiang-tiktok-live-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_chuhaijiang_tiktok_live_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
