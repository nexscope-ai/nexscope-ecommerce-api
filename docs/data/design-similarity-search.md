# Design Similarity Search API

Search design registrations using one image URL or Base64 image, with optional region, source-jurisdiction, Locarno and legal-status filters. Results support candidate review and do not establish infringement or freedom to operate.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/design-similarity-search?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

## Endpoint and authentication

`POST https://api.nexscope.ai/ai/designSimilaritySearch`

The existing alias `POST https://api.nexscope.ai/api/skill-api/v1/skills/design-similarity-search/run` remains supported. MCP tool name: `nexscope_design_similarity_search`.

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Calling the API consumes account credits under the existing pricing, caching and diagnostics rules. Check current account pricing before sending. Upstream `data.usage`, `costToken` and the HTTP envelope's `cost` do not define user charges; `cost` is elapsed milliseconds.

## Request parameters

| Name | Type | Description |
|---|---|---|
| `imageUrl` | string | Public HTTP(S) image URL, 8–4096 characters; exactly one image source. |
| `imageBase64` | string | Pure Base64 image bytes, 16–20971520 characters; omit imageUrl. |
| `title` | string | Optional image context, 1–4096 trimmed characters; not a standalone text query. |
| `topK` | integer | Candidate limit, 1–200; default 20. |
| `regions` | array | Up to 64 distinct two-letter region codes, e.g. US or EM; use EM for EU. |
| `jurisdictionCodes` | array | Up to 32 distinct source codes of 2–8 letters; intersects regions when both are supplied. |
| `topLoc` | array | Up to 32 distinct two-digit Locarno prefixes; preserve leading zeros. |
| `locarnoClasses` | array | Up to 64 distinct NN-NN Locarno classes. |
| `patentStatus` | array | One or two distinct integers: 0 inactive, 1 active; omit for no status preference. |

Exactly one of `imageUrl` and `imageBase64` must be supplied. Base64 is pure encoded image bytes (no data-URI prefix), 16–20971520 characters. `title` is context only and cannot replace an image. Filter arrays reject null and duplicate entries, including null elements; preserve leading zeros. Request `locarnoClasses` accepts only `NN-NN`, even when a response uses `06.01`.

The 29 candidate fields below are copied from the production response schema. Preserve returned candidate order: `similarity` is already the final 0–100 score; do not multiply by 100 or sort again. `images` contains at most six images; preserve signed URLs verbatim and their order. When images exist, `image_url` equals `images[0]`. Preserve returned Locarno values such as `06.01` and `09-01`. Missing/null means unknown; empty `tro_cases` does not establish absence of TRO, and an estimated expiration date does not establish confirmed expiration.

The [full request schema](../../schemas/design-similarity-search.request.json) defines nested constraints, unique arrays, ranges and mutually exclusive inputs. The generic example clients prepare requests; they do not replace server validation.

## Editable request sample

```json
{
  "topK": 20,
  "title": "Bottle",
  "imageUrl": "https://example.com/product.png"
}
```

Copy [the payload](../../payloads/design-similarity-search.json) to `request.json` and review it before submitting. Replace the reserved example image URL with your own public HTTP(S) image; the clients intentionally reject example domains, including during dry-run.

```bash
python3 examples/python/run.py design-similarity-search request.json --dry-run
# This next command sends a separate, potentially billable request:
bash examples/curl/run.sh design-similarity-search request.json
# Alternatives (each sends its own request):
# node examples/javascript/run.mjs design-similarity-search request.json
# python3 examples/python/run.py design-similarity-search request.json
```

## Response and tracing

Check outer `code === 0` before reading `data`; HTTP 200 alone does not imply business success. The platform envelope wraps the source result. Source `data.data.candidates` appears at HTTP `data.data.data.candidates`. Source `data.data.total` is at HTTP `data.data.data.total` and is not a page or displayed-candidate count.

Keep platform `data.requestId`, `data.upstreamRequestId`, source `data.data.request_id`, and outer `traceId` when present. They are distinct diagnostic identifiers and can be absent in illustrative examples. Keep optional coverage/warnings/asset/execution metadata when present. Neither API establishes infringement or freedom to operate.

### Candidate fields

