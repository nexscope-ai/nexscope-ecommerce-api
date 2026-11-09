# 1688 Cancel Order API

Cancel Order for the currently authenticated Nexscope user. Use your Nexscope API key. Requires an ACTIVE, unexpired 1688 authorization owned by the current user. Procurement responses are live; do not cache or automatically retry writes. Cancellation is not a refund. Eligibility depends on the current 1688 order state.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/1688-cancel-order?view=api&co-from=github-ecommerce-api)

Category: 1688 Procurement · Data API · Contract refreshed: 2026-11-09

## Endpoint

`POST https://api.nexscope.ai/alibaba1688/cancelOrder`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`. Invoking the API consumes credits. This is a Nexscope endpoint; do not supply a supplier API key or OAuth access token.

## Authorization, placeholders and confirmation

Read the [1688 authorization and procurement guide](../1688-procurement-guide.md) before calling. Product, SKU, address, order and logistics identifiers in examples are placeholders, not verified records. Replace them with records accessible to your own authorized buyer account; keep IDs as strings. Confirmation examples deliberately use `false`; set the operation-specific boolean to `true` only after explicit confirmation of the exact action. Never automatically retry an uncertain write.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `aliOrderId` | string | Yes | Exact positive integer identifier. Send as a JSON string. | {} |
| `cancelReason` | string | No |  | {} |
| `remark` | string | No |  | {} |
| `confirmCancel` | boolean | Yes | Must be JSON true after separate explicit user confirmation. Examples default to false and do not authorize this action. | {} |

The [complete request definition](../../schemas/1688-cancel-order.request.json) contains nested fields and conditional requirements. Required alternatives: `[]`. Preserve the documented names and types; examples are illustrative.

## Call this API

Copy the sample, replace illustrative values, and inspect it without sending a request:

```bash
cp payloads/1688-cancel-order.json request.json
python3 examples/python/run.py 1688-cancel-order request.json --dry-run
# Alternatively: node examples/javascript/run.mjs 1688-cancel-order request.json --dry-run
# After reviewing parameters and authorizing the call, remove --dry-run to submit once.
```

### Published request example

```json
{
  "aliOrderId": "3309156590237728779",
  "confirmCancel": false
}
```

## Response

Check Nexscope outer `code == 0` before reading `data`; HTTP 200 alone is not business success. `cost` is elapsed milliseconds, not credits. Inspect nested business results and partial failures before taking dependent actions. The [complete response definition](../../schemas/1688-cancel-order.response.json) and example below are current production documentation snapshots, not a live buyer/order test result.

```json
{
  "data": {
    "success": true,
    "aliOrderId": "3309156590237728779"
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
