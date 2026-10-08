# Amazon Opportunity Search By Metrics API

Amazon reverse product selection: filter Amazon niches and keywords by 30+ business dimensions (market size & growth, price tiers & share, competition density & top concentration, demographics such as age/gender/income, review highlights & pain points) from a metrics pool aggregated from historical business insight reports.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-opportunity-search-by-metrics?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Amazon reverse product selection: filter Amazon niches and keywords by 30+ business dimensions (market size & growth, price tiers & share, competition density & top concentration, demographics such as age/gender/income, review highlights & pain points) from a metrics pool aggregated from historical business insight reports.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-opportunity-search-by-metrics/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the response envelope and business fields documented in the current official API reference.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `amazonDomain` | string | No | Amazon site code (closed enum), currently only supports US. Defaults to US only if not specified | {} |
| `limit` | integer | No | Maximum number of results to return (1-200), default 25. No page parameter; returns the most recent N records sorted by collection time descending | {} |
| `keyword` | string | No | Search keyword text fragment (LIKE fuzzy match) | {} |
| `nicheName` | string | No | Normalized niche name fragment (LIKE, snake_case lowercase), suitable for niche time-series comparison | {} |
| `nicheRevenue360dMinUsdAtLeastGte` | number | No | Minimum 360-day market revenue lower bound (USD) | {} |
| `nicheRevenue360dMinUsdAtLeastLte` | number | No | Maximum 360-day market revenue lower bound (USD) | {} |
| `nicheRevenue360dMaxUsdAtLeastGte` | number | No | Minimum 360-day market revenue upper bound (USD) | {} |
| `nicheRevenue360dMaxUsdAtLeastLte` | number | No | Maximum 360-day market revenue upper bound (USD) | {} |
| `nichePeakSearchVolumeAtLeastGte` | integer | No | Peak monthly search volume minimum (non-negative integer) | {} |
| `nichePeakSearchVolumeAtLeastLte` | integer | No | Peak monthly search volume maximum (non-negative integer) | {} |
| `nicheSearchVolumeYoyChangePctAtLeastGte` | number | No | Search volume YoY change rate minimum (%, signed) | {} |
| `nicheSearchVolumeYoyChangePctAtLeastLte` | number | No | Search volume YoY change rate maximum (%, signed) | {} |
| `nichePeakMonthGte` | integer | No | Search peak month minimum (1-12) | {} |
| `nichePeakMonthLte` | integer | No | Search peak month maximum (1-12) | {} |
| `nicheBrandCountGte` | integer | No | Active brand count minimum | {} |
| `nicheBrandCountLte` | integer | No | Active brand count maximum | {} |
| `nicheBrandCountYoyChangePctAtLeastGte` | number | No | Brand count YoY change rate minimum (%, signed) | {} |
| `nicheBrandCountYoyChangePctAtLeastLte` | number | No | Brand count YoY change rate maximum (%, signed) | {} |
| `nicheTop5ProductClickSharePctAtLeastGte` | number | No | Top 5 product click share minimum (0-100) | {} |
| `nicheTop5ProductClickSharePctAtLeastLte` | number | No | Top 5 product click share maximum (0-100) | {} |
| `featureTop5BrandSharePctAtLeastGte` | number | No | Top 5 brand combined share minimum (0-100) | {} |
| `featureTop5BrandSharePctAtLeastLte` | number | No | Top 5 brand combined share maximum (0-100) | {} |
| `featureTopBrandsContains` | string | No | Top 3 brand name fragment (original text LIKE, case-sensitive) | {} |
| `priceMinUsdGte` | number | No | Niche minimum product price lower bound (USD) | {} |
| `priceMinUsdLte` | number | No | Niche minimum product price upper bound (USD) | {} |
| `priceMaxUsdGte` | number | No | Niche maximum product price lower bound (USD) | {} |
| `priceMaxUsdLte` | number | No | Niche maximum product price upper bound (USD) | {} |
| `priceSweetSpotMinUsdGte` | number | No | Sweet spot lower bound minimum (USD) | {} |
| `priceSweetSpotMinUsdLte` | number | No | Sweet spot lower bound maximum (USD) | {} |
| `priceSweetSpotMaxUsdGte` | number | No | Sweet spot upper bound minimum (USD) | {} |
| `priceSweetSpotMaxUsdLte` | number | No | Sweet spot upper bound maximum (USD) | {} |
| `priceEntryClickSharePctAtLeastGte` | number | No | Entry tier click share minimum (0-100) | {} |
| `priceEntryClickSharePctAtLeastLte` | number | No | Entry tier click share maximum (0-100) | {} |
| `priceMidClickSharePctAtLeastGte` | number | No | Mid tier click share minimum (0-100) | {} |
| `priceMidClickSharePctAtLeastLte` | number | No | Mid tier click share maximum (0-100) | {} |
| `priceHighClickSharePctAtLeastGte` | number | No | High tier click share minimum (0-100) | {} |
| `priceHighClickSharePctAtLeastLte` | number | No | High tier click share maximum (0-100) | {} |
| `demoPrimaryAgeMinGte` | integer | No | Primary audience age lower bound minimum (0-120 years) | {} |
| `demoPrimaryAgeMinLte` | integer | No | Primary audience age lower bound maximum (0-120 years) | {} |
| `demoPrimaryAgeMaxGte` | integer | No | Primary audience age upper bound minimum (0-120 years) | {} |
| `demoPrimaryAgeMaxLte` | integer | No | Primary audience age upper bound maximum (0-120 years) | {} |
| `demoGenderDominant` | string | No | Dominant gender (closed enum): female / male / mixed / unspecified | {} |
| `demoPrimaryIncomeTier` | string | No | Income tier (closed enum): low / middle_low / middle / middle_upper / upper_middle / high | {} |
| `demoLifeStageTagsContains` | string | No | Life stage tag fragment (snake_case, LIKE): parent, student, retiree, athlete, etc. | {} |
| `featureNewAvgReviewCountAtLeastGte` | integer | No | New product average review count minimum (non-negative integer) | {} |
| `featureNewAvgReviewCountAtLeastLte` | integer | No | New product average review count maximum (non-negative integer) | {} |
| `featureEstablishedAvgReviewCountAtLeastGte` | integer | No | Established product average review count minimum (non-negative integer) | {} |
| `featureEstablishedAvgReviewCountAtLeastLte` | integer | No | Established product average review count maximum (non-negative integer) | {} |
| `featureEmergingTrendTagsContains` | string | No | Emerging trend feature tag fragment (snake_case, LIKE): cordless, portable, smart, etc. | {} |
| `featureUncommonFeatureTagsContains` | string | No | Rare differentiation feature tag fragment (snake_case, LIKE): hema_free, medical_grade_silicone, etc. | {} |
| `searchTopCategory1Label` | string | No | Search traffic top category 1 label fragment (snake_case, LIKE): core_product_terms, set_kit_configurations, etc. | {} |
| `reviewPositiveTop1Topic` | string | No | Positive review #1 topic fragment (snake_case, LIKE): comfort, quality_overall_generic, etc. | {} |
| `reviewPositiveTop1PctAtLeastGte` | number | No | Positive review #1 topic share minimum (0-100, share among positive reviews) | {} |
| `reviewPositiveTop1PctAtLeastLte` | number | No | Positive review #1 topic share maximum (0-100) | {} |
| `reviewNegativeTop1Topic` | string | No | Negative review #1 topic fragment (snake_case, LIKE): size, quality, durability, etc. | {} |
| `reviewNegativeTop1PctAtLeastGte` | number | No | Negative review #1 topic share minimum (0-100, share among negative reviews) | {} |
| `reviewNegativeTop1PctAtLeastLte` | number | No | Negative review #1 topic share maximum (0-100) | {} |
| `reviewNegativeTop2Topic` | string | No | Negative review #2 topic fragment (snake_case, LIKE) | {} |
| `reviewStrategicInsightTagsContains` | string | No | Review strategic insight tag fragment (snake_case, LIKE): sizing_clarity, material_transparency, etc. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-opportunity-search-by-metrics.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-opportunity-search-by-metrics request.json
# Or: node examples/javascript/run.mjs amazon-opportunity-search-by-metrics request.json
# Or: python3 examples/python/run.py amazon-opportunity-search-by-metrics request.json
```

### Published request example

```json
{
  "amazonDomain": "US",
  "keyword": "phone case",
  "limit": 10
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "data": [],
  "keyword": "phone case",
  "nicheRevenue360dMinUsdAtLeast/nicheRevenue360dMaxUsdAtLeast": 1,
  "nichePeakSearchVolumeAtLeast": 1,
  "nichePeakMonth": 1,
  "nicheSearchVolumeYoyChangePctAtLeast": 1,
  "nicheBrandCount/nicheBrandCountYoyChangePctAtLeast": 1,
  "nicheTop5ProductClickSharePctAtLeast": 1,
  "featureTop5BrandSharePctAtLeast": 1,
  "featureTopBrands": [],
  "priceMinUsd/priceMaxUsd": 1,
  "priceSweetSpotMinUsd/priceSweetSpotMaxUsd": 1,
  "priceEntryClickSharePctAtLeast/priceMidClickSharePctAtLeast/priceHighClickSharePctAtLeast": 1,
  "demoPrimaryAgeMin/demoPrimaryAgeMax": 1,
  "demoLifeStageTags": [],
  "featureNewAvgReviewCountAtLeast/featureEstablishedAvgReviewCountAtLeast": 1,
  "featureEmergingTrendTags/featureUncommonFeatureTags": [],
  "reviewPositiveTop1Topic/reviewPositiveTop1PctAtLeast": 1,
  "reviewNegativeTop1Topic/reviewNegativeTop1PctAtLeast/reviewNegativeTop2Topic": 1,
  "reviewStrategicInsightTags": []
}
```

## Full definitions

- [Request definition](../../schemas/amazon-opportunity-search-by-metrics.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-opportunity-search-by-metrics.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-opportunity-search-by-metrics.json)
- [Response fixture](../../examples/responses/amazon-opportunity-search-by-metrics.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_opportunity_search_by_metrics`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
