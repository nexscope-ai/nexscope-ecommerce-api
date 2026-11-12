# WooCommerce Product Collection Data API

See price ranges, rating counts, and stock availability counts for WooCommerce products matching a keyword or category, where available.

[Official API documentation](https://www.nexscope.ai/api-docs/woocommerce-product-collection-data?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/woocommerce-product-collection-data.json)

[Repository API reference](../../../../docs/data/woocommerce-product-collection-data.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/woocommerce/woocommerce/woocommerce-product-collection-data
node demos/clients/node/run.mjs demos/woocommerce/woocommerce/woocommerce-product-collection-data
java demos/clients/java/Run.java demos/woocommerce/woocommerce/woocommerce-product-collection-data
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/woocommerce/productCollectionData`.
