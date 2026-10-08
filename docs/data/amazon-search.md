# Amazon Search API

Simulates a real user searching on Amazon's storefront to get real-time keyword ranking and search results page data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-search?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Simulates a real user searching on Amazon's storefront to get real-time keyword ranking and search results page data.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Keyword; please translate to the language of the target country whenever possible, e.g., use English keywords for the US, German keywords for Germany, etc. (max length 1024) | {} |
| `amazonDomain` | string | No | Amazon country site, default amazon.com | {} |
| `node` | string | No | Amazon category node (max length 1000) | {} |
| `language` | string | No | Language/region code, e.g., en_US, de_DE, ja_JP, fr_FR (max length 1000) | {} |
| `sort` | string | No | Sort order: relevanceblender (Featured, default), price-asc-rank (Price low to high), price-desc-rank (Price high to low), review-rank (Avg. customer review), date-desc-rank (Newest arrivals), exact-aware-popularity-rank (Best sellers) | {} |
| `page` | integer | No | Page number (starting from 1, ~20 items per page), default 1 | {} |
| `deliveryZip` | string | No | Delivery zip code, used to simulate Amazon frontend address. It is recommended to use commonly used zip codes for major cities in the target country, e.g., New York zip code 10001 for the US site (max length 1000) | {} |
| `device` | string | No | Device type: desktop, mobile, tablet, default desktop (max length 1000) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-search request.json
# Or: node examples/javascript/run.mjs amazon-search request.json
# Or: python3 examples/python/run.py amazon-search request.json
```

### Published request example

```json
{
  "keyword": "phone case",
  "page": 1
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "keyword": "phone case",
  "columns": [],
  "costToken": 1,
  "products": [
    {
      "asin": "B072MQ5BRX",
      "price": 1,
      "extractedPrice": 1,
      "oldPrice": 1,
      "extractedOldPrice": 1,
      "extractedPriceUnit": 1,
      "rating": 1,
      "ratings": 1,
      "position": 1,
      "sponsored": false,
      "imageUrl": "https://example.com/image.jpg",
      "asinUrl": "B072MQ5BRX",
      "availableDate": "2026-01-01",
      "monthlySalesUnits": 1,
      "snapEbtEligible": false,
      "keyword": "phone case"
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-search.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-search.json)
- [Response fixture](../../examples/responses/amazon-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
