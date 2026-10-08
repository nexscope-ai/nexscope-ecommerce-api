# Image Translation API

Translate text inside an image.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/image-translation?view=api&co-from=github-ecommerce-api)

Category: Multimodal AI · Creative API

Translate image text from a source language to a target language for ecommerce localization.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/image-translation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: asynchronous; submission returns a task ID. Follow [task polling](../calling-apis.md#asynchronous-creative-apis).

Creative API access requires an active subscription; trial credits do not enable API key access.

Task result: `GET https://api.nexscope.ai/api/skill-api/v1/skills/image-translation/tasks/{taskId}`

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | Public URL of a JPG, JPEG, PNG, or WEBP image up to 4 MB and between 385 and 3000 pixels. | {} |
| `translationPlatform` | string | Yes | Translation platform. Supported values: deepl (DeepL), chatgpt (ChatGPT). | {} |
| `sourceLanguage` | string | Yes | Source language code. Supported values: CHS (Simplified Chinese), ENG (English), CHT (Traditional Chinese), ESP (Spanish), JPN (Japanese), KOR (Korean), PT (Portuguese), ROM (Romanian), RUS (Russian), VIN (Vietnamese), DEU (German). | {} |
| `targetLanguage` | string | Yes | Target language code. Supported values: AR, BG, BN, CHS, CHT, CKB, CSY, DA, DEU, EL, ENG, ESP, ET, FA, FI, FIL, FRA, GU, HE, HI, HR, HUN, ID, ITA, JPN, JW, KOR, LO, LT, LV, MR, MS, MY, NLD, NO, PLK, PT, PTB, ROM, RUS, SK, SL, SV, SW, TA, TE, TG, TH, TL, TRK, UK, UR, VIN. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Media constraints

```json
[
  {
    "fieldName": "imageUrl",
    "mediaKind": "image",
    "acceptedContentTypes": [
      "image/jpeg",
      "image/png",
      "image/webp"
    ],
    "maxFileSizeBytes": "4194304",
    "maxFiles": 1,
    "minWidthPixels": 385,
    "maxWidthPixels": 3000,
    "minHeightPixels": 385,
    "maxHeightPixels": 3000,
    "minAspectRatio": null,
    "maxAspectRatio": null
  }
]
```

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/image-translation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh image-translation request.json
# Or: node examples/javascript/run.mjs image-translation request.json
# Or: python3 examples/python/run.py image-translation request.json
```

### Published request example

```json
{
  "imageUrl": "https://example.com/product.jpg",
  "translationPlatform": "deepl",
  "sourceLanguage": "CHS",
  "targetLanguage": "ENG"
}
```

## Response

Follow the response envelope and field paths in the current official API reference linked above. HTTP 200 alone does not establish business success; when the response includes `code`, check that it is `0` before reading `data`. For asynchronous APIs, distinguish the submission receipt from the final task result and follow the documented task polling contract. The response example below is a historical definition-service fixture; it has not been reconciled with the current HTTP response envelope and must not be used to infer top-level field paths.

### Published response example

```json
{
  "taskId": "6b3f1c61-1b7d-4a59-8a7d-3b23e4b0c9e2",
  "status": "PENDING",
  "message": "The task has been created. Use taskId to query the result."
}
```

## Full definitions

- [Request definition](../../schemas/image-translation.request.json) — field-descriptors
- [Response definition](../../schemas/image-translation.response.json) — field-descriptors
- [Editable request sample](../../payloads/image-translation.json)
- [Response fixture](../../examples/responses/image-translation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_image_translation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
