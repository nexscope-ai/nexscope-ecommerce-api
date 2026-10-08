# eBay Search API

Search and browse product listings across multiple eBay international sites.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ebay-search?view=api&co-from=github-ecommerce-api)

Category: eBay Marketplace · Data API

Search and browse product listings across multiple eBay international sites.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ebay-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | No | Search keyword, max 1024 characters | {} |
| `ebayDomain` | string | No | eBay site domain, default ebay.com. Options: ebay.com (United States), ebay.co.uk (United Kingdom), ebay.de (Germany), ebay.fr (France), ebay.it (Italy), ebay.es (Spain), ebay.ca (Canada), ebay.com.au (Australia), ebay.nl (Netherlands), ebay.at (Austria), ebay.ch (Switzerland), ebay.pl (Poland), ebay.ie (Ireland), ebay.com.hk (Hong Kong, China), ebay.com.my (Malaysia), ebay.com.sg (Singapore) | {} |
| `page` | integer | No | Page number for pagination, default 1 | {} |
| `pageSize` | integer | No | Maximum results per page, default 50. Options: 25, 50, 100, 200 | {} |
| `orderBy` | string | No | Sort order, default 12 (Best Match). Options: 1 (Ending soonest), 2 (Price lowest), 3 (Price highest), 7 (Distance nearest), 10 (Newly listed), 12 (Best Match), 15 (Price + shipping lowest), 16 (Price + shipping highest), 18 (New first), 19 (Used first) | {} |
| `priceMin` | number | No | Minimum price filter | {} |
| `priceMax` | number | No | Maximum price filter | {} |
| `itemCondition` | string | No | Item condition code, multiple separated by \ | {} |
| `buyingFormat` | string | No | Buying format. Options: Auction, BIN (Buy It Now), BO (Best Offer) | {} |
| `showOnly` | string | No | Filter conditions, comma-separated for multiple values. Options: Complete (Ended), Sold (Sold), FR (Free returns), RPA (Returns accepted), AS (Authorized seller), Savings (Discounts), SaleItems (Sale items), Lots (Lots), Charity (Charity), AV, FS (Free shipping), LPickup (Local pickup) | {} |
| `location` | integer | No | Country/region code of item location (e.g., 1=United States, 2=Canada, 3=United Kingdom, 45=China, 77=Germany) | {} |
| `prefLoc` | string | No | Preferred location scope. Options: 1 (Domestic), 2 (Regional), 3 (Worldwide) | {} |
| `zipCode` | string | No | ZIP or postal code for filtering shippable items by region | {} |
| `categoryId` | integer | No | eBay category ID for category-specific search | {} |
| `noCache` | boolean | No | Whether to bypass cache, default false | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ebay-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ebay-search request.json
# Or: node examples/javascript/run.mjs ebay-search request.json
# Or: python3 examples/python/run.py ebay-search request.json
```

### Published request example

```json
{
  "page": 1,
  "pageSize": 10,
  "keyword": "phone case"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "total": 1,
  "products": [
    {
      "productId": "example-id",
      "price": 1,
      "minPrice": 1,
      "maxPrice": 1,
      "oldPrice": 1,
      "imageUrl": "https://example.com/image.jpg",
      "sellerReviews": 1,
      "positiveFeedbackInPercentage": 1,
      "salesQuantity": 1,
      "bidsCount": 1,
      "sponsored": false
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ebay-search.request.json) — field-descriptors
- [Response definition](../../schemas/ebay-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ebay-search.json)
- [Response fixture](../../examples/responses/ebay-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ebay_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
