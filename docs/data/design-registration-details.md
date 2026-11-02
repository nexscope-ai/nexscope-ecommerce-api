# Design Registration Details API

Retrieve design-registration holders, designers, legal status, dates and classifications by exact identifiers. Results support candidate review, not an infringement verdict.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/design-registration-details?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

## Endpoint and authentication

`POST https://api.nexscope.ai/ai/designRegistrationDetails`

The existing alias `POST https://api.nexscope.ai/api/skill-api/v1/skills/design-registration-details/run` remains supported. MCP tool name: `nexscope_design_registration_details`.

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Calling the API consumes account credits under the existing pricing, caching and diagnostics rules. Check current account pricing before sending. Upstream `data.usage`, `costToken` and the HTTP envelope's `cost` do not define user charges; `cost` is elapsed milliseconds.

## Request parameters

| Name | Type | Description |
|---|---|---|
| `designRegistrationIds` | array | 1–200 unique exact registration IDs, each 1–128 trimmed characters; excludes primaryIdentifier and jurisdictionIso2. |
| `primaryIdentifier` | string | Exact primary number, 1–128 trimmed characters; preserve leading zeros. Excludes designRegistrationIds. |
| `jurisdictionIso2` | string | Optional two-letter jurisdiction, only with primaryIdentifier; use EM for EU. |

Supply `designRegistrationIds` (1–200 unique strings of 1–128 characters), or `primaryIdentifier` (1–128 characters), never both. `jurisdictionIso2` is optional only with `primaryIdentifier`; use two letters and `EM` for EU. Preserve leading zeros and exact identifiers; strings must be trimmed and contain no line breaks. These request limits are unchanged.

Read the source `data.data.items` result, not search candidates. In the complete HTTP envelope this is `data.data.data.items`. Preserve all returned records and optional fields. `image_count` and `has_readable_image` are metadata, not downloadable image URLs: do not generate links. Missing data is unknown, not a legal conclusion.

The [full request schema](../../schemas/design-registration-details.request.json) defines nested constraints, unique arrays, ranges and mutually exclusive inputs. The generic example clients prepare requests; they do not replace server validation.

## Editable request sample

```json
{
  "designRegistrationIds": [
    "DSR:wipo_hague:EMID.001431738-0001"
  ]
}
```

Copy [the payload](../../payloads/design-registration-details.json) to `request.json` and review it before submitting. Replace the illustrative identifier with the exact registration you need.

```bash
python3 examples/python/run.py design-registration-details request.json --dry-run
# This next command sends a separate, potentially billable request:
bash examples/curl/run.sh design-registration-details request.json
# Alternatives (each sends its own request):
# node examples/javascript/run.mjs design-registration-details request.json
# python3 examples/python/run.py design-registration-details request.json
```

## Response and tracing

Check outer `code === 0` before reading `data`; HTTP 200 alone does not imply business success. The platform envelope wraps the source result. Source `data.data.items` appears at HTTP `data.data.data.items`. Source `data.data.returned` is the returned-record count, not the dataset size.

Keep platform `data.requestId`, `data.upstreamRequestId`, source `data.data.request_id`, and outer `traceId` when present. They are distinct diagnostic identifiers and can be absent in illustrative examples. Keep optional coverage/warnings/asset/execution metadata when present. Neither API establishes infringement or freedom to operate.

### Registration item fields

| Field | Type | Meaning |
|---|---|---|
| `design_registration_id` | string | Exact registration ID. |
| `primary_identifier` | string | Primary number; preserve leading zeros. |
| `holder_names` | array | Source holders, when known. |
| `designer_names` | array | Source designers, when known. |
| `simple_legal_status` | string | Source legal status; do not infer missing values. |
| `as_of_date` | string | Source confirmation date, not necessarily today. |
| `has_readable_image` | integer | Source media hint; not an image URL. |
| `image_count` | integer | Source image count; do not construct download links. |
| `application_number` | string | Source application number; preserve leading zeros. |
| `registration_number` | string | Source registration number, not a constructed registration ID. |
| `publication_number` | string | Source publication number. |
| `data_version` | string | Source data version. |
| `right_type` | string | Source right type. |
| `registration_jurisdiction` | string | Original source jurisdiction value. |
| `registration_jurisdiction_code` | string | Original source jurisdiction code. |
| `jurisdiction_iso2` | string | Two-letter jurisdiction; EM represents the EU. |
| `title` | string | Original source title. |
| `title_language` | string | Source title language; may be unknown. |
| `title_en` | string | Source English title; do not translate independently. |
| `title_en_source` | string | Provenance of the English title. |
| `raw_status` | string | Unmapped original source status. |
| `application_date` | string | Application date, YYYY-MM-DD. |
| `registration_date` | string | Registration date, YYYY-MM-DD. |
| `publication_date` | string | Publication date, YYYY-MM-DD. |
| `data_quality_level` | string | Source data quality level; absent means unknown. |
| `coverage_level` | string | Source coverage level; no completeness guarantee. |
| `classification_count` | integer | Source fact count; missing values remain unknown. |
| `party_count` | integer | Source fact count; missing values remain unknown. |
| `text_count` | integer | Source fact count; missing values remain unknown. |
| `locarno_classes` | array | Source Locarno classes; preserve leading zeros. |

### Published HTTP response fixture

This is the production Catalog's illustrative response, not a newly executed query. Placeholder signed image URLs are examples only. No paid API calls were executed for this synchronization.

```json
{
  "data": {
    "data": {
      "code": "OK",
      "data": {
        "items": [
          {
            "simple_legal_status": "inactive",
            "design_registration_id": "DSR:wipo_hague:EMID.001431738-0001",
            "as_of_date": "2026-10-09",
            "holder_names": [
              "Example holder"
            ],
            "designer_names": [
              "Example designer"
            ],
            "title_en": "Bottles",
            "has_readable_image": 1,
            "image_count": 5,
            "primary_identifier": "001431738"
          }
        ],
        "returned": 1
      },
      "request_id": "example-request"
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

- [Request JSON Schema](../../schemas/design-registration-details.request.json)
- [Response JSON Schema](../../schemas/design-registration-details.response.json)
- [Editable payload](../../payloads/design-registration-details.json)
- [Published HTTP response fixture](../../examples/responses/design-registration-details.json)

Contract synchronized on 2026-11-02 from the production public definition service, reflecting the 2026-10-31 SIF source contract. This update adds only the two SIF operations; other API snapshots are unchanged.
