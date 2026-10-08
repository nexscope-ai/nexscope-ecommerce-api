# Amazon Product Research API

Browse the complete set of independently callable Amazon product-research APIs.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-research?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Use this directory to find the concrete API for a research goal. It returns links and typical inputs; invoke the linked API for the actual research data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-research/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `goal` | string | No | Optional filter: all, search, detail, reviews, image-search, opportunity, keyword, price-history, or sales-estimates. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-research.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-research request.json
# Or: node examples/javascript/run.mjs amazon-product-research request.json
# Or: python3 examples/python/run.py amazon-product-research request.json
```

### Published request example

```json
{
  "goal": "all"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "directoryType": "amazon-product-research-directory",
  "goal": "all",
  "count": 33,
  "recommendedApis": [
    {
      "slug": "amazon-search",
      "operation": "amazon_search",
      "typicalFields": [
        "keyword",
        "marketplace"
      ],
      "requestExample": {
        "keyword": "wireless speaker",
        "marketplace": "US"
      },
      "reason": "Search Amazon storefront results by keyword.",
      "endpoint": "/api/skill-api/v1/skills/amazon-search/run"
    },
    {
      "slug": "amazon-alexa-search",
      "operation": "amazon_alexa_search",
      "typicalFields": [
        "keyword",
        "marketplace"
      ],
      "requestExample": {
        "keyword": "wireless speaker",
        "marketplace": "US"
      },
      "reason": "Search Amazon Alexa ranking and product results.",
      "endpoint": "/api/skill-api/v1/skills/amazon-alexa-search/run"
    }
  ],
  "usage": "Invoke one recommended API directly for the actual research result."
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-research.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-research.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-research.json)
- [Response fixture](../../examples/responses/amazon-product-research.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_research`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
