# 1688 Product Detail API

Returns normalized public ecommerce research data with a fixed read-only provider path.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-product-detail?view=api&co-from=github-ecommerce-api)

Category: 1688 Sourcing · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/1688-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `offerId` | string | Yes | Positive integer 1688 product ID. Use a string to preserve large identifiers. | {} |
| `country` | string | No | Optional upstream compatibility field; defaults to en. | {} |
| `currency` | string | No | Optional three-letter currency code. The service normalizes it to uppercase. | {} |

The [complete request definition](../../schemas/1688-product-detail.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/1688-product-detail.json request.json
python3 examples/python/run.py 1688-product-detail request.json --dry-run
# Alternatively: node examples/javascript/run.mjs 1688-product-detail request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "offerId": "1040473674152"
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/1688-product-detail.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "product": {
      "skuList": [],
      "subject": "Example 1688 product",
      "offerId": "1040473674152",
      "shippingInfo": {},
      "saleInfo": {},
      "companyName": "Example supplier"
    }
  },
  "code": 0,
  "msg": null,
  "ts": "0",
  "time": "2026-01-01 00:00:00",
  "cost": "-1",
  "traceId": null
}
```

Keep the request trace when reporting errors. Do not infer authorization, order creation or payment success from a redirect, process exit or missing identifier alone.
