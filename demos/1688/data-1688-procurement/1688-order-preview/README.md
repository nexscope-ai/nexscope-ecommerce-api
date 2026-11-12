# 1688 Order Preview API

Preview a 1688 order to review items, shipping details, and payable amounts before submission. Requires an active 1688 store authorization.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-order-preview?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-order-preview.json)

[Repository API reference](../../../../docs/data/1688-order-preview.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-order-preview
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-order-preview
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-order-preview
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/orderPreview`.
