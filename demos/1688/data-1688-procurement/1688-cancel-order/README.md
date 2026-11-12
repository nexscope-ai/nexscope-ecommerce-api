# 1688 Cancel Order API

Request cancellation of an eligible 1688 order before fulfillment continues. Requires an active 1688 store authorization.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-cancel-order?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-cancel-order.json)

[Repository API reference](../../../../docs/data/1688-cancel-order.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-cancel-order
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-cancel-order
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-cancel-order
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/cancelOrder`.
