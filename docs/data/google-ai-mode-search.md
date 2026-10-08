# Google AI Mode Search API

AI Overview (AI Mode) scraping via Google Search. Returns AI-summarized key points for a single keyword, ideal for deep research, technical Q&A, long-tail product selection, and cross-border consumer preference analysis using the latest web information. Single-round only; follow-ups require the agent to summarize context and issue a new request. Triggered by: Google AI, AI Overview, AI Mode, Google AI search, AI search, deep research, consumer preference analysis, web summary, long-tail product research, cross-border market insights.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/google-ai-mode-search?view=api&co-from=github-ecommerce-api)

Category: Search & Trend Intelligence · Data API

AI Overview (AI Mode) scraping via Google Search. Returns AI-summarized key points for a single keyword, ideal for deep research, technical Q&A, long-tail product selection, and cross-border consumer preference analysis using the latest web information. Single-round only; follow-ups require the agent to summarize context and issue a new request. Triggered by: Google AI, AI Overview, AI Mode, Google AI search, AI search, deep research, consumer preference analysis, web summary, long-tail product research, cross-border market insights.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/google-ai-mode-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Google search keyword, passed as the q= parameter to initiate a Google AI Mode search. Only supports single-turn conversation; follow-up prompts are not supported. To ask follow-up questions, the agent must independently summarize key information from the previous AI overview, concatenate the new question, and send it as a new keyword in a new request | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/google-ai-mode-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh google-ai-mode-search request.json
# Or: node examples/javascript/run.mjs google-ai-mode-search request.json
# Or: python3 examples/python/run.py google-ai-mode-search request.json
```

### Published request example

```json
{
  "keyword": "best phone case material for iPhone"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "sourceUrl": "https://example.com/image.jpg",
  "resultsNum": 1,
  "errcode": 1,
  "costTime": 1,
  "costToken": 1,
  "taskId": "example-id"
}
```

## Full definitions

- [Request definition](../../schemas/google-ai-mode-search.request.json) — field-descriptors
- [Response definition](../../schemas/google-ai-mode-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/google-ai-mode-search.json)
- [Response fixture](../../examples/responses/google-ai-mode-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_google_ai_mode_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
