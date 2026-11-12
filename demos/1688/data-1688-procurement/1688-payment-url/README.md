# 1688 Payment URL API

Get a payment link for a 1688 order so you can complete payment yourself. Requires an active 1688 store authorization.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-payment-url?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-payment-url.json)

[Repository API reference](../../../../docs/data/1688-payment-url.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-payment-url
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-payment-url
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-payment-url
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/paymentUrl`.
