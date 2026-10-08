# Calling Nexscope APIs

[Back to README](../README.md)

## Authentication

Get your user key from [API Access](https://www.nexscope.ai/seller/api-access?co-from=github-ecommerce-api). Set `NEXSCOPE_API_KEY` and send `Authorization: Bearer YOUR_API_KEY`. JSON requests use `Content-Type: application/json`. Keep authenticated calls on your backend.

## Synchronous Data APIs

All 172 Data entries in the retrieved catalog are marked synchronous. Send `POST` to the exact endpoint in the API's reference, with its own request body. Follow the response structure in the current API reference. For [Amazon Product Detail](data/amazon-product-detail.md#response), check the platform envelope `code === 0`, then read `data.products` and `data.total`; `data` may be null. A successful HTTP response does not imply that the result set is nonempty or that every optional field exists.

## Asynchronous Creative APIs

All 53 Creative entries are marked asynchronous. Active subscription access is required; trial credits alone do not enable Creative API key access.

1. Submit the request once to its `/run` endpoint.
2. Save the returned `taskId` alongside the API slug in your application.
3. Send authenticated `GET` requests to that API's `taskResultEndpoint`, substituting the returned task ID.
4. Continue only for `PENDING` or `RUNNING`; use bounded polling and stop for `SUCCESS`, `FAILED`, or `TIMEOUT`.
5. On success, consume the actual response returned by the task query. Do not interpret the submission receipt as a generated image or video.

The public task schema lists `PENDING`, `RUNNING`, `SUCCESS`, `FAILED`, and `TIMEOUT`. The documentation says completed resources use Nexscope-hosted URLs and show actual credits charged. Do not invent a common nested field path for every tool: inspect the returned JSON and the live reference.

A 5-second polling interval and a bounded application deadline are suggested client choices, not published service guarantees. Respect rate-limit responses and any `Retry-After` header. For a client timeout, retain the task ID so the task can be queried later. Do not automatically create another generation job.

The included helpers support `SLUG --task TASK_ID` for one status check. They never automatically retry POSTs. Their 120-second per-request network timeout does not define the maximum server-side generation duration.

## Media inputs

Use publicly reachable media URLs that meet the individual API's dimensions, MIME types, size, file-count, and aspect-ratio rules. A field can be individually optional while still belonging to an alternative required group; consult `requiredAnyGroups` and field constraints. For example, Seedance 2.5 requires at least one of `imageUrl`, `imageList`, or `video`, and reference video mode has incompatible image inputs.

Published example.com URLs are illustrative. Replace them with your assets before submitting. The API documentation also exposes an upload workflow where available; use its current instructions rather than assuming every tool accepts the same upload format.

## Definitions and examples

- `json-schema`: the official definition supplies a JSON Schema structure.
- `field-descriptors`: the official definition supplies field descriptions, examples, and constraints. A missing `jsonSchema` is preserved as missing; this format is not advertised as a strict JSON Schema validator.

A request sample may omit optional fields or use illustrative IDs and media URLs. Review the whole definition, including nested objects and conditional inputs. A response fixture is not a live result or a stable guarantee for every future execution.

## MCP

Each API reference includes its published MCP tool name. Consult the [official MCP documentation](https://www.nexscope.ai/mcp-docs?co-from=github-ecommerce-api) for client configuration, tool discovery, and JSON-RPC request shapes. REST is the primary quick-start path in this repository; this repository is not an MCP server implementation.

## Source of truth

Use the [current API documentation](https://www.nexscope.ai/api-docs?co-from=github-ecommerce-api) to verify current capabilities and account access. Each local API reference links to its official API view. Report discrepancies with the slug and relevant field, without including credentials.
