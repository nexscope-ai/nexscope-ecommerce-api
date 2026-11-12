# Design Registration Details API

Retrieve design-registration holders, designers, legal status, dates and classifications by exact IDs or primary number through the Nexscope REST API or MCP.

[Official API documentation](https://www.nexscope.ai/api-docs/design-registration-details?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/design-registration-details.json)

[Repository API reference](../../../../docs/data/design-registration-details.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/cross-platform/patent-ip-risk/design-registration-details
node demos/clients/node/run.mjs demos/cross-platform/patent-ip-risk/design-registration-details
java demos/clients/java/Run.java demos/cross-platform/patent-ip-risk/design-registration-details
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/ai/designRegistrationDetails`.
