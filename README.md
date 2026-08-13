# 应用市场调研入库 / Application Market Research Lark Ingest

## 中文

这是一个 Codex Skill：把 App Store、Google Play、七麦数据或点点数据中的产品链接，整理为一条完整、可追溯的飞书多维表格记录。

### 能做什么

- 识别正确产品及 Apple ID 或 Android 包名。
- 提取标题、副标题、原始描述、中文产品简介、分类、评论数、版本、更新时间、链接和在架/下架状态。
- 使用七麦数据和点点数据追溯历史状态及准确下架时间。
- 下载官方 Logo 和 3-4 张市场图。
- 将市场图统一高度、等比裁切后横向拼合为一张大图，而非逐张上传。
- 写入前按稳定 ID、链接和名称查重；随后通过已接入的 Lark CLI 新增或补全记录。
- 上传 Logo 与横向市场图后，回查文本字段和附件，确认写入结果。

### 前置条件

- 已安装该 Codex Skill。
- 本机已有可用且已登录的 Lark CLI。
- 对目标飞书多维表格及目标数据表拥有访问权限。
- 若产品链接来自需登录的七麦或点点数据，需具备对应站点的访问权限。

本仓库不部署或配置飞书，不包含任何 Base 链接、表格 ID、账户资料或凭据。

### 安装与使用

通过 Codex 的 Skill 安装方式安装本仓库，然后在任务中提供产品链接、飞书 Base 链接和目标表名。

示例：

```text
使用 $app-market-research-lark-ingest，将这个产品录入 7-8 月调研表：
https://www.qimai.cn/app/baseinfo/appid/<APP_ID>/country/us

目标飞书多维表格：<Lark Base URL>
目标数据表：<表名>
```

### 工作流程

1. 确认产品身份并在目标表中查重。
2. 提取商店和第三方平台可获得的完整资料。
3. 判断产品在架、已下架或待核查，并记录可追溯的下架时间。
4. 下载并核对 Logo 和市场图。
5. 将市场图拼合为一张横向图片。
6. 通过 Lark CLI 写入文本字段与附件。
7. 回查记录，验证文字、链接和两类图片附件。

### 附带工具

- `scripts/extract_app_id.py`：从链接或文本中提取 Apple App ID。
- `scripts/stitch_market_screenshots.py`：统一截图尺寸并横向拼合。

完整 Agent 流程见 [SKILL.md](SKILL.md)，字段匹配说明见 [references/field-guide.md](references/field-guide.md)。

---

## English

This Codex Skill turns App Store, Google Play, Qimai, or Diandian product links into complete, traceable records in a Lark Base table.

### What It Does

- Identifies the correct app and its Apple ID or Android package ID.
- Collects titles, subtitles, original descriptions, Chinese product summaries, categories, reviews, versions, update times, links, and live/removed status.
- Uses Qimai and Diandian as traceable sources for historical status and exact removal time.
- Downloads the official Logo and 3-4 store screenshots.
- Normalizes and horizontally stitches market screenshots into one image instead of uploading them separately.
- Deduplicates by stable ID, links, and name before creating or enriching records through the existing Lark CLI.
- Re-reads the completed record and both attachments before reporting success.

### Prerequisites

- Codex with this Skill installed.
- An available, authenticated Lark CLI.
- Access to the destination Lark Base and target table.
- Access to Qimai or Diandian when the supplied source requires sign-in.

This repository does not deploy or configure Lark and contains no Base URLs, table IDs, account information, or credentials.

### Install and Use

Install this repository with Codex's Skill installer, then provide a product link, destination Base URL, and target table name.

Example:

```text
Use $app-market-research-lark-ingest to add this product to the 7-8 month research table:
https://www.qimai.cn/app/baseinfo/appid/<APP_ID>/country/us

Destination Lark Base: <Lark Base URL>
Target table: <table name>
```

### Workflow

1. Confirm the product identity and search for duplicates.
2. Extract all available store and third-party metadata.
3. Determine whether the app is live, removed, or needs verification, with traceable removal time where available.
4. Download and verify the Logo and market screenshots.
5. Stitch the screenshots into one horizontal image.
6. Write fields and attachments through Lark CLI.
7. Read the record back to verify text, links, and both image attachments.

### Included Utilities

- `scripts/extract_app_id.py`: extracts Apple App IDs from links or text.
- `scripts/stitch_market_screenshots.py`: normalizes and stitches screenshots horizontally.

See [SKILL.md](SKILL.md) for the complete agent workflow and [references/field-guide.md](references/field-guide.md) for expected table fields.
