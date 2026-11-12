# WooCommerce Product Reviews API

Read public reviews from a WooCommerce store. Focus on a specific product or category and review the returned feedback for that store.

[Official API documentation](https://www.nexscope.ai/api-docs/woocommerce-product-reviews?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/woocommerce-product-reviews.json)

[Repository API reference](../../../../docs/data/woocommerce-product-reviews.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/woocommerce/woocommerce/woocommerce-product-reviews
node demos/clients/node/run.mjs demos/woocommerce/woocommerce/woocommerce-product-reviews
java demos/clients/java/Run.java demos/woocommerce/woocommerce/woocommerce-product-reviews
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/woocommerce/productReviews`.
