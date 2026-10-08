# Amazon Alexa Search API

Initiate natural language Q&A through Amazon's storefront Alexa shopping assistant to get shopping guidance answers, recommended product groups, ASIN lists, and follow-up questions. Each call supports only 1 prompt; for follow-ups, the agent must summarize context and concatenate a new question for a new request. A url can be used to supplement Amazon page context.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-alexa-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Initiate natural language Q&A through Amazon's storefront Alexa shopping assistant to get shopping guidance answers, recommended product groups, ASIN lists, and follow-up questions. Each call supports only 1 prompt; for follow-ups, the agent must summarize context and concatenate a new question for a new request. A url can be used to supplement Amazon page context.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-alexa-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `prompts` | array | Yes | Conversation prompt array, supports only 1 entry. Each call accepts only 1 question. For follow-up questions, the agent must summarize key information from the previous response (recommended products, ASINs, key conclusions, etc.), concatenate it with the new question, and send it as a new prompts[0]. Each call is an independent new session and does not retain cross-call conversation history | {} |
| `format` | string | No | Response format: markdown (default) returns a readable report; json returns a structured data array | {} |
| `url` | string | No | Linked page URL, used to supplement the page context of Alexa's current response. Only pass this when the user provides a specific page (category page / search results page / product detail page, etc.); do not pass this parameter for the Amazon homepage (e.g. https://www.amazon.com/) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-alexa-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-alexa-search request.json
# Or: node examples/javascript/run.mjs amazon-alexa-search request.json
# Or: python3 examples/python/run.py amazon-alexa-search request.json
```

### Published request example

```json
{
  "format": "markdown",
  "prompts": [
    "What are good phone cases for iPhone?"
  ]
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": [
    {
      "followUpQuestions": [],
      "products": []
    }
  ],
  "resultsNum": 1,
  "errcode": 1,
  "costTime": 1,
  "costToken": 1,
  "taskId": "example-id",
  "products": [
    {
      "items": [
        {
          "asin": "B072MQ5BRX",
          "url": "https://example.com/image.jpg"
        }
      ]
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-alexa-search.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-alexa-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-alexa-search.json)
- [Response fixture](../../examples/responses/amazon-alexa-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_alexa_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
