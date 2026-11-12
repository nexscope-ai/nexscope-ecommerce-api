# 1688 Invoice Amount API

Check the invoiceable amount for a 1688 order before applying for an invoice. Requires an active 1688 store authorization.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-invoice-amount?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-invoice-amount.json)

[Repository API reference](../../../../docs/data/1688-invoice-amount.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-invoice-amount
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-invoice-amount
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-invoice-amount
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/invoiceAmount`.
