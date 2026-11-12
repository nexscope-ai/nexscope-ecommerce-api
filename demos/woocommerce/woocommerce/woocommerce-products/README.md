# WooCommerce Products API

Search for products within a WooCommerce store by keyword.

[Official API documentation](https://www.nexscope.ai/api-docs/woocommerce-products?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/woocommerce-products.json)

[Repository API reference](../../../../docs/data/woocommerce-products.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/woocommerce/woocommerce/woocommerce-products
node demos/clients/node/run.mjs demos/woocommerce/woocommerce/woocommerce-products
java demos/clients/java/Run.java demos/woocommerce/woocommerce/woocommerce-products
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/woocommerce/products`.
