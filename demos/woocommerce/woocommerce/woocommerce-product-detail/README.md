# WooCommerce Product Detail API

Look up one WooCommerce product using its store address and product ID to view the product details shared publicly by the store.

[Official API documentation](https://www.nexscope.ai/api-docs/woocommerce-product-detail?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/woocommerce-product-detail.json)

[Repository API reference](../../../../docs/data/woocommerce-product-detail.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/woocommerce/woocommerce/woocommerce-product-detail
node demos/clients/node/run.mjs demos/woocommerce/woocommerce/woocommerce-product-detail
java demos/clients/java/Run.java demos/woocommerce/woocommerce/woocommerce-product-detail
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/woocommerce/productDetail`.
