# TikTok Video Download URL API

Resolve TikTok video URLs to return no-watermark/watermarked download addresses, playback addresses, and cover image addresses for saving promotional video assets or offline analysis.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/tiktok-video-download-url?view=api&co-from=github-ecommerce-api)

Category: TikTok / Social Commerce · Data API

Resolve TikTok video URLs to return no-watermark/watermarked download addresses, playback addresses, and cover image addresses for saving promotional video assets or offline analysis.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/tiktok-video-download-url/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `url` | string | Yes | TikTok video URL, supports two formats: https://vt.tiktok.com/xxx short link or https://www.tiktok.com/@user/video/xxx full link. Max length 1000 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/tiktok-video-download-url.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh tiktok-video-download-url request.json
# Or: node examples/javascript/run.mjs tiktok-video-download-url request.json
# Or: python3 examples/python/run.py tiktok-video-download-url request.json
```

### Published request example

```json
{
  "url": "https://www.tiktok.com/@zachking/video/6768504823336815877"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "noWatermarkDownloadUrl": "https://example.com/image.jpg",
  "downloadUrl": "https://example.com/image.jpg",
  "playUrl": "https://example.com/image.jpg",
  "coverUrl": "https://example.com/image.jpg",
  "dynamicCoverUrl": "https://example.com/image.jpg",
  "videoId": "example-id",
  "columns": [],
  "costToken": 1,
  "errcode": 1
}
```

## Full definitions

- [Request definition](../../schemas/tiktok-video-download-url.request.json) — field-descriptors
- [Response definition](../../schemas/tiktok-video-download-url.response.json) — field-descriptors
- [Editable request sample](../../payloads/tiktok-video-download-url.json)
- [Response fixture](../../examples/responses/tiktok-video-download-url.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_tiktok_video_download_url`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
