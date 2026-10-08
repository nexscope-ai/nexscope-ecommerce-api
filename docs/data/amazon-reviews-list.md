# Amazon Reviews List API

Fetch and analyze Amazon product reviews by ASIN, supporting 15 marketplaces (including US) with star rating filtering.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-reviews-list?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Fetch and analyze Amazon product reviews by ASIN, supporting 15 marketplaces (including US) with star rating filtering.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-reviews-list/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asin` | string | Yes | Amazon product ASIN | {} |
| `domainCode` | string | No | Amazon domain code, default com. Options: com, ca, co.uk, in, de, fr, it, es, co.jp, com.au, com.br, nl, se, com.mx, ae. Use com for the US site | {} |
| `star1Num` | integer | No | Number of 1-star reviews, default 10, max 100 | {} |
| `star2Num` | integer | No | Number of 2-star reviews, default 10, max 100 | {} |
| `star3Num` | integer | No | Number of 3-star reviews, default 10, max 100 | {} |
| `star4Num` | integer | No | Number of 4-star reviews, default 10, max 100 | {} |
| `star5Num` | integer | No | Number of 5-star reviews, default 10, max 100 | {} |
| `filterByKeyword` | string | No | Filter reviews by keyword, max length 1000 characters | {} |
| `sortBy` | string | No | Review sort order: recent (most recent reviews) or helpful (most helpful reviews), default recent | {} |
| `reviewerType` | string | No | Reviewer type: all_reviews (all reviews) or avp_only_reviews (verified purchases only), default all_reviews | {} |
| `mediaType` | string | No | Media type: all_contents (all content) or media_reviews_only (reviews with media only), default all_contents | {} |
| `formatType` | string | No | Format type: all_formats (all formats) or current_format (current format), default all_formats | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-reviews-list.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-reviews-list request.json
# Or: node examples/javascript/run.mjs amazon-reviews-list request.json
# Or: python3 examples/python/run.py amazon-reviews-list request.json
```

### Published request example

```json
{
  "domainCode": "com",
  "star4Num": 1,
  "star3Num": 1,
  "star2Num": 1,
  "star1Num": 1,
  "star5Num": 1,
  "asin": "B072MQ5BRX"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "data": [],
  "columns": [
    {
      "reviewId": "example-id",
      "asin": "B072MQ5BRX",
      "date": "2026-01-01",
      "verified": false,
      "vine": false,
      "numberOfHelpful": 1,
      "imageUrlList": [],
      "videoUrlList": [],
      "countRatings": 1,
      "countReviews": 1,
      "variationId": "example-id",
      "variationList": [],
      "currentPage": 1,
      "statusCode": 1,
      "locale": {},
      "reviewSummary": {},
      "filters": {}
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/amazon-reviews-list.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-reviews-list.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-reviews-list.json)
- [Response fixture](../../examples/responses/amazon-reviews-list.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_reviews_list`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