| Field | Type | Meaning |
|---|---|---|
| `design_registration_id` | string | Exact registration ID for details; preserve unchanged. |
| `registration_jurisdiction_code` | string | Source jurisdiction code such as EU, EMID or USID; do not rewrite as ISO-2. |
| `jurisdiction_iso2` | string | Registration jurisdiction, distinct from protected jurisdictions. |
| `primary_identifier` | string | Primary display number; retain leading zeros. |
| `application_number` | string | Source application number. |
| `registration_number` | string | Source registration number. |
| `publication_number` | string | Source publication number; missing or null means unknown. |
| `title` | string | Source title, which may be a number. |
| `title_language` | string | Source title language; may be unknown. |
| `title_en` | string | Source English title; do not translate missing values. |
| `designer_names` | array | Source designers; missing or null means unknown. |
| `locarno_classes` | array | Preserve output codes such as 06.01 or 09-01; requests still require NN-NN. |
| `holder_names` | array | Source holders; do not resolve numeric identifiers to invented names. |
| `simple_legal_status` | string | Source legal status; do not infer it from similarity. |
| `application_date` | string | Source application date, YYYY-MM-DD. |
| `registration_date` | string | Source registration date, YYYY-MM-DD. |
| `publication_date` | string | Source publication date, YYYY-MM-DD. |
| `similarity` | number | Final 0-100 score, not a probability. Preserve returned order; never multiply by 100 or sort again. |
| `risk_level` | string | Source risk hint, separate from score and legal status; not an infringement verdict. |
| `image_url` | string | Complete signed first-image URL; when images exist this equals images[0]. Never strip query parameters. |
| `images` | array | At most six complete signed image URLs in original order; empty means no available images. |
| `specification` | ['object', 'array', 'string', 'number', 'boolean', 'null'] | Source JSON of any shape, or null; preserve actual structure without filling gaps. |
| `novelty_statement` | string | Source novelty statement; retain original text, not a legal conclusion. |
| `applicant_addresses` | array | Source applicant objects with name and address; never infer protection jurisdictions. |
| `locarno_details` | array | Source code, parent_code, label_zh and label_en; missing labels stay unknown. |
| `estimated_expiration_date` | string | Estimated date only, YYYY-MM-DD; not confirmed expiry or invalidity. |
| `expiration_date_basis` | ['object', 'array', 'string', 'number', 'boolean', 'null'] | Source JSON of any shape, or null; never invent an estimation basis. |
| `tro_cases` | array | Current TRO corpus associations; empty is not confirmation of no TRO. |
| `protected_jurisdictions` | array | HAGUE designated states or ordinary registration jurisdiction; null means unknown, never fill from regions. |

### Published HTTP response fixture

This is the production Catalog's illustrative response, not a newly executed query. Placeholder signed image URLs are examples only. No paid API calls were executed for this synchronization.

```json
{
  "data": {
    "data": {
      "code": "OK",
      "request_id": "req_example",
      "data": {
        "total": 1,
        "candidates": [
          {
            "design_registration_id": "DSR:euipo_design:001694860-0001",
            "registration_jurisdiction_code": "EU",
            "jurisdiction_iso2": "EM",
            "primary_identifier": "001694860-0001",
            "application_number": "001694860",
            "registration_number": "E077151-PC",
            "publication_number": null,
            "title": "E077151-PC",
            "title_language": "unknown",
            "title_en": "Chairs [seats]",
            "designer_names": null,
            "locarno_classes": [
              "06.01"
            ],
            "holder_names": [
              "237302"
            ],
            "simple_legal_status": "inactive",
            "application_date": "2010-04-13",
            "registration_date": null,
            "publication_date": null,
            "similarity": 99.88,
            "risk_level": "medium",
            "image_url": "https://example.com/design-1.png?signature=example%2Bsignature&expires=2000000000",
            "images": [
              "https://example.com/design-1.png?signature=example%2Bsignature&expires=2000000000",
              "https://example.com/design-2.png?signature=second&expires=2000000000"
            ],
            "specification": null,
            "novelty_statement": null,
            "applicant_addresses": null,
            "locarno_details": [
              {
                "code": "06.01",
                "parent_code": "06",
                "label_zh": null,
                "label_en": null
              }
            ],
            "estimated_expiration_date": null,
            "expiration_date_basis": null,
            "tro_cases": [],
            "protected_jurisdictions": [
              "EM"
            ]
          }
        ]
      },
      "message": "success"
    }
  },
  "code": 0,
  "msg": null,
  "ts": "0",
  "time": "2026-01-01 00:00:00",
  "cost": "-1",
  "traceId": null
}
```

## Errors

HTTP 401 indicates Nexscope authentication failure; HTTP 402 indicates insufficient credits. Preserve the platform error and tracing fields. Do not automatically retry ambiguous requests or silently substitute an image, identifier or jurisdiction.

- `DATA_IMAGE_DOWNLOAD_FAILED`: the provider could not download the image; check public reachability and the complete signed URL.
- `SYSTEM_PAYLOAD_TOO_LARGE`: the payload exceeded a service limit; check encoded image size before any deliberate resubmission.
- `SR_QUERY_ERROR`: the upstream query failed; preserve the request identifiers for diagnosis.
- `CAPABILITY_BACKEND_UNAVAILABLE`: the capability backend is unavailable; do not treat this as an empty successful result.

The four upstream codes are possible capability errors, not guarantees that each operation returns every code; image-download checks concern image search. Other source/platform errors must remain visible. Review corrected inputs and account credits before making a new call.

## Full definitions

- [Request JSON Schema](../../schemas/design-similarity-search.request.json)
- [Response JSON Schema](../../schemas/design-similarity-search.response.json)
- [Editable payload](../../payloads/design-similarity-search.json)
- [Published HTTP response fixture](../../examples/responses/design-similarity-search.json)

Contract synchronized on 2026-11-02 from the production public definition service, reflecting the 2026-10-31 SIF source contract. This update adds only the two SIF operations; other API snapshots are unchanged.
