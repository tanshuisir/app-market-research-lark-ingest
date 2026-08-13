# Application Market Research Lark Ingest

A Codex Skill that turns an App Store, Google Play, Qimai (七麦数据), or Diandian (点点数据) product link into a complete, verified record in a Lark Base table.

## What It Does

- Identifies the correct app and its Apple ID or Android package ID.
- Collects title, subtitle, descriptions, product summary, category, reviews, version, update time, links, and live/removed status.
- Uses Qimai and Diandian as traceable sources for historical status and removal time.
- Downloads the official Logo and 3-4 store screenshots.
- Produces one horizontally stitched market image rather than uploading separate screenshots.
- Finds existing records before writing, then creates or updates through the existing Lark CLI.
- Re-reads the finished record and both attachments before reporting completion.

## Prerequisites

- Codex with the Skill installed.
- An already authenticated and available Lark CLI.
- Access to the destination Lark Base and target table.
- Access to Qimai or Diandian when the supplied product source requires sign-in.

This repository does not deploy or configure Lark, and contains no Base URLs, table IDs, account information, or credentials.

## Install

Install the Skill from this repository with Codex's Skill installer, then provide a product link and the destination Base/table when you use it.

## Example Prompt

```text
Use $app-market-research-lark-ingest to add this product to the 7-8 month research table:
https://www.qimai.cn/app/baseinfo/appid/<APP_ID>/country/us

Destination: <Lark Base URL>
Target table: <table name>
```

## Workflow

1. Confirm the product identity and look for an existing record.
2. Extract all available store and third-party metadata.
3. Confirm whether the app is live, removed, or needs verification.
4. Download and check the Logo plus market screenshots.
5. Stitch the screenshots into one horizontal image.
6. Write fields and attachments through Lark CLI.
7. Read the record back to verify the result.

## Included Utilities

- `scripts/extract_app_id.py`: extract Apple App IDs from links or text.
- `scripts/stitch_market_screenshots.py`: normalize and stitch screenshots horizontally.

See [SKILL.md](SKILL.md) for the complete agent workflow and [references/field-guide.md](references/field-guide.md) for the expected table fields.
