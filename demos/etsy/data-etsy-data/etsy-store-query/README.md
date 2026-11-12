# Etsy Store Query API

Search Etsy stores by keyword, category, country, status, ratings, sales, favorites, reviews, and opening date with pagination.

[Official API documentation](https://www.nexscope.ai/api-docs/etsy-store-query?co-from=github-ecommerce-api) · [Request payload](../../../../payloads/etsy-store-query.json)

[Repository API reference](../../../../docs/data/etsy-store-query.md)

This demo uses the repository catalog request and endpoint. Review the payload and replace sample identifiers with valid inputs.
Commands preview the request. Add `--execute` only when you intend to send it; calls may consume credits or change account data.

Run from the repository root:

```bash
python demos/clients/python/run.py demos/etsy/data-etsy-data/etsy-store-query
node demos/clients/node/run.mjs demos/etsy/data-etsy-data/etsy-store-query
java demos/clients/java/Run.java demos/etsy/data-etsy-data/etsy-store-query
```

Transport: **REST**. Endpoint: `https://api.nexscope.ai/api/skill-api/v1/skills/etsy-store-query/run`.
