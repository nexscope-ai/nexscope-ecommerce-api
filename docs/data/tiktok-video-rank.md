# TikTok Video Rank API

TikTok Video Rank public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-video-rank?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-video-rank/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `date` | string | Yes | Ranking date in YYYY-MM-DD format | {} |
| `rankType` | integer | Yes | Ranking type: 1, 2, or 3 | {} |
| `region` | string | Yes | TikTok market region code | {} |
| `videoRankField` | integer | Yes | Video ranking field: 1 or 2 | {} |
| `productCategoryId` | string | No | Optional product category ID | {} |
| `createdByAi` | string | No | Filter AI-created videos using the string true or false | {} |
| `pageNum` | integer | No | Page number, starting at 1 | {} |
| `pageSize` | integer | No | Page size from 10 to 100 in multiples of 10 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-video-rank.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-video-rank request.json
# Or: node examples/javascript/run.mjs tiktok-video-rank request.json
# Or: python3 examples/python/run.py tiktok-video-rank request.json
```

### Published request example

```json
{
  "rankType": 1,
  "videoRankField": 1,
  "region": "US",
  "pageNum": 1,
  "date": "2026-08-26",
  "pageSize": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "videos": [
    {
      "totalViewsCnt": 1,
      "videoId": "example-video-id",
      "region": "US"
    }
  ],
  "total": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-video-rank.request.json) — json-schema
- [Response definition](../../schemas/tiktok-video-rank.response.json) — json-schema
- [Editable request sample](../../payloads/tiktok-video-rank.json)
- [Response fixture](../../examples/responses/tiktok-video-rank.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_video_rank`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
