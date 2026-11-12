# 1688 Confirm Receive API

Confirm receipt of a delivered 1688 order after checking the goods. Requires an active 1688 store authorization.

[Official API documentation](https://www.nexscope.ai/api-docs/1688-confirm-receive?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/1688-confirm-receive.json)

[Repository API reference](../../../../docs/data/1688-confirm-receive.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/1688/data-1688-procurement/1688-confirm-receive
node demos/clients/node/run.mjs demos/1688/data-1688-procurement/1688-confirm-receive
java demos/clients/java/Run.java demos/1688/data-1688-procurement/1688-confirm-receive
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/alibaba1688/confirmReceive`.
