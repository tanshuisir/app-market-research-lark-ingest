---
name: app-market-research-lark-ingest
description: Extract complete iOS or Android product information from App Store, Google Play, Qimai (七麦数据), or Diandian (点点数据) links and write it into a specified Lark Base table through an already available Lark CLI. Use when ingesting app research links, completing titles/subtitles/descriptions/product summaries/categories/reviews/update dates, checking whether an app is live or removed, downloading logos, cropping and horizontally stitching store screenshots, deduplicating records, or repairing incomplete app-research rows.
---

# Application Market Research Ingest

Turn a third-party app link into one complete, verified record in a user-specified Lark Base table. Assume Lark CLI is already connected; do not install, deploy, or configure Lark.

## Inputs

Obtain:

1. One or more product links from App Store, Google Play, Qimai, or Diandian; an Apple ID, Android package ID, or product name is also acceptable.
2. The destination Base link and target table name. Reuse a destination already confirmed for the same continuing batch.

If the destination is missing, ask only for the Base link and target table. Do not create deployment configuration files.

## Workflow

### 1. Identify the Product

- Resolve the canonical Apple ID or Android package ID. Use `scripts/extract_app_id.py` when a numeric Apple ID is embedded in text or a URL.
- Confirm the title and developer match across the third-party page and official store.
- Preserve the supplied third-party link as a traceable source.

### 2. Read the Target Table

- Use the existing `lark-base` CLI workflow to resolve the Base link and target table.
- List live fields and types before writing. Match them by name and compatible type using `references/field-guide.md`.
- Search existing records by stable ID, official-store URL, Qimai/Diandian URL, and normalized name.
- Update a matching record instead of creating a duplicate.

### 3. Collect Product Information

Collect every available element:

- Project name, store title, and subtitle
- Apple ID or Android package ID
- Official-store and third-party links
- Original store description
- Concise Chinese product introduction covering positioning, main functions, and social framework
- Category, review count, release date, latest update time, and current version
- Current availability and exact removal time when traceable

Use the official store for current public metadata. Use Qimai mainly for iOS history and Diandian for Android or supporting history. Apply `references/source-and-status-rules.md` when deciding availability.

### 4. Prepare Logo and Market Screenshots

- Download the highest practical resolution official Logo.
- Download 3-4 representative store screenshots from the verified product and storefront.
- Correct orientation and crop only irrelevant outer whitespace or browser chrome. Never crop away product UI, marketing copy, or device content.
- Normalize screenshots to one height while preserving aspect ratio, then stitch them horizontally without gaps:

```bash
python3 scripts/stitch_market_screenshots.py shot1.png shot2.png shot3.png --output market-strip.jpg
```

- Visually inspect the Logo and stitched image. Confirm identity, orientation, order, legibility, and absence of accidental cropping.
- Upload one Logo attachment and one stitched market-image attachment, not several separate screenshots.

### 5. Write Through Lark CLI

- Write ordinary text, number, date, select, and URL fields first.
- Use the Lark CLI attachment command for Logo and market-image fields.
- Keep link labels concise when the table provides formula/display fields: `七麦数据`, `点点数据`, `App Store`, or `Google Play`.
- Serialize writes to the same table.

### 6. Verify

- Re-read the changed record after all uploads.
- Confirm product identity, title, subtitle, descriptions, links, category, reviews, update time, status, Logo, and stitched market image.
- Report whether the record was created, updated, or skipped as a duplicate, plus any fields that could not be verified.

## Availability Rules

- Write `在架` only when the correct product is live in the requested storefront.
- Write `已下架` only when evidence supports removal; include the exact removal time when the historical source provides it.
- Write `待核查` when login failure, regional ambiguity, conflicting identity, or source errors prevent a reliable conclusion.
- Never treat one failed lookup as proof of removal or invent a removal date.

## Boundaries

- Do not install, deploy, authenticate, or configure Lark unless the user separately asks for that work.
- Do not create persistent destination configuration files.
- Do not create or modify Base fields unless the user explicitly requests schema changes.
- Do not delete duplicate records without explicit authorization.
- Do not claim completion before reading back the record and both attachments.
